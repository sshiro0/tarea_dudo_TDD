import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from juego.dado import Dado


class Cacho:
    """
    Clase que representa un cacho (conjunto) de dados en el juego.

    Un cacho contiene 5 dados inicialmente y proporciona métodos para
    manipular y obtener información sobre los dados que contiene.
    """

    def __init__(self):
        """
        Inicializa un nuevo cacho con 5 dados.

        Cada dado es una instancia de la clase Dado, inicializado con
        un valor aleatorio dentro del rango permitido.
        """
        self.dados = []
        for i in range(5):
            self.dados.append(Dado())

    def get_lista_dados(self):
        """
        Retorna la lista de dados que conforman el cacho.
        """
        return self.dados

    def revolver(self):
        """
        Revuelve todos los dados del cacho.

        Cada dado en el cacho es "revuelto", lo que significa que
        se genera un nuevo valor aleatorio para cada uno.
        """
        for dado in self.dados:
            dado.revolver()

    def get_valor_dados(self):
        """
        Obtiene los valores numéricos de todos los dados del cacho.
        """
        valores = []
        for dado in self.dados:
            valor = dado.get_valor()
            valores.append(valor)
        return valores

    def get_denominaciones(self):
        """
        Obtiene las denominaciones (nombres) de todos los dados del cacho.
        """
        denominaciones = []
        for dado in self.dados:
            denominacion = dado.get_denominacion()
            denominaciones.append(denominacion)
        return denominaciones

    def agregar_dado(self):
        """
        Agrega un nuevo dado al cacho.

        El cacho tiene un máximo de 5 dados. Si ya tiene 5 dados,
        este método no tiene efecto
        """
        if len(self.dados) < 5:
            self.dados.append(Dado())

    def eliminar_dado(self):
        """
        Elimina el último dado del cacho.

        Remueve el último dado de la lista de dados. Si el cacho
        queda vacío, no se pueden eliminar más dados.
        """
        self.dados.pop()