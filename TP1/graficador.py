from funciones import generar_funciones
import matplotlib.pyplot as plt
import numpy as np
from sys import argv

def evaluar_funciones(secs, a, v, x):
	return list(map(a, secs)), list(map(v, secs)), list(map(x, secs))

def graficar(secs, a_values, v_values, x_values):
    plt.plot(secs, a_values, label='Aceleración')
    plt.plot(secs, v_values, label='Velocidad')
    plt.plot(secs, x_values, label='Posición')
    plt.legend()
    plt.xlabel('Tiempo')
    plt.title('Gráfico de funciones aceleración, velocidad y posición')
    plt.show()

def main(n_personas):
    tf, a, v, x, _ = generar_funciones(n_personas)
    secs = np.arange(0, tf, 0.25)
    a_values, v_values, x_values = evaluar_funciones(secs, a, v, x)

    print("aceleración")
    print(a_values)
    print("velocidad")
    print(v_values)
    print("posición")
    print(x_values)

    graficar(secs, a_values, v_values, x_values)

if __name__ == "__main__":
    n_personas = int(argv[1])
    main(n_personas)