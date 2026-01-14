# Indicador de Peso
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
print(f'{cor["negrito"]}{cor["amarelo"]}Indicador de Peso{cor["reset"]}') # Titulo
print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha
sleep(3) # Delay
peso = float(input('Digite seu Peso: ')) # Recebe peso
print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha
sleep(2)# Delay
altura = float(input('Digite sua Altura: ')) # Recebe altura
print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha
sleep(2)# Delay
print('Calculando Indice de massa corporal...')# Mensagem de espera
print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha
imc = peso / (altura ** 2) # Calcula indece de massa corporal (imc)
print('Seu Índice de Massa Corporal é {:.2f}'.format(imc)) # Exibe imc
print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha
sleep(2)# Delay
if imc < 18.5: # Se imc for menor que 18.5
    print('Voce está abaixo do peso') # Abaixo do peso
elif  imc >= 18.5 and imc < 26: # Se imc for maior ou igual a 18.5 e menor ou igual a 25
    print('Seu Peso está ideal')# Peso ideal
elif imc >= 26 and imc <31: # Se imc for maior ou igual a 26 e menor ou igaul a 30
    print('Voce esta Sobrepeso') # Sobrepeso
elif imc >= 31 and imc <= 40: #Se imc for maior ou igual a 31 e menor ou igual a 40
    print('Voce esta com Obsidade')#Obsidade
elif imc >= 41:# se imc for maior ou igual a 41
    print('Voce esta com obsidade morbida') #Obsidade morbida
print(40*f'{cor["roxo"]}=-{cor["reset"]}') #linha