# Replace the "ANSWER HERE" for your answer
def roots(a, b, c):
    discr = b**2 - 4*a*c
    if discr > 0:
        root1 = (-b + discr**0.5) / (2*a)
        root2 = (-b - discr**0.5) / (2*a)
        return f"({root1}, {root2})"
    elif discr == 0:
        root = -b / (2*a)
        return f"({root})"
    else:
        return f"( )"

def value_y(a, b, c, x):
    y = a*x**2 + b*x + c
    return y


def to_string(a, b, c):
    if a != 0 and b != 0 and c != 0:
        cuadratica = f"f(x) = {a} * X^2 + {b} * X + {c}"  
    elif a == 0 and b != 0 and c != 0:
        cuadratica = f"f(x) = {b} * X + {c}"
    return cuadratica
    

def derivation(a, b, c):
    if a != 0:
        derivada = f"f'(x) = {2*a} * X + {b}"
        return derivada
    elif a == 0 and b != 0:
        derivada = f"f'(x) = {b}"
        return derivada
    elif a == 0 and b == 0:
        derivada = f"f'(x) = 0"
        return derivada
    else:
        derivada = f"f'(x) = {2*a} * X"
        return derivada

