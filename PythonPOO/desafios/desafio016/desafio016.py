from rich import print
class Funcionario:
    """
    Recebe informaçoes de um funcionario
    nome, setor, cargo
    retorna uma mensagem formatada das informaçoes

    """
    #Atributo de Classe
    empresa = 'Construcciones y Auxiliar de Ferrocarriles' # Esse é um atributo de classe é igual para todos os objetos

    def __init__(self, nome, setor, cargo): # Metodo Construtor
        #Atributos de instancia
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    #Metódos
    def apresentar(self):
        return f' :raised_hand_with_part_between_middle_and_ring_fingers: Olá, sou [red]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa} :train:'



Funcionario.empresa = 'CAF' # Muda o Atributo de classe


#Instacias do objeto
c1 = Funcionario('Yãn', 'Manutenção', 'Eletricista')
print(c1.apresentar())

c2 = Funcionario('Vagner', 'Manutenção', 'Supervisor')
print(c2.apresentar())

