class ValidadorApuesta:
    """
    Clase responsable de validar las apuestas en el juego según las reglas establecidas.

    Implementa la lógica de validación para diferentes escenarios: primera apuesta,
    cambio de pintas, manejo de ases como comodines, y validaciones en modo especial.
    """

    def validar_apuesta(self, apuesta_actual, apuesta_nueva, cantidad_dados_jugador, especial=False):
        """
        Valída si una nueva apuesta es válida según las reglas del juego.
        """
        cantidad_nueva, pinta_nueva = apuesta_nueva

        # Primera apuesta
        if apuesta_actual is None:

            # Ronda especial: Se puede comenzar con ases
            if especial:
                return True

            # Ronda normal: No se puede empezar con ases (solo si se tiene 1 dado)
            if pinta_nueva == 1:
                return cantidad_dados_jugador == 1
            return True

        cantidad_actual, pinta_actual = apuesta_actual

        # Ya no se puede calzar desde el validador
        if apuesta_nueva == apuesta_actual:
            return False

        # Cambio de pinta: de AS a OTRA PINTA
        if pinta_actual == 1 and pinta_nueva != 1:
            if especial:
                # Ronda especial: validación normal, ases no son comodines
                return cantidad_nueva > cantidad_actual
            cantidad_minima = (cantidad_actual * 2) + 1
            return cantidad_nueva >= cantidad_minima

        # Cambio de pinta: de OTRA PINTA a AS
        if pinta_nueva == 1 and pinta_actual != 1:
            if especial:
                # Ronda especial: validación normal, ases no son comodines
                return cantidad_nueva > cantidad_actual

            # Caso par: +1
            if cantidad_actual % 2 == 0:
                cantidad_minima = (cantidad_actual // 2) + 1

            # Caso impar: redondear arriba
            else:
                cantidad_minima = (cantidad_actual + 1) // 2

            return cantidad_nueva >= cantidad_minima

        # Misma pinta: la apuesta debe ser mayor en cantidad o en pinta
        if cantidad_nueva > cantidad_actual:
            return True
        if cantidad_nueva == cantidad_actual and pinta_nueva > pinta_actual:
            return True

        # Cualquier otra situación es inválida
        return False