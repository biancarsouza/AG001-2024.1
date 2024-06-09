from sympy import Limit, Symbol, S 

c = 226 % 10
x = Symbol('x')

def function(x):
    return (((2 * x ** 2) - 7) / ((7 * x ** 5) - 2)) * (c + 1)

res1 = Limit(function(x), x, 1).doit()
res2 = Limit(function(x), x, S.Infinity).doit()
res3 = Limit(function(x), x, -S.Infinity).doit()

print('Respostas do exercício 1:')
print('a) O limite para x -> 1 é de {}.'.format(res1))
print('b) O limite para x -> +oo é de {}.'.format(res2))
print('c) O limite para x -> -oo é de {}.'.format(res3))