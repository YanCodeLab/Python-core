from rich import print
from time import sleep

class Livro:

    def __init__(self, nome, qtd):
        self.livro = nome
        self.qtd = qtd # qtd de paginas do livro
        self.pagina = 1

        print(f':open_book:Você acabou de abrir o livro [red]{self.livro}[/] que tem [green]{self.qtd} páginas[/] no total.')
        print(f'Pagina Atual: {self.pagina}')

    def avançar(self, pg):

            pg_destino = min(self.pagina + pg, self.qtd) # Valor de paginas que sera avançado (soma a pagina atual + a qtd desejada pelo o usuario, e comparar esse resultado com a qtd total de paginas do livro, e retorna o menor valor)
            contador_avanco = 0

            for c in range(self.pagina, pg_destino): # Ele conta somente até o limite de paginas
                 print(f'{self.pagina} :arrow_right: ', end='')
                 self.pagina += 1
                 contador_avanco +=1
                 sleep(0.5)

            print(f'{self.pagina}  [blue]Voce avançou {contador_avanco} paginas e agora esta na pagina[/] [yellow]{self.pagina}[/]')
            if self.pagina == self.qtd:
                print(f':rotating_light: [red]Voce chegou ao final do livro {self.livro}[/]')


l1 = Livro('Narnia', 20)

l1.avançar(5)
l1.avançar(10)
l1.avançar(100)
