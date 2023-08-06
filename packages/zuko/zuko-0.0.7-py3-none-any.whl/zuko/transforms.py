r"""Parameterizable transformations."""

import math
import torch
import torch.nn.functional as F

from torch import Tensor, LongTensor, Size
from torch.distributions import *
from torch.distributions import constraints
from typing import *

from .utils import bisection, broadcast, gauss_legendre, odeint


torch.distributions.transforms._InverseTransform.__name__ = 'Inverse'


def _call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
    r"""Returns both the transformed value and the log absolute determinant of the
    transformation's Jacobian."""

    y = self._call(x)
    ladj = self.log_abs_det_jacobian(x, y)

    return y, ladj


Transform.call_and_ladj = _call_and_ladj


class IdentityTransform(Transform):
    r"""Creates a transformation :math:`f(x) = x`."""

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, IdentityTransform)

    def _call(self, x: Tensor) -> Tensor:
        return x

    def _inverse(self, y: Tensor) -> Tensor:
        return y

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return torch.zeros_like(x)


class CosTransform(Transform):
    r"""Creates a transformation :math:`f(x) = -\cos(x)`."""

    domain = constraints.interval(0, math.pi)
    codomain = constraints.interval(-1, 1)
    bijective = True
    sign = +1

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, CosTransform)

    def _call(self, x: Tensor) -> Tensor:
        return -x.cos()

    def _inverse(self, y: Tensor) -> Tensor:
        return (-y).acos()

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return x.sin().abs().log()


class SinTransform(Transform):
    r"""Creates a transformation :math:`f(x) = \sin(x)`."""

    domain = constraints.interval(-math.pi / 2, math.pi / 2)
    codomain = constraints.interval(-1, 1)
    bijective = True
    sign = +1

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, SinTransform)

    def _call(self, x: Tensor) -> Tensor:
        return x.sin()

    def _inverse(self, y: Tensor) -> Tensor:
        return y.asin()

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return x.cos().abs().log()


class SoftclipTransform(Transform):
    r"""Creates a transform that maps :math:`\mathbb{R}` to the inverval :math:`[-B, B]`.

    .. math:: f(x) = \frac{x}{1 + \left| \frac{x}{B} \right|}

    Arguments:
        bound: The codomain bound :math:`B`.
    """

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __init__(self, bound: float = 5.0, **kwargs):
        super().__init__(**kwargs)

        self.bound = bound

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(bound={self.bound})'

    def _call(self, x: Tensor) -> Tensor:
        return x / (1 + abs(x / self.bound))

    def _inverse(self, y: Tensor) -> Tensor:
        return y / (1 - abs(y / self.bound))

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return -2 * torch.log1p(abs(x / self.bound))


