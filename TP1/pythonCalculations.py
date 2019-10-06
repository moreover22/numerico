from busquedaRaices import secante, newton_raphson, punto_fijo, biseccion
import matplotlib.pyplot as plt
import numpy as np
import math

F = 900
m = 475

A = 0
B = 9

xO = 0

tf = math.sqrt((6 * (B - A) * m) / F)

a = lambda t: (F / m) - 2 * (F / (m * tf)) * t
v = lambda t: (F / m) * t - (F/(m * tf))* t ** 2
x = lambda t: xO + (F / (2 * m)) * t ** 2 - (F / (3 * m * tf)) * t ** 3

secs = np.arange(0, 9, 0.5)


a_values = ()
v_values = ()
x_values = ()

print("aceleración")
a_values = list(map(a, secs))
print(a_values)


print("velocidad")
v_values = list(map(v, secs))
print(v_values)


print("posición")
x_values = list(map(x, secs))
print(x_values)

plt.plot(secs, a_values, label='Aceleración')
plt.plot(secs, v_values, label='Velocidad')
plt.plot(secs, x_values, label='Posición')
plt.legend()
plt.xlabel('Tiempo')
plt.title('Gráfico de funciones aceleración, velocidad y posición')
plt.show()
