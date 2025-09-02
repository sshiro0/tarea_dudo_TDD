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
        index_inicial = gestor.definir_jugador_inicial()

        # Verificar que el jugador inicial es el primero de la lista
        assert gestor.get_jugador_actual() == gestor.jugadores[0]
        # Verificar que el índice actual se estableció correctamente
        assert index_inicial == 0

    def test_siguiente_turno(self):
        """
        Test para verificar el avance de turnos entre jugadores.
        """
        gestor = GestorPartida(3)
        gestor.index_actual = 0

        assert gestor.siguiente_turno() == 1
        assert gestor.siguiente_turno() == 2
        assert gestor.siguiente_turno() == 0
        assert gestor.siguiente_turno() == 1

    def test_obtener_jugador_actual(self):
        """
        Test para verificar la obtención del jugador actual según el índice.
        También valida que se retorne None si no hay un índice asignado.
        """
        gestor = GestorPartida(3)
        gestor.index_actual = 1

        jugador_actual = gestor.get_jugador_actual()
        assert jugador_actual is gestor.jugadores[1]

        gestor.index_actual = None
        assert gestor.get_jugador_actual() is None

    def test_obtener_jugador_por_indice(self):
        """
        Test para verificar que se obtiene correctamente un jugador
        a partir de su índice en la lista de jugadores.
        """
        gestor = GestorPartida(3)

        assert gestor.get_jugador_indice(0) is gestor.jugadores[0]
        assert gestor.get_jugador_indice(2) is gestor.jugadores[2]

    def test_get_jugador_actual_index_valido(self):
        """
        Test para verificar que se retorna correctamente el índice
        del jugador actual cuando está definido.
        """
        gestor = GestorPartida(3)
        gestor.index_actual = 1
        assert gestor.get_jugador_actual_index() == 1

    def test_get_jugador_actual_index_none(self):
        """
        Test para verificar que se retorna None cuando no hay un
        jugador actual definido (index_actual es None).
        """
        gestor = GestorPartida(3)
        gestor.index_actual = None
        assert gestor.get_jugador_actual_index() is None

