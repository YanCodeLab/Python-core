#Progresão Aritmetica (P.A)
from time import sleep # Importa comando para delay
print('-=' * 50) #Linha
print('10 TERMOS DE UMA P.A')
print('-=' * 50) #Linha
termo = int(input('Digite o Primeiro Termo da P.A: ')) # Recebe o termo da P.A (Numero inicial)
sleep(1) #Delay
print('-=' * 50) #Linha
sleep(1)#Delay
razão = int(input('Digite Qual será a Razão da P.A: '))# Recebe Razão da P.A 
print('-=' * 50) #Linha 
formula = termo + (10-1) * razão # Formula Termo Geral (decobrir o decimo numero da progressão)

'''
# FORMULA DO TERMO GERAL P.A

An = a1 + (n - 1 * r)

Onde,

an: termo que queremos calcular
a1: primeiro termo da P.A.
n: posição do termo que queremos descobrir
r: razão

Entretanto para chegar até o 10 o limite tem que ser 11 então retirei o -1 
caso contrario ele so iria fazer as 09 sequencias da PA e queremos os 10 primeiros

'''
for c in range(termo, formula + razão, razão): # Exibe a sequencia dos 10 priemiros numeros da P.A com a Razão
    print(c, end='->  ') # Exibi numero P.A
    sleep(1)#Delay