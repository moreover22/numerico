import numpy as np
from math import sin, radians
from RK import runge_kutta_4_segundo_orden
from tabla import mostrar_tabla
from grafico import empezar_grafico, graficar, cargar_grafica
from romberg import romberg_por_valores, romberg

def pendulo_amortiguado(m, l, b, angulo_0, velocidad_0, t_min, t_max, orden, h=0.2, g=9.81):
    aceleracion = lambda angulo, velocidad: -(b / m) * velocidad - (g / l) * sin(angulo)
    angulo_0 = radians(angulo_0)
    velocidad_0 = radians(velocidad_0)
    data = np.array(runge_kutta_4_segundo_orden(aceleracion, angulo_0, velocidad_0, h, t_min, t_max))
    mostrar_tabla(data, m, l, b)
    data = np.array(runge_kutta_4_segundo_orden(aceleracion, angulo_0, velocidad_0, 0.01, t_min, t_max))
    tiempos = data[:, 0]
    angulos = data[:, 1]
    print("Aproximación de la integral del módulo del ángulo: ", end="")
    print(romberg_por_valores(tiempos, angulos))
    cargar_grafica(data, m, l, b, orden)
    
empezar_grafico()
pendulo_amortiguado(1, 1, 0, 30, 0, 0, 20, 1, 0.2)
pendulo_amortiguado(1, 1, 0.5, 30, 100, 0, 20, 2, 0.2)

graficar()