import sys
import os

from juego.cacho import Cacho
from juego.gestor_partida import GestorPartida


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class TestGestorPartida:
    """Clase de pruebas para la clase GestorPartida que gestiona partidas del juego."""

    def test_crear_partida(self):
        """
        Test para verificar la creación correcta de una partida con múltiples jugadores.
        """
        # Crear una partida con 7 jugadores
        gestor = GestorPartida(7)

        # Verificar que el gestor se creó correctamente
        assert gestor is not None
        # Verificar que se crearon exactamente 7 jugadores
        assert len(gestor.jugadores) == 7

        # Verificar que cada jugador es una instancia de Cacho y tiene 5 dados
        for jugador in gestor.jugadores:
            assert isinstance(jugador, Cacho)
            assert len(jugador.get_lista_dados()) == 5

    def test_seleccionar_jugador_inicial(self, mocker):
        """
        Test para verificar la selección del jugador inicial usando torneo de dados.
        """
        gestor = GestorPartida(5)  # Crea los jugadores ANTES del mock

        # Simulamos dos rondas de torneo:
        # Primer torneo: [2, 6, 3, 6, 1] (empate en 6 entre 1 y 3)
        # Segundo torneo: [1, 5, 3, 2, 2] (jugador 1 gana con 5)
        torneo_numeros = [2, 6, 3, 6, 1, 1, 5, 3, 2, 2]

        with mocker.patch('random.randint', side_effect=torneo_numeros):
            index_inicial = gestor.definir_jugador_inicial()

        assert gestor.get_jugador_actual() == gestor.jugadores[1]
        assert index_inicial == 1


    def test_siguiente_turno(self):
        """
        Test para verificar el avance de turnos entre jugadores.
        """
        gestor = GestorPartida(3)
        gestor.index_actual = 0

        assert gestor.siguiente_turno() == 1
        assert gestor.siguiente_turno() == 2
        assert gestor.siguiente_turno() == 0
        assert gestor.siguiente_turno() == 1

    def test_obtener_jugador_actual(self):
        """
        Test para verificar la obtención del jugador actual según el índice.
        También valida que se retorne None si no hay un índice asignado.
        """
        gestor = GestorPartida(3)
        gestor.index_actual = 1

        jugador_actual = gestor.get_jugador_actual()
        assert jugador_actual is gestor.jugadores[1]

        gestor.index_actual = None
        assert gestor.get_jugador_actual() is None

    def test_obtener_jugador_por_indice(self):
        """
        Test para verificar que se obtiene correctamente un jugador
        a partir de su índice en la lista de jugadores.
        """
        gestor = GestorPartida(3)

        assert gestor.get_jugador(0) is gestor.jugadores[0]
        assert gestor.get_jugador(2) is gestor.jugadores[2]

    def test_get_jugador_actual_index_valido(self):
        """
        Test para verificar que se retorna correctamente el índice
        del jugador actual cuando está definido.
        """
        gestor = GestorPartida(3)
        gestor.index_actual = 1
        assert gestor.get_jugador_actual_index() == 1

    def test_get_jugador_actual_index_none(self):
        """
        Test para verificar que se retorna None cuando no hay un
        jugador actual definido (index_actual es None).
        """
        gestor = GestorPartida(3)
        gestor.index_actual = None
        assert gestor.get_jugador_actual_index() is None

    def test_obtener_jugadores_activos(self):
        """
        Test para verificar la obtención correcta de jugadores activos (con dados).
        """
        gestor = GestorPartida(3)

        activos = gestor.get_jugadores_activos()
        assert len(activos) == 3
        assert activos == [0, 1, 2]

        gestor.jugadores[1].dados = []
        activos = gestor.get_jugadores_activos()
        assert len(activos) == 2
        assert activos == [0, 2]

    def test_jugador_tiene_dados(self):
        """
        Test para verificar si un jugador tiene dados.
        """
        gestor = GestorPartida(3)

        assert gestor.jugador_tiene_dados(0) is True
        assert gestor.jugador_tiene_dados(1) is True

        gestor.jugadores[1].dados = []
        assert gestor.jugador_tiene_dados(1) is False


    def test_definir_sentido(self):
        """
        Test para verificar que el sentido de la partida se define correctamente.
        """
        gestor = GestorPartida(3)
        assert gestor.sentido == 1
        assert gestor.definir_sentido(-1) == -1
        assert gestor.sentido == -1
        assert gestor.definir_sentido(1) == 1
        assert gestor.sentido == 1
        assert gestor.definir_sentido(0) is None  # Valor inválido, no cambia

    def test_activar_estado_especial(self):
        """
        Test para verificar que se activa correctamente el estado especial.
        """
        gestor = GestorPartida(3)
        assert gestor.estado_especial is None
        gestor.activar_estado_especial(1)
        assert gestor.estado_especial == 1
        gestor.activar_estado_especial(2)
        assert gestor.estado_especial == 2
        gestor.activar_estado_especial(3)  # Valor inválido, no cambia
        assert gestor.estado_especial == 2

    def test_desactivar_estado_especial(self):
        """
        Test para verificar que se desactiva correctamente el estado especial.
        """
        gestor = GestorPartida(3)
        gestor.activar_estado_especial(1)
        assert gestor.estado_especial == 1
        gestor.desactivar_estado_especial()
        assert gestor.estado_especial is None

    def test_es_ronda_especial(self):
        """
        Test para verificar la función que indica si la ronda es especial.
        """
        gestor = GestorPartida(3)
        assert gestor.es_ronda_especial() is False
        gestor.activar_estado_especial(1)
        assert gestor.es_ronda_especial() is True
        gestor.desactivar_estado_especial()
        assert gestor.es_ronda_especial() is False

    def test_get_tipo_ronda_especial(self):
        """
        Test para verificar que se obtiene correctamente el tipo de ronda especial.
        """
        gestor = GestorPartida(3)
        assert gestor.get_tipo_ronda_especial() is None
        gestor.activar_estado_especial(2)
        assert gestor.get_tipo_ronda_especial() == 2
        gestor.desactivar_estado_especial()
        assert gestor.get_tipo_ronda_especial() is None

    def test_otorgar_dado_extra(self):
        """
        Test para verificar que se otorga correctamente el dado extra.
        """
        gestor = GestorPartida(2)
        idx = 0
        # El jugador tiene menos de 5 dados, debe agregar uno
        gestor.jugadores[idx].dados.pop()  # Deja con 4 dados
        gestor.otorgar_dado_extra(idx)
        assert len(gestor.jugadores[idx].dados) == 5
        assert gestor.buffer_dados_extra[idx] == 0

        # El jugador ya tiene 5 dados, debe aumentar el buffer
        gestor.otorgar_dado_extra(idx)
        assert len(gestor.jugadores[idx].dados) == 5
        assert gestor.buffer_dados_extra[idx] == 1

    def test_intentar_recuperar_dado_extra(self):
        """
        Test para verificar que el jugador recupera dados del buffer cuando pierde uno.
        """
        gestor = GestorPartida(2)
        idx = 0

        # Simula buffer extra
        gestor.buffer_dados_extra[idx] = 2
        # Quita un dado al jugador
        gestor.jugadores[idx].dados.pop()
        assert len(gestor.jugadores[idx].dados) == 4
        gestor.intentar_recuperar_dado_extra(idx)
        assert len(gestor.jugadores[idx].dados) == 5
        assert gestor.buffer_dados_extra[idx] == 1

        # Quita otro dado y recupera el segundo
        gestor.jugadores[idx].dados.pop()
        gestor.intentar_recuperar_dado_extra(idx)
        assert len(gestor.jugadores[idx].dados) == 5
        assert gestor.buffer_dados_extra[idx] == 0

    def test_get_buffer_dados_extra(self):
        """
        Test para verificar el acceso al buffer de dados extra.
        """
        gestor = GestorPartida(2)
        assert gestor.get_buffer_dados_extra(0) == 0
        gestor.buffer_dados_extra[0] = 3
        assert gestor.get_buffer_dados_extra(0) == 3

    def test_verificar_ronda_especial(self):
        """
        Test para verificar la detección y activación de ronda especial al quedar con un dado.
        """
        gestor = GestorPartida(2)
        idx = 0

        # Quita hasta que tenga 1 dado
        gestor.jugadores[idx].dados = gestor.jugadores[idx].dados[:1]
        assert gestor.verificar_ronda_especial(idx) is True
        # Si lo vuelve a llamar, ya no activa de nuevo
        assert gestor.verificar_ronda_especial(idx) is False