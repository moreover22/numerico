from funciones import showTpCalculations

def main():
    for n_personas in [0, 3, 6]:
        print(f'Para {n_personas} personas:')
        showTpCalculations(n_personas)    

if __name__ == "__main__":
    main()