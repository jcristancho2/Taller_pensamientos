"""
4. Eliminando elementos de una lista
    Crea una lista llamada animales con valores a tu elección (ej. ["perro", "gato", "elefante", "tigre"]).

    Pide al usuario un nombre de animal para eliminar de la lista.

    Antes de eliminar, utiliza una estructura if para verificar si el animal está en la lista.

    Si está, usa remove() para quitarlo.
    Si no está, muestra un mensaje indicando que no se encontró.
    Imprime la lista final.

    Puntos a reforzar:

    Uso de remove() y validación previa con if ... in ....

"""



import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()

animales = ['perro' , 'gato' , 'elefante' , 'tigre']
removerAnimal = vd.validateAlpha(f' {animales} \n escribir el nombre de el animal que deseas eliminar -> ').lower()

if removerAnimal in animales:
    animales.remove(removerAnimal)
    print(animales)
else:
    print('no se encuentra en la lista')
    
cs.pauseScreen()
