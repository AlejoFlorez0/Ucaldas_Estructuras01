import os
import tkinter

from Views.Menu import Menu
from Models.Tree import Tree

class index:

    def __init__(self):
        
        self.Tree = Tree()
        self.windows = tkinter.Tk()
        self.windows.iconbitmap("image.ico")
        self.windows.geometry("500x300")
        self.windows.title("Peajes Dora - Alejandro González - Marlon Herrera")

        self.config()

    # Validará sí ya existe un archivo de carga de archivos
    # En caso de que exista hará una pregunta de validación
    # Caso contrarío abrirá la interfaz inicial
    def config(self):
        if(os.path.exists("File/Toll")):
            self.toBeContinue()
        else:
            instanceMenu = Menu(self.Tree)
            self.windows.destroy()
            instanceMenu.show()

    # Interfaz gráfica al iniciar
    def toBeContinue(self):

        label1 = tkinter.Label(self.windows, text="Peajes DORA\n ¿Desea Continuar?")
        label1.config(bg="#C861D3", fg="white", font=("Comic Sans", 18))
        label1.place(x=0,y=0,relwidth=1,relheight=0.2)

        btn = tkinter.Button(self.windows, text="Si", command=self.isSuccess)
        btn.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btn.place(relx=0.35,rely=0.3, relwidth=0.3, relheight=0.15)

        btn = tkinter.Button(self.windows, text="No", command=self.cancelledSystem)
        btn.config(bg="#d9534f", fg="white", font=("Comic Sans", 18))
        btn.place(relx=0.35,rely=0.6, relwidth=0.3, relheight=0.15)

        self.windows.mainloop()

    # Función cuando desea continuar con el sistema anterior
    def isSuccess(self):
        instanceMenu = Menu(self.Tree)
        self.windows.destroy()
        instanceMenu.show()

    # Apagar el sistema
    def cancelledSystem(self):
        print("Adios!!")
        self.windows.destroy()

instance = index()
