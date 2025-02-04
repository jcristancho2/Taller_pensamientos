'''
11. Copiar listas con copy()
    Crea una lista llamada lista_original con varios elementos.
    Asigna lista_copia = lista_original.copy().
    Modifica la lista original (por ejemplo, cambia un elemento).
    Imprime ambas listas para comprobar que la copia se mantiene independiente.
'''
import modules.controlScreen as cs

cs.deleteScreen()
listaOriginal = ["Manzana", "Banana", "Cereza", "Durazno", "Uva", "Pera", "Mango"]
listaCopy =listaOriginal.copy()
print(f'lista original -> {listaOriginal}\nlista copy ->{listaCopy} \n')
listaOriginal[4] = 'limones'
print(f'lista original modificada -> {listaOriginal} \n modificacion (listaOriginal[4] = limones) ')
cs.pauseScreen()
