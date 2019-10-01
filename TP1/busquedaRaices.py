def punto_medio(a, b):
    """ Dado dos puntos de la recta real, devuelve
    el punto medio.
    """
    return (a + b) / 2

def error_relativo(p, p_anterior):
    return error(p, p_anterior) / abs(p)

def error(p, p_anterior):
    return abs(p - p_anterior)

def biseccion(f, intervalo, tolerancia=1e-2, max_iteracion=100):
    """ Busca la raiz de f en el intervalo mediante el método de biseccion.
    f: función que recibe un número y devuelve un número.
    intervalo: tupla que representa un intervalo donde f es continua.
    tolerancia: cota del error que se comete con el método.
    max_iteracion: cantidad máxima de iteraciones que realizará 
    la función antes de cortar. 
    """
    historial = []
    a, b = intervalo
    p = punto_medio(a, b)
    
    for iteracion in range(max_iteracion):
        historial.append((iteracion + 1, a, b, p, f(p)))
        if f(a) * f(p) < 0: b = p
        if f(p) * f(b) < 0: a = p        
        p_anterior = p
        p = punto_medio(a, b)
        if error_relativo(p, p_anterior) < tolerancia:
            break
    return p, historial

def punto_fijo(g, semilla, tolerancia=1e-2, max_iteracion=100):
    """ Metodo para buscar punto fijo de g desde la semilla.
    g: funcion que se le buscará el punto fijo.
    semilla: número inicial para iterar.
    tolerancia: cota de error.
    max_iteraciones: máxima cantidad de iteraciones.
    """
    historial = []
    p = semilla
    for iteracion in range(max_iteracion):
        p_proximo = g(p)
        historial.append((iteracion + 1, p, error_relativo(p_proximo, p)))
        if error(p_proximo, p) < tolerancia:
            break
        p = p_proximo
    return p, historial

def newton_raphson(f, Df, semilla, tolerancia=1e-2, max_iteracion=100):
    """ Busca la raiz de f desde la semilla con el método de Newton-Raphson.
    f: función que se le buscará la raiz.
    Df: es la función derivada de f.
    semilla: número inicial para iterar.
    tolerancia: cota de error.
    max_iteraciones: máxima cantidad de iteraciones.
    """
    historial = []
    p = semilla
    for iteracion in range(max_iteracion):
        p_anterior = p
        p = p - f(p) / Df(p)
        historial.append((iteracion + 1, p_anterior, error_relativo(p, p_anterior)))
        if error_relativo(p, p_anterior) < tolerancia:
            break
    return p, historial

def pendiente_secante(f, abscisa_1, abscisa_2):
    """ Devuelve la pendiente de la recta secante a f
    que pasa por los puntos de abscisa_1 y abscisa_2.
    f: función que recibe un número como parametro y devuelve un número.
    abscisa_1 | abscisa_2: son números que pertenecen al dominio de f.
    """
    dy = f(abscisa_1) - f(abscisa_2)
    dx = abscisa_1 - abscisa_2
    return dy / dx

def secante(f, semilla_1, semilla_2, tolerancia=1e-2, max_iteracion=100):
    """ Busca la raiz de f desde la semilla con el método de las secantes.
    f: función que se le buscará la raiz.
    semilla_1 | semilla_2: números iniciales para iterar.
    tolerancia: cota de error.
    max_iteraciones: máxima cantidad de iteraciones.
    """
    historial = []
    p_anterior = semilla_2
    p = semilla_1

    for iteracion in range(max_iteracion):
        p_siguiente = p - f(p) / pendiente_secante(f, p, p_anterior)
        historial.append((iteracion + 1, p, error_relativo(p_siguiente, p)))
        if error_relativo(p_siguiente, p) < tolerancia:
            break
        p = p_siguiente
    return p, historial
