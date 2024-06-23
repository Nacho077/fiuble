from tkinter import *
from csv import *
from constantes import ARCHIVO_USUARIOS

def repeticion_contrasenia_correcta(contrasenia_nueva_repeticion, contrasenia_nueva): # un solo return
    # Funcion para ver si la repeticion de la contraseña es correcta
    # Creador: Bogarin Juan
    valido=False
    if contrasenia_nueva_repeticion == contrasenia_nueva:
        valido=True
    return valido

def contrasenia_valida(contrasenia_nueva):
    # funcion para validar la contraseña
    # Creador: Bogarin Juan
    valido=False
    posicion_caracter= 0
    contador_mayusculas= 0
    contador_minusculas= 0
    contador_digitos= 0
    contador_guiones= 0
    contador_no_valido= 0
    
    if 8 <= len(contrasenia_nueva) <= 12:
        while posicion_caracter < len(contrasenia_nueva) and contador_no_valido == 0:
            if contrasenia_nueva[posicion_caracter].isupper():
                contador_mayusculas+= 1
            elif contrasenia_nueva[posicion_caracter].islower():
                contador_minusculas+= 1
            elif contrasenia_nueva[posicion_caracter].isdigit():
                contador_digitos+= 1
            #cambie el in ((_)or(-)) ya que no me validaba la contra si usaba "-", pero si cuando usaba "_",RARO   # deberia ser in ("_", "-")
            elif contrasenia_nueva[posicion_caracter] == "_" or contrasenia_nueva[posicion_caracter] == "-":
                contador_guiones+= 1
            else:
                contador_no_valido+= 1
            posicion_caracter+= 1
        if contador_mayusculas >= 1 and contador_minusculas >= 1 and contador_digitos >= 1 and contador_guiones >= 1 and contador_no_valido == 0:
            valido=True
    return valido

def usuario_valido(usuario_nuevo):
    # Funciona para validar un usuario
    # Creador: Bogarin Juan
    valido=False
    posicion_caracter= 0
    contador_no_valido= 0
    if 4 <= len(usuario_nuevo) <= 15:
        while posicion_caracter < len(usuario_nuevo) and contador_no_valido == 0:
            if not usuario_nuevo[posicion_caracter].isalnum() and not usuario_nuevo[posicion_caracter] == "_": # se puede guion medio?
                contador_no_valido+= 1
            posicion_caracter+= 1
        if contador_no_valido == 0:
            valido=True
    return valido
 
def boton_registrarse(entry_usuario_registro, entry_contrasenia_registro, entry_validacion_contrasenia_registro, contenedor_registro):
    # Funcion para crear el boton de "REGISTRARSE" y llamar a las validaciones
    # Creador: Guzman Leonel
    usuarios_registrados=open(ARCHIVO_USUARIOS, "r")
    usuario_nuevo=(entry_usuario_registro.get())
    contrasenia_nueva=(entry_contrasenia_registro.get())
    contrasenia_nueva_repeticion=(entry_validacion_contrasenia_registro.get())

    registrado="no"
    for info_usuarios in usuarios_registrados:
        usuario_registrado, contrasenia_registrada=info_usuarios.rstrip("\n").split(",")
        if usuario_nuevo==usuario_registrado:
            registrado="amedias"
            if contrasenia_nueva==contrasenia_registrada:
                registrado="si"
                label_aviso=Label(contenedor_registro, text="este usuario ya ha sido registrado", font=("bold", 13), bg="black", fg="red")
                label_aviso.grid(row=1, column=0, sticky="W")

            else:
                label_aviso=Label(contenedor_registro, text="el usuario ya esta ocupado          ", font=("bold", 13), bg="black", fg="red")
                label_aviso.grid(row=1, column=0, sticky="W")
    usuarios_registrados.close()

    if registrado=="no" and usuario_valido(usuario_nuevo) and contrasenia_valida(contrasenia_nueva) and repeticion_contrasenia_correcta(contrasenia_nueva_repeticion, contrasenia_nueva):
        usuarios_registrados=open(ARCHIVO_USUARIOS, "a")
        usuarios_registrados.write(f"{usuario_nuevo},{contrasenia_nueva}\n")
        usuarios_registrados.close()
        label_aviso=Label(contenedor_registro, text="has sido registrado exitosamente  ", font=("bold", 13), bg="black", fg="green")
        label_aviso.grid(row=1, column=0, sticky="W")
    elif registrado=="no" and usuario_valido(usuario_nuevo) and contrasenia_valida(contrasenia_nueva) and not repeticion_contrasenia_correcta(contrasenia_nueva_repeticion, contrasenia_nueva):
        label_aviso=Label(contenedor_registro, text="repetiste mal la contraseña       ", font=("bold", 13), bg="black", fg="red")
        label_aviso.grid(row=1, column=0, sticky="W")
    elif registrado=="no" and not usuario_valido(usuario_nuevo):
        label_aviso=Label(contenedor_registro, text="el usuario no es valido          ", font=("bold", 13), bg="black", fg="red")
        label_aviso.grid(row=1, column=0, sticky="W")
    elif registrado=="no" and usuario_valido(usuario_nuevo) and not contrasenia_valida(contrasenia_nueva):
        label_aviso=Label(contenedor_registro, text="la contraseña no es valida        ", font=("bold", 13), bg="black", fg="red")
        label_aviso.grid(row=1, column=0, sticky="W")

    #saque el close

