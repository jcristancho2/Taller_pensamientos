import modules.controlScreen as cc
import modules.validateData as vd

calificaciones = []

while True:
    cc.deleteScreen()
    nota = float(vd.validatefloat(' ingrese la calificacion de (0 - 5) segun corresponda /->> '))
    if 0<= nota <=5 :
        calificaciones.append(nota)
        
    else:
        print('nota ingresada no es valida')
        cc.pauseScreen()
        continue
    
    promedio = sum(calificaciones)/len(calificaciones)
    
    while True:
        option = vd.validateAlpha('desea ingresar mas notas (S/N) /->>').upper().strip() 
        if option in ['S','N']:
            if option == 'S':                           
                break
            else:
                print(f'las notas ingresadas son {calificaciones}')                      
                print (f'el promedio es {promedio:.2f}')
                cc.pauseScreen()
        else:
            print('caracter invalid') 
            break   
    