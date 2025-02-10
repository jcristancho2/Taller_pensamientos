"""
30. Función recursiva que sume elementos de una lista
    Crea una lista de números.

    Define una función recursiva suma_lista(lista) que:

    Si la lista está vacía, retorne 0.
    Si no está vacía, retorne el primer elemento más el resultado de suma_lista con el resto de la lista.
    Imprime el resultado de la suma al llamar la función.
"""

numeros = [1, 2, 3, 4, 5]

def suma_lista(lista):

    if lista == []:
        return 0
    else:
        return lista[0]+suma_lista(lista[1:])
    
resultado =suma_lista(numeros)
print(f'la suma de la lista es {resultado} ')    