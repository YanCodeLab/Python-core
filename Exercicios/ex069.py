#Analise de dados em grupo
maioridade = men = mulher= 0 # Contadores 
'''
maioridade = armazena a quantidade de pessoas com mais de 18 anos

men = armazena a quantidade de homens cadastrados

mulher = armazena a quantidade de mulheres com menos de 20 anos
'''
while True: # Loop infinito
    print('='*30) # Linha
    print('CADASTRE UMA PESSOA') # Titulo
    print('='*30) # Linha
    
    idade = int(input('Idade: ')) # Recebe a idade 
    if idade >= 18: # se a idade for maior que 18
        maioridade += 1 # Adiciona 1 no contador 
    sexo = str(input('SEXO [M/F]:')).upper().strip() # Recebe sexo
    if sexo == 'M': # Se sexo for igual a 'M'
        men += 1 # Adiciona 1 no contador men
    
    if idade <= 20 and sexo == 'F': # Se idade for menor que 20 e o sexo for igual a 'F'
        mulher += 1 # Adiciona 1 nop contador
    print('='*30) # Linha
    loop = ' '# defini variavel loop vazia
    while loop not in 'SN': # Enquanto a variavelmloop nao for S ou N
        loop = str(input('Deseja continuar? [S/N]')).upper().strip() # Recebe informação se a pesssoa deseja continuar
    if loop == 'N': # Se o loop for igual a N
        print('='*30) # Linha
        break # Encerra o loop infinito
    
#Exibi informaçoes salvas nos contadores
print(f'Total de pessoas com menos de 18 anos: {maioridade} ')
print(f'Foram Cadastrados {men} homens ')
print(f'E temos {mulher} com menos de 20 anos')