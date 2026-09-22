from ex107 import moeda
preço = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.metade(preço, True)}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço, True)}')
print(f'Aumentando em 10% fica {moeda.aumentar(preço, 10, True)}')
print(f'Reduzindo em 13% fica {moeda.aumentar(preço, 13, True)}')