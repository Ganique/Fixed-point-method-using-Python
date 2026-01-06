# THE ITERATION OF THE FIXED POINT IS USED TO COMPUTE FIXED POINTS OF A FUNCTION

from sympy import symbols
import numpy as np
import math


tol = 1e-6 #  tolerance
maxIter = 200 #Maximun number of iterations

#The function g is the function where we want to compute a fixed point. This function can be changed depending on the function we are working on
def g(x):
    return math.sin(x)

#fixedPoint takes three arguments: a starting point x0, the tolerance tol that defines the desired accuracy for the fixed point approximation.
def fixedPoint(x0, tol, maxIter):
    iter = 0
    x = x0
    while iter < maxIter:
        x_new = g(x)
        if abs(x_new - x) < tol:
            exit1 = x_new
        x = x_new
        iter = iter + 1

    return (x, iter)
