import numpy as np
from sympy import cos, sin, pi, Symbol, lambdify, integrate
from scipy.integrate import quad
import matplotlib.pyplot as plt
import time
print(f'\033[32m')


def riemann_method(func, a: float, b: float, n: int) -> float:
    """
    Метод Рімана (середні точки)
    """
    f = lambdify(Symbol('x'), func, 'numpy')
    width = (b - a) / n
    return sum(f(a + (i + 0.5) * width) * width for i in range(n))


def trapezoidal_method(func, a: float, b: float, n: int) -> float:
    """
    Метод трапецій
    """
    f = lambdify(Symbol('x'), func, 'numpy')
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b)) + sum(f(a + i*h) for i in range(1, n))
    return result * h


def easy_sci_py(func, a: float, b: float) -> float:
    """
    Обчислення інтеграла за допомогою SciPy
    """
    f = lambdify(Symbol('x'), func, 'numpy')
    result, _ = quad(f, a, b)
    return result

def compare_accuracy(func, a: float, b: float, n: int):
    real_value = float(integrate(func, (Symbol('x'), a, b)))
    r_val = riemann_method(func, a, b, n)
    t_val = trapezoidal_method(func, a, b, n)
    s_val = easy_sci_py(func, a, b)

    print(f"\nФункція: {func}")
    print(f"Точне значення (SymPy): {real_value}")
    print(f"Метод Рімана: {r_val}  Похибка: {abs(real_value - r_val)}")
    print(f"Метод трапецій: {t_val}  Похибка: {abs(real_value - t_val)}")
    print(f"SciPy quad: {s_val}  Похибка: {abs(real_value - s_val)}")

def compare_time(func, a: float, b: float, n_values):
    riemann_times = []
    trapezoid_times = []

    for n in n_values:
        start = time.time()
        riemann_method(func, a, b, n)
        riemann_times.append(time.time() - start)

        start = time.time()
        trapezoidal_method(func, a, b, n)
        trapezoid_times.append(time.time() - start)

    plt.plot(n_values, riemann_times, label="Метод Рімана", marker='o')
    plt.plot(n_values, trapezoid_times, label="Метод трапецій", marker='x')
    plt.xlabel("Кількість підінтервалів (n)")
    plt.ylabel("Час (секунди)")
    plt.title("Порівняння швидкодсті методів")
    plt.show()

def get_plot_of_error(func, a: float, b: float):
    real_value = float(integrate(func, (Symbol('x'), a, b)))
    n_values = np.arange(10, 1000, 20)
    errors = [abs(trapezoidal_method(func, a, b, n) - real_value) for n in n_values]

    plt.plot(n_values, errors)
    plt.yscale("log")
    plt.xlabel("Кількість підінтервалів (n)")
    plt.ylabel("Абсолютна похибка")
    plt.title(f"Похибка методу трапецій для {func} (O(1/n²))")
    plt.show()

if __name__ == "__main__":
    x = Symbol("x")
    functions = [
        (sin(x), 0, pi),
        (x**2, 0, 3),
        (1/x, 1, 5),
        (x**3 , 1, -10)
    ]

    print("=== ПОРІВНЯННЯ ТОЧНОСТІ ===")
    for func, a, b in functions:
        compare_accuracy(func, float(a), float(b), 200)

    print("\n=== ПОРІВНЯННЯ ШВИДКОДІЇ ===")
    compare_time(cos(x), 0, float(pi), [10, 50, 100, 500, 1000, 3000])

    print("\n=== ГРАФІКИ ПОХИБКИ (МЕТОД ТРАПЕЦІЙ) ===")
    for func, a, b in functions:
        print(f"\nФункція: {func}")
        get_plot_of_error(func, float(a), float(b))
