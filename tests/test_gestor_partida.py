import sys
import os

from juego.cacho import Cacho
from juego.gestor_partida import GestorPartida

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class TestGestorPartida:

    def test_crear_partida(self):
        gestor = GestorPartida(7)

        assert gestor is not None
        assert len(gestor.jugadores) == 7

        for jugador in gestor.jugadores:
            assert isinstance(jugador, Cacho)

            assert len(jugador.get_lista_dados()) == 5

    def test_seleccionar_jugador_inicial(self, mocker):
        mocker.patch('random.randint', return_value=0)

        gestor = GestorPartida(4)
        jugador_inicial = gestor.definir_jugador_inicial()

        assert jugador_inicial == gestor.jugadores[0]
        assert gestor.index_actual == 0


    def test_siguiente_turno(self):
        gestor = GestorPartida(3)
        gestor.definir_jugador_inicial()

        siguiente = gestor.siguiente_turno()
        assert siguiente is gestor.jugadores[1]

        siguiente = gestor.siguiente_turno()
        assert siguiente is gestor.jugadores[2]

        siguiente = gestor.siguiente_turno()
        assert siguiente is gestor.jugadores[0]