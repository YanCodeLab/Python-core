numeros = [[], []]
for n in range (1, 8): # repete 7 vezes
   num = int(input(f'Digite o {n}° numero: ')) # Recebe numero
   if num % 2 == 0: # Se for par
        numeros[0].append(num) # Armazena no sublista 0 
   else: # Se for impar
      numeros[1].append(num) # Adiciona na sub-lista 1 

#Ordena os numeros em crescente
numeros[0].sort() 
numeros[1].sort()

print(f'Pares: {numeros[0]}')
print(f'Impares: {numeros[1]}')
