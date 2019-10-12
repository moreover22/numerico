import math
from busquedaRaices import biseccion, newton_raphson

def polinomio(coeficientes):
    return lambda x: sum([coeficiente * x ** i for i, coeficiente in enumerate(coeficientes)])

def generar_funciones(n_personas=6):
    MASA_PERSONA = 75
    m_cabina = 400
    m = n_personas * MASA_PERSONA + m_cabina

    F = 1200

    n_pisos = 3
    ALTURA_POR_PISO = 2.5
    A, B = (0, n_pisos * ALTURA_POR_PISO)
    F_m = F / m

    tf = math.sqrt((6 * (B - A) * m) / F)
    a = polinomio([F_m, - 2 * (F_m / tf)])
    v = polinomio([0, F_m, - F_m / tf])
    x = polinomio([A, 0, F_m / 2, - (F_m / (3 * tf))])
    g = lambda t: x(t) - 0.28175 * B
    return tf, a, v, x, g


def mostrar_historial_nr(historial):
    print(f'{"n":^3} | {"p":^17s} | {"abs(p_n-p_n+1)":^17s}')
    print('-' * 40)
    print(f'{historial[0][0]:^3} | {historial[0][1]:^15.15f} | {"-":^12s} |')
    for i, p, e in historial[1:]:
        print(f'{i:^3} | {p:^15.15f} | {e:^10.10f} |')

def mostrar_historial_biseccion(historial):
    print(f'{"n":^3} | {"a":^7s} | {"b":^7s} | {"p":^7s} | {"f(p)":^7s} ')
    print('-' * 40)
    for i, a, b, p, f_p in historial:
        print(f'{i:^3} | {a:^5.5f} | {b:^5.5f} | {p:^5.5f} | {f_p:^5.5f} ')

def showTpCalculations(cantidadDePersonas):
    tf, _, v, _, g = generar_funciones(cantidadDePersonas)
    Dg = v
    semilla, historial_biseccion = biseccion(g, (0, tf), max_iteracion=2)
    mostrar_historial_biseccion(historial_biseccion)
    print(f'Semilla: {semilla: .5f}.\n')

    pf, historial = newton_raphson(g, Dg, semilla, tolerancia=1e-3)
    mostrar_historial_nr(historial)
    print(f'Tiempo hasta alcanzar el 30% de aceleración: {pf: .3f} s .')