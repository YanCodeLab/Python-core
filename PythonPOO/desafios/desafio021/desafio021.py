from rich import print

class Caneta:

    def __init__(self, cor='azul'):
        escolha = ''
        match cor.lower().rstrip(): # Compara o valor cor com os cases abaixo
            case 'azul':
                escolha = '[blue]'

            case 'vermelho | vermelha':
                escolha = '[red]'

            case 'verde':
                escolha = '[green]'

            case _:
                escolha = '[white]'

        self.cor = escolha
        self.tampado = True # Estado da caneta, com tampa

    def tampar(self):
        self.tampado = True

    def destapar(self):
        self.tampado = False

    def escrever(self, txt):
        if not self.tampado: # Se não for verdadeiro =False
            print(f'{self.cor}{txt}[/]', end='')
        else:
            print(f':no_entry_sign: A {self.cor}caneta[/] está tampada ')

    def quebrar_linha(self, linhas):
         print('\n' * linhas)


c1 = Caneta('azul')
c2 = Caneta('verde')
c3 = Caneta('vermelho')

c1.destapar()
c2.destapar()

c1.escrever('Ola mundo')
c1.quebrar_linha(1)
c2.escrever('Hello Word')
c2.quebrar_linha(2)

c3.escrever("Kon'nichiwa sekai")







