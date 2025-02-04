'''2. Extendiendo una lista
        Crea una lista llamada numeros con algunos valores iniciales, por ejemplo: [1, 2, 3].
        Pide al usuario que ingrese tres números adicionales separados por espacio y conviértelos a enteros.
        Usa extend() para agregar estos nuevos números a la lista numeros.
        Imprime la lista final.
'''
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()
numeros =[6,7,8]
a = vd.validateAlnum (f'ingrese 3 numeros separados por espacios -> ').split()
for i in range(len(a)):
    a[i] = int(a[i])

numeros.extend(a)

print(numeros)

cs.pauseScreen()

