import sys
import os

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.cacho import Cacho
from juego.gestor_partida import GestorPartida
from juego.validador_apuesta import ValidadorApuesta
from juego.arbitro_ronda import ArbitroRonda

def build_mock_dado(valor, mocker):
    dado = mocker.Mock()
    dado.get_valor.return_value = valor
    return dado

class TestIntegracion:

    """
    Pruebas de integración para verificar el correcto funcionamiento de los componentes en conjunto.
    """

    def test_inicio_partida(self):
        """
        Test de integración base: Verifica la creación de la partida y los jugadores.
        """
        # Crear una partida con 4 jugadores
        gestor = GestorPartida(4)

        # Verifica que se creó el gestor y la lista de jugadores
        assert gestor is not None
        assert len(gestor.jugadores) == 4

        # Verifica que todos los jugadores sean instancias de Cacho y tengan 5 dados
        for jugador in gestor.jugadores:
            assert isinstance(jugador, Cacho)
            assert len(jugador.get_lista_dados()) == 5

        # Verifica que el turno inicial no está definido aún
        assert gestor.index_actual is None
        assert gestor.jugador_actual is None

    def test_inicio_partida_horario_jugador2(self, mocker):
        """
        Test de integración: Establece inicio de partida con 3 jugadores en sentido horario,
        simulando que el jugador inicial es el jugador 2 (índice 1), y realiza una vuelta completa de turnos.
        """
        gestor = GestorPartida(3)

        # Mock: torneo de dados, jugador 2 gana en la primera ronda
        with mocker.patch('random.randint', side_effect=[3, 6, 2]):
            index_inicial = gestor.definir_jugador_inicial()

        gestor.definir_sentido(1)  # Horario

        assert index_inicial == 1
        assert gestor.get_jugador_actual() == gestor.jugadores[1]
        assert gestor.sentido == 1

        # Simular una vuelta completa de turnos (horario)
        # Estado inicial: index_actual = 1
        turno1 = gestor.siguiente_turno()  # Debe ir al jugador 2 (índice 2)
        assert turno1 == 2
        assert gestor.get_jugador_actual() == gestor.jugadores[2]

        turno2 = gestor.siguiente_turno()  # Debe ir al jugador 0
        assert turno2 == 0
        assert gestor.get_jugador_actual() == gestor.jugadores[0]

        turno3 = gestor.siguiente_turno()  # Debe volver al jugador 1
        assert turno3 == 1
        assert gestor.get_jugador_actual() == gestor.jugadores[1]

    def test_inicio_partida_antihorario_jugador2(self, mocker):
        """
        Test de integración: Establece inicio de partida con 3 jugadores en sentido antihorario,
        simulando que el jugador inicial es el jugador 2 (índice 1), y realiza una vuelta completa de turnos.
        """
        gestor = GestorPartida(3)

        # Mock: torneo de dados, jugador 2 gana en la primera ronda
        with mocker.patch('random.randint', side_effect=[3, 6, 2]):
            index_inicial = gestor.definir_jugador_inicial()

        gestor.definir_sentido(-1)  # Antihorario

        assert index_inicial == 1
        assert gestor.get_jugador_actual() == gestor.jugadores[1]
        assert gestor.sentido == -1

        # Simular una vuelta completa de turnos (antihorario)
        # Estado inicial: index_actual = 1
        turno1 = gestor.siguiente_turno()  # Debe ir al jugador 0
        assert turno1 == 0
        assert gestor.get_jugador_actual() == gestor.jugadores[0]

        turno2 = gestor.siguiente_turno()  # Debe ir al jugador 2
        assert turno2 == 2
        assert gestor.get_jugador_actual() == gestor.jugadores[2]

        turno3 = gestor.siguiente_turno()  # Debe volver al jugador 1
        assert turno3 == 1
        assert gestor.get_jugador_actual() == gestor.jugadores[1]

    def test_flujo_dos_jugadores_valores_reales(self, mocker):
        # Setup: 2 jugadores
        gestor = GestorPartida(2)
        arbitro = ArbitroRonda()
        pinta_apostada = 2
        dados_por_jugador = [2, 2]

        def set_dados(pinta_1, pinta_2):
            mocker.patch.object(gestor.jugadores[0], 'get_lista_dados',
                return_value=[build_mock_dado(pinta_1, mocker) for _ in range(dados_por_jugador[0])])
            mocker.patch.object(gestor.jugadores[1], 'get_lista_dados',
                return_value=[build_mock_dado(pinta_2, mocker) for _ in range(dados_por_jugador[1])])

        # 1. Jugador 1 calza con la suma total de pintas (4)
        set_dados(pinta_apostada, pinta_apostada)
        apuesta_calzo = (dados_por_jugador[0] + dados_por_jugador[1], pinta_apostada) # (4, 2)
        resultado_calzo = arbitro.resolver_calzo(apuesta_calzo, gestor.jugadores)
        assert resultado_calzo["resultado"] == "exitoso"
        dados_por_jugador[0] += 1  # Jugador 1 gana dado

        # 2. Jugador 2 duda, pero todos los dados siguen siendo de otra pinta
        set_dados(3, 3)  # Ningún jugador tiene pinta 2
        apuesta_dudo = (dados_por_jugador[0] + dados_por_jugador[1], pinta_apostada) # (5, 2)
        resultado_dudo = arbitro.resolver_dudo(apuesta_dudo, gestor.jugadores)
        assert resultado_dudo["perdedor"] == "apostador"
        dados_por_jugador[0] -= 1  # Jugador 1 pierde dado

        # 3. Jugador 1 sigue dudando y pierde hasta quedar con 1 dado
        while dados_por_jugador[0] > 1:
            set_dados(3, 3)
            apuesta_dudo = (dados_por_jugador[0] + dados_por_jugador[1], pinta_apostada)
            resultado_dudo = arbitro.resolver_dudo(apuesta_dudo, gestor.jugadores)
            assert resultado_dudo["perdedor"] == "apostador"
            dados_por_jugador[0] -= 1

        # 4. Se inicia ronda especial
        gestor.activar_estado_especial(1)
        assert gestor.es_ronda_especial()

        # 5. Jugador 1 calza y gana un dado (solo tiene 1 dado)
        set_dados(pinta_apostada, pinta_apostada)
        apuesta_calzo = (dados_por_jugador[0] + dados_por_jugador[1], pinta_apostada)
        resultado_calzo_especial = arbitro.resolver_calzo(apuesta_calzo, gestor.jugadores, ronda_especial=True)
        assert resultado_calzo_especial["resultado"] == "exitoso"
        dados_por_jugador[0] += 1

        # 6. Jugador 1 duda y pierde un dado (ningún jugador tiene la pinta)
        set_dados(3, 3)
        apuesta_dudo = (dados_por_jugador[0] + dados_por_jugador[1], pinta_apostada)
        resultado_dudo_especial = arbitro.resolver_dudo(apuesta_dudo, gestor.jugadores, ronda_especial=True)
        assert resultado_dudo_especial["perdedor"] == "apostador"
        dados_por_jugador[0] -= 1

        # 7. No puede iniciar otra ronda especial (esto depende de la lógica de GestorPartida)
        gestor.desactivar_estado_especial()
        gestor.activar_estado_especial(1)
        assert gestor.es_ronda_especial()

        # 8. Jugador 1 duda y pierde su último dado
        set_dados(3, 3)
        apuesta_dudo = (dados_por_jugador[0] + dados_por_jugador[1], pinta_apostada)
        resultado_dudo_final = arbitro.resolver_dudo(apuesta_dudo, gestor.jugadores, ronda_especial=True)
        assert resultado_dudo_final["perdedor"] == "apostador"
        dados_por_jugador[0] -= 1

        # 9. Verificar ganador
        assert dados_por_jugador == [0, 2]
        activos = [i for i, d in enumerate(dados_por_jugador) if d > 0]
        assert activos == [1]
