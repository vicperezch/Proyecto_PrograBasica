# Nils Muralles
# Luis Padilla
# Victor Pérez
# Alejandro Rivera
# Módulo que contiene las funciones para las operaciones de la interfaz


# Función que destruye todos los widget de la pantalla
def destruir_widgets(widgets):
    for widget in widgets:
        widget.destroy()


# Función que obtiene los datos en los inputs de una pantalla
def obtener_datos(pantalla, variables, diccionario):
    entradas = []

    for variable in variables:
        entrada = variable.get()
        entradas.append(entrada)

    if len(diccionario) == 0:
        diccionario['Microcrédito 1'] = entradas
    elif len(diccionario) == 1:
        diccionario['Microcrédito 2'] = entradas 
    else:
        print('Ha alcanzado el límite de microcréditos') 

    pantalla()


def pagar(pantalla, varibales, microcreditos):
    datos = []

    for variable in varibales:
        entrada = variable.get()
        datos.append(entrada)

    if datos[1] in list(microcreditos.keys()):
        print('Pago realizado exitosamente')
        pantalla()
    else:
        print('No se encontró ningún microcrédito bajo ese nombre')


# Función que imprime los resúmenes de los microcréditos
def resumenes(microcreditos):
    for k, v in microcreditos.items():
        microcredito = f'El {k} tiene un valor de {v[0]}'
        print(microcredito)