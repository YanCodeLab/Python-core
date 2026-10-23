# Leitura de peso
pesagem = [] # lista de pesos
for i in range(1,6): # Repete 5 vezes
    peso = float(input(f'Digite o peso da {i}° pessoa: ')) # Recebe peso 
    print('-'*50) #linha
    pesagem.append(peso)# armazena o peso recebido na lista
print(f'O maior peso é {max(pesagem)}Kg, e o menor peso {min(pesagem)}Kg.')# exibi o maior e o menor peso da lista usando o comando max() e min()
print('-'*50)#linha