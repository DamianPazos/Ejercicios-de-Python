def vocal(caracter :str):
    """Devuelve si es una vocal o no

    Args:
        caracter (str): caracter a evaluar

    Returns:
        bool: Afirmacion o negacion de la vocal
    """    
    vocal = ('a','e','i','o','u')
    if caracter in vocal:
        return True
    else:
        return False
    
# Casos de prueba
print(vocal('a'))
print(vocal('j'))
print(vocal('o'))