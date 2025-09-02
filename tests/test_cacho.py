import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.cacho import Cacho
from unittest.mock import MagicMock


class TestCacho:
    """Clase de pruebas para la clase Cacho que gestiona un conjunto de dados."""

    def test_crear_cacho(self):
        """
        Test para verificar la creación correcta de un cacho con 5 dados.
        """
        cacho = Cacho()
        assert len(cacho.get_lista_dados()) == 5

    def test_revolver_cacho(self, mocker):
        """
        Test para verificar que el método revolver() cambia los valores de los dados.
        """
        # Valores mock para la primera generación de dados
        initial_mock = [1, 2, 3, 4, 5]
        # Valores mock después de revolver
        final_mock = [6, 1, 2, 3, 4]

        # Mock que devuelve los valores iniciales primero y luego los finales
        mock_randint = MagicMock(side_effect=initial_mock + final_mock)
        mocker.patch('juego.dado.random.randint', mock_randint)

        # Crear cacho y obtener valores iniciales
        cacho = Cacho()
        initial_dados = cacho.get_lista_dados()

        initial_values = []
        for dado in initial_dados:
            dado_value = dado.get_valor()
            initial_values.append(dado_value)

        # Verificar que los valores iniciales coinciden con el mock
        assert initial_values == initial_mock

        # Revolver el cacho y obtener nuevos valores
        cacho.revolver()
        final_dados = cacho.get_lista_dados()

        final_values = []
        for dado in final_dados:
            dado_update = dado.get_valor()
            final_values.append(dado_update)

        # Verificar que los valores cambiaron después de revolver
        assert final_values == final_mock

    def test_mostrar_dados(self, mocker):
        """
        Test para verificar que get_valor_dados() retorna los valores correctos.
        """
        mock_valores = [1, 3, 5, 2, 4]
        mock_randint = MagicMock(side_effect=mock_valores)
        mocker.patch('juego.dado.random.randint', mock_randint)

        cacho = Cacho()
        valores_mostrados = cacho.get_valor_dados()

        # Verificar que los valores mostrados coinciden con los mockeados
        assert valores_mostrados == mock_valores

    def test_mostrar_denominaciones(self, mocker):
        """
        Test para verificar que get_denominaciones() retorna las denominaciones correctas.
        """
        mock_valores = [1, 2, 3, 4, 5]
        mock_randint = MagicMock(side_effect=mock_valores)
        mocker.patch('juego.dado.random.randint', mock_randint)

        cacho = Cacho()
        denominaciones = cacho.get_denominaciones()

        denominaciones_esperadas = ['AS', 'TONTO', 'TREN', 'CUADRA', 'QUINA']
        # Verificar que las denominaciones coinciden con las esperadas
        assert denominaciones == denominaciones_esperadas

    def test_alterar_cantidad_dados(self, mocker):
        """
        Test para verificar los métodos eliminar_dado() y agregar_dado().
        """
        # Mock que proporciona valores para 7 dados (5 iniciales + 2 nuevos)
        mock_randint = MagicMock(side_effect=[1, 2, 3, 4, 5, 6, 1])
        mocker.patch('juego.dado.random.randint', mock_randint)

        cacho = Cacho()
        # Verificar que empieza con 5 dados
        assert len(cacho.get_lista_dados()) == 5

        # Eliminar 2 dados y verificar que quedan 3
        cacho.eliminar_dado()
        cacho.eliminar_dado()
        assert len(cacho.get_lista_dados()) == 3

        # Agregar 1 dado y verificar que quedan 4
        cacho.agregar_dado()
        assert len(cacho.get_lista_dados()) == 4

        # Agregar otro dado y verificar que vuelve a 5
        cacho.agregar_dado()
        assert len(cacho.get_lista_dados()) == 5

        # Intentar agregar un sexto dado (no debería ser posible)
        cacho.agregar_dado()
        assert len(cacho.get_lista_dados()) == 5  # Se mantiene en 5