"""
3. Insertar elementos en posiciones específicas
    Crea una lista llamada lenguajes que contenga ["Python", "C", "Java"].
    Pide al usuario un nuevo lenguaje de programación.
     insert() para colocar el nuevo lenguaje en la posición 1 de la lista.
    Muestra el resultado final.
"""

import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()

lenguajes = ['python','C','Java']

lenguajes.insert(0,vd.validateAlpha('inserte un nuevo lenguaje de programacion ->'))
print(lenguajes)