class Estado:
    def __init__(self, es_final=False):
        self.es_final = es_final
        self.transiciones = {}

    def agregar_transicion(self, caracter, estado):
        self.transiciones[caracter] = estado
