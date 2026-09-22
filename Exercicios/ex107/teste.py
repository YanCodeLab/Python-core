import moeda

preço = float(input('Digite um preço: '))
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é igual á {moeda.dobro(preço)}')
print(f'Aumentando em 10% temos {moeda.aumentar(preço, 10)}')
print(f'Reduzindo em 13% temos {moeda.diminuir(preço, 13)}')