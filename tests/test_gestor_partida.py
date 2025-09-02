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