"""
22. Creación de funciones con parámetros y retorno
    Crea una función llamada sumar(a, b) que retorne la suma de dos números.
    En la función principal, pide al usuario dos números, llama a sumar(a, b) y muestra el resultado.
    Pide al usuario si desea realizar otra operación (sí/no). Si la respuesta es "sí", repite el ciclo.
"""

import modules.validateData as vd
import modules.controlScreen as cc
def suma(a,b):
    return a + b
 
 
def principal(): 
    cc.deleteScreen()
    print('vamos a realizar la suma de dos numeros')
    num_1 = int(vd.validateInt('ingrese el primer numero que sea entero ->>'))
    num_2 = int(vd.validateInt('ingrese el segundo numero que sea entero ->>'))
    resultado = suma(num_1,num_2)
    print (f'el resultado de la suma es ->> {resultado}')
    option = vd.validateAlpha('desea realizar otra operacion (si/no) /->> ').lower()
    if option in ['si', 'no']:
        if option == 'si':
            return principal()
        elif option != 'si':
            exit
    else:
        print('option invalid')
        return        

if __name__ == "__main__":
    principal()


