'''9. Ordenar una lista con sort()
    Crea una lista de números desordenados: por ejemplo [3, 8, 1, 7, 2].
    Aplica sort() para ordenarla de forma ascendente.
    Imprime la lista resultante.
    Pide al usuario que indique si desea el orden
    ascendente o descendente
    Si indica descendente, vuelve a aplicar sort(reverse=True).
    Imprime el resultado final.
'''

import modules.controlScreen as cs
import modules.validateData as vd
import random

cs.deleteScreen()

listaNumeros = []
x = int(vd.validateAlnum(f'Ingrese la cantidad de numeros que desea en la lista -> '))
for i in range(x):
    listaNumeros.append(random.randint(0, x))

while True:
    menu = int(vd.validateAlnum('desea ordenar la lista de numeros \n [1]Desendente \n [2]Asendente \n [3]Salir \n -> '))
    match menu:
        case 1:
            print(listaNumeros)
            listaNumeros.sort()
            print(f'{listaNumeros}')
            cs.pauseScreen(),cs.deleteScreen()  
        case 2:
            print(listaNumeros)
            listaNumeros.reverse()
            print(f'{listaNumeros}')
            cs.pauseScreen(),cs.deleteScreen()  
        case 3:
            cs.pauseScreen()  
            break   
        case _:
            print('opcion no valida *!*')
        
            

