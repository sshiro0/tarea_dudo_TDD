import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.cacho import Cacho
from unittest.mock import MagicMock


class TestCacho:

    def test_crear_cacho(self):
        cacho = Cacho()
        assert len(cacho.get_lista_dados()) == 5

    def test_revolver_cacho(self, mocker):
        initial_mock = [1, 2, 3, 4, 5]
        final_mock = [6, 1, 2, 3, 4]

        mock_randint = MagicMock(side_effect = initial_mock + final_mock)
        mocker.patch('juego.dado.random.randint', mock_randint)

        # Antes de revolver
        cacho = Cacho()
        initial_dados = cacho.get_lista_dados()

        initial_values = []

        for dado in initial_dados:
            dado_value = dado.get_valor()
            initial_values.append(dado_value)

        assert initial_values ==  initial_mock

        # Después de revolver
        cacho.revolver()
        final_dados = cacho.get_lista_dados()

        final_values = []

        for dado in final_dados:
            dado_update = dado.get_valor()
            final_values.append(dado_update)

        assert final_values == final_mock

    def test_mostrar_dados(self, mocker):
        mock_valores = [1, 3, 5, 2, 4]
        mock_randint = MagicMock(side_effect=mock_valores)
        mocker.patch('juego.dado.random.randint', mock_randint)

        cacho = Cacho()
        valores_mostrados = cacho.get_valor_dados()

        assert valores_mostrados == mock_valores

    def test_mostrar_denominaciones(self, mocker):
        mock_valores = [1, 2, 3, 4, 5]
        mock_randint = MagicMock(side_effect=mock_valores)
        mocker.patch('juego.dado.random.randint', mock_randint)

        cacho = Cacho()
        denominaciones = cacho.get_denominaciones()

        denominaciones_esperadas = ['AS', 'TONTO', 'TREN', 'CUADRA', 'QUINA']
        assert denominaciones == denominaciones_esperadas

    def test_alterar_cantidad_dados(self, mocker):
        mock_randint = MagicMock(side_effect=[1, 2, 3, 4, 5, 6, 1])
        mocker.patch('juego.dado.random.randint', mock_randint)

        cacho = Cacho()
        assert len(cacho.get_lista_dados()) == 5

        cacho.eliminar_dado()
        cacho.eliminar_dado()
        assert len(cacho.get_lista_dados()) == 3

        cacho.agregar_dado()
        assert len(cacho.get_lista_dados()) == 4

        cacho.agregar_dado()
        assert len(cacho.get_lista_dados()) == 5

        cacho.agregar_dado()
        assert len(cacho.get_lista_dados()) == 5
