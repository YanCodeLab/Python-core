soma = qtd = 0 # Contadores para soma e qtd de vezes digitado
while True: # Loop infinito
    n = int(input('Digite um numero [999 para parar]: ')) # Recebe numero
    if n == 999: # Se o numero recebido for igual a 999 (desconsidera o flag)
        break # Interrompa o loop
    soma += n # Soma os valores de n
    qtd += 1 # Conta a qtd de numeros digitados
print(f'A soma dos {qtd} numeros é igual á {soma}') # Exibe informação