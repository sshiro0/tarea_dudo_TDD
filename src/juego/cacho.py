import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dados = []
        for i in range(5):
            self.dados.append(Dado())

    def get_lista_dados(self):
        return self.dados

    def revolver(self):
        for dado in self.dados:
            dado.revolver()

