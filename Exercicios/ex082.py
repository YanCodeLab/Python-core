numeros = [] #Lista principal armazena todos os numeros
par = [] # Lista para os numeros pares 
impar = [] # Lista para os numeros impares
while True:
    numeros.append(int(input('Digite um numero: '))) # Recebe o numero digitado e armazena na lista

    end = str(input('Deseja continuar [S/N]: ')).upper() # Pergunta se deseja continuar
    if end == 'N': # Se for N
        break # Encerra o loop

for n in numeros:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('-'*20)
print(f'A lista completa é: {numeros}')
print(f'Os numeros pares são: {par}')
print(f'Os numeros impares são: {impar}')
print('-'*20)
