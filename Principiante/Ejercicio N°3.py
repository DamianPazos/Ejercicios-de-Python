def longitud(cadena):
    """Devuelve la cantidad de elementos de un string, lista o tupla (Si devuelve el valor '-1' no es ningun tipo de dato mencionado anteriormente)

    Args:
        cadena (_type_): Cadena, string o tupla a la cual se le va a calcular los elementos

    Returns:
        int: Cantidad de elementos
    """    
    long = 0
    if type(cadena) == str or type(cadena) == list or type(cadena) == tuple:
        for x in cadena:
            long += 1
    else:
        long = -1
    return long

# Casos de prueba
print(longitud('Argentina'))
print(longitud((1,5,1,5,62,2)))
print(longitud([1,4,6,3,7]))
print(longitud(1.5))