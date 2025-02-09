"""
25. Ejercicio integral de listas y cadenas
    Crea una lista vacía palabras.
    Pide al usuario que ingrese 5 palabras.
    Para cada palabra, convierte a mayúsculas (upper()) y agrega a la lista usando append().
    Imprime la lista.
    Ordena la lista alfabéticamente con sort() y vuelve a imprimirla.
    Pide al usuario que ingrese una palabra. Si existe en la lista, elimina la primera ocurrencia con remove().

"""
import modules.controlScreen as cc
import modules.validateData as vd

palabras = []

print('\n ingrese 5 palabaras \n')
cc.pauseScreen()
for i in range(1 ,6): 
    cc.deleteScreen()
    ingrese = vd.validateAlpha(f'ingrese {i} palabra /->> ' )
    palabras.append(ingrese.upper())
print (palabras) 
palabras.sort()   
print(palabras)

eliminar_palabras = vd.validateAlpha(f'ingrese la palabra que desea eliminar /->> ').upper()
if eliminar_palabras in palabras:
    palabras.remove(eliminar_palabras)
    print('palabra removida')
    
else:
    print('palabra no esta en la lista')

print(palabras)    
cc.pauseScreen()    