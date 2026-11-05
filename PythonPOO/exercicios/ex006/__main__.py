from rich import inspect, print
from aluno import Aluno
from  professor import Professor
from funcionario import Funcionaria

#Objetos
a1 = Aluno('Yan', 19, 'Eng.Computação', '2-a')
a1.fazer_aniversario() #Metodo de Pessoa (superclasse)
a1.fazer_matricula() # Metodo de aluno (subclasse)
#inspect(a1, methods=True)

p1 = Professor('Adriana', 50, 'Psicologia', 'Mestrado')
p1.fazer_aniversario() #Metodo de Pessoa (superclasse)
p1.dar_aula() # Metodo de profeesor (subclasse)
#inspect(p1, methods=True)

f1 = Funcionaria('Lydia', 30, 'Supervisora', 'Compras')
f1.bater_ponto() # Metodo de funcionario (subclasse)
#inspect(f1, methods=True)