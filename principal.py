from afd import AFD

# Prueba
afd = AFD()
print(afd.es_expresion_aritmetica('+1'))  # Debería imprimir: False
print(afd.es_expresion_aritmetica('11+1'))  # Debería imprimir: True
print(afd.es_expresion_aritmetica('11++1'))  # Debería imprimir: False
print(afd.es_expresion_aritmetica('11+11'))  # Debería imprimir: True
print(afd.es_expresion_aritmetica('11+11+'))  # Debería imprimir: False
print(afd.es_expresion_aritmetica('11+11+11'))  # Debería imprimir: True
print(afd.es_expresion_aritmetica('23*3/5-8+1'))  # Debería imprimir: True