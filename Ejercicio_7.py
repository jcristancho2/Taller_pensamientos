'''
7. Encontrar el índice de un elemento con index()
    Crea una lista con varios colores, por ejemplo ["rojo", "azul", "verde", "amarillo", "negro"].

    Pide al usuario que ingrese un color.

    Usa un

    try/except
    para manejar posibles errores:

    Dentro del try, usa index() para obtener la posición del color ingresado.
    Muestra la posición en pantalla.
    En el except, muestra un mensaje indicando que el color no está en la lista.
'''

import modules.controlScreen as cs
cs.deleteScreen()

while True:
    cs.deleteScreen()

    colores_varios = ["rojo", "azul", "verde", "amarillo", "negro"]

    new_color = input('Ingrese un nuevo Color -> ').strip().lower()

    try:
        lista = colores_varios.index(new_color)
        print(f'el color {new_color} \nse encuentra en la posicion {lista}')
    except ValueError:
        print(f' el color {new_color} no esta en la lista')
            
    cs.pauseScreen()        