import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.cacho import Cacho
from unittest.mock import MagicMock


class TestCacho:

    def test_crear_cacho(self):
        cacho = Cacho()
        assert len(cacho.get_lista_dados()) == 5




