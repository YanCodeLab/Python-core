from rich import print
from rich.panel import Panel
from rich.text import Text

class Produto:

    def __init__(self, nome, pre):
        self.nome = nome # Nome do produto
        self.preco = float(pre) # Armazena preço


    def __str__(self) -> str:
        return f"{self.nome} custa R${self.preco}"

    def etiqueta(self):
        precof = f'R${self.preco:,.2f}'# Formata o valor de preço
        etiqueta = Panel(Text(f"{self.nome}\n{'-' * 36}\n{precof}", justify='center'),  title="Etiqueta", width=40, )
        print(etiqueta)

# Objetos
p1 = Produto('Celular', '2000')
p2 = Produto('Carro', '15000')

#Chama metodo etiqueta
p1.etiqueta()
p2.etiqueta()