import tkinter

from tkinter import *
from Models.Toll import Toll

class tollCreate:

    def __init__(self,Tree):

        self.Tree = Tree
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Peajes Dora - Alejandro González Flórez - Marlon Aristizabal Herrea")

        # Define el valor de identificación
        self.nameValue = Entry(self.windows)

        # Define el valor de identificación
        self.valueBaseValue = Entry(self.windows)

        # Define el valor de identificación
        self.leftIncreValue = Entry(self.windows)

        # Define el valor de identificación
        self.rightIncreValue = Entry(self.windows)

        # Define el valor de la categoria
        self.category = Entry(self.windows)

    #Mostrar interfaz grafica
    def show(self):

        self.Tree.imprimir_pre_order(self.Tree.raiz)

        title = Label(self.windows, text="Peajes DORA")
        title.config(bg="#C861D3", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        b = Label(self.windows ,text = "Nombre",borderwidth=2, relief="groove")
        b.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        b.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)

        self.nameValue = Entry(self.windows,textvariable=self.nameValue)
        self.nameValue.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)

        c = Label(self.windows ,text = "Valor Base",borderwidth=2, relief="groove")
        c.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        c.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.1)

        self.valueBaseValue = Entry(self.windows,textvariable=self.valueBaseValue)
        self.valueBaseValue.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1)

        d = Label(self.windows ,text = "Valor Incremental de la Izquierda",borderwidth=2, relief="groove")
        d.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        d.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.1)

        self.leftIncreValue = Entry(self.windows,textvariable=self.leftIncreValue)
        self.leftIncreValue.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.1)

        e = Label(self.windows ,text = "Valor Incremental de la Derecha",borderwidth=2, relief="groove")
        e.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        e.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.1)

        self.rightIncreValue = Entry(self.windows,textvariable=self.rightIncreValue)
        self.rightIncreValue.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.1)

        f = Label(self.windows ,text = "Categoria",borderwidth=2, relief="groove")
        f.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        f.place(relx=0,rely=0.6,relwidth=0.5,relheight=0.1)

        self.category = Entry(self.windows,textvariable=self.category)
        self.category.place(relx=0.5,rely=0.6,relwidth=0.5,relheight=0.1)

        btnSave = Button(self.windows,text="Guardar",relief="groove",cursor="hand2",command=self.__save)
        btnSave.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnSave.place(relx=0.35,rely=0.8, relwidth=0.3, relheight=0.1)

        self.windows.mainloop()

    # Creará una instancia de la clase Toll
    def __save(self):
        
        instaceToll = Toll(self.Tree)
        instaceToll.setName(self.nameValue.get())
        instaceToll.setvalueBase(self.valueBaseValue.get())
        instaceToll.setIncreLeft(self.leftIncreValue.get())
        instaceToll.setIncreRight(self.rightIncreValue.get())
        instaceToll.setCategory(self.category.get())
        
        if instaceToll.save():
            self.windows.destroy()
