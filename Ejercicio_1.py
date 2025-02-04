"""_
EJERCICIO 1 

1.Creación y manipulación básica de listas
    1.Crea una lista vacía llamada frutas.
    2.Pide al usuario que ingrese 3 frutas y añádelas a la lista usando append().
    3. Muestra la lista resultante.
    4. Crea una función definida por el usuario que reciba una lista y la imprima en pantalla.
    5. Llama a la función pasando la lista frutas.

"""
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()

def Frutas (frutas):
    print(f'{frutas}')
    
frutas = []
cantidad = 3
for i in range(cantidad):
    frutas.append(vd.validateAlpha(f'ingrese tres frutas -> '))
    
Frutas(frutas)

cs.pauseScreen()