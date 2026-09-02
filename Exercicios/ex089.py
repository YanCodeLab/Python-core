boletim = []
aluno = []
while True:
    aluno.append(input('Nome: '))
    aluno.append(int(input('Nota 1: ')))
    aluno.append(int(input('Nota 2: ')))

    boletim.append(aluno[:])
    aluno.clear()

    continua = str(input('Deseja continuar [S/N]: ')).upper()
    if continua == 'N':
        break
print('-='*30)
print('   Nome       Media')
print('-'*30)

for v in range(0, len(boletim)):
    print(f'{v}   {boletim[v][0]}         {(boletim[v][1] + boletim[v][2]) / 2}')

print('-'*50)


while True:
    exibir = int(input('Deseja consultar notas de qual aluno? (999 interrompe) '))

    if exibir == 999:
        break
    else:
        print(f'Notas de {boletim[exibir][0]} são [{boletim[exibir][1], boletim[exibir][2]}]')
        print('-'*50)

print('-='*30)
print('FINALIZANDO')
print('Volte Sempre!!!')
print(';)')
