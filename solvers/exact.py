import numpy as np
import math
from functools import lru_cache


class Exact:
    @staticmethod
    @lru_cache(maxsize=4096)
    def default_derivative(x: float, y: float):
        return x * y - x * y ** 3

    """
    slope: y'(x)=f(x, y)
    x0, y0, X, N_initial
    N_final
    """

    def __init__(self, x0, y0, X):
        self.derivative = Exact.default_derivative
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.coef = self._get_coefficient()

    def x_list(self, n: int) -> np.array:
        return np.linspace(self.x0, self.X, num=n)

    def step(self, n: int) -> float:
        return (self.X - self.x0) / n

    # TODO: clarify way of super().solution for euler at el.
    def solve(self, n: int) -> np.array:
        # Apply vectorized '_exact_at' to each x point
        vfunc = np.vectorize(self._exact_at)
        return vfunc(self.x_list(n))

    def pointwise_error(self, n: int) -> np.array:
        """
        Return array of absolute (<cur_method>.solve - exact.solve)
        """
        return np.abs(self.solve(n) - self.__solve(n))

    def total_approximation_error(self, n_i: int, n_f: int):
        """
        Return list of maxs of pointwise errors for each n
        in range of ns: n_i to n_f
        """
        ns = np.arange(n_i, n_f)
        # TODO: recheck, that we take maximum of errors for current method
        vfunc = np.vectorize(lambda n: np.max(self.pointwise_error(n)))
        return vfunc(ns)

    """
    Exact solution specific functions
    """
    # We introduce __solve, to preserve _exact__solve among inheritance
    # 'name mangling' feature
    __solve = solve

    def _get_coefficient(self) -> float:
        return ((math.e ** (self.x0 ** 2 / 2)) / self.y0) ** 2 \
               - math.e ** (self.x0 ** 2)

    def _exact_at(self, x: float):
        return math.e ** (x ** 2 / 2) / \
               math.sqrt(self.coef + math.e ** (x ** 2))
