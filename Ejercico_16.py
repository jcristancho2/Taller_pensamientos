'''
Crea una lista de tareas vacía.

Al realizar un ciclo while True, se muestra un menú con:

1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Salir
Usa match para cada opción.

Opción 1: pide la descripción de la tarea y agregala con append().
Opción 2: recorre la lista e imprime cada tarea.
Opción 3: pide la descripción de la tarea y si está en la lista, elimínala con remove(). Si no está, indica que no existe.
Opción 4: rompe el ciclo ( break).
Verifica el correcto funcionamiento del menú.
'''
import modules.controlScreen as cc , modules.validateData as vd

menu = """
|||||||||||||||||||||||||||||||||||||||
||          MENU PRINCIPAL           ||
|||||||||||||||||||||||||||||||||||||||

[1] AGREGAR TAREA
[2] MOSTRAR TAREA
[3] ELIMINAR TAREA
[4] SALIR

"""
lista_tareas = []
ERROR = 'Opción inválida'

def agregar_tarea(lista_tareas):
    cc.deleteScreen()
    while True:
        tarea = vd.validateAlnum("Ingrese la tarea que desea agregar /->> ").strip()
        lista_tareas.append(tarea)
        print("Tarea agregada.")
        option = vd.validateAlpha("¿Desea guardar otra tarea? <S|N> /->> ").strip().upper()
        if option in ['S', 'N']:
            if option == 'N':
                break
        else:
            print(f'{ERROR} \n')    
          
    cc.pauseScreen()

def mostrar_tarea(lista_tareas):
    cc.deleteScreen()
    if lista_tareas:
        print("\n<< Lista de Tareas >>")
        for i, tarea in enumerate(lista_tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas registradas.")
    cc.pauseScreen()

def eliminar_tarea(lista_tareas):
    mostrar_tarea(lista_tareas)
    tarea = vd.validateAlnum("Ingrese la tarea que desea eliminar /->> ").strip()
    if tarea in lista_tareas:
        lista_tareas.remove(tarea)
        print("Tarea eliminada.")
    else:
        print("La tarea no existe en la lista.")
    cc.pauseScreen()

def main():
    while True:
        cc.deleteScreen()
        print(menu)
        op1 = vd.validateInt("/->> ")

        match op1:
            case 1:
                agregar_tarea(lista_tareas)
            case 2:
                mostrar_tarea(lista_tareas)
            case 3:
                eliminar_tarea(lista_tareas)
            case 4:
                print("Salir...")
                break
            case _:
                print(ERROR)
                cc.pauseScreen()

# Ejecutar el programa
if __name__ == "__main__":
    main()