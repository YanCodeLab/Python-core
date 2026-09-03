valores = [] # ARmeza todos os valoresd digitados
mini = 0 # Armazena o menor valor
maxi = 0 # Armazena o maior valor
for v in range(0, 5): # Repete 5 vezes 
    valores.append(int(input(f'Digite um valor para a posição {v}: '))) # Recebe o valor 
    if v == 0: # Se for o primeira vez que recebe o numero 
        mini = maxi = valores[v] # Esse primeiro valor se torna o maior e o menor valor
    else: # Se não
        #Logica para descobrir o menor e o maior valor 
        if valores[v] > maxi: # Se o valor atual do loop for maior que o valor em maxi
            maxi = valores[v] # Atualiza o valor de maxi
        elif valores[v] < mini: # Se o valor atual do loop for menor que o valor em mini
            mini = valores[v] # Atualiza o valor de mini
print('-'*30) # linha decorativa
print(f'Voce digitou {valores}') # exibe a lista com todos os numeros digitados
print(f'O maior valor é {maxi} Ele se encontra nas posiçoes', end='') # Exibe o maior valor e nao quebra a linha
for pos, i in enumerate(valores): # Varre a lista em busca da posição do maior valor 
    if i == maxi: # Se o valor atual for o maior valor 
        print(f' {pos}...', end='')   #Exibe a posição, e não quebra linha    
print()# Pula linha

print(f' O menor valor é {mini} Ele se encontra nas posiçoes', end='') # Exibe o menor numero e nao quebra a linha
for posi, a in enumerate(valores): # Varre a lista preocurando a posição do menor valor 
    if a == mini: # Se o valor atual for o menor da lista 
        print(f'{posi}...', end='') # exibe a posição atual e nao quebra a linha 
print()# pula linha 
print('-'*30) # Linha decorativa 
