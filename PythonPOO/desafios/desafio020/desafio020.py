from rich import print
from rich.panel import Panel

class Gamer:

    #Metodo contrutor
    def __init__(self, nome, nick): # Recebe o nome e o nick
        #Atributos de instancia
        self.nome = nome
        self.nick = nick
        self.favoritos = [] # Cria lista para salvar os jogos favoritos do user

    def ficha(self):
        '''
        Formata as informaçoes e exibe uma ficha com nome e os jogos favoritos
        '''

        #Conteudos dentro da ficha
        mensagem_nome = f'Nome Real: [bold black on blue]{self.nome}[/]\n'
        mensagem_jogos = '' # Nomes dos jogos salvos

        for j in self.favoritos: # Acessa a lista de jogos
            mensagem_jogos += f':video_game: [blue]{j}[/]\n' # Formata a exibição dos jogos salvos na lista

        conteudo = mensagem_nome + mensagem_jogos # Concatena todas os textos


        ficha = Panel(conteudo, title=f'Jogadora <{self.nick}>', width=35) # Cria ficha
        print(ficha)# exibe ficha

    def add_favoritos(self, jogo):

        '''
        Recebe os jogos, salva na lista self.favoritos, e formata a lista para ordem alfabetica
        '''

        self.favoritos.append(jogo.title())
        self.favoritos.sort() # Organiza lista de jogos em ordem alfabetica



#Instacia do Objeto
g1 = Gamer('Yan', 'Blade001')

#Metodos
g1.add_favoritos('Detroit Because Human')
g1.add_favoritos("assassin's Creed Black Flag")
g1.add_favoritos('read dead 2')

g1.ficha()

g2 = Gamer('Bia', 'bIA')

g2.add_favoritos('Minecraft')
g2.add_favoritos('the sims')
g2.add_favoritos('Stardew Valley')

g2.ficha()
