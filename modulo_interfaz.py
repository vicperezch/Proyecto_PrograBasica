# Nils Muralles
# Luis Padilla
# Victor Pérez
# Alejandro Rivera
# Módulo que contiene las funciones para mostrar la interfaz al usuario

# Librerías necesarias para que funcionen las vistas del programa
from tkinter import *
from turtle import RawTurtle, TurtleScreen, ScrolledCanvas
import modulo_funciones as f
import modulo_figuras as d

# Lista que contiene los widgets del programa
widgets = []
microcreditos = {}
usuarios = {}
pagos = {}
sesion = False

# Función que obtiene los datos de los usuarios y los coloca en una base de datos
def obtener_usuarios(pantalla, diccionario, usuario, contrasena, confirm):
    global sesion

    usuario = usuario.get()
    contraseña = contrasena.get()
    confirm = confirm.get()

    if contraseña == confirm:
        diccionario[usuario] = contraseña
        sesion = True
        main()
        pantalla()
    else:
        cambiar_coordenadas(-235, -75)
        t.color('red')
        t.write('*Las contraseñas no coinciden', font=('Arial', 14, 'normal'))

    print(diccionario)


# Crea el entorno de trabajo
def iniciar():
    global root, s, t, dim_x, dim_y, lx, ly, uy

    # Dimensiones de la ventana
    dim_x = 1280
    dim_y = 720

        # Coordenadas guía
    lx = -dim_x/2 # Izquierda
    ly = -dim_y/2 # Abajo
    uy = dim_y/2 # Arriba

    root = Tk()
    root.title('Microcréditos')
    canvas = ScrolledCanvas(root, width=dim_x, height=dim_y)
    canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

    s = TurtleScreen(canvas)
    t = RawTurtle(canvas)
    s.setworldcoordinates(-dim_x/2, -dim_y/2, dim_x/2, dim_y/2)
    t.pensize(3)
    t.speed(0)
    t.hideturtle()


# Cambia la posición de la tortuga
def cambiar_coordenadas(x, y):
    t.pu()
    t.setpos(x, y)
    t.pd()


# Dibuja la barra de menú superior
def menu():
    cambiar_coordenadas(lx - 5, uy - dim_y/7)
    d.rectangulo(t, dim_x + 5, dim_y/7 + 5, 'lime green')


# Muestra la pantalla para solicitar un microcrédito
def pantalla_solicitar():
    t.clear()
    t.seth(0)
    f.destruir_widgets(widgets)
    menu()

    cambiar_coordenadas(-325, -250)
    d.rectangulo_red(t, 700, 400, 'white')

    # Línea del encabezado
    cambiar_coordenadas(-375, 150)
    t.fd(750)

    # Encabazado de formulario de registro
    cambiar_coordenadas(0, 165)
    t.write('Solicitar Credito', align='center', font=('Arial', 14, 'normal'))

    # Entrada que solicita el número de tarjeta
    cambiar_coordenadas(-200, 75)
    t.write('Monto a Solicitar:', font=('Arial', 14, 'normal'))
    num = Entry(root, width = 15, font = 'Arial 14', border = 5)
    num.grid(row = 4, column = 4)
    widgets.append(num)

    # Entrada que solicita el microcrédito a cancelar
    cambiar_coordenadas(0, 75)
    t.write('No. de DPI:', font=('Arial', 14, 'normal'))
    micro = Entry(root, width = 15, font = 'Arial 14', border = 5)
    micro.grid(row = 4, column = 5)
    widgets.append(micro)

    # Entrada que solicita la fecha de vencimiento de la tarjeta
    cambiar_coordenadas(-200, -10)
    t.write('Empresa:', font=('Arial', 14, 'normal'))
    fecha = Entry(root, width = 15, font = 'Arial 14', border = 5)
    fecha.grid(row = 5, column = 4)
    widgets.append(fecha)

    # Entrada que solicita el cvv de la tarjeta
    cambiar_coordenadas(0, -10)
    t.write('Plan de negocios:', font=('Arial', 14, 'normal'))
    cvv = Entry(root, width = 15, font = 'Arial 14', border = 5)
    cvv.grid(row = 5, column = 5)
    widgets.append(cvv)

    # Botón de pago
    boton_pago = d.boton(root, 'Solicitar', lambda: f.obtener_datos(pantalla_principal, [num, micro, fecha, cvv], microcreditos), 4, 6)
    widgets.append(boton_pago)

    # Botón de cancelar
    boton_cancelar = d.boton(root, 'Cancelar', pantalla_principal, 5, 6)
    widgets.append(boton_cancelar)
    

