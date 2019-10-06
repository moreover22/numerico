from busquedaRaices import newton_raphson, biseccion
from funciones import generar_funciones


def main():
    tf, _, v, x = generar_funciones()

    t_30 = 0.35 * tf # tiempo en que se alcanza 30% de aceleración
    g = lambda t: x(t) - x(t_30)
    Dg = v
    semilla, _ = biseccion(g, (0, tf), max_iteracion=1)
    pf, historial = newton_raphson(g, Dg, semilla, tolerancia=1e-4)
    for i, p, e in historial:
        print(f'{i:^3} | {p:^15.15f} | {e:^10.10f} |')
    print(f'Tiempo que tarda en alcanzar el 30% de aceleración: {pf: .2f} s .')

    
if __name__ == "__main__":
    main()