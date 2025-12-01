import numpy as np
from sympy import diff, cos, sin, pi, evalf, Symbol, lambdify, integrate
from scipy import integrate as sp_integrate
import matplotlib.pyplot as plt
import time


def riemann_method(func, a: float, b: float, n: int) -> float:
    """
    [a, b] - interval
    n - number of subintervals in the partition.
    func = cos(x), for example, where x = Symbol("x")
    Must return the approximate value of the integral of 'func' on [a, b]
    
    This version uses the midpoint of each subinterval instead of a random point.
    """
    x = Symbol('x')
    f = lambdify(x, func, 'numpy')
    width = (b - a) / n
    result = 0
    for i in range(n):
        x_i = a + (i + 0.5) * width
        result += f(x_i) * width

    return result

def trapezoidal_method(func, a: float, b: float, n: int) -> float:
    """
    [a, b] - interval
    n - number of subintervals in the partition (all should be the same size)
    func = 1/x, for example, where x = Symbol("x")
    Must return the approximate value of the integral of 'func' on [a, b]
    """
    x = Symbol('x')
    f = lambdify(x, func, 'numpy')
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h


def easy_sci_py(func, a: float, b: float) -> float:
    """
    Computes the integral using SciPy's quad() method
    func = tg(x), for example, where x = Symbol("x")
    Must return highly accurate approximation of the integral
    """
    x = Symbol('x')
    f = lambdify(x, func, 'numpy')
    result, _ = sp_integrate.quad(f, a, b)
    return result


def compare_accuracy(func, a: float, b: float, n: int):
    """
    Compares the real integral value and the one received from two upper functions.
    """
    x = Symbol('x')
    real_value = integrate(func, (x, a, b)).evalf()
    riemann_value = riemann_method(func, a, b, n)
    trapezoid_value = trapezoidal_method(func, a, b, n)
    scipy_value = easy_sci_py(func, a, b)
    print(f"Real value (SymPy): {real_value}")
    print(f"Riemann method: {riemann_value} | Error: {abs(real_value - riemann_value)}")
    print(f"Trapezoidal method: {trapezoid_value} | Error: {abs(real_value - trapezoid_value)}")
    print(f"SciPy quad: {scipy_value} | Error: {abs(real_value - scipy_value)}")


def compare_time(func, a, b, n_values):
    """
    Compare speed of calculating by Rimman and Trapezoid
    """
    riemann_times = []
    trapezoid_times = []

    for n in n_values:
        start = time.time()
        riemann_method(func, a, b, n)
        riemann_times.append(time.time() - start)
        start = time.time()
        trapezoidal_method(func, a, b, n)
        trapezoid_times.append(time.time() - start)
        
    plt.plot(n_values, riemann_times, label="Riemann")
    plt.plot(n_values, trapezoid_times, label="Trapezoid")
    plt.xlabel("n")
    plt.ylabel("Time (seconds)")
    plt.title("Time comparison")
    plt.legend()
    plt.show()


def get_plot_of_error(func, a: float, b: float):
    """
    Consider different n to see the error decrease, then plot the result
    """
    x = Symbol('x')
    real_value = float(integrate(func, (x, a, b)))
    n_values = np.arange(10, 1000, 20)
    riemann_errors = []
    trapezoid_errors = []
    for n in n_values:
        riemann_errors.append(abs(real_value - riemann_method(func, a, b, n)))
        trapezoid_errors.append(abs(real_value - trapezoidal_method(func, a, b, n)))

    plt.plot(n_values, riemann_errors, label="Riemann error")
    plt.plot(n_values, trapezoid_errors, label="Trapezoid error")
    plt.yscale("log")
    plt.xlabel("n")
    plt.ylabel("Error")
    plt.title("Error vs number of subintervals (n)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    x = Symbol("x")
    func = cos(x)

    print("\n-ЛЕГІТ ТОЧНІСТЬ")
    compare_accuracy(func, 0, pi, 100)
    print("\nЛЕГІТ ЧАС")
    compare_time(func, 0, pi, [10, 50, 100, 500, 1000, 3000])
    print("\n--- ERROR PLOT ---")
    get_plot_of_error(func, 0, pi)
