'''
12. Creación de una agenda de contactos
    Crea una lista vacía para almacenar contactos.
    Cada contacto será un diccionario con {"nombre": <str>, "tel": <str>}.
    Crea una función de llamada agregar_contactoque recibe la lista y agrega un nuevo contacto a partir de los datos ingresados ​​por el usuario.
    La función debe usar append()para insertar el diccionario.
    Muestra la lista de contactos después de cada inserción.
'''
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
        
        
        print(f'contacto guardado \n {listaContactos}')
        
agregarcontacto(contactosAgendados)    

