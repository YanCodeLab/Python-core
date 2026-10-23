from time import sleep
def maior(*num):
    print('-='*40)
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c} ', end='', flush=True)
        sleep(0.4)
    print(f'Foram informados {len(num)} ao todo.')

    if len(num) != 0:
        print(f'O maior valor informado foi {max(num)}')

    else:
        print('Não foi informado nenhum valor')
    print('-='*40)
    sleep(1)


maior(2,9,4,5,7,3)
maior(4,7,0)
maior(1,2)
maior(6)
maior()