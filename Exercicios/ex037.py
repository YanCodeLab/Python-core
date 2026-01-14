#Convertendo numeros

from time import sleep             # Importa comando para delay

# Códigos ANSI para cores e formatação de texto
cor = {
    'reset': '\033[0m',
    'negrito': '\033[1m',
    'sublinhado': '\033[4m',

    # Cores de texto
    'preto': '\033[30m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m',
    'branco': '\033[37m',

    # Cores de fundo
    'fundo_preto': '\033[40m',
    'fundo_vermelho': '\033[41m',
    'fundo_verde': '\033[42m',
    'fundo_amarelo': '\033[43m',
    'fundo_azul': '\033[44m',
    'fundo_roxo': '\033[45m',
    'fundo_ciano': '\033[46m',
    'fundo_branco': '\033[47m',
}

print(40*f'{cor["azul"]}=-{cor["reset"]}')                                         #Linha decorativa
print(f'{cor["negrito"]}{cor["roxo"]} CONVERSÃO DE NUMEROS {cor["reset"]}')        #Titulo
print(40*f'{cor["azul"]}=-{cor["reset"]}')
sleep(1)
number = int(input(f'{cor["ciano"]}Digite um numero:{cor["reset"]}')) # Recebe numero do usuario
print(40*f'{cor["azul"]}=-{cor["reset"]}')
sleep(1)
base_num = int(input(f'{cor["ciano"]}Escolha um dos numeros abaixo para a coversão{cor["reset"]}\n{cor["verde"]}1{cor["reset"]} {cor["ciano"]}Para Binario{cor["reset"]}\n{cor["verde"]}2{cor["reset"]} {cor["ciano"]}Para Octal{cor["reset"]}\n{cor["verde"]}3{cor["reset"]}{cor["ciano"]} Para Hexaecimal{cor["reset"]}\n{cor["verde"]}-->')) # Comando para usuario converter
print(40*f'{cor["azul"]}=-{cor["reset"]}')
if base_num == 1:  # Se comando do usuario for igual a 1
    print(f'{cor["ciano"]}O numero{cor["reset"]} {cor["amarelo"]}{number}{cor["reset"]}{cor["ciano"]} convertido para binario é{cor["reset"]} {cor["verde"]}{bin(number)[2:]}{cor["reset"]}') #Converte para binario

elif base_num == 2: # Se comando do usuario for igual a 2
    print(f'{cor["ciano"]}O numero{cor["reset"]} {cor["amarelo"]}{number}{cor["reset"]}{cor["ciano"]} convertido para octal é{cor["reset"]} {cor["verde"]}{oct(number)[2:]}{cor["reset"]}') #converte para octal

elif base_num == 3: # Se comando do usuario for igual a 3
    print(f'{cor["ciano"]}O numero{cor["reset"]} {cor["amarelo"]}{number}{cor["reset"]}{cor["ciano"]} convertido para hexadecimal é{cor["reset"]} {cor["verde"]}{hex(number)[2:]}{cor["reset"]}')#converte para hexadecimal

else: #Se não
    print(f'{cor["vermelho"]}ERRO\nDigite um valor valido\nReinicie o Prorama') # Mensagem de erro