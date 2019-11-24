import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
from math import degrees

def empezar_grafico():
    plt.figure("Péndulo amortizado - TP2 numérico")

def cargar_grafica(data, m, l, b, orden):
    tiempo = data[:, 0]
    angulo = np.degrees(data[:, 1])
    velocidad = np.degrees(data[:, 2])

    plt.subplot(2, 1, orden)
    plt.plot(tiempo, angulo, label='angulo')
    plt.plot(tiempo, velocidad, label='velocidad')

    plt.xlabel('tiempo [s]')
    plt.ylabel(r'$\theta$ [deg] y $\dot{\theta}$ [deg/s]')
    plt.title(f'Péndulo - masa = {m} long = {l} b = {b}')
    plt.legend()

def graficar():
    plt.tight_layout()
    plt.show()