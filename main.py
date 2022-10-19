from tkinter import *
from tkinter import messagebox
import comandostk




root = Tk()
root.iconbitmap("bookstack_libr_3024.ico")
root.attributes("-fullscreen", True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("RCS")


imagen_salir = PhotoImage(file = "images\LogOut_32x32.gif")
salir = Button(root, image=imagen_salir)
salir.place(relheight="0.05", relwidth="0.05", relx=0.9, rely=0.1)
salir.config(command=comandostk.cerrar_programa)

guardar = Button(root, text="guardar")
guardar.place(relheight="0.05", relwidth="0.05", relx=0.3, rely=0.3)





#tabla = Frame(root, relief = "solid", height=200, width=400, bg="burlywood1")
#tabla.place(relheight="0.1", relwidth="0.05", relx=0.9, rely=0.1)

root.mainloop()