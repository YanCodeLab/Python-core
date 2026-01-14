somaidade = 0 # Contador soma das idades
nomehomemvelho = 0 #Contador homem mais velho
idadehomemvelho = 0 #Contador idade do homem mais velho
totmulher20 = 0 #Contador qtd de mulhers com menos de 20 anos
for p in range (1, 5): # Repete 4 vezes
  print(f'---{p}º PESSOA---') # Titulo
  nome = str(input('Nome: ')).strip().upper() #Recebe nome, formatado
  idade = int(input('Idade: '))#Recebe idade
  sexo = str(input('Sexo [M/F]: ')).upper() #Recebe opção do sexo formatado em maiusculo
  somaidade += idade #Soma a idade + valor docontador de idades
  if p == 1 and sexo == 'M': # Considera provisoriamente a primeira pessoa como homem mais velho
    nomehomemvelho = nome # Armazena o nome no contador
    idadehomemvelho += idade #Armazena a idade no contador
  
  if sexo == 'M' and idade > idadehomemvelho: # Aqui ele vai comparar, se existir um homem mais velhor que o valor no contador 'idadehomemvelho'
    idadehomemvelho = idade #Armazena a idade no contador
    nomehomemvelho = nome # Armazena o nome no contador
  
  if sexo == 'F' and idade > 20: # Se for feminino e menor que 20 anos
    totmulher20 += 1 #adiciona 1 no contador 

media = somaidade / 4 # Calcula a media de idade do grupo
print(f'A media de idade do grupo é {media}')
print(f'O homem mais velho se chama {nomehomemvelho} com {idadehomemvelho} anos')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')
