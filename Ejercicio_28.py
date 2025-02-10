"""
28. Combinar dos listas con extend() de forma controlada
    Crea dos listas de cualquier tipo.
    Pide confirmación al usuario (sí/no) para unirlas.
    Si el usuario confirma, usa extend() para unir la segunda lista a la primera.
    Imprime la lista resultante. Si no confirma, no hagas nada.
"""

import modules.validateData as vd
import modules.controlScreen as cc

numeros = [1, 2, 3, 4, 5]
ciudades = ["Bogotá", "Madrid", "Tokio", "Nueva York", "París"]


while True:
    cc.deleteScreen()
    option = vd.validateAlpha('desea combinar las dos listas (S/N) /->>').upper().strip()
    if option in ['S','N']:
        if option == 'S':
            ciudades.extend(numeros)
            print(ciudades)
            cc.pauseScreen()
        else:
            cc.pauseScreen()
            break    