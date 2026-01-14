#Categoria de Atletas
from datetime import date
from time import sleep

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

print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha
print(f'{cor["amarelo"]}Confederação de Natação{cor['reset']}')# Titulo
print(40*f'{cor["roxo"]}=-{cor["reset"]}')#linha
nasceu = int(input(f'{cor["azul"]}Digite o ano do seu nascimento{cor['reset']}'))
print(40*f'{cor["roxo"]}=-{cor["reset"]}')#linha
sleep(1)
ano = date.today().year # Consulta ano atual
idade = ano - nasceu # Calcula idade
print(f'{cor["azul"]}Consultando dados...{cor['reset']}')
print(40*f'{cor["roxo"]}=-{cor["reset"]}')#linha
print(f'{cor["azul"]}Voce tem {idade} anos{cor['reset']}') #idade
sleep(2)

if idade <= 9:   # Se idade for menor ou igual a 9
    print(f'{cor["azul"]}Sua categoria é {cor['reset']}{cor["verde"]}MIRIM{cor['reset']}')  #CATEGORIA MIRIM
elif idade <= 14:   # Se idade for  menor ou igual 14
    print(f'{cor["azul"]}Sua categora é{cor['reset']} {cor["verde"]}NFANTIL{cor['reset']}') # Categoria Infantil
elif idade <= 19:                    # Se idade for menor ou igual a 19
    print(f'{cor["azul"]}Sua categoria é {cor['reset']} {cor["verde"]}JUNIOR{cor['reset']}')   #Categoria JUNIOR
elif idade == 20: # Se idade for igual a 20
    print(f'{cor["azul"]}Sua categoria é{cor['reset']} {cor["verde"]}SENIOR{cor['reset']}') # Categoria Senior
elif idade > 20: # Se idade for maior que 20
    print(f'{cor["azul"]}Sua categoria é{cor['reset']} {cor["verde"]}MASTER{cor['reset']}') # Categoria Master
else:
    print(f'{cor["vermelho"]}Valor digitado não é valido{cor['reset']}')# Mensagem de erro
print(40*f'{cor["reset"]}{cor["roxo"]}=-{cor["reset"]}{cor['reset']}')#linha
   