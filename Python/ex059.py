#Menu de Opçoes
from time import sleep # Importa comando de delay
opção = 0 # Variavel responsavel pelas opçoes
n1 = int(input('Digite um numero: ')) # Recebe n1
print(20 * '---') # linha
sleep(1)# Delay 1 segundo
n2 = int(input('Digite um segundo numero: ')) # Recebe n2
print(20 * '---') # linha
sleep(1) #delay
while opção != 5: # Enquanto o contador menu for igual a 0 repete:
    print(''' 
     ----ESCOLHA UMA OPÇÃO ABAIXO----
          [1] somar
          [2] multiplicar
          [3] maior
          [4] novos numeros
          [5] sair do programa
          ''') # exibi opçoes
    opção = int(input('Digite a opção escolhida aqui ---> '))# recebe opção escolhida
    sleep(1) # delay 1 segundo
    if opção == 1: # Se a opçao for igual a 1 
        print(f'A soma de {n1} e {n2} é igual á {n1+n2} ') # Soma n1 e n2
    if opção == 2: # De opçao for igual a 2
        print(f'A multiplicação entre {n1} e {n2} resulta em {n1*n2}') # Multiplica n1 e n2
    if opção == 3: # Se opção for igual a 3 (ANALISA QUAL NUMERO É MAIOR)
        if n1 > n2:  # Se n1 for maior que n2
            print(f'O maior numero digitado é {n1}') # exibi n1 é o maior
        if n1 < n2: # Se n1 for menor que n2
            print(f'O maior numero digitado é {n2}') # Exibi n2 é o maior
        else: # se não
            print(f'{n1} e {n2} são iguais') # n1 e n2 são iguais
    if opção == 4: # Se a opão for igual a 4
             n1 = int(input('Digite um numero: ')) # Recebe n1
             print(20 * '---') # linha
             sleep(1)# Delay 1 segundo
             n2 = int(input('Digite um segundo numero: ')) # Recebe n2
             print(20 * '---') # linha
             sleep(1) #delay
             sleep(1)# delay 1 segundo
print('Encerrando Programa') #Exibi mensagem de finalização    
sleep(1)# delay 1 segundo
print(20 * '---') # linha
print('Fim por agora, aprendizado para sempre.') # mensagem final...