import numpy as np

from solvers.exact import Exact


class Euler(Exact):

    def solve(self, n: int) -> np.array:
        t = self.x_list(n)
        y = np.full(n, self.y0)
        step = self.step(n)

        for i in range(1, n):
            y[i] = y[i - 1] + step * self.derivative(t[i - 1], y[i - 1])
        return y
