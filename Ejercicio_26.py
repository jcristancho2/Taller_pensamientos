"""
26. Función que reciba lista y devuelva estadísticas
    Crea una lista de números con al menos 10 elementos.
    
    Crea una función estadisticas(numeros) que retorne:
    
    El número máximo
    El número mínimo
    El promedio
    Muestra los resultados al llamar la función.
"""
import modules.controlScreen as cc

numeros = [1,3,5,8,20,54,74,2,7,6,25]

def estadisticas(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)
    return maximo, minimo, promedio

maximo, minimo, promedio = estadisticas(numeros)
cc.deleteScreen()
print(f'lista de numeros \n {numeros}')
print(f'Máximo: {maximo}')
print(f'Mínimo: {minimo}')
print(f'Promedio: {promedio:.2f}')
cc.pauseScreen(
    
)