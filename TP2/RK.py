import numpy as np

def runge_kutta_4_segundo_orden(f, y_0, dy_0, h, t_min, t_max):
    y_n = y_0
    u_n = dy_0

    historial = [(0, y_n, u_n)]

    N = (t_max - t_min) / h
    for t in np.linspace(t_min + h, t_max, num=N, endpoint=True):
        k1 = f(y_n, u_n)
        q1 = u_n

        k2 = f(y_n + h * q1 / 2, u_n + h * k1 / 2)
        q2 = u_n + h * k1 / 2

        k3 = f(y_n + h * q2 / 2, u_n + h * k2 / 2)
        q3 = u_n + h * k2 / 2

        k4 = f(y_n + h * q3, u_n + h * k3)
        q4 = u_n + h * k3

        y_n_1 = y_n + (h / 6) * (q1 + 2 * q2 + 2 * q3 + q4)
        u_n_1 = u_n + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

        historial.append((t, y_n_1, u_n_1))
        y_n = y_n_1
        u_n = u_n_1

    return historial