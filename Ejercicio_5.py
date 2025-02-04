'''
5. Extrayendo elementos con pop()
    Crea una lista con números del 1 al 5.

    Crea un

    menú

    usando un ciclo que pregunte al usuario:

    1. Hacer pop sin índice (pop al final)
    2. Hacer pop con índice
    3. Salir
    En el caso 1, haz pop() sin argumentos para extraer el último elemento y muéstralo en pantalla.

    En el caso 2, pide al usuario el índice y haz pop(indice). Muestra el elemento extraído.

    En cada extracción, imprime la lista resultante.

    Finaliza cuando el usuario elija la opción 3.
'''
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()
numeros = list(range(1, 6))

print(f'uso de la funcion pop \nlista de numeros {numeros}\n')

menu = vd.validateInt(f'[1]Hacer pop sin índice (pop al final) \n[2]Hacer pop con índice \n[3]salir \n ->')

while True:
    match menu:
        case 1:
            print(f'el numero removido -> {numeros.pop()}')       
        case 2:
            print(f'el numero removido indice 3 -> {numeros.pop(3)}')
        case 3:
            break
        case _:
            print('opcion no valida')
        
    

cs.pauseScreen()