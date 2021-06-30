import tkinter

from Toll import Toll

from tkinter import *

class tollIndex:

    def __init__(self):

        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")

        # Define el valor de identificación
        self.idValue = tkinter.StringVar()

        # Define el valor de identificación
        self.nameValue = tkinter.StringVar()

        # Define el valor de identificación
        self.valueBaseValue = tkinter.StringVar()

        # Define el valor de identificación
        self.leftIncreValue = tkinter.StringVar()

        # Define el valor de identificación
        self.rightIncreValue = tkinter.StringVar()

        pass

    def show(self):

        title = Label(self.windows, text="Peajes DORA")
        title.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        a = Label(self.windows ,text = "Identificador",borderwidth=2, relief="groove")
        a.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        a.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)

        a1 = Entry(self.windows,textvariable=self.idValue)
        a1.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)

        b = Label(self.windows ,text = "Nombre",borderwidth=2, relief="groove")
        b.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        b.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.1)

        b1 = Entry(self.windows,textvariable=self.nameValue)
        b1.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1)

        c = Label(self.windows ,text = "Valor Base",borderwidth=2, relief="groove")
        c.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        c.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.1)

        c1 = Entry(self.windows,textvariable=self.valueBaseValue)
        c1.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.1)

        d = Label(self.windows ,text = "Valor Incremental de la Izquierda",borderwidth=2, relief="groove")
        d.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        d.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.1)

        d1 = Entry(self.windows,textvariable=self.leftIncreValue)
        d1.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.1)

        e = Label(self.windows ,text = "Valor Incremental de la Derecha",borderwidth=2, relief="groove")
        e.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        e.place(relx=0,rely=0.6,relwidth=0.5,relheight=0.1)

        e1 = Entry(self.windows,textvariable=self.rightIncreValue)
        e1.place(relx=0.5,rely=0.6,relwidth=0.5,relheight=0.1)

        btnSave = Button(self.windows,text="Guardar",relief="groove",cursor="hand2",command=self.__save)
        btnSave.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnSave.place(relx=0.35,rely=0.8, relwidth=0.3, relheight=0.1)

        self.windows.mainloop()

    # Creará una instancia de la clase Toll
    def __save(self):
        
        instaceToll = Toll(self.idValue.get(),self.nameValue.get(),self.valueBaseValue.get(),self.leftIncreValue.get(),self.rightIncreValue.get())
        instaceToll.save()

instace = tollIndex()
instace.show()