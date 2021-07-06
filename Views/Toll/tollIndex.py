import os
import tkinter

from tkinter import *
from Views.Toll.tollCreate import tollCreate

class tollIndex:

    def __init__(self,Tree):

        self.Tree = Tree
        self.tolls=[]
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Peajes Dora - Alejandro González Flórez - Marlon Aristizabal Herrea")
        self.__config()

    # Configuración de la vista principal
    def __config(self):

        if os.path.exists("File/Toll"):
            contentPath = os.listdir("File/Toll")
            for file in contentPath:
                self.tolls.append(file)
    
    # Mostrará la interfaz gráfica
    def show(self):

        btnAdd = Button(self.windows,text="Crear Peaje",relief="groove",cursor="hand2",command=self.add)
        btnAdd.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnAdd.place(relx=0.65,rely=0, relwidth=0.35, relheight=0.1)

        frame = Frame(self.windows)
        frame.config(height=600) 
        frame.pack(fill="x",pady=100)
        
        for file in self.tolls:
            
            lblToll = Label(frame,text=file,relief="groove",cursor="hand2")
            lblToll.config(bg="#5bc0de", fg="white", font=("Comic Sans", 10))
            lblToll.pack(padx=15, pady=15, ipadx=15, ipady=15)  

        self.windows.mainloop()

    # Abrirá un nuevo formulario para agregar un nuevo peaje
    def add(self):
        instanceTollCreate = tollCreate(self.Tree)
        #self.windows.destroy()
        instanceTollCreate.show()
        pass
#a = tollIndex()
#a.show()