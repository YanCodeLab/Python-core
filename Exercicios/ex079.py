valores = list() # Cria lista Vazia
while True: # Loop infinito
    num = int(input('Digite um numero: ')) # Recebe numero digitado
    if num in valores: # Se o numero digitado ja estives dentro da lista
        print(f'O numero {num} ja foi digitado') # Não e possivel salvar
    else: # Se o numero digitado nao estiver dentro da lista
        valores.append(num) # adiciona o novo numero a lista
   
    continuar = str(input('Deseja continuar [S/N]:')).upper() # Recebe string [S/N] para continuar ou encerrar o programa
    if continuar == 'N': # se a oopção escolhida for N
        break # Encerra o programa
valores.sort()
print(f'Valores Armazenados:{valores} ') # Exibe os numeros salvos ordenados em ordem crescente
