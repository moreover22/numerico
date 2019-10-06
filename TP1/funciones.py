import matplotlib.pyplot as plt
import numpy as np
import math

def polinomio(coeficientes):
    return lambda x: sum([coeficiente * x ** i for i, coeficiente in enumerate(coeficientes)])

def evaluar_funciones(secs, a, v, x):
	return list(map(a, secs)), list(map(v, secs)), list(map(x, secs))

def generar_funciones():
    F = 900
    n = 4
    m_personas = 75
    m_cabina = 100
    m = n * m_personas + m_cabina
    A, B = (0, 9)
    F_m = F / m

    tf = math.sqrt((6 * (B - A) * m) / F)
    a = polinomio([F_m, - 2 * (F_m / tf)])
    v = polinomio([0, F_m, - F_m / tf])
    x = polinomio([A, 0, F_m / 2, - (F_m / (3 * tf))])
    return tf, a, v, x

def graficar(secs, a_values, v_values, x_values):
	plt.plot(secs, a_values, label='Aceleración')
	plt.plot(secs, v_values, label='Velocidad')
	plt.plot(secs, x_values, label='Posición')
	plt.legend()
	plt.xlabel('Tiempo')
	plt.title('Gráfico de funciones aceleración, velocidad y posición')
	plt.show()


def main():
    tf, a, v, x = generar_funciones()
    secs = np.arange(0, tf, 0.25)
    a_values, v_values, x_values = evaluar_funciones(secs, a, v, x)

    print("aceleración")
    print(a_values)
    print("velocidad")
    print(v_values)
    print("posición")
    print(x_values)
	
    print(f'100% ac: {a(0)}, {a(0.35 * tf)}')
    graficar(secs, a_values, v_values, x_values)

if __name__ == "__main__":
    main()