'''
13. Función para mostrar contactos con filtro
    Partiendo de la agenda del ejercicio anterior, crea una función llamada mostrar_contactos que reciba la lista de contactos y un filtro (una cadena) para el nombre.

    La función recorre la lista de contactos (usando un ciclo for):

    Si el nombre del contacto contiene la cadena del filtro (usa funciones de cadena como in, lower()), imprime los datos del contacto.
    Prueba la función solicitando al usuario un filtro.

'''

''' ejercicio anterior '''
import modules.controlScreen as cs
import modules.validateData as vd

cs.deleteScreen()
contactosAgendados = []


def agregarcontacto(listaContactos):
    while True:
        nombre = vd.validateAlpha('Ingrese Nombre del Contacto: ')
        tel = int(vd.validateAlnum('ingrese numero de telefono ->'))
        
        contacto = {'Nombre': nombre, 'Tel': tel}
        listaContactos.append(contacto)
        
        respuesta = vd.validateAlnum(f'desea agregar otro contacto (S/N)-> ').upper().strip()
        if respuesta != 'N':
            
            return
        else:
            break
    print(f'contacto guardado \n {listaContactos}')
        
agregarcontacto(contactosAgendados)    

'''/////////////////////////////////////////////////////////////////////////'''

def mostrarContactos(listaContactos, filtro):
    filtro = filtro.upper()
    for contacto in listaContactos:
        if filtro in contacto['Nombre'].upper():
            print(f"Nombre: {contacto['Nombre']}, Tel: {contacto['Tel']}")


agregarcontacto(contactosAgendados)
filtro_usuario = input("\nIngrese el nombre a buscar: ")
mostrarContactos(contactosAgendados, filtro_usuario)