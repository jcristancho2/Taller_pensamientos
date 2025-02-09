"""
24. Ordenamiento de lista de cadenas con sort() y uso de key
    Crea una lista de cadenas con diferentes longitudes, por ejemplo ["Python", "C", "JavaScript", "Go", "Java"].
    Usa sort(key=len) para ordenar la lista según la longitud de las cadenas.
    Imprime el resultado.
    Luego ordena alfabéticamente solo usando sort().
    Imprime el nuevo resultado.
"""

lista =["Python", "C", "JavaScript", "Go", "Java"]

print(f'lisra original \n {lista}\n')

lista.sort(key=len)
print(f'lisra ordenada por longitud \n {lista}\n')

lista.sort()
print(f'lisra original \n {lista}\n')

