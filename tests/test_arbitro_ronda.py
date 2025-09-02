import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from unittest.mock import MagicMock, patch
from juego.arbitro_ronda import ArbitroRonda


class TestArbitroRonda:

    def test_crear_arbitro_ronda(self):
        """Test que verifica la creación correcta del árbitro."""
        arbitro = ArbitroRonda()
        assert arbitro is not None

    def test_resolver_dudo_apostador_pierde(self):
        """Test cuando el apostador pierde por exagerar."""
        arbitro = ArbitroRonda()

        with patch.object(arbitro.contador, 'contar_pintas_global') as mock_contar:
            mock_contar.return_value = 4

            apuesta_actual = (5, 3)
            jugadores_mock = [MagicMock(), MagicMock()]

            veredicto = arbitro.resolver_dudo(apuesta_actual, jugadores_mock, False)

            assert veredicto["perdedor"] == "apostador"
            assert veredicto["accion"] == "pierde_dado"
            assert veredicto["tipo"] == "dudo"

            mock_contar.assert_called_once_with(3, jugadores_mock, False)

    def test_resolver_dudo_dudador_pierde(self):
        """Test cuando el dudador pierde porque la apuesta era válida."""
        arbitro = ArbitroRonda()

        with patch.object(arbitro.contador, 'contar_pintas_global') as mock_contar:
            mock_contar.return_value = 5

            apuesta_actual = (5, 3)
            jugadores_mock = [MagicMock(), MagicMock()]

            veredicto = arbitro.resolver_dudo(apuesta_actual, jugadores_mock, False)

            assert veredicto["perdedor"] == "dudador"
            assert veredicto["accion"] == "pierde_dado"
            assert veredicto["tipo"] == "dudo"

            mock_contar.assert_called_once_with(3, jugadores_mock, False)

    def test_resolver_calzo_exitoso(self):
        """Test cuando el jugador calza exactamente."""
        arbitro = ArbitroRonda()

        with patch.object(arbitro.contador, 'contar_pintas_global') as mock_contar:
            mock_contar.return_value = 5

            apuesta_actual = (5, 3)
            jugadores_mock = [MagicMock(), MagicMock()]

            veredicto = arbitro.resolver_calzo(apuesta_actual, jugadores_mock, False)

            assert veredicto["resultado"] == "exitoso"
            assert veredicto["accion"] == "gana_dado"
            assert veredicto["tipo"] == "calzo"

    def test_resolver_calzo_fallido(self):
        """Test cuando el jugador no calza."""
        arbitro = ArbitroRonda()

        with patch.object(arbitro.contador, 'contar_pintas_global') as mock_contar:
            mock_contar.return_value = 4

            apuesta_actual = (5, 3)
            jugadores_mock = [MagicMock(), MagicMock()]

            veredicto = arbitro.resolver_calzo(apuesta_actual, jugadores_mock, False)

            assert veredicto["resultado"] == "fallido"
            assert veredicto["accion"] == "pierde_dado"
            assert veredicto["tipo"] == "calzo"

    def test_puede_calzar(self):
        """Test para verificar las condiciones de calzo."""
        arbitro = ArbitroRonda()

        jugador_1_dado = MagicMock()
        jugador_1_dado.get_lista_dados.return_value = [MagicMock()]

        jugador_3_dados = MagicMock()
        jugador_3_dados.get_lista_dados.return_value = [MagicMock()] * 3

        assert arbitro.puede_calzar(jugador_1_dado, 5,20) is True
        assert arbitro.puede_calzar(jugador_3_dados, 5, 13) is True
        assert arbitro.puede_calzar(jugador_3_dados, 5,5) is False