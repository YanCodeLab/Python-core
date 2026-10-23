num = ( int(input('Digite um numero:')),
        int(input('Digite um numero:')),
        int(input('Digite um numero:')),
        int(input('Digite um numero:')),
       )
print(f'Voce digitou {num}')
print(f'Voce digitou {num.count(9)} vezes o numero nove')
if 3 in num:
    print(f'O primeiro valor 3 esta na posição {num.index(3) + 1}°')
else:
    print(f'Voce não digitou o numero 3')

print('Os valores pares digitados são', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')