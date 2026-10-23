# Pedra Papel Tesoura
from time import sleep
import random
print(30*'=-') # Linha
print('Pedra, Papel, Tesoura') # Titulo
print(30*'=-') # Linha
sleep(2) # Delay
print('Escolha a sua jogada\n[ T ] para Tesoura\n[ P ] para Pedra\n[ F ] para papel') # Exibe opçoes de jogada para o usuario
print(30*'=-') # Linha
sleep(2) # Delay
jogada = str(input('-->')).upper().strip() # Recebe jogada do usuario, e formarta para letra maiuscula sem espaços inuteis
print(30*'=-') # Linha
sleep(2) # Delay
print('JO') # Mensagem Interativa
sleep(1) # Delay
print('KEN')# Mensagem Interativa
sleep(1) # Delay
print('PO!!!')# Mensagem Interativa
sleep(1) # Delay
print(30*'=-') # Linha
sleep(3) # Delay
maquina = random.choice(['T', 'P', 'F']) # Sorteia uma jogada para Maquina
if jogada == maquina: # Se o valor da jogada e d maquina forem iguais 
    print('Empatou, vamos tentar novamente') # Resulta em empate
elif jogada == 'T' and maquina == 'F': # Se o jogador escolher Tesoura e a maquina escolher Papel
    print('Eu escolho Tesoura') # Exibe jogada sorteada pela maquina
    sleep(1) # Delay
    print('Parabens voce me venceu, Tesoura ganha de Papel\nVamos tentar novamente, na proxima eu venço :/') # Resulta em Vitoria do usuario
elif jogada == 'T' and maquina == 'P': # Se a jogada for Tesoura e a maquina for Pedra
    print('Eu escolho Pedra')# Exibe jogada sorteada pela maquina
    sleep(1) # Delay
    print('Voce perdeu eu venci, Pedra ganha de Tesoura\nTente novamente, Quem sabe voce não ganha de mim na proxima ;)') # Resulta em Derrota do usuario
elif jogada == 'P' and maquina == 'T': # Se a jogada for Pedra e a maquina for tesoura
    print('Eu escolho Tesoura')# Exibe jogada sorteada pela maquina
    sleep(1) # Delay
    print('Parabens voce me venceu, Pedra ganha de Tesoura\nVamos tentar novamente, na proxima eu venço :/') # Resulta em Vitoria do usuario
elif jogada == 'P' and maquina == 'F': # Se a Jogada for Pedra e a da maquina for Papel
    print('Eu escolho Papel')# Exibe jogada sorteada pela maquina
    sleep(1) # Delay
    print('Voce perdeu eu venci, Papel ganha de Pedra\nTente novamente, Quem sabe voce não ganha de mim na proxima ;)') # Resulta em Derrota do usuario
elif jogada == 'F' and maquina == 'P': # Se a jogada for papel e a da maquina for pedra
    print('Eu escolho Pedra')# Exibe jogada sorteada pela maquina
    sleep(1) # Delay
    print('Parabens voce me venceu, Papel ganha de Pedra\nVamos tentar novamente, na proxima eu venço :/') # Resulta em Vitoria do usuario
elif jogada == 'F' and maquina == 'T': # Se a jogada for papel e a maquina for tesoura
    print('Eu escolho Tesoura')# Exibe jogada sorteada pela maquina
    sleep(1) # Delay
    print('Voce perdeu eu venci, Tesoura ganha de Papel\nTente novamente, Quem sabe voce não ganha de mim na proxima ;)') # Resulta em Derrota do usuario
else: # Se não
    print('Valor digitado Invalalido\n Por favor Escolha somente entre T, P, F') # Mensagem de erro 
print(30*'=-') # Linha
sleep(2) # Delay
print('Reinicei o Programa para Recomeçar') # Mensagem final
print(30*'=-') # Linha