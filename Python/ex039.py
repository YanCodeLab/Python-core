#Alistamento Militar
from datetime import date #Importa comando ano atual
from time import sleep # Importa comando delay
print(30*'=-') # Linha
print('ALISTAMENTO MILITAR') # Titulo
print(30*'=-')
nasceu = int(input('Digite o seu ano de nascimento: ')) # Recebe ano de nascimento
print(30*'=-')
sleep(2) #Delay
ano = date.today().year #Descobre Ano atual
idade = ano - nasceu # Descobre idade do usuario
if idade < 18: # S e idade for menor do que 18 anos
    alistamento = 18 - idade # Calcula quantos anos falta para o alistamento
    print('Consultando seus dados...') #Mensagem de carregamento
    sleep(3)
    print(f'Voce deve se alistar no Exercito Militar daqui á {alistamento} anos') # Mensagem
elif idade == 18 or idade == 17: # Se idade for igual a 18 ou 17
     print('Consultando seus dados...') #Mensagem de carregamento
     sleep(3)
     print('Voce ja deve se Alistar Para o Exercito') # Mensagem
else: # Se não (idade maior que 18)
    alistamento = idade - 18  # Descobre á quantos anos ele deveria ter se alistado
    print('Voce ja passou do prazo para o alistamento') # aviso
    sleep(1)
    print('Consultando seus dados...') #Mensagem de carregamento
    sleep(3)
    print(f'Deveria ter se alistado a {alistamento} anos atras')# Mensagem
    
