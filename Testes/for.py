from time import sleep
print('TESTES COM LAÇOS DE REPETIÇÃO (for)')
s = 0


'''for c in range(0,11): # Conta de 0 até 10, o 11 é o limite por isso ele não conta
    print(c)
    sleep(1)
'''

for c in range (1,5):
    print(f'Valor:{c}')
    s = s+c #soma valores dentro da repetição
    print(f'Soma entre esses valores é {s}')