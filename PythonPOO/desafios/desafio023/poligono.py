from abc import ABC, abstractmethod #Importaçoes para abstração
import math
from re import match


class Poligono(ABC): # Classe mãe abstrata

    def __init__(self, lados): # Metodo construtor
        self.qtd_lados = lados

    #METODOS ABSTRATOS (OBRIGATORIOS)
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class  Quadrado(Poligono): #Classe filha de Poligono
    def __init__(self, lado = 1):
       super().__init__(4)
       self.lado = lado

    def perimetro(self): #Metodo para Calcular o perimetro do quadrado
        return  self.qtd_lados * self.lado

    def area(self): # Metodo para calcular Area do quadrado
        return self.lado ** 2 # 𝑨rea = L x L


class Circulo(Poligono):

    def __init__(self, raio = 1 ):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio # Formula para calcular perimetro de um circulo 2 x pi x raio

    def area(self):
        return math.pi * self.raio ** 2 #Formula para calcular area do circulo