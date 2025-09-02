import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from .denominacion import Denominacion
import random


class Dado:
    """
    Clase que representa un dado de juego con valores entre 1 y 6.

    Proporciona funcionalidades para obtener el valor numérico, la denominación
    correspondiente y para revolver el dado para obtener un nuevo valor aleatorio.
    """

    def __init__(self):
        """
        Inicializa un nuevo dado con un valor aleatorio entre 1 y 6.

        El valor se genera aleatoriamente usando random.randint() al momento
        de la creación de la instancia.
        """
        self.valor = random.randint(1, 6)

    def get_valor(self):
        """
        Retorna el valor numérico actual del dado.
        """
        return self.valor

    def get_denominacion(self):
        """
        Retorna la denominación (nombre) correspondiente al valor actual del dado.

        Utiliza la enumeración Denominación para mapear el valor numérico
        a su representación textual correspondiente.
        """
        return Denominacion(self.valor).name

    def revolver(self):
        """
        Revuelve el dado, generando un nuevo valor aleatorio entre 1 y 6.

        Actualiza el valor interno del dado con un nuevo número aleatorio
        dentro del rango permitido.
        """
        self.valor = random.randint(1, 6)
