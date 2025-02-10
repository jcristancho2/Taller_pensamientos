"""
29. Buscador de índices múltiple
    Crea una lista de palabras con algunas repetidas.
    Pide al usuario una palabra a buscar.
    Usa un ciclo para recorrer la lista y cada vez que se encuentre esa palabra, guarda el índice en otra lista indices_encontrados.
    Al final, imprime la lista indices_encontrados.
    Si está vacía, indica que la palabra no se encontró.
"""

import modules.validateData as vd
import modules.controlScreen as cc

palabras = ["manzana", "banana", "manzana", "uva", "pera", "banana", "manzana", "pera"]
indices_encontrados = []
cc.deleteScreen()
print(f'esta es la lista de palabras \n {palabras}')
buscador = vd.validateAlpha('ingrese la palabra a buscar /->> ').strip().lower()

for i in range(len(palabras)):
    if palabras[i] == buscador:
        indices_encontrados.append(i)
        
if indices_encontrados:
    print(f"La palabra '{buscador}' se encontró en los índices: {indices_encontrados}")
else:
    print(f"La palabra '{buscador}' no se encontró en la lista.")
    cc.pauseScreen()
