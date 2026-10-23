matriz = [[0,0,0], 
          [0,0,0], 
          [0,0,0]] #Monta matriz


for l in range (0,3):# Linhas
    for c in range(0,3): # Colunas
        matriz[l][c] = int(input(f'Digite Um numero [{l,c}]:')) # Usa l c para posicionar no lugar extato da matriz linha e coluna


print('=-'*30)
for l in range (0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
