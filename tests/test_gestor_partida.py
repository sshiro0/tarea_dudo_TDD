import sys
import os

from juego.cacho import Cacho
from juego.gestor_partida import GestorPartida


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestGestorPartida:
    """Clase de pruebas para la clase GestorPartida que gestiona partidas del juego."""

    def test_crear_partida(self):
        """
        Test para verificar la creación correcta de una partida con múltiples jugadores.
        """
        # Crear una partida con 7 jugadores
        gestor = GestorPartida(7)

        # Verificar que el gestor se creó correctamente
        assert gestor is not None
        # Verificar que se crearon exactamente 7 jugadores
        assert len(gestor.jugadores) == 7

        # Verificar que cada jugador es una instancia de Cacho y tiene 5 dados
        for jugador in gestor.jugadores:
            assert isinstance(jugador, Cacho)
            assert len(jugador.get_lista_dados()) == 5

    def test_seleccionar_jugador_inicial(self, mocker):
        """
        Test para verificar la selección aleatoria del jugador inicial.
        """
        # Mockear random.randint para que siempre retorne 0 (primer jugador)
        mocker.patch('random.randint', return_value=0)

        # Crear partida con 4 jugadores
        gestor = GestorPartida(4)
        # Seleccionar jugador inicial
        jugador_inicial = gestor.definir_jugador_inicial()

        # Verificar que el jugador inicial es el primero de la lista
        assert jugador_inicial == gestor.jugadores[0]
        # Verificar que el índice actual se estableció correctamente
        assert gestor.index_actual == 0

    def test_siguiente_turno(self):
        """
        Test para verificar el avance de turnos entre jugadores.
        """
        # Crear partida con 3 jugadores
        gestor = GestorPartida(3)
        # Establecer jugador inicial (índice aleatorio, pero luego testeamos secuencia)
        gestor.definir_jugador_inicial()

        # Avanzar al siguiente turno y verificar que es el jugador 1
        siguiente = gestor.siguiente_turno()
        assert siguiente is gestor.jugadores[1]  # Misma instancia

        # Avanzar otro turno y verificar que es el jugador 2
        siguiente = gestor.siguiente_turno()
        assert siguiente is gestor.jugadores[2]  # Misma instancia

        # Avanzar otro turno y verificar que vuelve al jugador 0 (comportamiento circular)
        siguiente = gestor.siguiente_turno()
        assert siguiente is gestor.jugadores[0]  # Misma instancia