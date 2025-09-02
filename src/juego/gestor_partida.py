import sys
import os
import random


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .cacho import Cacho

class GestorPartida:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.jugadores = []
        self.index_inicial = None
        self.jugador_inicial = None

        for i in range(cantidad):
            self.jugadores.append(Cacho())

    def definir_jugador_inicial(self):
        self.index_inicial = random.randint(0, self.cantidad - 1)
        self.jugador_inicial = self.jugadores[self.index_inicial]

        return self.jugador_inicial