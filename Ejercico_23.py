"""
23. Uso de break y continue en un ciclo
    Crea un ciclo for que itere del 1 al 10.
    Si el número es 5, usa continue para saltar la impresión.
    Si el número es 8, usa break para detener el ciclo.
    Imprime los números que sí se procesan.
"""

for i in range(1, 11):
    if i == 5:
        print('\n')  
        continue
    elif i == 8:
        break
    print (i)