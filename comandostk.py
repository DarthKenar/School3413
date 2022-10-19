from tkinter import messagebox
import tkinter
def cerrar_programa():
    mensaje = messagebox.askyesno(title="Salir", message="¿Seguro desea salir?")
    if mensaje == "Sí":
        print(mensaje.__str__)
        tkinter.Tk.destroy()
    else:
        pass