import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import MagicMock
from juego.contador_pintas import ContadorPintas

class TestContadorPintas:
    def test_contar_pintas_ronda_normal(self):
        mock_dados = [
            MagicMock(get_valor=MagicMock(return_value=1)),
            MagicMock(get_valor=MagicMock(return_value=2)),
            MagicMock(get_valor=MagicMock(return_value=1)),
            MagicMock(get_valor=MagicMock(return_value=4)),
            MagicMock(get_valor=MagicMock(return_value=5))
        ]

        mock_cacho = MagicMock(get_lista_dados=MagicMock(return_value=mock_dados))
        contador = ContadorPintas()

        assert contador.contar_pintas_global(3, [mock_cacho], especial=False) == 2
        assert contador.contar_pintas_global(6, [mock_cacho], especial=False) == 2
        assert contador.contar_pintas_global(1, [mock_cacho], especial=False) == 2

    def test_contar_pintas_ronda_especial(self):
        mock_dados = [
            MagicMock(get_valor=MagicMock(return_value=1)),
            MagicMock(get_valor=MagicMock(return_value=2)),
            MagicMock(get_valor=MagicMock(return_value=1)),
            MagicMock(get_valor=MagicMock(return_value=4)),
            MagicMock(get_valor=MagicMock(return_value=5))
        ]

        mock_cacho = MagicMock(get_lista_dados=MagicMock(return_value=mock_dados))
        contador = ContadorPintas()

        assert contador.contar_pintas_global(3, [mock_cacho], especial=True) == 0
        assert contador.contar_pintas_global(6, [mock_cacho], especial=True) == 0
        assert contador.contar_pintas_global(1, [mock_cacho], especial=True) == 2
        assert contador.contar_pintas_global(2, [mock_cacho], especial=True) == 1