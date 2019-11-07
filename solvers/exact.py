import numpy as np
import math


class Exact:
    @staticmethod
    def default_derivative(x: float, y: float):
        return x*y-x*y**3

    """
    slope: y'(x)=f(x, y)
    x0, y0, X, N_initial
    N_final
    """

    """
    3 plots:
    solution, ith_step_error, total_approximation_error
    """

    def __init__(self, x0,y0, X):
        self.derivative = Exact.default_derivative
        self.x0 = x0
        self.y0 = y0
        self.X = X
        self.coef = self.get_coefficient()

    def get_coefficient(self):
        return ( (math.e**(self.x0**2/2)) / self.y0 )**2 - math.e**(self.x0**2)

    def default_exact(self, x: float):
        return math.e**(x**2/2) / math.sqrt(self.coef + math.e**(x**2))

    def solution(self, N):
        pass

    def pointwise_error(self, N):
        raise NotImplementedError

    def total_approximation_error(self, N_i, N_f):
        raise NotImplementedError
