import sys
import os
import random


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .cacho import Cacho

class GestorPartida:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.jugadores = []
        self.index_actual = None
        self.jugador_actual = None

        for i in range(cantidad):
            self.jugadores.append(Cacho())

    def definir_jugador_inicial(self):
        self.index_actual = random.randint(0, self.cantidad - 1)
        self.jugador_actual = self.jugadores[self.index_actual]
        return self.index_actual

    def get_jugador_actual_index(self):
        if self.index_actual is not None:
            return self.index_actual
        return None

    def get_jugador_actual(self):
        if self.index_actual is not None:
            return self.jugadores[self.index_actual]
        return None

    def siguiente_turno(self):
        self.index_actual = (self.index_actual + 1) % self.cantidad
        self.jugador_actual = self.jugadores[self.index_actual]
        return self.index_actual

    def get_jugador_indice(self, index):
        return self.jugadores[index]

    def get_jugadores_activos(self):
        indices_activos = []
        total_jugadores = len(self.jugadores)

        for indice_jugador in range(total_jugadores):
            jugador_actual = self.jugadores[indice_jugador]
            dados_del_jugador = jugador_actual.get_lista_dados()

            if len(dados_del_jugador) > 0:
                indices_activos.append(indice_jugador)

        return indices_activos

    def jugador_tiene_dados(self, jugador_idx):
        jugador_actual = self.jugadores[jugador_idx]
        lista_dados_jugador = jugador_actual.get_lista_dados()
        cantidad_dados = len(lista_dados_jugador)
        tiene_dados = cantidad_dados > 0
        return tiene_dados