import pytest
from src.dado import Dado

class TestDado:

    def test_crear_dado(self):
        dado = Dado()
        assert 1 <= dado.get_valor() <= 6