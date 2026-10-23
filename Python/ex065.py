loop = 'S' # Condição para o loop infinito
qtd = 0 # Armazena a quantidade de numeros digitados
soma = 0 # Armazena a Soma de todos os numeros digitados
Maior = 0 # Armazena o Maior numero
Menor = 1  # Armazena o menor numero
while loop == 'S': # Enquanto o loop for igual a S
    num = int(input('Digite um Numero: ')) #Recebe numero
    soma += num # Soma o numero com o valor armazenado no contador, e salva
    qtd += 1 # Adiciona 1 no contador de quantidade
    if num >= Maior: # Se o numero digitado for maior que o numero salvo na variavel
        Maior = num # Atualiza a variavel, para esse novo numero
    if num <= Menor: # Se o numero digitado for menor que o valor da variavel
        Menor = num # Atualiza o valor da variavel por esse novo numero
    loop = str(input('Deseja continuar [S/N]? -> ')).upper() # Pergunta se deseja continuar, Caso receba 'N' Encerra o loop
print('~'*30) #Linha
print(f'Voce digitou cerca de {qtd} numeros') # Exibi Quantidade de numeros digitados
print(f'A media de todos os numeros digitados é {soma / qtd }') # Faz calculo da media de todos os numeros e exibi
print(f'O maior numero digitado {Maior}') # Exibi o Maior numero
print(f'O menor numero digitado {Menor}') # Exibi o menor numero
print('~'*30) #Linha
