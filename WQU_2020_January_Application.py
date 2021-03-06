import math
#from WQU_2020_January_Application import f, f2, g3
def f(w):
    '''A function to calculate a value using the equation
f(w) = 2w^3 - 5'''
    return (((2*w)**3)-5)

def g(x):
    '''A function to calculate a value using the equation
g(x) = cos(x/2) - 3x'''
    #import math
    return ((math.cos(x/2)) - 3*x)

def f(x):
    #import math
    return ((2*x)+5)
    
def g2():
    '''A function to calculate an equation
 using the equation'''
    #import math
    import WQU_2020_January_Application.f
    y = 2*x + 5
    z = ((math.cos(y/2)) - 3*y)
    return z

def f2(x):
    return math.tan(x) - (2/x)

def g3(x):
    return (x**2) + 8

def FxGx():
    '''A function that multiplies two
functions (f2(x) and g3(x)) together'''
    import WQU_2020_January_Application.f2
    import WQU_2020_January_Application.g3
    yy = f2(x) * g3(x)
    return yy

