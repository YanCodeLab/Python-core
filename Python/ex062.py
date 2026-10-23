# 10 TERMOS DE UMA P.A
print('-=' * 50) #Linha
print('10 TERMOS DE UMA P.A')
print('-=' * 50) #Linha
bonus = 1 # Representa o numero de termos a mais que serão adicionados
termo = int(input('Digite o inicio da P.A: ')) #termo é o primeiro numero (inicio)
razao = int(input('Digite a razão da P.A: '))#razão  a diferença constante entre dois termos consecutivos da sequência
formula = termo + (10) * razao # Formula Termo Geral (decobrir o decimo numero da progressão)
while termo != formula: # Enquanto o o termo não chegar no decimo valor da P.A
  print(termo, end='->  ') # exibe a progressão
  termo += razao # conta de acordo  com a razão

# PARTE RESPONSAVEL POR ADICIONAR MAIS TERMOS 
while bonus != 0: # Enquanto o bonus for diferente de 0
  bonus = int(input('Quantos termos a mais vc quer: '))# Recebe quanto termos a mais a pessoa quer 
  formula = termo + (bonus) * razao # Formula Termo Geral (decobrir o ultimo numero da sequencia numero da progressão) 
  while formula != termo: # Enquanto o termo não chegar no ultimo valor da progresssão
     print(termo, end='->  ') # exibe a progressão 
     termo += razao # conta de acordo  com a razão
print('FIM')   