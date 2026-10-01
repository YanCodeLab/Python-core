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




def linha(tam=42):
    print('-'*tam)

def cabeçalho(txt):
    linha()
    print(f'{txt}'.center(42))
    linha()

def menu(lista):
    cabeçalho('MENU')
    c = 1
    for item in lista:
        print(f'\033[33m{c}-\033[0m \033[34m{item}\033[0m')
        c += 1
    linha()
    opc = leiaInt('\033[33mSua Opção: \033[0m')
    return opc


