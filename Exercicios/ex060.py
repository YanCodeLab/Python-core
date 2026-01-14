# Fatorial
#10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800

n1 = int(input('Digite um numero: ')) # Recebe o numero 
limite = 0 # Contador limite (Para encerrar o loop )
fatorial = 1 # Contadore responsavel pela multiplicação dos numeros fatoriais
while limite == 0 : # Enquanto o limite for igual a zero
  print(f'{n1} x', end =' ') # Exibi o valor de n1, sem pular linha
  fatorial *= n1 # Multiplica o valor de fatorial com o atual valor de n1
  n1 = n1 - 1 #Subtrai 1 de n1
  #Repete o loop ate n1 chegar a 1
  if n1 == 1: #Se n1 chegou ao 1
    limite += 1 # Adiciona 1 no limite e encerra o loop
    print(f'{n1} x', end =' ') # Mostra o 1 na decomposição do numero fatorial
print(f' O Fatorial  é igual á {fatorial}')# Exibe a multiplicação de todos os numeros antecesssores de n1 ate 1
  
