from pessoa import Pessoa

class Funcionaria(Pessoa):  #Subclasse
    def __init__(self, nome, idade, cargo, setor): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'A {self.nome} bateu o ponto')
