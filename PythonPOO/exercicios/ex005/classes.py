class Pessoa: #SuperClasse
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1


class Aluno(Pessoa): #Subclasse
    def __init__(self, nome, idade, curso, turma): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O {self.nome} fez a matricula')


class Professor(Pessoa):  #Subclasse
    def __init__(self, nome, idade, especialidade, nivel): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} começou a dar aula')


class Funcionaria(Pessoa):  #Subclasse
    def __init__(self, nome, idade, cargo, setor): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'A {self.nome} bateu o ponto')