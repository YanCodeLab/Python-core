#Idade
from datetime import date 
from time import sleep
atual = date.today().year # Ano atual
maior = 0 #Contador maior de idade
menor = 0 #Contador menor de idade
for i in range(1,8): # Repete 7 vezes
    nasc = int(input(f'Em que ano {i}° nasceu?: ')) # Ano de nascimento
    print('-'*50) # Linha
    sleep(1) #delay
    idade = atual - nasc # Decobre a idade
    if idade >= 18: # Se a idade for maior ou igual a 18
     maior += 1 # Adiciona 1 na variavel maior
    elif idade < 18: #Se a idade for menor de 18
       menor += 1 # Adiciona 1 na variavel menor
sleep(2)    
print(f'Analisando  os anos de nascimento, No total á {menor} pessoas menor de idade, e {maior} sendo de maior')
