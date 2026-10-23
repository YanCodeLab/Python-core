import random # Importa random
tentativas = 0
computador = random.randint(0,10)
print('Sou seu computador, acabei de pensar em um numero entre 0 e 10')
print('Sera que voce consegue advinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite?: '))
    tentativas += 1
    if jogador == computador:
        print(f'Acertou com {tentativas} tentativas. Parabens!')
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez')
        elif jogador > computador:
            print('Menos... tente mais uma vez')
        
    