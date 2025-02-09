"""
18. Búsqueda dentro de una lista (uso de for, if y funciones de cadena)
    Crea una lista de nombres de personas.

    Pide al usuario un nombre o parte de él.

    Haz una función buscar_personas que reciba la lista y el texto a buscar.

    Dentro de la función, recorre la lista con un for:

    Si el nombre contiene el texto (usando lower() y in), imprímelo.
    Prueba la función.
"""
import modules.validateData as vd , modules.controlScreen as cc

def buscar_personas(list_nombre,buscar):
    buscar = buscar.lower()
    for nombr in list_nombre:
        if buscar in nombr.lower():
            print(nombr)
    

nombres = ['carlos', 'maría', 'jorge', 'ana', 'camila', 'david', 'paula','josé', 'diana', 'alejandro', 'verónica']
cc.deleteScreen()
nombre = vd.validateAlpha('ingrese el nombre o parte del nombre que desea buscar /->> ')    
buscar_personas(nombres, nombre)