import os
import tkinter

from tkinter import *
from Views.Auto.autoCreate import autoCreate

class autoIndex:

    def __init__(self):
        self.autos=[]
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Peajes Dora - Alejandro González Flórez - Marlon Aristizabal Herrea")
        self.__config()

    # Configuración de la vista principal
    def __config(self):

        if os.path.exists("File/Auto"):
            contentPath = os.listdir("File/Auto")
            for file in contentPath:
                self.autos.append(file)
    
    # Mostrará la interfaz gráfica
    def show(self):

        btnAdd = Button(self.windows,text="Crear Auto",relief="groove",cursor="hand2",command=self.add)
        btnAdd.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnAdd.place(relx=0.65,rely=0, relwidth=0.35, relheight=0.1)

        frame = Frame(self.windows)
        frame.config(height=600) 
        frame.pack(fill="x",pady=100)
        
        iterator = 0
        for file in self.autos:
            
            lblToll = Button(frame,text=file,relief="groove",cursor="hand2")
            lblToll.config(bg="#5bc0de", fg="white", font=("Comic Sans", 10))
            lblToll.pack(padx=15, pady=15, ipadx=15, ipady=15)  

        self.windows.mainloop()

    # Abrirá un nuevo formulario para agregar un nuevo peaje
    def add(self):
        instanceAutoCreate = autoCreate()
        #self.windows.destroy()
        instanceAutoCreate.show()