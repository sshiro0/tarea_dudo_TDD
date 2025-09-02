import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .cacho import Cacho

class GestorPartida:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.jugadores = []

        for i in range(cantidad):
            self.jugadores.append(Cacho())