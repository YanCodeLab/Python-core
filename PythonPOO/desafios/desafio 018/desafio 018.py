from rich import print
from rich.panel import Panel

class Churrasco:
    """
       Representa um churrasco, calculando a quantidade recomendada de carne,
       o custo total e o valor aproximado por pessoa, com base no número
       de convidados e no preço por quilo da carne.
       """
#   Atributos de classe
    consumo_padrao = 0.400  # Consumo por pessoa
    preco = 82.40           #Preço por Kg de carne

    def __init__(self, titulo, qtd):
        self.titulo = titulo
        self.qtd = qtd

    #Metodos

    def quan_recomendada(self):
         return self.qtd * Churrasco.consumo_padrao    #  Quantidade recomendada de carne de acordo com a qtd de pessoas

    def tot_custo(self):
       return self.quan_recomendada() * Churrasco.preco  # Calcula o preço com base nos Kgs recomendados

    def custo_ppesoa(self):
        return self.tot_custo() / self.qtd  # Calcula quanto cada participante devera pagar (custo por pessoa)

    def analisar(self):
        conteudo = (f'Analisando [green]{self.titulo}[/] com [blue]{self.qtd} convidados[/]\n'
                    f'Cada participante comera 0,4Kg e cada Kg custa R$82,40\n'
                    f'Recomendo comprar [blue]{self.quan_recomendada():.3f}Kg[/] de carne\n'
                    f'O custo total será de [green]R${self.tot_custo():,.2f}[/]\n'
                    f'Cada pessoa deverá pagar cerca de [yellow]R${self.custo_ppesoa():.2f}[/]')



        analise = Panel(conteudo,
                        title=f'{self.titulo}')
        print(analise)


c1 = Churrasco('Churras', 15)
c2 = Churrasco('Festa Fim de Ano', 80)

c1.analisar()
c2.analisar()