def interfaz_registro():
    # Funcion para invocar la interfaz de registro
    # Creador: Guzman Leonel
    base_registro= Tk()

    base_registro.title("Registro")
    base_registro.resizable(0, 0)

    contenedor_registro=Frame(base_registro, bg="black", padx="15", pady="15")
    contenedor_registro.pack()

    label_registro=Label(contenedor_registro, text="Registro", font=("bold", 35), bg="black", fg="white")
    label_registro.grid(row=0, column=0, pady=35)

    #el aviso sirve para poner texto en caso de que no se cumpla las condiciones necesarios para poner un usuario o una contraseña de manera correcta
    #preguntar como mrd ponemos las condiciones de validacion de contraseña y usuario, ya que pide demasiado y se haria largo
    #una idea es que al momento de pasar el mouse por el ENTRY salga un texto mostrando los requisitos
    label_aviso_registro=Label(contenedor_registro, text="", font=("bold", 30), bg="black", fg="white")
    label_aviso_registro.grid(row=1, column=0)

    label_usuario_registro=Label(contenedor_registro, text="Ingrese nombre de usuario", font=("bold", 15), bg="black", fg="white")
    label_usuario_registro.grid(row=2, column=0, padx=10, pady=5, sticky="W")

    entry_usuario_registro=Entry(contenedor_registro, font=("bold", 20))
    entry_usuario_registro.grid(row=3, column=0, padx=10, pady=10)

    label_contrasenia_registro=Label(contenedor_registro, text="Ingrese contraseña", font=("bold", 15), bg="black", fg="white")
    label_contrasenia_registro.grid(row=4, column=0, padx=10, pady=5, sticky="W")

    entry_contrasenia_registro=Entry(contenedor_registro, font=("bold", 20), show="*")
    entry_contrasenia_registro.grid(row=5, column=0, padx=10, pady=10)

    label_validacion_contrasenia_registro=Label(contenedor_registro, text="Ingrese la contraseña nuevamente", font=("bold", 15), bg="black", fg="white")
    label_validacion_contrasenia_registro.grid(row=6, column=0, padx=10, pady=5, sticky="W")

    entry_validacion_contrasenia_registro=Entry(contenedor_registro, font=("bold", 20), show="*")
    entry_validacion_contrasenia_registro.grid(row=7, column=0, padx=10, pady=10)

    button_registrarse_registro=Button(contenedor_registro, text="Registrarse", font=("bold", 18), bg="black", fg="white", bd="5", command=lambda:[boton_registrarse(entry_usuario_registro, entry_contrasenia_registro, entry_validacion_contrasenia_registro, contenedor_registro)])
    button_registrarse_registro.config(cursor="hand2")
    button_registrarse_registro.grid(row=8, column=0, pady=15)

    button_registrarse_atras=Button(contenedor_registro, text="Atras", font=("bold", 14), bg="black", fg="white", bd="5", command=lambda:[base_registro.destroy()])
    button_registrarse_atras.config(cursor="hand2")
    button_registrarse_atras.grid(row=9, column=0, sticky="W")

    base_registro.mainloop()

