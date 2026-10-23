def ficha(n='<desconhecido>', g=0):
    '''
    Exibe dados do jogador
    --> Para n armazena o nome do jogador, se não receber nenhum nome sera igual a <desconhecido>
    -- Para g é a qtd de gols feita pelo jogador 

    '''
    
    print(f'O jogador {n} fez {g} gols')
    


jogador = str(input('Digite o nome do jogador: ')) # Recebe o nome do jogador 
gols = str(input('Quantidade de gols feitos: ')) # Recebe a qtd de gols feitas pelo jogador como string

if gols.isnumeric(): # Se a variavel gols tiver apenas numeros
    gols = int(gols) #muda a variavel para o tipo inteiro
else: # Se caso tiver letras
    gols = 0 # define gols como 0

if jogador == '': # Se o nome do jogador ficar em branco
    ficha(g=gols)# Chama a função somente com a referencia dos gols
else: # se não (Caso tenha digitado algum nome)
    ficha(jogador, gols)# Chama a função ficha com os parametros