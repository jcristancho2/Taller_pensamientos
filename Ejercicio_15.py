'''
. Menú con match (versión de Python 3.10+)
Crea una variable opcion que el usuario ingresará (valor entero).

Usa una estructura match opcion:

para manejar estos casos:

1: imprimir "Seleccionaste opción 1"
2: imprimir "Seleccionaste opción 2"
_: imprimir "Opción inválida"
Muestra cómo se comporta el programa según la opción elegida.
'''
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()
opcion = int(vd.validateInt("Ingresa una opción \n [1] impresion A\n [2] impresion B \n ->"))


match opcion:
    case 1:
        print("Seleccionaste opción 1")
    case 2:
        print("Seleccionaste opción 2")
    case _:
        print("Opción inválida")