#los labels con texto y que tienen espacios vacios, son para que tapen el texto anterior
def boton_inicio(contenedor, contrasenia, usuario, base):
    # Funcion para el boton "INICIO" y validar que el usuario exista
    # Creador: Guzman Leonel
    usuarios_registrados=open(ARCHIVO_USUARIOS, "r")
    usuario=(usuario.get())
    contrasenia=(contrasenia.get())

    registrado="no"
    for info_usuario in usuarios_registrados:      
        usuario_registrado, contrasenia_registrada= info_usuario.rstrip("\n").split(",")
        
        if usuario == usuario_registrado:
            registrado="amedias"
            if contrasenia == contrasenia_registrada:
                registrado="si"
                label_aviso=Label(contenedor, text="ese usuario no existe      ", font=("bold", 13), bg="black", fg="black")
                label_aviso.grid(row=1, column=0, sticky="W")

                base.destroy()

            else:
                label_aviso=Label(contenedor, text="la contraseña es incorrecta", font=("bold", 13), bg="black", fg="red")
                label_aviso.grid(row=1, column=0, sticky="W")
        elif registrado== "no":
            label_aviso=Label(contenedor, text="ese usuario no existe          ", font=("bold", 13), bg="black", fg="red")
            label_aviso.grid(row=1, column=0, sticky="W")

    usuarios_registrados.close()


def interfaz_inicio_sesion():
    # Funcion para invocar la interfaz de inicio de sesion
    base= Tk()

    base.title("Acceso")
    base.resizable(0, 0)

    contenedor=Frame(base, bg="black", padx="15", pady="15")
    contenedor.pack()

    label_iniciar_sesion=Label(contenedor, text="Iniciar sesion", font=("bold", 35), bg="black", fg="white")
    label_iniciar_sesion.grid(row=0, column=0, pady=35)
        
    #el label de aviso servira para poner texto en caso de que el usuario no exista o se ingrese mal la contraseña, una de esas 2
    # ej -> "el usuario no existe" -> "la contraseña es incorrecta"
    label_aviso=Label(contenedor, text="", font=("bold", 13), bg="black", fg="red")
    label_aviso.grid(row=1, column=0, sticky="W")

    label_usuario=Label(contenedor, text="Usuario", font=("bold", 15), bg="black", fg="white")
    label_usuario.grid(row=2, column=0, padx=10, pady=5, sticky="W")

    usuario=StringVar()
    entry_usuario=Entry(contenedor, font=("bold", 20), textvariable=usuario)
    entry_usuario.grid(row=3, column=0, padx=10, pady=10)

    label_contrasenia=Label(contenedor, text="Contraseña", font=("bold", 15), bg="black", fg="white")
    label_contrasenia.grid(row=4, column=0, padx=10, pady=5, sticky="W")

    contrasenia=StringVar()
    entry_contrasenia=Entry(contenedor, font=("bold", 20), show="*", textvariable=contrasenia)
    entry_contrasenia.grid(row=5, column=0, padx=10, pady=10)

    button_inicio=Button(contenedor, text="Inicio", font=("bold", 18), bg="black", fg="white", bd="5", command=lambda:[boton_inicio(contenedor, contrasenia, usuario, base)])
    button_inicio.config(cursor="hand2")
    button_inicio.grid(row=6, column=0, pady=10)

    button_registrarse=Button(contenedor, text="Registrarse", font=("bold", 14), bg="black", fg="white", bd="5", command=lambda:[interfaz_registro()])
    button_registrarse.config(cursor="hand2")
    button_registrarse.grid(row=7, column=0, pady=10, sticky="E")

    base.mainloop()

    return usuario.get()


interfaz_registro()