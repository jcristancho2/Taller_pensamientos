"""
17. Uso de if y match en la misma función
    Crea una función evaluar_estado que reciba una nota (entero) como parámetro.

    Dentro de la función:

    Primero, usa un if para verificar si la nota es válida (0 a 10). Si no lo es, retorna "Nota inválida".

    Si es válida, usa match nota:

    para imprimir:

    10: "Excelente"
    8 o 9: "Muy bien"
    6 o 7: "Bien"
    4 o 5: "Regular"
    _: "Reprobado"
    Prueba la función con notas ingresadas por el usuario.

"""
import modules.validateData as vd , modules.controlScreen as cc

def evaluar_estado():
    cc.deleteScreen()
    nota = int(vd.validateInt('ingrese la nota /->> '))
    if (0<= nota <= 10):
        match nota:
            case n if n == 10:
                print('exelete')
                cc.pauseScreen()
                return evaluar_estado()
            case n if 8<= n <= 9:
                print('muy bien')
                cc.pauseScreen()
                return evaluar_estado()
            case n if 6 <= n <= 7:
                print ('bien')
                cc.pauseScreen()
                return evaluar_estado()
            case n if 4<= n <= 5:
                print('regular')
                cc.pauseScreen()
                return evaluar_estado()
            case n if 0<= n <4:
                print('reprobado')
                cc.pauseScreen()
                return evaluar_estado()
            case _:
                print('option invalid')
                return evaluar_estado()
    else:
        print('solo se reciben datos positivos de 0 a 10')
        cc.pauseScreen()
        return evaluar_estado()
   
if __name__ == "__main__":
    evaluar_estado()