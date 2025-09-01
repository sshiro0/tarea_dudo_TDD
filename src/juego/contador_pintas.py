import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class ContadorPintas:
    def contar_pintas_global(self, pinta, cachos, especial = False):
        contador = 0
        for cacho in cachos:
            contador += self.contar_pintas_jugador(pinta, cacho, especial)
        return contador

    def contar_pintas_jugador(self, pinta, cacho, especial):
        contador = 0
        for dado in cacho.get_lista_dados():
            valor = dado.get_valor()
            if valor == pinta:
                contador += 1
            elif valor == 1 and not especial:
                contador += 1
        return contador