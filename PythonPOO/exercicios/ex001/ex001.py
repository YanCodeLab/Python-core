#Definição de Classe
class Gafanhoto:
    def __init__(self): # Metodo Construtor
     # atributos de instancia
        self.nome = ''
        self.idade = 0

     # Metódos de instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'O Gafanhoto(a) {self.nome} tem {self.idade} anos.\n{'-'*40}'




#Declaração dos objetos

g1 = Gafanhoto() # Instancia o objeto
g1.nome = 'Yãn' # Adiciona dados
g1.idade = 19
#chama os metodos
g1.aniversario() # soma + 1 na idade
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'José'
g2.idade = '45'
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = input('Digite seu Nome Gafanhoto:')
g3.idade = int(input('Digite sua Idade:'))
print(g3.mensagem())
