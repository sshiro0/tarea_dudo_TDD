import pytest
from src.dado import Dado

class TestDado:

    def test_crear_dado(self):
        Dado = Dado()
        assert 1 <= Dado.get_valor() <= 6

    
