'''
8. Contar ocurrencias con count()
    Crea una lista con varios elementos repetidos, por ejemplo ["manzana", "pera", "manzana", "naranja", "manzana"].
    Pide al usuario una fruta para contar cuántas veces aparece en la lista.
    Usa count() y muestra el resultado.
    Si la cuenta es 0, indica que la fruta no está en la lista.
'''

import modules.controlScreen as cs
import modules.validateData as vd



while True:
    cs.deleteScreen()
    lista_varios = ["manzana", "pera", "manzana", "naranja", "manzana"]

    fruta = vd.validateAlpha('Ingrese el nombre de una fruta \n->').lower().strip()

    x = lista_varios.count(fruta)

    if x>0:
        print(f'la cantidad de flutas {fruta} es de {x}')
    else:
        print(f'la fruta {fruta} no se encuentra en la lista') 
        
    cs.pauseScreen()    

