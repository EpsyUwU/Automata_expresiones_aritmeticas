from estado import Estado

class AFD:
    def __init__(self):
        # Crear los estados
        q0 = Estado()
        q1 = Estado()
        q2 = Estado()
        q3 = Estado(es_final=True)

        # Definir las transiciones
        for digito in '0123456789':
            q0.agregar_transicion(digito, q1)
            q1.agregar_transicion(digito, q1)
            q2.agregar_transicion(digito, q3)
            q3.agregar_transicion(digito, q3)
        for operador in '+-*/':
            q1.agregar_transicion(operador, q2)
            q3.agregar_transicion(operador, q2)

        # Definir el estado inicial
        self.estado_inicial = q0

    def es_expresion_aritmetica(self, cadena):
        estado_actual = self.estado_inicial
        for caracter in cadena:
            if caracter not in estado_actual.transiciones:
                return False
            estado_actual = estado_actual.transiciones[caracter]
        return estado_actual.es_final