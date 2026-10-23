print('='*30) # Linha
print('LOJAS RANGEL ;)') # Nome da loja :)
print('='*30) # Linha
# Contadores
gastos = totmil = barato = cont = 0 
nomeproduto = ''
'''
gastos = Soma o valor de todos os produtos cadastrados

totmil = Conta quantos produtos custam mais que R$1000.00

barato = Salva o menor preço cadastrado

cont = para contar quantos produtos foram cadastrados

nomeproduto = salva o nome do produto mais barato
'''
while True: #loop infinito
    produto = str(input('Nome do Produto: ')) # Recebe nome do produto
    preço = float(input('Preço: R$')) # Recebe PREÇO
    cont += 1 # Adiciona 1 no contador 

    gastos += preço # acumula e soma os preços cadastrados
    if preço > 1000: # Se o preço for maior que 1000
       totmil += 1 # Adiciona 1 no contador totmil
    
    if cont == 1: # Se o cont for igual a 1 (Ou seja o primeiro produto castrado)
       barato = preço # Considera provisoriamente o primeiro produto cadastrado como mais barato
    else: # Se não for o primeiro produto cadastrado
        if preço < barato: # E se o preço atual do produto for menor que o valor salvo na variavel barato(Variavel que armazena o menor valor)
            barato = preço # Atualiza valores, considerando o preço atual mais barato
            nomeproduto = produto# E salva o nome do produto
     
    loop = ' ' # Limpa a variavel loop
    while loop not in 'SN': # Enquanto O loop não for S o N
      loop = str(input('Deseja continuar[S/N]')).upper().strip() # Envia pergunta se deseja continuar
    print('='*30) # Linha
    if loop == 'N': # Se o valor de loop for igual a 'N'
        break # Encerra o loop
#EXIBE RESULTADO DOS DADOS
print('------FIM DO PROGRAMA------')
print(f'O total da Compra Foi {gastos:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeproduto} que custa R${barato}')