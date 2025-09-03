import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .cacho import Cacho


class GestorPartida:
    """
    Clase que gestiona una partida del juego, administrando los jugadores,
    turnos y estado general de la partida.

    Responsable de crear los jugadores, asignar turnos, y mantener el estado
    actual de la partida incluyendo qué jugador tiene el turno actual.
    """

    def __init__(self, cantidad_jugadores):
        """
        Inicializa una nueva partida con la cantidad especificada de jugadores.
        """
        self.cantidad_jugadores = cantidad_jugadores
        self.jugadores = []
        self.index_actual = None
        self.jugador_actual = None

        self.sentido = 1

        self.estado_especial = None

        self.buffer_dados_extra = {i: 0 for i in range(cantidad_jugadores)}

        self.ronda_especial_activada = {i: False for i in range(cantidad_jugadores)}

        for i in range(cantidad_jugadores):
            self.jugadores.append(Cacho())

    def definir_jugador_inicial(self):
        """
        Se establece jugador incial mediante un torneo que dura hasta que un jugador obtiene el dado mayor.
        """
        ganador = -1
        index_actual = 0
        while ganador == -1:
            torneo = []
            for jugador in range(self.cantidad_jugadores):
                torneo.append(random.randint(1, 6))

            for jugador in range(self.cantidad_jugadores):
                if torneo[jugador] > ganador:
                    ganador = torneo[jugador]
                    index_actual = jugador
                elif torneo[jugador] == ganador:
                    ganador = -1
                    index_actual = 0
                    break
        self.index_actual = index_actual
        self.jugador_actual = self.jugadores[self.index_actual]
        return self.index_actual

    def get_jugador_actual_index(self):
        """
        Obtiene el índice del jugador que tiene el turno actual.
        """
        if self.index_actual is not None:
            return self.index_actual
        return None

    def get_jugador_actual(self):
        """
        Obtiene el objeto Cacho del jugador que tiene el turno actual.
        """
        if self.index_actual is not None:
            return self.jugadores[self.index_actual]
        return None

    def siguiente_turno(self):
        """
        Avanza al siguiente turno de manera circular.

        El turno pasa al siguiente jugador en la lista, volviendo al primero
        después del último jugador (comportamiento circular).
        """
        self.index_actual = (self.index_actual + 1) % self.cantidad_jugadores
        self.jugador_actual = self.jugadores[self.index_actual]
        return self.index_actual

    def get_jugador(self, index):
        """
        Obtiene el objeto Cacho de un jugador específico por su índice.
        """
        return self.jugadores[index]

    def get_jugadores_activos(self):
        """
        Obtiene los índices de todos los jugadores que aún tienen dados.

        Un jugador se considera activo si tiene al menos un dado en su cacho.
        """
        indices_activos = []
        total_jugadores = len(self.jugadores)

        for indice_jugador in range(total_jugadores):
            jugador_actual = self.jugadores[indice_jugador]
            dados_del_jugador = jugador_actual.get_lista_dados()

            if len(dados_del_jugador) > 0:
                indices_activos.append(indice_jugador)

        return indices_activos

    def jugador_tiene_dados(self, jugador_idx):
        """
        Verifica si un jugador específico aún tiene dados.
        """
        jugador_actual = self.jugadores[jugador_idx]
        lista_dados_jugador = jugador_actual.get_lista_dados()
        cantidad_dados = len(lista_dados_jugador)
        tiene_dados = cantidad_dados > 0
        return tiene_dados

    def definir_sentido(self, sentido):
        if sentido in (1, -1):
            self.sentido = sentido
            return self.sentido
        return None

    def activar_estado_especial(self, tipo):
        if tipo in (1, 2):
            self.estado_especial = tipo

    def desactivar_estado_especial(self):
        self.estado_especial = None

    def es_ronda_especial(self):
        return self.estado_especial is not None

    def get_tipo_ronda_especial(self):
        return self.estado_especial

    def otorgar_dado_extra(self, idx_jugador):
        jugador = self.jugadores[idx_jugador]
        if len(jugador.get_lista_dados()) < 5:
            jugador.agregar_dado()
        else:
            self.buffer_dados_extra[idx_jugador] += 1

    def intentar_recuperar_dado_extra(self, idx_jugador):
        if self.buffer_dados_extra[idx_jugador] > 0:
            jugador = self.jugadores[idx_jugador]
            if len(jugador.get_lista_dados()) < 5:
                jugador.agregar_dado()
                self.buffer_dados_extra[idx_jugador] -= 1

    def get_buffer_dados_extra(self, idx_jugador):
        return self.buffer_dados_extra.get(idx_jugador, 0)

    def verificar_ronda_especial(self, idx_jugador):
        jugador = self.jugadores[idx_jugador]
        if len(jugador.get_lista_dados()) == 1 and not self.ronda_especial_activada[idx_jugador]:
            self.ronda_especial_activada[idx_jugador] = True
            return True
        return False
