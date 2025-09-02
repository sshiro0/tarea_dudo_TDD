import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.validador_apuesta import ValidadorApuesta

class TestValidadorApuesta:
    """Clase de pruebas para la lógica de validación de apuestas en el juego."""

    def setup_method(self):
        """Configura una instancia de ValidadorApuesta antes de cada test."""
        self.validador = ValidadorApuesta()
        self.cantidad_dados_jugador = 4

    def test_apuesta_valida(self):
        """
        Test para verificar que una apuesta es válida cuando:
        - se aumenta la cantidad manteniendo la misma pinta,
        - se mantiene la cantidad pero se sube la pinta.
        """
        apuesta_actual = (8, 2)
        assert self.validador.validar_apuesta(apuesta_actual, (9, 2), self.cantidad_dados_jugador) is True
        assert self.validador.validar_apuesta(apuesta_actual, (8, 3), self.cantidad_dados_jugador) is True
        assert self.validador.validar_apuesta(apuesta_actual, (8, 4), self.cantidad_dados_jugador) is True

    def test_apuesta_invalida(self):
        """
        Test para verificar que una apuesta es inválida cuando:
        - se reduce la cantidad,
        - se mantiene la cantidad pero se baja la pinta,
        - se intenta apostar a ases con una cantidad insuficiente.
        """
        apuesta = (7, 3)
        assert self.validador.validar_apuesta(apuesta, (6, 3), self.cantidad_dados_jugador) is False
        assert self.validador.validar_apuesta(apuesta, (7, 2), self.cantidad_dados_jugador) is False
        assert self.validador.validar_apuesta(apuesta, (3, 1), self.cantidad_dados_jugador) is False

    def test_apuesta_repetida(self):
        """
        Test para verificar que no se permite repetir exactamente la misma apuesta.
        """
        assert self.validador.validar_apuesta((6, 5), (6, 5), self.cantidad_dados_jugador) is False
        assert self.validador.validar_apuesta((4, 2), (4, 2), self.cantidad_dados_jugador) is False
        assert self.validador.validar_apuesta((7, 3), (7, 3), self.cantidad_dados_jugador) is False

    def test_cambiar_a_as(self):
        """
        Test para verificar la lógica al cambiar la apuesta a ases (pinta = 1):
        - En caso de cantidad par, la mínima es (cantidad_actual // 2) + 1.
        - En caso de cantidad impar, la mínima es (cantidad_actual + 1) // 2.
        - Se rechaza la apuesta si la cantidad de ases no cumple con el mínimo requerido.
        """
        assert self.validador.validar_apuesta((9, 2), (5, 1), self.cantidad_dados_jugador) is True
        assert self.validador.validar_apuesta((10, 2), (4, 1), self.cantidad_dados_jugador) is False
        assert self.validador.validar_apuesta((10, 2), (6, 1), self.cantidad_dados_jugador) is True

        assert self.validador.validar_apuesta((3, 3), (2, 1), self.cantidad_dados_jugador) is True
        assert self.validador.validar_apuesta((5, 4), (3, 1), self.cantidad_dados_jugador) is True
        assert self.validador.validar_apuesta((5, 4), (2, 1), self.cantidad_dados_jugador) is False

    def test_cambiar_de_as(self):
        """
        Test para verificar la lógica al cambiar de ases a otra pinta:
        - La nueva cantidad mínima debe ser (cantidad_actual * 2) + 1.
        - Si no alcanza esa cantidad mínima, la apuesta es inválida.
        """
        assert self.validador.validar_apuesta((4, 1), (9, 3), self.cantidad_dados_jugador) is True
        assert self.validador.validar_apuesta((4, 1), (8, 3), self.cantidad_dados_jugador) is False
        assert self.validador.validar_apuesta((3, 1), (7, 4), self.cantidad_dados_jugador) is True

    def test_ronda_especial_primera_apuesta(self):
        """
        Test para verificar que en una ronda especial la primera apuesta siempre
        es válida, incluso si apuesta directamente a ases (pinta = 1).
        """
        assert self.validador.validar_apuesta(None, (2, 1), 5, True) is True
        assert self.validador.validar_apuesta(None, (3, 1), 5, True) is True

    def test_ronda_especial_cambio_pintas(self):
        """
        Test para verificar las reglas de cambio de pintas en una ronda especial:
        - De ases a otra pinta: se debe cumplir la cantidad mínima requerida.
        - De otra pinta a ases: se debe cumplir la conversión de cantidad mínima.
        - Se rechaza si no se supera la apuesta anterior en cantidad o pinta.
        """
        assert self.validador.validar_apuesta((4, 1), (5, 3), 5, True) is True
        assert self.validador.validar_apuesta((4, 1), (4, 3), 5, True) is False
        assert self.validador.validar_apuesta((6, 3), (7, 1), 5, True) is True
        assert self.validador.validar_apuesta((6, 3), (4, 1), 5, True) is False

    def test_primera_apuesta_ronda_normal_con_ases(self):
        """
        Test para verificar la regla de la primera apuesta en ronda normal:
        - Si se apuesta a ases y el jugador tiene más de un dado, la apuesta es inválida.
        - Si el jugador solo tiene un dado, la apuesta a ases es válida.
        """
        assert self.validador.validar_apuesta(None, (2, 1), 5, False) is False
        assert self.validador.validar_apuesta(None, (1, 1), 1, False) is True