class MonotonicAffineTransform(Transform):
    r"""Creates a transformation :math:`f(x) = \alpha x + \beta`.

    Arguments:
        shift: The shift term :math:`\beta`, with shape :math:`(*,)`.
        scale: The unconstrained scale factor :math:`\alpha`, with shape :math:`(*,)`.
        slope: The minimum slope of the transformation.
    """

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __init__(
        self,
        shift: Tensor,
        scale: Tensor,
        slope: float = 1e-3,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.shift = shift
        self.log_scale = scale / (1 + abs(scale / math.log(slope)))
        self.scale = self.log_scale.exp()

    def _call(self, x: Tensor) -> Tensor:
        return x * self.scale + self.shift

    def _inverse(self, y: Tensor) -> Tensor:
        return (y - self.shift) / self.scale

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return self.log_scale.expand(x.shape)


class MonotonicRQSTransform(Transform):
    r"""Creates a monotonic rational-quadratic spline (RQS) transformation.

    References:
        | Neural Spline Flows (Durkan et al., 2019)
        | https://arxiv.org/abs/1906.04032

    Arguments:
        widths: The unconstrained bin widths, with shape :math:`(*, K)`.
        heights: The unconstrained bin heights, with shape :math:`(*, K)`.
        derivatives: The unconstrained knot derivatives, with shape :math:`(*, K - 1)`.
        bound: The spline's (co)domain bound :math:`B`.
        slope: The minimum slope of the transformation.
    """

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __init__(
        self,
        widths: Tensor,
        heights: Tensor,
        derivatives: Tensor,
        bound: float = 5.0,
        slope: float = 1e-3,
        **kwargs,
    ):
        super().__init__(**kwargs)

        widths = widths / (1 + abs(2 * widths / math.log(slope)))
        heights = heights / (1 + abs(2 * heights / math.log(slope)))
        derivatives = derivatives / (1 + abs(derivatives / math.log(slope)))

        widths = 2 * F.softmax(widths, dim=-1)
        heights = 2 * F.softmax(heights, dim=-1)
        derivatives = derivatives.exp()

        self.horizontal = bound * torch.cumsum(F.pad(widths, (1, 0), value=-1), dim=-1)
        self.vertical = bound * torch.cumsum(F.pad(heights, (1, 0), value=-1), dim=-1)
        self.derivatives = F.pad(derivatives, (1, 1), value=1)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(bins={self.bins})'

    @property
    def bins(self) -> int:
        return self.horizontal.shape[-1] - 1

    def bin(self, k: LongTensor) -> Tuple[Tensor, ...]:
        mask = torch.logical_and(0 <= k, k < self.bins)

        k = k % self.bins
        k0_k1 = torch.stack((k, k + 1))

        k0_k1, hs, vs, ds = broadcast(
            k0_k1[..., None],
            self.horizontal,
            self.vertical,
            self.derivatives,
            ignore=1,
        )

        x0, x1 = hs.gather(-1, k0_k1).squeeze(dim=-1)
        y0, y1 = vs.gather(-1, k0_k1).squeeze(dim=-1)
        d0, d1 = ds.gather(-1, k0_k1).squeeze(dim=-1)

        s = (y1 - y0) / (x1 - x0)

        return mask, x0, x1, y0, y1, d0, d1, s

    @staticmethod
    def searchsorted(seq: Tensor, value: Tensor) -> LongTensor:
        return torch.searchsorted(seq, value[..., None]).squeeze(dim=-1)

    def _call(self, x: Tensor) -> Tensor:
        k = self.searchsorted(self.horizontal, x) - 1
        mask, x0, x1, y0, y1, d0, d1, s = self.bin(k)

        z = mask * (x - x0) / (x1 - x0)

        y = y0 + (y1 - y0) * (s * z**2 + d0 * z * (1 - z)) / (
            s + (d0 + d1 - 2 * s) * z * (1 - z)
        )

        return torch.where(mask, y, x)

    def _inverse(self, y: Tensor) -> Tensor:
        k = self.searchsorted(self.vertical, y) - 1
        mask, x0, x1, y0, y1, d0, d1, s = self.bin(k)

        y_ = mask * (y - y0)

        a = (y1 - y0) * (s - d0) + y_ * (d0 + d1 - 2 * s)
        b = (y1 - y0) * d0 - y_ * (d0 + d1 - 2 * s)
        c = -s * y_

        z = 2 * c / (-b - (b**2 - 4 * a * c).sqrt())

        x = x0 + z * (x1 - x0)

        return torch.where(mask, x, y)

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        _, ladj = self.call_and_ladj(x)
        return ladj

    def call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        k = self.searchsorted(self.horizontal, x) - 1
        mask, x0, x1, y0, y1, d0, d1, s = self.bin(k)

        z = mask * (x - x0) / (x1 - x0)

        y = y0 + (y1 - y0) * (s * z**2 + d0 * z * (1 - z)) / (
            s + (d0 + d1 - 2 * s) * z * (1 - z)
        )

        jacobian = (
            s**2
            * (2 * s * z * (1 - z) + d0 * (1 - z) ** 2 + d1 * z**2)
            / (s + (d0 + d1 - 2 * s) * z * (1 - z)) ** 2
        )

        return torch.where(mask, y, x), mask * jacobian.log()


class MonotonicTransform(Transform):
    r"""Creates a transformation from a monotonic univariate function :math:`f_\phi(x)`.

    The inverse function :math:`f_\phi^{-1}` is approximated using the bisection method.

    Arguments:
        f: A monotonic univariate function :math:`f_\phi`.
        phi: The parameters :math:`\phi` of :math:`f_\phi`.
        bound: The domain bound :math:`B`.
        eps: The absolute tolerance for the inverse transformation.
    """

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __init__(
        self,
        f: Callable[[Tensor], Tensor],
        phi: Iterable[Tensor] = (),
        bound: float = 5.0,
        eps: float = 1e-6,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.f = f
        self.phi = tuple(filter(lambda p: p.requires_grad, phi))
        self.bound = bound
        self.eps = eps

    def _call(self, x: Tensor) -> Tensor:
        return self.f(x)

    def _inverse(self, y: Tensor) -> Tensor:
        return bisection(
            f=self.f,
            y=y,
            a=torch.full_like(y, -self.bound),
            b=torch.full_like(y, self.bound),
            n=math.ceil(math.log2(2 * self.bound / self.eps)),
            phi=self.phi,
        )

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        _, ladj = self.call_and_ladj(x)
        return ladj

    def call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        with torch.enable_grad():
            x = x.requires_grad_()
            y = self.f(x)

        jacobian = torch.autograd.grad(y, x, torch.ones_like(y), create_graph=True)[0]

        return y, jacobian.log()


class UnconstrainedMonotonicTransform(MonotonicTransform):
    r"""Creates a monotonic transformation :math:`f(x)` by integrating a positive
    univariate function :math:`g(x)`.

    .. math:: f(x) = \int_0^x g(u) ~ du + C

    The definite integral is estimated by a :math:`n`-point Gauss-Legendre quadrature.

    Arguments:
        g: A positive univariate function :math:`g`.
        C: The integration constant :math:`C`.
        n: The number of points :math:`n` for the quadrature.
        kwargs: Keyword arguments passed to :class:`MonotonicTransform`.
    """

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __init__(
        self,
        g: Callable[[Tensor], Tensor],
        C: Tensor,
        n: int = 16,
        **kwargs,
    ):
        super().__init__(self.f, **kwargs)

        self.g = g
        self.C = C
        self.n = n

    def f(self, x: Tensor) -> Tensor:
        return gauss_legendre(
            f=self.g,
            a=torch.zeros_like(x),
            b=x,
            n=self.n,
            phi=self.phi,
        ) + self.C

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return self.g(x).log()

    def call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        return self.f(x), self.g(x).log()


class SOSPolynomialTransform(UnconstrainedMonotonicTransform):
    r"""Creates a sum-of-squares (SOS) polynomial transformation.

    The transformation :math:`f(x)` is expressed as the primitive integral of the
    sum of :math:`K` squared polynomials of degree :math:`L`.

    .. math:: f(x) = \int_0^x \sum_{i = 1}^K
        \left( 1 + \sum_{j = 0}^L a_{i,j} ~ u^j \right)^2 ~ du + C

    References:
        | Sum-of-Squares Polynomial Flow (Jaini et al., 2019)
        | https://arxiv.org/abs/1905.02325

    Arguments:
        a: The polynomial coefficients :math:`a`, with shape :math:`(*, K, L + 1)`.
        C: The integration constant :math:`C`.
        kwargs: Keyword arguments passed to :class:`UnconstrainedMonotonicTransform`.
    """

    domain = constraints.real
    codomain = constraints.real
    bijective = True
    sign = +1

    def __init__(self, a: Tensor, C: Tensor, **kwargs):
        super().__init__(self.g, C, phi=(a,), n=a.shape[-1], **kwargs)

        self.a = a
        self.i = torch.arange(a.shape[-1]).to(a.device)

    def g(self, x: Tensor) -> Tensor:
        x = x / self.bound
        x = x[..., None] ** self.i
        p = 1 + self.a @ x[..., None]

        return p.squeeze(dim=-1).square().sum(dim=-1)


class FFJTransform(Transform):
    r"""Creates a free-form Jacobian (FFJ) transformation.

    The transformation is the integration of a system of first-order ordinary
    differential equations

    .. math:: x(T) = \int_0^T f_\phi(x(t), t) ~ dt .

    The log-determinant of the Jacobian is replaced by an unbiased stochastic
    linear-time estimate.

    References:
        | FFJORD: Free-form Continuous Dynamics for Scalable Reversible Generative Models (Grathwohl et al., 2018)
        | https://arxiv.org/abs/1810.01367

    Arguments:
        f: A system of first-order ODEs :math:`f_\phi`.
        time: The integration time :math:`T`.
        phi: The parameters :math:`\phi` of :math:`f_\phi`.
    """

    domain = constraints.real_vector
    codomain = constraints.real_vector
    bijective = True

    def __init__(
        self,
        f: Callable[[Tensor, Tensor], Tensor],
        time: Tensor,
        phi: Iterable[Tensor] = (),
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.f = f
        self.t0 = time.new_tensor(0.0)
        self.t1 = time
        self.phi = tuple(filter(lambda p: p.requires_grad, phi))

    def _call(self, x: Tensor) -> Tensor:
        return odeint(self.f, x, self.t0, self.t1, self.phi)

    def _inverse(self, y: Tensor) -> Tensor:
        return odeint(self.f, y, self.t1, self.t0, self.phi)

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        _, ladj = self.call_and_ladj(x)
        return ladj

    def call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        shape = x.shape
        size = x.numel()

        eps = torch.randn_like(x)

        def f_aug(x_aug: Tensor, t: Tensor) -> Tensor:
            x = x_aug[:size].reshape(shape)

            with torch.enable_grad():
                x = x.requires_grad_()
                dx = self.f(x, t)

            epsjp = torch.autograd.grad(dx, x, eps, create_graph=True)[0]
            trace = (epsjp * eps).sum(dim=-1)

            return torch.cat((dx.flatten(), trace.flatten()))

        zeros = x.new_zeros(shape[:-1])

        x_aug = torch.cat((x.flatten(), zeros.flatten()))
        y_aug = odeint(f_aug, x_aug, self.t0, self.t1, self.phi)

        y, score = y_aug[:size], y_aug[size:]

        return y.reshape(shape), score.reshape(shape[:-1])


class AutoregressiveTransform(Transform):
    r"""Transform via an autoregressive scheme.

    .. math:: y_i = f(x_i; x_{<i})

    Arguments:
        meta: A meta function which returns a transformation :math:`f`.
        passes: The number of passes for the inverse transformation.
    """

    domain = constraints.real_vector
    codomain = constraints.real_vector
    bijective = True

    def __init__(
        self,
        meta: Callable[[Tensor], Transform],
        passes: int,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.meta = meta
        self.passes = passes

    def _call(self, x: Tensor) -> Tensor:
        return self.meta(x)(x)

    def _inverse(self, y: Tensor) -> Tensor:
        x = torch.zeros_like(y)
        for _ in range(self.passes):
            x = self.meta(x).inv(y)

        return x

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return self.meta(x).log_abs_det_jacobian(x, y).sum(dim=-1)

    def call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        y, ladj = self.meta(x).call_and_ladj(x)
        return y, ladj.sum(dim=-1)


class CouplingTransform(Transform):
    r"""Transform via a coupling scheme.

    .. math:: \begin{cases}
            y_{<d} = x_{<d} \\
            y_{\geq d} = f(x_{\geq d}; x_{<d})
        \end{cases}

    Arguments:
        meta: A meta function which returns a transformation :math:`f`.
        d: The number of unaltered elements :math:`d`.
        dim: The dimension along which the elements are split.
    """

    bijective = True

    def __init__(
        self,
        meta: Callable[[Tensor], Transform],
        d: int,
        dim: int = -1,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.meta = meta
        self.d = d
        self.dim = dim

    @property
    def domain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    @property
    def codomain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    def _call(self, x: Tensor) -> Tensor:
        x0, x1 = x.tensor_split((self.d,), dim=self.dim)
        y1 = self.meta(x0)(x1)

        return torch.cat((x0, y1), dim=self.dim)

    def _inverse(self, y: Tensor) -> Tensor:
        x0, y1 = y.tensor_split((self.d,), dim=self.dim)
        x1 = self.meta(x0).inv(y1)

        return torch.cat((x0, x1), dim=self.dim)

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        x0, x1 = x.tensor_split((self.d,), dim=self.dim)
        _, y1 = y.tensor_split((self.d,), dim=self.dim)

        return self.meta(x0).log_abs_det_jacobian(x1, y1).flatten(self.dim).sum(dim=-1)

    def call_and_ladj(self, x: Tensor) -> Tuple[Tensor, Tensor]:
        x0, x1 = x.tensor_split((self.d,), dim=self.dim)
        y1, ladj = self.meta(x0).call_and_ladj(x1)

        return torch.cat((x0, y1), dim=self.dim), ladj.flatten(self.dim).sum(dim=-1)


class LULinearTransform(Transform):
    r"""Creates a transformation :math:`f(x) = LU x`.

    Arguments:
        LU: A matrix whose lower and upper triangular parts are the non-zero elements
            of :math:`L` and :math:`U`, with shape :math:`(*, D, D)`.
        dim: The dimension along which the product is applied.
    """

    bijective = True

    def __init__(
        self,
        LU: Tensor,
        dim: int = -1,
        **kwargs,
    ):
        super().__init__(**kwargs)

        I = torch.eye(LU.shape[-1]).to(LU)

        self.L = torch.tril(LU, diagonal=-1) + I
        self.U = torch.triu(LU, diagonal=+1) + I

        if hasattr(torch.linalg, 'solve_triangular'):
            self.solve = torch.linalg.solve_triangular
        else:
            self.solve = lambda A, B, **kws: torch.triangular_solve(B, A, **kws).solution

        self.dim = dim

    @property
    def domain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    @property
    def codomain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    def _call(self, x: Tensor) -> Tensor:
        shape = x.shape
        flat = shape[: self.dim] + (shape[self.dim], -1)

        return ((self.L @ self.U) @ x.reshape(flat)).reshape(shape)

    def _inverse(self, y: Tensor) -> Tensor:
        shape = y.shape
        flat = shape[: self.dim] + (shape[self.dim], -1)

        return self.solve(
            self.U,
            self.solve(
                self.L,
                y.reshape(flat),
                upper=False,
                unitriangular=True,
            ),
            upper=True,
            unitriangular=True,
        ).reshape(shape)

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return x.new_zeros(x.shape[: self.dim])


class PermutationTransform(Transform):
    r"""Creates a transformation that permutes the elements along a dimension.

    Arguments:
        order: The permutation order, with shape :math:`(*, D)`.
        dim: The dimension along which the elements are permuted.
    """

    bijective = True

    def __init__(self, order: LongTensor, dim: int = -1, **kwargs):
        super().__init__(**kwargs)

        self.order = order
        self.dim = dim

    def __repr__(self) -> str:
        order = self.order.tolist()

        if len(order) > 10:
            order = str(order[:5] + [...] + order[-5:]).replace('Ellipsis', '...')

        return f'{self.__class__.__name__}({order})'

    @property
    def domain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    @property
    def codomain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    def _call(self, x: Tensor) -> Tensor:
        return x.index_select(self.dim, self.order)

    def _inverse(self, y: Tensor) -> Tensor:
        return y.index_select(self.dim, torch.argsort(self.order))

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return x.new_zeros(x.shape[: self.dim])


class PixelShuffleTransform(Transform):
    r"""Creates a transformation that rearranges pixels into channels.

    See :class:`torch.nn.PixelShuffle` for a 2-d equivalent.

    Arguments:
        dim: The channel dimension.
    """

    bijective = True

    def __init__(self, dim: int = -3, **kwargs):
        super().__init__(**kwargs)

        self.dim = dim
        self.src = [i * 2 + 1 for i in range(dim + 1, 0)]
        self.dst = [i + dim + 1 for i in range(dim + 1, 0)]

    @property
    def domain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    @property
    def codomain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    def _call(self, x: Tensor) -> Tensor:
        space = ((s // 2, 2) for s in x.shape[self.dim + 1 :])
        space = (b for a in space for b in a)

        x = x.reshape(*x.shape[: self.dim], -1, *space)
        x = x.movedim(self.src, self.dst)
        x = x.flatten(self.dim * 2 + 1, self.dim)

        return x

    def _inverse(self, y: Tensor) -> Tensor:
        shape = self.inverse_shape(y.shape)

        y = y.unflatten(self.dim, [shape[self.dim]] + [2] * (abs(self.dim) - 1))
        y = y.movedim(self.dst, self.src)
        y = y.reshape(shape)

        return y

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        return x.new_zeros(x.shape[: self.dim])

    def forward_shape(self, shape: Size) -> Size:
        shape = list(shape)
        shape[self.dim] *= 2 ** (abs(self.dim) - 1)

        for i in range(self.dim + 1, 0):
            shape[i] //= 2

        return Size(shape)

    def inverse_shape(self, shape: Size) -> Size:
        shape = list(shape)
        shape[self.dim] //= 2 ** (abs(self.dim) - 1)

        for i in range(self.dim + 1, 0):
            shape[i] *= 2

        return Size(shape)


class DropTransform(Transform):
    r"""Creates a transformation that drops elements along a dimension.

    The :py:`log_abs_det_jacobian` method returns the log-density of the dropped
    elements :math:`z` within a distribution :math:`p(Z)`. The inverse transformation
    augments the dimension with a random variable :math:`z \sim p(Z)`.

    References:
        | Augmented Normalizing Flows: Bridging the Gap Between Generative Flows and Latent Variable Models (Huang et al., 2020)
        | https://arxiv.org/abs/2002.07101

    Arguments:
        dist: The distribution :math:`p(Z)`.
    """

    bijective = False

    def __init__(self, dist: Distribution, **kwargs):
        super().__init__(**kwargs)

        if dist.batch_shape:
            dist = Independent(dist, len(dist.batch_shape))

        assert dist.event_shape, "'dist' has to be multivariate"

        self.dist = dist
        self.dim = -len(dist.event_shape)
        self.d = dist.event_shape[0]

    @property
    def domain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    @property
    def codomain(self):
        return constraints.independent(constraints.real, abs(self.dim))

    def _call(self, x: Tensor) -> Tensor:
        z, x = x.tensor_split((self.d,), dim=self.dim)
        return x

    def _inverse(self, y: Tensor) -> Tensor:
        z = self.dist.sample(y.shape[: self.dim])
        return torch.cat((z, y), dim=self.dim)

    def log_abs_det_jacobian(self, x: Tensor, y: Tensor) -> Tensor:
        z, x = x.tensor_split((self.d,), dim=self.dim)
        return self.dist.log_prob(z)

    def forward_shape(self, shape: Size) -> Size:
        shape = list(shape)
        shape[self.dim] -= self.d
        return Size(shape)

    def inverse_shape(self, shape: Size) -> Size:
        shape = list(shape)
        shape[self.dim] += self.d
        return Size(shape)
