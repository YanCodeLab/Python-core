from time import sleep #Importa comando para delay
cont = 0 # Variavel contador
soma = 0 # Variavel soma
for c in range(1,7): # Repete 6 vezes
    number = int(input('Digite um numero:'))# Recebe numero
    sleep(1) # Delay
    print('-'*20) # linha
    if number % 2 == 0: # Se o numero digitado for par
     soma += number # Soma os pares
     cont += 1 # Conta quantos pares tem
    


print(f'Existe {cont} numeros pares e a soma desses numeros é igual á {soma}')# Exibe a soma dos numeros
print('-'*40)# linha
sleep(2) # Delay


   