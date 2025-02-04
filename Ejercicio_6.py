'''
6. Limpiando una lista con clear()
    Crea una lista con al menos 5 elementos a tu elección.
    Define una función llamada limpiar_lista que reciba una lista y la vacíe usando clear().
    Antes de llamar a la función, muestra la lista original.
    Llama a la función y luego imprime la lista para confirmar que está vacía.
'''
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()

def limpiar_lista(datos):
    datos.clear()
    print(f'{datos}')
    
datos = ['manzana','perra', 'perro', 'coco', 'casa']
print(datos)


# datos.clear()
# print(datos)


    



