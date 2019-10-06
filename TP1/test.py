from busquedaRaices import secante, newton_raphson, punto_fijo, biseccion

# print(
# """ _______________
#     Secante
# """)
# f = lambda x: 4 * x ** 4 - x ** 2 + 2 * x - 3
# pf, historial = secante(f, 0.8, 1.0)
# for i, p, e in historial:
#     print(f'{i:^3} | {p:^15.15f} | {e:^5.5f} |')

# print(
# """ _______________
#     Newton-Raphson
# """)
# f = lambda x: 4 * x ** 4 - x ** 2 + 2 * x - 3
# Df = lambda x: 16 * x ** 3 - 2 * x + 2
# pf, historial = newton_raphson(f, Df, 0.9)
# for i, p, e in historial:
#     print(f'{i:^3} | {p:^15.15f} | {e:^5.5f} |')

# import math

# print(
# """ _______________
#     Punto fijo
# """)
# g = lambda x: math.e ** (0.25 * x)
# pf, historial = punto_fijo(g, 4)
# for i, p, e in historial:
#     print(f'{i:^3} | {p:^15.15f} | {e:^5.5f} |')

# print(
# """ _______________
#     Biseccion
# """)
# f = lambda x: 1 + math.sin(x) - x ** 0.5
# cero, historial = biseccion(f, (1, 4))
# for i, a, b, p, f_ in historial:
#     print(f'{i:^3} | {a:^5.5f} | {b:^5.5f} | {p:^15.15f} | {f_:^10.5f} |')


f = lambda x: x ** 3 - 2 * x
Df = lambda x: 3 * x ** 2 - 2

print(
""" _______________
    Secante
""")
pf, historial = secante(f, 1, 2)
for i, p, e in historial:
    print(f'{i:^3} | {p:^15.15f} | {e:^5.5f} |')

print(
""" _______________
    Newton-Raphson
""")

pf, historial = newton_raphson(f, Df, 1.5)
for i, p, e in historial:
    print(f'{i:^3} | {p:^15.15f} | {e:^5.5f} |')

import math

print(
""" _______________
    Punto fijo
""")
g = lambda x: x ** 3 / 2
pf, historial = punto_fijo(g, 1.4)
for i, p, e in historial:
    print(f'{i:^3} | {p:^15.15f} | {e:^5.5f} |')

print(
""" _______________
    Biseccion
""")
cero, historial = biseccion(f, (1, 2))
for i, a, b, p, f_ in historial:
    print(f'{i:^3} | {a:^5.5f} | {b:^5.5f} | {p:^15.15f} | {f_:^10.5f} |')
