from pessoa import Pessoa


class Professor(Pessoa):  #Subclasse
    def __init__(self, nome, idade, especialidade, nivel): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} começou a dar aula')
