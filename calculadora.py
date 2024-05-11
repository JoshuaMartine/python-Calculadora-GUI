import tkinter as tk
from tk import *


def agregar_digito(digito):
    actual = pantalla.get()
    if actual == '0':
        pantalla.set(digito)
    else:
        pantalla.set(actual + digito)

def agregar_operacion(operacion):
    actual = pantalla.get()
    if actual[-1] in '+-*/':
        pantalla.set(actual[:-1] + operacion)
    else:
        pantalla.set(actual + operacion)

def calcular_resultado():
    actual = pantalla.get()
    try:
        resultado = str(eval(actual))
        pantalla.set(resultado)
    except Exception as e:
        pantalla.set("Error")

def limpiar_pantalla():
    pantalla.set("0")

root = tk.Tk()
root.title("Calculadora")

pantalla = tk.StringVar()
pantalla.set("0")

display = tk.Entry(root, textvariable=pantalla, font=("Arial", 24), bd=10, insertwidth=4, width=15, justify='right')
display.grid(row=0, column=0, columnspan=4)

botones = [
    ('C', 1, 0, limpiar_pantalla),
    ('%', 1, 1),
    ('/', 1, 2),
    ('*', 1, 3),
    ('7', 2, 0),
    ('8', 2, 1),
    ('9', 2, 2),
    ('-', 2, 3),
    ('4', 3, 0),
    ('5', 3, 1),
    ('6', 3, 2),
    ('+', 3, 3),
    ('1', 4, 0),
    ('2', 4, 1),
    ('3', 4, 2),
    ('=', 4, 3, calcular_resultado),
    ('0', 5, 0, None, tk.E+tk.W, 3),
    ('.', 5, 3)
]


for texto, fila, columna, *extra in botones:
    command = None
    sticky = tk.W + tk.E
    rowspan = 1
    columnspan = 1
    if extra:
        if len(extra) >= 1:
            command = extra[0]
        if len(extra) >= 2:
            sticky = extra[1]
        if len(extra) == 4:
            rowspan = extra[2]
            columnspan = extra[3]
    
    if command:
        action = lambda cmd=command: cmd()
    else:
        action = lambda txt=texto: agregar_digito(txt)
    
    tk.Button(root, text=texto, command=action, font=("Arial", 20), height=2, width=4).grid(row=fila, column=columna, sticky=sticky, rowspan=rowspan, columnspan=columnspan)

root.mainloop()