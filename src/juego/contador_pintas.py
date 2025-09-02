import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


class ContadorPintas:
    """
    Clase responsable de contar la cantidad de ocurrencias de una pinta específica
    en los dados de uno o múltiples cachos (conjuntos de dados).

    Proporciona funcionalidad para contar tanto en modo normal (con ases como comodines)
    como en modo especial (ases solo cuentan como pinta 1).
    """

    def contar_pintas_global(self, pinta, cachos, especial=False):
        """
        Cuenta la cantidad total de una pinta específica across múltiples cachos.
        """
        contador = 0
        for cacho in cachos:
            contador += self.contar_pintas_jugador(pinta, cacho, especial)
        return contador

    def contar_pintas_jugador(self, pinta, cacho, especial):
        """
        Cuenta la cantidad de una pinta específica en los dados de un solo cacho.

        En modo normal (especial=False):
        - Los ases (valor 1) cuentan como comodines para cualquier pinta
        - Excepto cuando se cuenta la pinta 1, donde solo cuentan los ases naturales

        En modo especial (especial=True):
        - Los ases solo cuentan para la pinta 1
        - No funcionan como comodines para otras pintas
        """
        contador = 0
        for dado in cacho.get_lista_dados():
            valor = dado.get_valor()
            if valor == pinta:
                contador += 1
            elif valor == 1 and not especial:
                contador += 1
        return contador