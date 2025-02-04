'''
14. Clasificación de números (uso de if y ciclos)
    Pide al usuario ingresar 5 números.

    Guárdalos en una lista.

    Define una función llamada clasificar números que reciba la lista y:

    Imprima cuáles son pares.
    Imprima cuáles son impares.
    Dentro de la función, utiliza un ciclo for y un condicional if para la clasificación.

    Llama a la función y muestra la salida.


'''
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()
numeros = []
cantidad = 5

print(f'ingrese {cantidad} numeros')
for i in range(cantidad):
    x = vd.validateDigit('-> ')
    numeros.append(int(x))
    
def clasificarNumeros(N):
    par = []
    impar = []
    
    for num in N:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    
    print(f'Números pares: {par}')
    print(f'Números impares: {impar}')

# Llamar a la función
clasificarNumeros(numeros)
    


 
    