from busquedaRaices import secante, newton_raphson, punto_fijo, biseccion
import matplotlib.pyplot as plt

F = 900
m = 475
tf = 9

xO = 0

a = lambda t: (F / m) - 2 * (F / (m * tf)) * t
v = lambda t: (F / m) * t - (F/(m * tf))* t ** 2
x = lambda t: xO + (F/2*m) * t ** 2 - (F / (3 * m * tf)) * t ** 3


secs = [0, 0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9]

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

plt.plot(a_values, v_values, x_values)
plt.show()