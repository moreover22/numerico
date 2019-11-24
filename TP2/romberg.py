import numpy as np

def romberg(f, a, b, e=1E-8):
    R = [[R_0_0(f, a, b)]]
    i = 1
    while True:
        R.append([None] * (i + 1))
        R[i][0] = R_i_0(f, a, b, i, R)

        for j in range(1, i + 1):
            R[i][j] = R_i_j(i, j, R)

        if abs(R[i][i - 1] - R[i][i]) < e:
            return R[i][i]
        i += 1


def _h(i, a, b):
    return (b - a) / 2 ** i

def R_0_0(f, a, b):
    return 0.5 * (b - a) * (f(a) + f(b))

def R_i_0(f, a, b, i, R):
    suma = 0
    h_i = _h(i, a, b)
    for k in range(1, 2 ** (i - 1) + 1):
        suma += f(a + (2 * k - 1) * h_i)
    return 0.5 * R[i - 1][0] + h_i * suma

def R_i_j(i, j, R):
    return ((4 ** j) * R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1) 


def romberg_por_valores(tiempos, valores):
    resultado = {}
    for i, tiempo in enumerate(tiempos):
        nuevo_indice = round(tiempo * 10)
        resultado[nuevo_indice] = valores[i]

    def funcion(i):
        entero = round(i * 10)
        entero_par = entero + entero % 2
        return abs(resultado[entero_par])
    
    return romberg(funcion, tiempos[0], tiempos[-1])