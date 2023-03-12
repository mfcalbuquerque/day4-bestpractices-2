"""
A collection of simple math operations.
"""

def simple_add(a,b):
    """ 
    Adds two number: a+b.

    E.g.: simple_add(a,b)

    Returns: a number 
    """
    return a+b

def simple_sub(a,b):
    """ 
    Subtracts two numbers: a-b.

    E.g.: simple_sub(a,b)

    Returns: a number 
    """
    return a-b

def simple_mult(a,b):
    """ 
    Multiplies two numbers: a*b.

    E.g.: simple_mult(a,b)

    Returns: a number 
    """
    return a*b

def simple_div(a,b):
    """ 
    Divides two numbers: a/b. b should not be 0: this operation doesn't exist!

    E.g.: simple_div(a,b)

    Returns: a number 
    """
    return a/b

def poly_first(x, a0, a1):
    """ 
    First order polynomial: a1 + a0*x.

    E.g.: poly_first(x,a0,a1), where a0 and a1 are regular parameters, and x can be a list or sequence of numbers.

    Returns: a number 
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """ 
    Second order polynomial: a2 + a1*x + a0**x. It calls poly_first() when returning.

    E.g.: poly_second(x,a0,a1,a2), where a0, a1 and a2 are regular parameters, and x can be a list or sequence of numbers.

    Returns: a number 
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
