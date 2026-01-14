#Analisando Numeros
from time import sleep
print(40*'=-')
print('ANALISANDO NUMEROS')
print(40*'=-')
sleep(1) # Delay
n1 = int(input('Digite um numero inteiro:')) # Recebe numero 
sleep(1)
n2 = int(input('Digite um numero inteiro:')) # Recebe segundo numero
sleep(1) 
if n1 > n2: # se n1 for maior que n2
    print(f'O numero {n1} é maior do que o numero {n2}')
elif n1 < n2: # Se n1 for menor que n2
    print(f'O numero {n2} é maior do que o numero {n1}')
else: # se não
    print(f'Os numeros são Iguais')