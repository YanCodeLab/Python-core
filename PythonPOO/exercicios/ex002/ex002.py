#Definição de Classe
class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa com nome e idade

    Para criar um gafanhoto faça
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = 'vazio', idade = 0): # Metodo Construtor
     # atributos de instancia
        self.nome = nome   # um '.self.nome' e o atributo e 'nome' e o parametro
        self.idade = idade # um '.self.idade' e o atributo e 'idade' e o parametro

     # Metódos de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f'O Gafanhoto(a) {self.nome} tem {self.idade} anos.\n{'-' * 40}'

    def __getstate__(self):
        return f'Estado: Nome;{self.nome} ,  Idade;{self.idade}'


#Declaração dos objetos

g1 = Gafanhoto('Yãn', 19) # Instancia o objeto
#chama os metodos
g1.aniversario() # soma + 1 na idade
print(g1)

print(g1.__dict__) #Attribute exibe o objeto como dicionario
print(g1.__getstate__()) #Dunder Method exibe o objeto mas vc que edita ja que é um metodo da sua classe
print('-' * 40)


g2 = Gafanhoto('José', 45)
print(g2)
print(g2.__getstate__()) # Dunder Method exibe o objeto mas vc que edita ja que é um metodo da sua classe
print('-' * 40)

g3 = Gafanhoto()
print(g3)
print(g3.__getstate__()) #Dunder Method exibe o objeto mas vc que edita ja que é um metodo da sua classe
print('-' * 40)

print(g1.__doc__) # DocString/ Dunder Attribute