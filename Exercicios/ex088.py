from random import randint
from time import sleep
print('-'*30)

print('-'*30)

jogos = [] # Armazena todos os jogos
lista = [] # Cria jogos individuais
num_jogos = int(input('Quantos jogos voce quer que eu sorteie? ')) # Recebe numero de quntas listas vai criar para salvar os numeros

for j in range(0, num_jogos): #Ira criar a quantidade de josgos (listas)
    
     while len(lista) != 6: # Enquanto não tiver 6 numeros dentro da lista
         number = randint(1, 60) # Sorteia um numero entre 1 e 60
         if number not in lista: # Se esse numero não estiver na lista 
           lista.append(number) # Adiciona o mesmo 

     lista.sort() # Organiza em forma crescente
     jogos.append(lista[:]) # Passa os valores do jogo atual para a lista principal
     lista.clear() # apaga os dados atuais para gerar novos

print('~'*50)
for c in range(0, len(jogos)): # Repete para exibir todos os jogos
    print()
    print(f'JOGO {c + 1}: {jogos[c]}') # Exibe jogo salvo dentro de 'jogos'
    print()
    sleep(2) #delay de 2 segundos

print('~'*50)
