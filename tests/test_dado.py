import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.dado import Dado
from unittest.mock import MagicMock
from juego.denominacion import Denominacion


class TestDado:

    def test_crear_dado(self):
        dado = Dado()
        assert 1 <= dado.get_valor() <= 6

    def test_denominaciones(self, mocker):
        mock_randint = MagicMock(side_effect=[1, 2, 3, 4, 5, 6])
        mocker.patch('juego.dado.random.randint', mock_randint)

        dado1 = Dado()
        dado2 = Dado()
        dado3 = Dado()
        dado4 = Dado()
        dado5 = Dado()
        dado6 = Dado()

        assert dado1.get_valor() == Denominacion.AS.value
        assert dado2.get_valor() == Denominacion.TONTO.value
        assert dado3.get_valor() == Denominacion.TREN.value
        assert dado4.get_valor() == Denominacion.CUADRA.value
        assert dado5.get_valor() == Denominacion.QUINA.value
        assert dado6.get_valor() == Denominacion.SEXTO.value

        assert dado1.get_denominacion() == Denominacion.AS.name
        assert dado2.get_denominacion() == Denominacion.TONTO.name
        assert dado3.get_denominacion() == Denominacion.TREN.name
        assert dado4.get_denominacion() == Denominacion.CUADRA.name
        assert dado5.get_denominacion() == Denominacion.QUINA.name
        assert dado6.get_denominacion() == Denominacion.SEXTO.name

        assert mock_randint.call_count == 6
        mock_randint.assert_called_with(1, 6)