# Muestra la pantalla de inicio
def pantalla_principal():
    t.clear()
    t.seth(0)
    f.destruir_widgets(widgets)
    
    menu()
    cambiar_coordenadas(lx - 5, ly - 5)
    d.rectangulo(t, dim_x + 5, dim_y/4, 'dark green')

    # Dibuja el cuadro con la información escrita
    cambiar_coordenadas(lx + 100, ly)
    t.color('black', 'white')
    t.begin_fill()
    t.seth(90)
    t.fd(dim_y/3)
    t.circle(-50, 90)
    t.fd(dim_x - 300)
    t.circle(-50, 90)
    t.fd(dim_y/3)
    t.end_fill()

    cambiar_coordenadas(0, ly + 25)
    t.seth(90)
    t.fd(dim_y/3)

    # Escribe la información
    cambiar_coordenadas(-(dim_x - 200)/4, ly + dim_y/3)
    t.write('¿Qué es un microcrédito?', align='center', font=('Arial', 16, 'normal'))

    cambiar_coordenadas(-(dim_x - 200)/4, ly + dim_y/3 - 50)
    t.write('Es un tipo de préstamo de corta duración y cantidad reducida', align='center', font=('Arial', 12, 'normal'))
    cambiar_coordenadas(-(dim_x - 200)/4, ly + dim_y/3 - 75)
    t.write('dirigido a personas que buscan financiar un proyecto o empresa,', align='center', font=('Arial', 12, 'normal'))
    cambiar_coordenadas(-(dim_x - 200)/4, ly + dim_y/3 - 100)
    t.write('pero no tienen los recursos necesarios.', align='center', font=('Arial', 12, 'normal'))

    cambiar_coordenadas((dim_x - 200)/4, ly + dim_y/3)
    t.write('¿Cuáles son los requisitos?', align='center', font=('Arial', 16, 'normal'))

    cambiar_coordenadas((dim_x - 200)/4 - 200, ly + dim_y/3 - 50)
    t.write('- Ser mayor de edad', align='left', font=('Arial', 12, 'normal'))
    cambiar_coordenadas((dim_x - 200)/4 - 200, ly + dim_y/3 - 75)
    t.write('- Ser propietario de una cuenta bancaria', align='left', font=('Arial', 12, 'normal'))
    cambiar_coordenadas((dim_x - 200)/4 - 200, ly + dim_y/3 - 100)
    t.write('- Buscar utilizar el crédito para un emprendimiento', align='left', font=('Arial', 12, 'normal'))

    cambiar_coordenadas(0, 75)
    t.write('*Imagen*', align='center', font=('Arial', 15, 'italic'))


# Muestra la pantalla de pagos
def pantalla_pagos():
    t.clear()
    t.seth(0)
    f.destruir_widgets(widgets)
    
    menu()
    cambiar_coordenadas(-325, -250)
    d.rectangulo_red(t, 700, 400, 'white')

    # Línea del encabezado
    cambiar_coordenadas(-375, 150)
    t.fd(750)

    # Encabazado de formulario de registro
    cambiar_coordenadas(0, 165)
    t.write('Pagar', align='center', font=('Arial', 14, 'normal'))

    # Entrada que solicita el número de tarjeta
    cambiar_coordenadas(-200, 75)
    t.write('Número de tarjeta:', font=('Arial', 14, 'normal'))
    num = Entry(root, width = 15, font = 'Arial 14', border = 5)
    num.grid(row = 4, column = 4)
    widgets.append(num)

    # Entrada que solicita el microcrédito a cancelar
    cambiar_coordenadas(20, 75)
    t.write('Microcrédito a cancelar:', font=('Arial', 14, 'normal'))
    micro = Entry(root, width = 15, font = 'Arial 14', border = 5)
    micro.grid(row = 4, column = 5)
    widgets.append(micro)

    # Entrada que solicita la fecha de vencimiento de la tarjeta
    cambiar_coordenadas(-200, -20)
    t.write('Fecha de vencimiento\n(MM/AA):', font=('Arial', 14, 'normal'))
    fecha = Entry(root, width = 15, font = 'Arial 14', border = 5)
    fecha.grid(row = 5, column = 4)
    widgets.append(fecha)

    # Entrada que solicita el CCV de la tarjeta
    cambiar_coordenadas(20, -20)
    t.write('CVV:', font=('Arial', 14, 'normal'))
    ccv = Entry(root, width = 15, font = 'Arial 14', border = 5)
    ccv.grid(row = 5, column = 5)
    widgets.append(ccv)

    # Botón de pago
    boton_pago = d.boton(root, 'Pago', lambda: f.pagar(pantalla_principal, [num, micro, fecha, ccv], microcreditos), 4, 6)
    widgets.append(boton_pago)

    # Botón de cancelar
    boton_cancelar = d.boton(root, 'Cancelar', pantalla_principal, 5, 6)
    widgets.append(boton_cancelar)


