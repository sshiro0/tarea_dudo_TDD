import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.dado import Dado
from unittest.mock import MagicMock
from juego.denominacion import Denominacion


class TestDado:
    """Clase de pruebas para la clase Dado que representa un dado de juego."""

    def test_crear_dado(self):
        """
        Test para verificar la creación correcta de un dado.
        """
        dado = Dado()
        valor = dado.get_valor()

        # Verificar que el valor está en el rango permitido
        assert 1 <= valor <= 6

        # Verificar que el valor es un entero
        assert isinstance(valor, int)

    def test_denominaciones(self, mocker):
        """
        Test para verificar las denominaciones de los valores del dado.
        """
        # Configurar mock para que devuelva valores secuenciales del 1 al 6
        mock_randint = MagicMock(side_effect=[1, 2, 3, 4, 5, 6])
        mocker.patch('juego.dado.random.randint', mock_randint)

        # Crear 6 dados (cada uno obtendrá un valor diferente del mock)
        dados = []
        for i in range(6):
            dado = Dado()
            dados.append(dado)

        # Denominaciones esperadas en el orden de los valores 1-6
        denominaciones = [
            Denominacion.AS, Denominacion.TONTO, Denominacion.TREN,
            Denominacion.CUADRA, Denominacion.QUINA, Denominacion.SEXTO
        ]

        # Verificar que cada dado tiene el valor y denominación correctos
        for i in range(6):
            # Verificar el valor numérico del dado
            assert dados[i].get_valor() == denominaciones[i].value

            # Verificar la denominación (nombre) del dado
            assert dados[i].get_denominacion() == denominaciones[i].name

        # Verificar que random.randint fue llamado 6 veces (una por cada dado)
        assert mock_randint.call_count == 6

        # Verificar que la última llamada fue con los parámetros correctos
        mock_randint.assert_called_with(1, 6)
