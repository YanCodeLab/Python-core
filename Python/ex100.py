from random import randint
from time import sleep

def sorteio(lista):
     print('Sorteando os valores para a lista: ', end='', flush=True)
     for c in range(0,5):
       lista.append(randint(0,10))
       print(f'{lista[c]} ', end='', flush=True)
       sleep(0.4)
     print()


def soma_pares(numeros):
    soma = 0
    for p in numeros:
        if p % 2 == 0:
            soma += p

    print(f'Os valores pares de {numeros}, temos {soma}')


numbers = []
sorteio(numbers)
soma_pares(numbers)
