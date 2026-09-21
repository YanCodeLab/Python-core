from time import sleep

c =(  '\033[0m', # 0 e o reset
      '\033[31m', # 1 e vermelho
      '\033[32m', #  2 e verde
      '\033[47m', # 3 e branco
      '\033[34m' # 4 e azul
    )


def ajuda(com):
   titulo(f'Acesando manual de comando do \'{com}\'', 4)
   print(c[0])
   print(c[3], end='')
   help(com)
   print(c[0], end='')
   sleep(2)


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)
   


#Programa principal
comando = ''
while True:
     
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('FUNÇÃO OU BIBLIOTECA: '))

    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO', 1)
        break

    else:
        ajuda(comando)
