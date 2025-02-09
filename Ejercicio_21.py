"""
21.Uso de while para validar entrada
    Pide al usuario que ingrese un número par.
    Si no es par, vuelve a pedirlo (ciclo while).
    Cuando finalmente ingrese un número par, añádelo a una lista e imprime la lista.
    Repite el proceso para 3 números par.
"""
import modules.validateData as vd
import modules.controlScreen as cc

lista = []

while len(lista)<3:
    cc.deleteScreen()
    registro = int(vd.validateInt('ingrese un numero par /->> '))
    if registro %2 == 0:
        lista.append(registro)
    else:
        print('el numero es impar')
        cc.pauseScreen()   

print(lista)     