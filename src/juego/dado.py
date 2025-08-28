import random

class Dado:
    def __init__(self):
        self.valor = random.randint(1, 6)

    def get_valor(self):
        return self.valor
