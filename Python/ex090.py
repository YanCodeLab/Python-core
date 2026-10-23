aluno = {} # Cria dicionario
aluno['Nome'] = str(input('Nome: ')) # Cria keys e armazena nome
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: ')) # Cria keys e armazena media
aluno['Situação'] = 'Aprovado' # Cria keys como aprovado
if aluno['Media'] < 7: # Se a media for abixo de 7
    aluno['Situação'] = 'Reprovado' # Atualiza a situação para reprovado
for k, v in aluno.items(): # Percore os itensdo dicionario
    print(f'{k} é {v}') # Exibi situação
