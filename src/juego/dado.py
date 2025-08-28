import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .denominacion import Denominacion
import random

class Dado:
    def __init__(self):
        self.valor = random.randint(1, 6)

    def get_valor(self):
        return self.valor

    def get_denominacion(self):
        return Denominacion(self.valor).name

