from functools import lru_cache

import numpy as np

from solvers.exact import Exact


class RungeKutta(Exact):

    @lru_cache(maxsize=4096)
    def solve(self, n: int) -> np.array:
        t = self.x_list(n)
        y = np.full(n, self.y0)
        step = self.step(n)

        for i in range(1, n):
            k1 = step * self.derivative(t[i - 1], y[i - 1])
            k2 = step * self.derivative(t[i - 1] + step / 2, y[i - 1] + k1 / 2)
            k3 = step * self.derivative(t[i - 1] + step / 2, y[i - 1] + k2 / 2)
            k4 = step * self.derivative(t[i - 1] + step, y[i - 1] + k3)

            y[i] = y[i - 1] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        return y
