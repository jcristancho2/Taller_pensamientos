"""
19. Conversión de cadena a lista y viceversa
    Pide al usuario que ingrese una frase.
    Convierte la frase a lista de palabras usando split().
    Muestra la lista obtenida.
    Une la lista de nuevo en una cadena usando join(), separando por espacio.
    Imprime la cadena resultante.
"""
import modules.validateData as vd, modules.controlScreen as cc

cc.deleteScreen()
frase = vd.validateAlpha('ingrese una frace /->> ').split()
print(f'la frace usando el comando split() /->> {frase}')
frase_unida =' '.join(frase)
print(f'la frase con la funcion join() /->> {frase_unida}') 