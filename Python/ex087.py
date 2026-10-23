matriz = [[0,0,0], 
          [0,0,0], 
          [0,0,0]] #Monta matriz

pares = soma_terceira_coluna = 0


for l in range (0,3):# Linhas
    for c in range(0,3): # Colunas
        matriz[l][c] = int(input(f'Digite Um numero [{l,c}]:')) # Usa l c para posicionar no lugar extato da matriz linha e coluna

        if matriz[l][c] % 2 == 0: #Se o valor atual for par
            pares += matriz[l][c] #soma ele com os outros valores pares

        if c == 2:
            soma_terceira_coluna += matriz[l][c]

print('=-'*30)
for l in range (0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('=-'*30)
print(f'A soma de todos os valores pares é: {pares}')
print('-'*50)
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print('-'*50)
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
print('-'*50)