import math
import datetime

def f(w):
    return 2*(w**3) - 5

def f(x):
    return 2 * x + 5

def g(func, *arg):
    return math.cos(func/2) - 3 * func
    
def square(x):
    return x**2

def fourth(func, *arg):
    return func ** func

def g2(x):
    return 2 * x + 8

def f2(x):
    return math.tan(x) - 2/x

def derivative(x):
    ''' f(x) = x^2 - x + 3 '''
    return 2 * x - 1

def list_():
    return [n for n in range(10) if n % 2]

def date_():
    return datetime.datetime(1970,1,1).strftime("%Y-%d-%B")
