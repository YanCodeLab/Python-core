from operator import itemgetter # PARA USAR O sort() nos dicionarios
jogador = {} # Cria dicionario (Armazena dados do jogador)
gol = [] # Guarda os valores dos gols feitos nesta lista
jogadores = []
continuar = 'S'

while continuar == 'S': 
    jogador['nome'] = input('Digite o nome do jogador: ') # Recebe o nome do jogador 
    partidas = int(input(f'Quantas Partidas {jogador['nome']} disputou:')) # Recebe numero de partidass realizadas

    for p in range(0, partidas): # Repete a de acordo com o numero de partidas disputadas
        gol.append(int(input(f'Quantos gols na partida {p}: '))) # Adiciona o gol na lista

    print('-=' * 50)
    jogador['gols'] = gol[:] # copia a lista gol no dicionario
    jogador['total'] = sum(gol) # salva a soma de todos os gols no dicionario
    gol.clear()
    
    jogadores.append(jogador.copy()) # Salva dados do jogador individual para a lista contendo todos os outros jogadores 

    while True:
     continuar = str(input('Deseja continuar [S/N]: ')).upper()[0]
     if continuar not in 'SN':
        print('ERRO; Digite somente S ou N')
     if continuar == 'N':
        break
     if continuar == 'S':
        break
     


print('-=' * 50)

jogadores.sort(key=itemgetter('gols'), reverse=True) # Ordena a lista para que o os jogadores que fizerem mais gols fiquem na frente

# Exibe informaçoes sobre jogador
# ---------------------------------
print(f'cod ' , end='')
for i in jogador.keys():
   print(f'{i:<15}', end='')
print()

for pos,v in enumerate(jogadores): # Percorre a lista salva a posição em pos e o valor em c
   print(f'{pos:>3} ', end='') 
   for d in v.values():
      print(f'{str(d):<15}', end='')
   print()

print('-=' * 50)
# -----------------------------------------
while True: # loop de levantamento de dados
   busca = int(input('Qual jogador vc gostaria de acessar os dados (999 para encerrar) ')) # recebe indice de busca 

   if busca == 999: # se for 99 encerra o programa
      break

   if busca >= len(jogadores): # se for um numero acima da qtd de indeces da lista 
      print(f'Não existe jogador com o codigo {busca}') # este  jogador nao existe

   else: # se não
      print('-' * 30)
      print(f'LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
      print('-' * 30)
      for pos, v in enumerate(jogadores[busca]['gols']): # PERCORRE A LISTA com base no jogador escolhido e acessa os dados de gols
         print(f'No Jogo {pos} fez {v} gols') # exibe quantos gols ele fez por partida
    
  
print('-=' * 50)
print('VOLTE SEMPRE')
