def max(nr1 :int, nr2 :int):
    """Devuelve el mayor de los dos numeros comparados

    Args:
        nr1 (int): Numero a comparable
        nr2 (int): Numero a comparable

    Returns:
        int: Numero mayor
    """    
    if nr1 >= nr2:
        return nr1
    else:
        return nr2
    
# Casos de prueba
print(max(2,5))
print(max(3,-1))
print(max(7,7))    

'''
Detalles: Cuando a un argumento le agregas ': int', lo obligas a que el valor sea en ese tipo de dato.
'''    