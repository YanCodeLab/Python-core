def leiaInt(msg):
    valido = False
    while not valido:
        try:
            valor = int(input(msg))
            
        
        except (ValueError, TypeError):
            print('\033[31mErro: Valor invalido, por gentileza digite um valor Inteiro Valido\033[0m')
            continue # Continua o laço de repetição

        except (KeyboardInterrupt): # Se interromper o programa     
            print('\033[31mErro: Entrada de dados interrompida pelo usuario\033[0m')
            return 0

        else:
            valido = True
            return valor
        

def leiaFloat(msg):
    valido = False
    while not valido:
        try:
            valor = float(input(msg))

        except (ValueError, TypeError):
            print('\033[31mErro: Valor invalido, por gentileza digite um valor Real Valido\033[0m')
            continue

        except (KeyboardInterrupt): # Se interromper o programa     
            print('\033[31mErro: Entrada de dados interrompida pelo usuario\033[0m')
            return 0
        

        else:
            valido = True
            return valor



inteiro = leiaInt('Digite um numero Inteiro: ')
real = leiaFloat('Digite um numero Real: ')
print(f'Voce acabou de digitar o numero Inteiro: \033[32m{inteiro}\033[0m e Real \033[32m{real}\033[0m')
