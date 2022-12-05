def max_de_tres(nr1 :int, nr2:int, nr3 :int):
    """Devuelve el mayor de los tres numeros comparados

    Args:
        nr1 (int): Numero a comparar
        nr2 (int): Numero a comparar
        nr3 (int): Numero a comparar

    Returns:
        int: Numero mayor
    """    
    nr_max = None
    if nr1 >= nr2:
        nr_max = nr1
    else:
        nr_max = nr2
    if nr_max >= nr3:
        return nr_max
    else:
        return nr3
    
# Casos de prueba
print(max_de_tres(2,5,8))
print(max_de_tres(3,-1,1))
print(max_de_tres(7,7,7))
print(max_de_tres(-10,8,0))   