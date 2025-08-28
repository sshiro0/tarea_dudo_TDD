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

        dados = []
        for i in range(6):
            dado = Dado()
            dados.append(dado)

        denominaciones = [
            Denominacion.AS, Denominacion.TONTO, Denominacion.TREN,
            Denominacion.CUADRA, Denominacion.QUINA, Denominacion.SEXTO
        ]

        for i in range(6):
            assert dados[i].get_valor() == denominaciones[i].value
            assert dados[i].get_denominacion() == denominaciones[i].name

        assert mock_randint.call_count == 6
        mock_randint.assert_called_with(1, 6)