import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from enum import Enum

class Denominacion(Enum):
    AS = 1
    TONTO = 2
    TREN = 3
    CUADRA = 4
    QUINA = 5
    SEXTO = 6


