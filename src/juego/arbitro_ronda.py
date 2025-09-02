import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .contador_pintas import ContadorPintas

class ArbitroRonda:
    def __init__(self):
        self.contador = ContadorPintas()

    def resolver_dudo(self, apuesta_actual, jugadores, ronda_especial=False):
        cantidad, pinta = apuesta_actual
        total_pintas = self.contador.contar_pintas_global(pinta, jugadores, ronda_especial)

        if total_pintas < cantidad:
            return {
                "perdedor": "apostador",
                "accion": "pierde_dado",
                "tipo": "dudo"
            }
        return {
            "perdedor": "dudador",
            "accion": "pierde_dado",
            "tipo": "dudo"}

    def resolver_calzo(self, apuesta_actual, jugadores, ronda_especial=False):
        cantidad, pinta = apuesta_actual
        total_pintas = self.contador.contar_pintas_global(pinta, jugadores, ronda_especial)

        if total_pintas == cantidad:
            return {
                "resultado": "exitoso",
                "accion": "gana_dado",
                "tipo": "calzo"
            }
        return {
            "resultado": "fallido",
            "accion": "pierde_dado",
            "tipo": "calzo"
        }

    def puede_calzar(self, jugador, cantidad_jugadores, total_dados_en_juego):
        """Determina si un jugador puede calzar."""
        dados_jugador = len(jugador.get_lista_dados())
        return (dados_jugador == 1 or
                cantidad_jugadores * 5 // 2 <= total_dados_en_juego)