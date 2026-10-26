from rich import print
from rich.table import Table

tabela = Table(title ='Tabela de Preços')

tabela.add_column('Nome', style='red')
tabela.add_column('Preço', width=10)

tabela.add_row('Lapis', 'R$: 1,50')
tabela.add_row('Carro', '[yellow]R$ 1500[/]')

print(tabela)