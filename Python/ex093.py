jogador = {} # Cria dicionario (Armazena dados do jogador)
gol = [] # Guarda os valores dos gols feitos nesta lista

jogador['nome'] = input('Digite o nome do jogador: ') # Recebe o nome do jogador 
partidas = int(input(f'Quantas Partidas {jogador['nome']} disputou:')) # Recebe numero de partidass realizadas

for p in range(0, partidas): # Repete a de acordo com o numero de partidas disputadas
    gol.append(int(input(f'Quantos gols na partida {p}: '))) # Adiciona o gol na lista

print('-=' * 50)
jogador['gols'] = gol[:] # copia a lista gol no dicionario
jogador['total'] = sum(gol) # salva a soma de todos os gols no dicionario

print(jogador) # exibe dicionario
print('-=' * 50)

for k,v in jogador.items(): #Para cada key e valor em jogador
    print(f'O campo {k} tem o valor {v}')
print('-=' * 50)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.') #Titulo exibindo quantas partidas o jogador disputou

for p, g in enumerate(jogador['gols']): 
    print(f'=> Na partida {p} marcou {g} gols') #Ira exibir a partida e o gol feito nela (so passando pelo dicionario gols)

print(f'Foi um total de {jogador["total"]} gols')# Total de gols
print('-=' * 50)
