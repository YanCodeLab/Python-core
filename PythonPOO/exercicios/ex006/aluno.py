from pessoa import Pessoa


class Aluno(Pessoa): #Subclasse
    def __init__(self, nome, idade, curso, turma): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O {self.nome} fez a matricula')
