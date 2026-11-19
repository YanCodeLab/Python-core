from abc import ABC, abstractclassmethod # Biblioteca de metodos abastratos

class Pessoa(ABC): #Classe Mãe Abstrata
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractclassmethod #Cria metodo abstrato (obriga todas a classes filhas terem esse metodo)
    def estudar(self):
        pass


class Aluno(Pessoa): #Subclasse
    def __init__(self, nome, idade, curso, turma): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O {self.nome} fez a matricula')


    def estudar(self):
        print(f'O aluno {self.nome} está estudando {self.curso}')



class Professor(Pessoa):  #Subclasse
    def __init__(self, nome, idade, especialidade, nivel): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'{self.nome} começou a dar aula')


    def estudar(self):
        print(f'O {self.nome} está estudando {self.nivel} em {self.especialidade}')

class Funcionaria(Pessoa):  #Subclasse
    def __init__(self, nome, idade, cargo, setor): # Define parametros a ser recebido
        super().__init__(nome, idade) # Parametros que são herança da superclasse
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'A {self.nome} bateu o ponto')


    def estudar(self):
        print(f'{self.nome} está se estudando sobre {self.setor}')