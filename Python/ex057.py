sexo = '' # Cria variavel que armazena a informação
while sexo == '': #Enquanto a variavel sexo estivel vazia repete
    sexo = str(input('Digite seu sexo [M/F]: ')).upper() # Recebe valor do usuario M ou F
    if sexo == 'M' or sexo == 'F': # Se o valor for M ou F
     print(f'Sexo {sexo} registrado com sucesso') # Dados salvos
    else: # Se não
       sexo = '' # Limpa a variavel e reinicia o loop
       print('Valor invalido')
       print('Digite Novamente')
