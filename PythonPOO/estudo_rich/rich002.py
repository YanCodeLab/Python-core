from rich import print
from rich.panel import Panel

caixa = Panel('[white]Esse é um painel usando .rich[/]', title='Painel', style='red', width=35, height=5)
print(caixa)