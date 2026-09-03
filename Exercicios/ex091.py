from random import randint
from time import sleep
from operator import itemgetter
jogo = dict() # Cria dicionario
print('Valores Sorteados')
for j in range(1, 5): # Sorteia os dados para 1 a 4 jogadores
    jogo[f'Jogador{j}'] = randint(1,6)

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

print('=-'*35)
print('=== RANKING DOS JOGADORES ===')

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) # Comando que ordena de maneira decresente os valores de jogo na lista ranking

for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')

