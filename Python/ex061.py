# 10 TERMOS DE UMA P.A
print('-=' * 50) #Linha
print('10 TERMOS DE UMA P.A')
print('-=' * 50) #Linha
termo = int(input('Digite o inicio da P.A: ')) #termo é o primeiro numero (inicio)
razao = int(input('Digite a razão da P.A: '))#razão  a diferença constante entre dois termos consecutivos da sequência
cont = 1 # Contador para repetição
while cont <= 10: # Enquanto o contador não chegar a 10 (10 repetiçoes)
  print(termo, end='->  ') # exibe a progressão
  termo += razao # conta de acordo  com a razão
  cont += 1 # adciona 1 no contador
print('FIM')
