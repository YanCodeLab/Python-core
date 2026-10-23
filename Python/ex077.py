palavras = ('Sabao', 
            'Yan',
            'cachorro',
            'gato',
            'pipa',
            'comida',
            'lanche',
            'cavalo',
            'Curso',
            'python')

for p in palavras: # Cada palavra na tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # cada letra nas palavras
        if letra.lower() in 'aeiou':
            print(letra, end='')



