from sympy import Integral, Derivative, Symbol

c = 226 % 10
x = Symbol('t')

def v(t):
    return (5 * c) + (7 * t ** 4) + (t ** (1 / 3)) - (3 * c * t ** 3)

aceleracao = Derivative(v(x), x).doit()
deslocamento = Integral(v(x), x).doit()

print('Respostas do exercício 2:')
print('Equação de deslocamento:', deslocamento, '.')
print('Deslocamento de t = 1 segundo a t = 7 segundos:', deslocamento.subs({x: 7}) - deslocamento.subs({x: 1}), '.')
print('Equação de aceleração:', aceleracao, '.')