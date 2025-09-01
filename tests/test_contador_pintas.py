import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import MagicMock
from juego.contador_pintas import ContadorPintas


def crear_mock_dado(valor):
    dado_mock = MagicMock()
    dado_mock.get_valor.return_value = valor
    return dado_mock

def crear_mock_cacho(valores):
    dados_mock = []
    for valor in valores:
        dados_mock.append(crear_mock_dado(valor))

    cacho_mock = MagicMock()
    cacho_mock.get_lista_dados.return_value = dados_mock
    return cacho_mock

class TestContadorPintas:

    def test_contar_pintas_ronda_normal(self):
        cacho_mock = crear_mock_cacho([1, 2, 1, 4, 5])
        contador = ContadorPintas()

        assert contador.contar_pintas_global(3, [cacho_mock], False) == 2
        assert contador.contar_pintas_global(6, [cacho_mock], False) == 2
        assert contador.contar_pintas_global(1, [cacho_mock], False) == 2

    def test_contar_pintas_ronda_especial(self):
        cacho_mock = crear_mock_cacho([1, 2, 1, 4, 5])
        contador = ContadorPintas()

        assert contador.contar_pintas_global(3, [cacho_mock], True) == 0
        assert contador.contar_pintas_global(6, [cacho_mock], True) == 0
        assert contador.contar_pintas_global(1, [cacho_mock], True) == 2
        assert contador.contar_pintas_global(2, [cacho_mock], True) == 1