# Muestra la pantalla de inicio de sesión
def pantalla_login():
    t.clear()
    t.seth(0)
    f.destruir_widgets(widgets)

    # Mostrar el menú
    menu()
    cambiar_coordenadas(-325, -250)
    d.rectangulo_red(t, 700, 400, 'white')

    # Línea del encabezado
    cambiar_coordenadas(-375, 150)
    t.fd(750)

    # Encabazado de formulario de inicio de sesión
    cambiar_coordenadas(0, 165)
    t.write('Inciar Sesión', align='center', font=('Arial', 14, 'normal'))

    # Entrada que solicita el correo del usuario
    cambiar_coordenadas(-275, 75)
    t.write('Correo:', font=('Arial', 14, 'normal'))
    solilcitar_correo = Entry(root, width = 15, font = 'Arial 14', border = 5)
    solilcitar_correo.grid(row = 4, column = 4)
    widgets.append(solilcitar_correo)

    # Entrada que solicita la contraseña del usuario
    cambiar_coordenadas(-275, -10)
    t.write('Contraseña:', font=('Arial', 14, 'normal'))
    solilcitar_password = Entry(root, width = 15, font = 'Arial 14', border = 5)
    solilcitar_password.grid(row = 5, column = 4)
    widgets.append(solilcitar_password)

    # Botón de inicio de sesión
    boton_iniciar = d.boton(root, 'Iniciar', lambda: obtener_usuarios(pantalla_principal, usuarios, solilcitar_correo, solilcitar_password), 4, 6)
    widgets.append(boton_iniciar)

    # Botón de registro
    boton_registrar = d.boton(root, 'Registrar', pantalla_register, 5, 6)
    widgets.append(boton_registrar)


# Muestra la pantalla de registro
def pantalla_register():
    t.clear()
    t.seth(0)
    f.destruir_widgets(widgets)

    # Mostrar el menú
    menu()
    cambiar_coordenadas(-325, -250)
    d.rectangulo_red(t, 700, 400, 'white')

    # Línea del encabezado
    cambiar_coordenadas(-375, 150)
    t.fd(750)

    # Encabazado de formulario de registro
    cambiar_coordenadas(0, 165)
    t.write('Crea tu cuenta', align='center', font=('Arial', 14, 'normal'))

    # Entrada que solicita el correo del usuario
    cambiar_coordenadas(-230, 95)
    t.write('Correo:', font=('Arial', 14, 'normal'))
    solilcitar_correo = Entry(root, width = 15, font = 'Arial 14', border = 5)
    solilcitar_correo.grid(row = 4, column = 4)
    widgets.append(solilcitar_correo)

    # Entrada que solicita la contraseña del usuario
    cambiar_coordenadas(-230, 0)
    t.write('Contraseña:', font=('Arial', 14, 'normal'))
    solilcitar_password = Entry(root, width = 15, font = 'Arial 14', border = 5, show='*')
    solilcitar_password.grid(row = 5, column = 4)
    widgets.append(solilcitar_password)

    # Entrada que solicita confirmar la contraseña del usuario
    cambiar_coordenadas(40, 0)
    t.write('Confirmar ontraseña:', font=('Arial', 14, 'normal'))
    confirmar_password = Entry(root, width = 15, font = 'Arial 14', border = 5, show='*')
    confirmar_password.grid(row = 5, column = 5)
    widgets.append(confirmar_password)

    # Botón de registro
    boton_register = d.boton(root, 'Crear cuenta', lambda: obtener_usuarios(pantalla_principal, usuarios, solilcitar_correo, solilcitar_password, confirmar_password), 4, 6)
    widgets.append(boton_register)

    # Botón para regresar
    boton_cancelar = d.boton(root, 'Cancelar', pantalla_principal, 5, 6)
    widgets.append(boton_cancelar)


#Mostrar pantalla de gestion de microcreditos
def pantalla_gestionar():
    t.clear()
    t.seth(0)
    f.destruir_widgets(widgets)

    # Mostrar el menú
    menu()
    cambiar_coordenadas(-325, -250)
    d.rectangulo_red(t, 700, 400, 'white')

    # Línea del encabezado
    cambiar_coordenadas(-375, 150)
    t.fd(750)

    # Encabazado de formulario de Gestionar microcreditos
    cambiar_coordenadas(0, 165)
    t.write('Gestionar Microcréditos', align='center', font=('Arial', 14, 'normal'))

    i = 75
    for k, v in microcreditos.items():
        cambiar_coordenadas(-275, i)
        t.write(f'El {k} tiene como monto Q{v[0]}', font=('Arial', 14, 'normal'))
        i -= 85

    # Botón de inicio imprimir resumen
    boton_imprimir = d.boton(root, 'Imprimir resumen', lambda: f.resumenes(microcreditos), 4, 6)
    widgets.append(boton_imprimir)


# Función principal
def main():
    global root, sesion

    # Muestra y configura cada botón del menú
    if sesion == False:
        pantalla_register()
    else: 
        pantalla_principal()
        d.boton(root, 'Inicio', pantalla_principal, 3, 0)
        d.boton(root, 'Solicitar\nmicrocrédito', pantalla_solicitar, 4, 0)
        d.boton(root, 'Gestionar\nmicrocréditos', pantalla_gestionar, 5, 0)
        d.boton(root, 'Pagar', pantalla_pagos, 6, 0)