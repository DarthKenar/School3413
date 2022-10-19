from tkinter import Label, ttk
from tkinter import messagebox
from tkinter import Entry
import tkinter as tk
from functools import partial
from gestor_db import buscar_libro_db

def mostrar_tabla(root,libro):
    print(libro)
    libro_lista = [libro]
    bloque_alumnos = buscar_libro_db(libro_lista)
    seccion = 1

    nombres = ["DNI", "NOMBRE", "FOLIO", "LIBRO"]

    for name_col in range(0,4):
        cell = Label(root, width=25)
        cell.grid(padx=15, pady=5, row=1, column=name_col)
        cell.config(text=nombres[name_col])

    for r in range(0, 12):
        for c in range(0, 4):
            cell = Entry(root, width=25)#, state= "readonly"
            cell.grid(padx=15, pady=5, row=r+4, column=c)
            try:
                #print(bloque_alumnos[0][r][c])
                cell.insert(0, f'{bloque_alumnos[seccion][r][c]}')
                cell.config(state= "readonly")
            except:
                cell.insert(0, '')
                cell.config(state= "readonly")


            
            




