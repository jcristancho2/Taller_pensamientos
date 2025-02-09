"""
20. Filtros con condicionales y creación de sublistas
    Genera una lista de números del 1 al 10.

    Crea una función filtrar_lista(numeros, tipo):

    Si tipo es "pares", devuelve una nueva lista con solo los números pares.
    Si tipo es "impares", devuelve solo los impares.
    Usa un ciclo for y un if para filtrar.
    Imprime los resultados para ambos casos.
"""
import modules.controlScreen as cc
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
    
def filtrar_lista(numeros):
    cc.deleteScreen()    
    par = []
    impar = []
    
    for num in numeros:
        if num %2==0:
            par.append(num)
        else:
            impar.append(num)
    
    print(f'Números pares: {par}')
    print(f'Números impares: {impar}')     
               
    
filtrar_lista(lista_numeros)