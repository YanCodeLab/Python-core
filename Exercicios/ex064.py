num = 0 # Declara variavel que recebe numeros
soma = 0 # Contador responsavel pela soma dos numeros
qtd = 0 # Conatador responsavel pela quantidade de numero digitado
while num != 999: # Enquanto num for diferente de 999
    num = int(input('Digite Qualquer numero [999 para para]: ')) # Recebe numero
    soma += num # Soma  os numero, e armazena
    qtd += 1 # Cada vez que um numero é digitado recebe 1 (Serve para conttar quantas vezes o usuario digitou)
print('Codigo 999: ')#Mensagem
print('-'*30)# Linha
print('ANALISE COMPLETA ABAIXO')# Mensagem
print('-'*30)# Linha
print(f'Foram digitados cerca de {qtd - 1} numeros') # Exibe a quantidade de numerops digitados, desconsiderando o 999 (por isso o -1)
print(f'A soma de todos esses numeros é {soma - 999}') # Exibi a soma de todos os numeros, desconsiderando o 999
print('-'*30)# Linha
