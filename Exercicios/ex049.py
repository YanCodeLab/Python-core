#Tabuada
from time import sleep
print('TABUADA')
n = int(input('Digite um numero:'))
f = int(input('Digite o final da tabuada:'))
for c in range (0, f+1):
   r = n * c
   print(f'{n} x {c} = {r}')
   sleep(1) 