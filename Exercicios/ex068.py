#JOGO PAR OU IMPAR
from random import randint
print('-='*50)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*50)
vitoria = 0
while True:
    #Configuraçoes do JOGADOR
    numjogador = int(input('Digite um numero: '))
    jogador = '' #Limpa memoria
    while jogador != 'P' and jogador != 'I':
        jogador = str(input('PAR OU IMPAR [P/I]: ')).upper()
    

    #Configuraçoes do Computador
    numcomputador = randint(1,10)
    #Configura para que a jogada do computador seja a inversa do jogador humano
    if jogador == 'P':
        computador = 'I'
    if jogador == 'I':
        computador = 'P'

    #Configuraçoes do Jogo
    soma = numcomputador + numjogador # Soma os valores
   
     #Analisa Se a Soma é Par ou Impar
    if soma % 2 == 0:
        jogadafinal = 'P'
        resultado = 'DEU PAR'
    else:
        jogadafinal = 'I'
        resultado = 'DEU IMPAR'
    
    #Mensagem Resutado da soma
    print('-='*50)
    print(f'Voce jogou {numjogador} e o computador {numcomputador}. Total deu {soma} {resultado}')
    print('-='*50)

    #Analisa quem venceu
    if jogadafinal == jogador:
        print('Voce VENCEU')
        print('Vamos Jogar Novamente...')
        print('-='*50)
        vitoria += 1
    else:
        print('VOCE PERDEU')
        break

print('-='*50)
print(f'GAME OVER, Voce teve um total de {vitoria} vitorias')
