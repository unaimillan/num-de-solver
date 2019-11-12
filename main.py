#!/bin/python3
import tkinter as tk
import tkinter.ttk
import matplotlib.pyplot as plt
import math
from solvers.exact import Exact
from solvers.euler import Euler
from solvers.improved_euler import ImprovedEuler
from solvers.runge_kutta import RungeKutta

"""
5 textfields:
x0, y0, X, N
N_i, N_f

1 button or make reactive
4 checkbox: turn on/off
Exact, Euler, Improved Euler, Runge-Kutta

3 plots:
solution, pointwise_error, total_approximation_error
"""

"""
root = tk.Tk()
app = tk.Frame()
app.mainloop()
"""

if __name__ == "__main__":
    X = 3
    ex = Exact(0, math.sqrt(0.5), X)
    eu = Euler(0, math.sqrt(0.5), X)
    ieu = ImprovedEuler(0, math.sqrt(0.5), X)
    rk = RungeKutta(0, math.sqrt(0.5), X)

    n = 25
    x = ex.x_list(n)
    y1 = ex.solve(n)
    y2 = eu.solve(n)
    y3 = ieu.solve(n)
    y4 = rk.solve(n)

    plt.plot(x, y1, label="exact")
    plt.plot(x, y2, label="euler")
    plt.plot(x, y3, label="improved euler")
    plt.plot(x, y4, label="runge kutta")
    plt.legend()
    plt.show()
