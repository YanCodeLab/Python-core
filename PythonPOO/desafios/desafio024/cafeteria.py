from abc import ABC, abstractmethod

class Bebida_quente(ABC): # Classe mãe ABSTRATA

    def preparar(self): # Metodo Principal,  Reune todos os outros metodos
        print('--- Iniciando Preparo ---')
        self.fever_agua()
        self.misturar()
        self.servir()
        print('-- Bebida Pronta --')

    def fever_agua(self): # Metodo COMUM PARA TODOS
        print('1 - Fervendo agua á 100 C°')


    #   METODOS ABSTRATOS/ OBRIGATORIOS
    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(Bebida_quente):


    def misturar(self):
        print('2 - Passando agua pressurizada pelo pó de café moido')

    def servir(self):
        print(' 3 - Servindo em xicara pequena')


class Cha(Bebida_quente):


    def misturar(self):
        print('2 - Mergulhando sache de ervas na água.')

    def servir(self):
        print('3 - Servido na caneca de porcelana com limão')


class Leite(Bebida_quente):


    def misturar(self):
        print('2 - Passando vapor pressurizado pelo bico do leite ')

    def servir(self):
        print('3 - Servindo na caneca grande, já com café')
