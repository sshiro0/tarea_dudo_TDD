import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from enum import Enum


class Denominacion(Enum):
    """
    Enumeración que representa las denominaciones (nombres) de los valores de los dados.

    Proporciona un mapeo entre los valores numéricos de los dados (1-6) y sus
    correspondientes nombres descriptivos utilizados en el juego.
    """

    AS = 1
    """Denominación para el valor 1 del dado."""

    TONTO = 2
    """Denominación para el valor 2 del dado."""

    TREN = 3
    """Denominación para el valor 3 del dado."""

    CUADRA = 4
    """Denominación para el valor 4 del dado."""

    QUINA = 5
    """Denominación para el valor 5 del dado."""

    SEXTO = 6
    """Denominación para el valor 6 del dado."""

