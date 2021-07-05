import tkinter

from Views.Menu import Menu
from Models.Tree import Tree

class index:

    def __init__(self):
        
        self.Tree = Tree()
        self.windows = tkinter.Tk()
        self.windows.geometry("500x300")

        self.config()

    # Validará sí ya existe un archivo de carga de archivos
    # En caso de que exista hará una pregunta de validación
    # Caso contrarío abrirá la interfaz inicial
    def config(self):
        if(True):
            self.toBeContinue()

    # Interfaz gráfica al iniciar
    def toBeContinue(self):

        label1 = tkinter.Label(self.windows, text="Peajes DORA")
        label1.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
        label1.place(x=0,y=0,relwidth=1,relheight=0.2)

        label2 = tkinter.Label(self.windows, text="¿Desea Continuar?")
        label2.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
        label2.place(x=0,y=60,relwidth=1,relheight=0.2)

        btn = tkinter.Button(self.windows, text="Si", command=self.isSuccess)
        btn.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btn.place(x=40,y=180, relwidth=0.3, relheight=0.15)

        btn = tkinter.Button(self.windows, text="No", command=self.cancelledSystem)
        btn.config(bg="#d9534f", fg="white", font=("Comic Sans", 18))
        btn.place(x=300,y=180, relwidth=0.3, relheight=0.15)

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
