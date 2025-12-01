import numpy as np
from sympy import diff, cos, sin, pi, evalf, Symbol, lambdify, integrate
from scipy import integrate as sp_integrate
import matplotlib.pyplot as plt
import time
#fghh
def riemann_method(func, a: float, b: float, n: int) -> float:
    """
    [a, b] - interval
    n - number of subintervals in the partition. points in them are chosen randomly
    func = cos(x), for example, where x = Symbol("x")
    Must return the approximate value of the integral of 'func' on [a, b]
    """
    #Тут має бути ваш код
    pass

def trapezoidal_method(func, a: float, b: float, n: int) -> float:
    """
    [a, b] - interval
    n - number of subintervals in the partition (all should be the same size)
    func = 1/x, for example, where x = Symbol("x")
    Must return the approximate value of the integral of 'func' on [a, b]
    """
    #Тут має бути ваш код
    pass
def easy_sci_py(func, a: float, b: float) -> float:
    """
    Computes the integral using SciPy's quad() method
    func = tg(x), for example, where x = Symbol("x")
    Must return highly accurate approximation of the integral
    """
    #Тут має бути ваш код
    pass

def compare_accuracy(func, a: float, b: float, n: int):
    """
    Compares the real integral value and the one received from two upper functions.
    """
    #Тут має бути ваш код
    pass

def compare_time(func, a, b, n_values):
  """ Compare speed of calculating by Rimman and Trapezoid"""
  #Тут має бути ваш код
  pass

def get_plot_of_error(func, a: float, b: float):
    """
    Consider different n to see the error decrease, then plot the result
    """
    #Тут має бути ваш код
    pass
