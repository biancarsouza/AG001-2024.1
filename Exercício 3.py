from sympy import Integral, Symbol

c = 226 % 10
x = Symbol('x')

def f(x):
    return (5 * x ** 3) + ((x / 3) ** (3 / 5)) + ((3 / 4) * x) - (3 * c)

trabalho = Integral(f(x), (x, 3, 8)).doit()

print('Resposta do exercício 3:')
print('Trabalho realizado pela força correspondente sobre o objeto entre as posições x = 3 metros e x = 8 metros:', trabalho, 'joules.')