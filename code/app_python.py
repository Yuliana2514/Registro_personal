import os
list_personal = []
#tabnine:test|explain|document|ask|commentCode
def fnt_limpiar():
    os.system('cls')
    print('Autora: Yuliana Jimenez\n')
    print('Politecnico Jaime Isaza Cadavid\n')
    
def fnt_agregar():
    fnt_limpiar()
    print('\n<<< REGISTRAR PERSONA >>>\n')
    id = input('ID:  ')
    nombre = input('Nombre:  ')
    apellido = input('Apellido:  ')
    contacto = input('Contacto:  ')
    correo = input('Correo:  ')
    r = id + '  '   + nombre + '   ' + apellido +  '   '  + contacto  +  '   '  +  correo
    list_personal.append(r)
    input('\nPersona Registrada con exito <Enter> para continuar\n')
    
    
def fnt_mostrar():
    fnt_limpiar()
    print('<<< LISTA DE PERSONAS >>>\n')
    print('ID  NOMBRE    APELLIDO    CONTACTO    CORREO\n')
    for i in list_personal:  
        print(i)
    input('\n Fin del registro <ENTER> para continuar\n')
    
def fnt_menu(m):
    while m == True:
        fnt_limpiar()
        opcion = input('<<< MENU PRINCIPAL >>>\n\n1. AGREGAR\n2. MOSTRAR\n3. SALIR\n -> ')    
        if opcion == '3':
            m = False
        elif opcion == '1':
            fnt_agregar()
        elif opcion == '2':
            fnt_mostrar()
        else:
            input('\nOpcion NO valida <ENTER> para continuar\n')
        
fnt_menu(True)
     
    