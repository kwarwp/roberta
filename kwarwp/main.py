# roberta.kwarwp.main.py
# SPDX-License-Identifier: GPL-3.0-or-later
""" Jogo para ensino de programação Python.

.. codeauthor:: Carlo Oliveira <carlo@ufrj.br>

Changelog
---------
.. versionadded::    20.07
        classe Vitollino.

"""
from _spy.vitollino.main import Jogo, STYLE
from kwarwp.kwarwpp import main as kwarwp_main, Indio
MOANGEKO = """
.@.........
...........
.....#.¨...
...........
.....^.....

"""
API = """

|||||||||||||
|^.########.&
|||||||||||||

"""
APO = """
|||||||||||||
|.|||...|...|
|¨..|.|.|.|.|
|^|...|...|.&
"""
APA = """
°°°°°.++.°°
°°°°++°°..°
°°.++°°°°#°
°++°°°°°°#°
°^°°°°°°°.C
"""

class Moangeko(Indio):
    def executa(self):
        """
            Conjunto de comandos que o índio executa:
        """
        self.anda()
        #self.direita()
        #self.esquerda()
        #self.pega()
        #self.larga()
        #self.empurra()

class Api(Indio):
    def executa(self):
        """ Ajude o indio a chegar na oca.
        
            CONSELHO DO PAGÉ:
               "Há um enigma de meu tatara avô que sempre me ajudou a fazer tudo mais rápido:
                SE PADRÕES você encontrar INVOQUE o espírito dos Laços CORRETAMENTE e ele te ajudará:
                     for etapas in range(?):
                         self.o_que_você_deseja()
        """
        self.direita()
        self.anda()
        for passos in range(8):
            self.pega()
            self.esquerda()
            self.esquerda()
            self.larga()
            self.esquerda()
            self.esquerda()
            self.anda()
        self.anda()
        self.anda()
        self.anda()
        
class Apo(Indio):
    def executa(self):
        """ Ajude o indio a chegar na oca.
        
            CONSELHO DO PAGÉ:
               "Um feitiço de meu tatara avó me ajudava a fazer tudo mais rápido.
                O espírito dos Laços te ajudará se você o invocar corretamente:
                     for passos in range(?):
                         self.o_que_você_deseja()
        """
        self.direita()
        self.anda()
        for passos in range(8):
            self.pega()
            self.esquerda()
            self.esquerda()
            self.larga()
            self.esquerda()
            self.esquerda()
            self.anda()
        self.anda()
        self.anda()
        self.anda()

class Apa(Indio):
    def executa(self):
        """ Ajude o indio a chegar na oca.
        
            CONSELHO DO PAGÉ:
               "Um feitiço de meu tatara avó me ajudava a fazer tudo mais rápido.
                O espírito dos Laços te ajudará se você o invocar corretamente:
                     for passos in range(?):
                         self.o_que_você_deseja()
        """
        self.anda()
        self.empurra()


class Vitollino(Jogo):
    """ Empacota o engenho de jogo Vitollino """
    pass

def main(vitollino, medidas):
    return kwarwp_main(vitollino=vitollino, medidas=medidas, mapa=APA, indios=(Apa,))
        
    
if __name__ == "__main__":
    main(Jogo, STYLE)
