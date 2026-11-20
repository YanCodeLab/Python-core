from rich import print
from poligono import *

def main():

    p1 = Circulo(20) # Instacia do obj
    print(f'Perimetro = {p1.perimetro():.2f}')
    print(f'Área = {p1.area():.2f}')

    print()  # Pular linha

    p2 = Quadrado(10) # Instacia do obj
    print(f'Perimetro = {p2.perimetro():.2f}')
    print(f'Área = {p2.area():.2f}')

if __name__ == "__main__":
    main()
