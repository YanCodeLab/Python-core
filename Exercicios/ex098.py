from time import sleep
def contagem(i,f,p): #inicio meio passo
    print('-'*30)
    print(f'Contagem de {i} ate {f} de {p} em {p}')

    for c in range (i, f+1, p):
       print(f'{c} ', end='', flush=True)
       sleep(0.5)
    print('FIM!')
    print()
    print('-'*30)


contagem(1, 10, 1)
sleep(1)
contagem(10, -3, -2)
sleep(1)

print('Agora é sua vez de personalizar a contagem')
inicio = int(input('INICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
print('-='*30)

if inicio > fim:
    if passo > 0:
     passo = -passo
    fim = fim - 2

contagem(inicio, fim, passo)
