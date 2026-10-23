from datetime import date 

usuario = {}

usuario['nome'] = str(input('Nome: '))
usuario['nascimento'] = int(input('Ano de Nascimento: '))
usuario['ctps'] = int(input('Carteira de Trabalho (0 Se não tiver): '))

if usuario['ctps'] != 0:
    usuario['contratação'] = int(input('Ano de Contratação: '))
    usuario['salario'] = float(input('Salario: R$: '))

print('=-'*30)

print(f'O nome tem o valor de {usuario["nome"]}')
usuario['idade'] = date.today().year - usuario["nascimento"]
print(f'A idade tem o valor de { usuario["idade"] }')
print(f'Valor de ctps: {usuario["ctps"]}')
if usuario['ctps'] != 0:
    print(f'O salario tem o valor de R${usuario["salario"]}')
    usuario['aposentadoria'] = usuario['idade'] + (usuario['contratação'] + 35) - date.today().year
    print(f'Aposentadoria = {usuario["aposentadoria"]} ')
