VERTICAL = '\u2502'
HORIZONTAL = '\u2500'
CRUCE = '\u253C'

def mostrar_tabla(data, m, l, b):
    print_header()
    for t, theta, dtheta in data[:5]:
        print_row(t, theta, dtheta)
    print("...")
    for t, theta, dtheta in data[-5:]:
        print_row(t, theta, dtheta)
    print()

def print_header():
    print(f' {"t":^4s} {VERTICAL} {"angulo":^10s} {VERTICAL} {"velocidad":^10s}')
    print(HORIZONTAL * 6, end="")
    print(CRUCE, end="")
    print(HORIZONTAL * 12, end="")
    print(CRUCE, end="")
    print(HORIZONTAL * 12)

def print_row(t, theta, dtheta):
    print(f' {t:>04.1f} {VERTICAL} {theta:10.6f} {VERTICAL} {dtheta:10.6f}')

