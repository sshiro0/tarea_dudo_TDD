class ValidadorApuesta:
    def validar_apuesta(self, apuesta_actual, apuesta_nueva, cantidad_dados_jugador, especial = False):
        cantidad_nueva, pinta_nueva = apuesta_nueva

        # Primera apuesta
        if apuesta_actual is None:
            return True

        cantidad_actual, pinta_actual = apuesta_actual

        # Ya no se puede calzar desde el validador
        if apuesta_nueva == apuesta_actual:
            return False

        # Cambio de pinta: de AS a OTRA PINTA
        if pinta_actual == 1 and pinta_nueva != 1:
            cantidad_minima = (cantidad_actual * 2) + 1
            return cantidad_nueva >= cantidad_minima

        # Cambio de pinta: de OTRA PINTA a AS
        if pinta_nueva == 1 and pinta_actual != 1:

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