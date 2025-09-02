import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import MagicMock
from juego.contador_pintas import ContadorPintas


def crear_mock_dado(valor):
    """
    Crea un mock de un dado con un valor específico.
    """
    dado_mock = MagicMock()
    dado_mock.get_valor.return_value = valor
    return dado_mock


def crear_mock_cacho(valores):
    """
    Crea un mock de un cacho (conjunto de dados) con valores específicos.
    """
    dados_mock = []
    for valor in valores:
        dados_mock.append(crear_mock_dado(valor))

    cacho_mock = MagicMock()
    cacho_mock.get_lista_dados.return_value = dados_mock
    return cacho_mock


class TestContadorPintas:
    """Clase de pruebas para la clase ContadorPintas que cuenta ocurrencias de pintas."""

    def test_contar_pintas_ronda_normal(self):
        """
        Test para verificar el conteo de pintas en ronda normal.
        """
        cacho_mock = crear_mock_cacho([1, 2, 1, 4, 5])
        contador = ContadorPintas()

        # Pinta 3: Los 2 ases cuentan como comodines + ningún tres natural = 2
        assert contador.contar_pintas_global(3, [cacho_mock], False) == 2

        # Pinta 6: Los 2 ases cuentan como comodines + ningún seis natural = 2
        assert contador.contar_pintas_global(6, [cacho_mock], False) == 2

        # Pinta 1: Solo los ases naturales (2) + comodines no cuentan para sí mismos = 2
        assert contador.contar_pintas_global(1, [cacho_mock], False) == 2

    def test_contar_pintas_ronda_especial(self):
        """
        Test para verificar el conteo de pintas en ronda especial.
        """
        cacho_mock = crear_mock_cacho([1, 2, 1, 4, 5])
        contador = ContadorPintas()

        # Pinta 3: No hay comodines + ningún tres natural = 0
        assert contador.contar_pintas_global(3, [cacho_mock], True) == 0

        # Pinta 6: No hay comodines + ningún seis natural = 0
        assert contador.contar_pintas_global(6, [cacho_mock], True) == 0

        # Pinta 1: 2 ases naturales (los comodines no existen en especial) = 2
        assert contador.contar_pintas_global(1, [cacho_mock], True) == 2

        # Pinta 2: 1 dos natural = 1
        assert contador.contar_pintas_global(2, [cacho_mock], True) == 1