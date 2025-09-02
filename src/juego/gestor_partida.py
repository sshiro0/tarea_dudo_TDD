import sys
import os
import random


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .cacho import Cacho

class GestorPartida:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.jugadores = []
        self.jugador_actual = None

        for i in range(cantidad):
            self.jugadores.append(Cacho())

    def definir_jugador_inicial(self):
        index = random.randint(0, self.cantidad - 1)
        self.jugador_actual = self.jugadores[index]
        return self.jugador_actual