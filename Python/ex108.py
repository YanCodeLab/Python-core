from ex107 import moeda
preço = float(input('Digite o Preço: R$'))
print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando em 10% fica {moeda.moeda(moeda.aumentar(preço, 10))}')