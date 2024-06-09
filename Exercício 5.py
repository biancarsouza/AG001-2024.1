from sympy import Symbol, solve, sin, exp
import math

c = 226 % 10

def eq1(x):
    return (exp(x - 3)) + (exp(x - 1)) + (exp(x))

def eq2(y):
    return (y ** 4) - (4 * (y ** 3)) + (3 * y)

def eq3(z):
    return 4 * sin((c + 1) * z)

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

resultado_eq1 = solve(eq1(x) - (c + 1), x)
resultado_eq2 = solve(eq2(y) - c, y)
resultado_eq3 = solve(eq3(z) - (- 2), z)

print('Equação 1:', resultado_eq1)
print('Equação 2:', resultado_eq2)
print('Equação 3:', resultado_eq3)