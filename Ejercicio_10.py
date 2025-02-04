'''
10. Invertir una lista con reverse()
Crea una lista de cadenas a tu elección.
Imprime la lista original.
Aplica reverse() para invertir su orden.
Vuelve a imprimir la lista.
'''
import modules.controlScreen as cs


cs.deleteScreen()

cadena = ['perro','gato','conejo', 'serpiente', 'planta', 'cerdo', 'edificio' ,'paredes','calle','persona']
print(f'la lista original es : \n{cadena}\n')
print(f'la lista aplicado el .reverse() es : \n{cadena}\n')

cs.pauseScreen()
