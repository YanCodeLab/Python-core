from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 6

    def __init__(self, canal= 1, volume= 2):
        self.canal_atual:int = canal
        self.volume_atual = volume
        self.tv_status = False

    def aumenta_canal(self):
        if self.tv_status: # Se a TV estiver ligada
            if self.canal_atual == ControleRemoto.canal_max: # Se o canal atual ja estiver no ultimo canal disponivel
                self.canal_atual = ControleRemoto.canal_min  # Volta para o canal inicial
            else:
                self.canal_atual += 1

    def diminui_canal(self):
        if self.tv_status: #Se a Tv estiver ligada
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def aumenta_volume(self):
        if self.tv_status: #Se a Tv estiver ligada
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1

    def diminui_volume(self):
        if self.tv_status:  # Se a Tv estiver ligada
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def liga_desliga_tv(self):
        self.tv_status = not self.tv_status # Inverte o estado da TV

    def mostra_tv(self):
       conteudo = ''
       if not self.tv_status: # Se o status da TV for False
         conteudo = f':no_entry_sign: [red]A TV está desligada[/]'

       else:
           conteudo = 'CANAL ='
           for c in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1): # Exibição de canais disponiveis
               if c == self.canal_atual:
                 conteudo += f'[yellow on yellow] {c} [/]' #Exibição Canal atual
               else:
                 conteudo += f' {c}'

           conteudo += '\nVOLUME ='
           for v in range(ControleRemoto.volume_min, ControleRemoto.volume_max):
               if v <= self.volume_atual:
                 conteudo += f'[black on cyan] [/]' # Volume selecionado
               else:
                 conteudo += f'[black on white] [/]' # Volume não selecionado


       tv = Panel(conteudo, title='[ TV ]', width=40)
       print(tv)

c1 = ControleRemoto() # Criação do objeto
while True:
    c1.mostra_tv()
    comando = str(input(f'\n< CH{c1.canal_atual} >  - VOL{c1.volume_atual} + '))
    match comando:
        case '0':
            break

        case '@':
            c1.liga_desliga_tv()

        case '>':
            c1.aumenta_canal()

        case '<':
            c1.diminui_canal()

        case '-':
            c1.diminui_volume()

        case '+':
            c1.aumenta_volume()

    print('\n' * 10) #Pula linha
