# Nils Muralles
# Luis Padilla
# Victor Pérez
# Alejandro Rivera
# Módulo que contiene las formas y elementos para dibujar con tkinter

from tkinter import *


# Dibuja un rectángulo con un color dado
def rectangulo(t, base, altura, col):
    t.color(col, col)
    t.begin_fill()
    for i in range(2):
        t.fd(base)
        t.lt(90)
        t.fd(altura)
        t.lt(90)
    t.end_fill()


# Dibuja un rectángulo con esquinas redondas
def rectangulo_red(t, base, altura, col):
    t.color('black', col)
    t.begin_fill()
    for i in range(4):
        t.fd(base - 50)
        t.circle(50, 90)
        t.fd(altura - 50)
        t.circle(50, 90)
    t.end_fill()


# Crea un botón y lo configura para mostrar en pantalla
def boton(raiz, mensaje, comando, columna, fila):
    b = Button(raiz, text=mensaje, command=comando)
    b.config(bg='white', font='Arial 11', height=2, width=15)
    b.grid(column=columna, row=fila)

    return b 