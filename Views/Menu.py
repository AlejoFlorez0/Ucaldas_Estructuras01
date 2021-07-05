import tkinter
from Views.Toll.tollIndex import tollIndex
from Views.Auto.autoIndex import autoIndex

class Menu:

    def __init__(self,Tree):

        self.Tree = Tree
        self.windows = tkinter.Tk()
        self.windows.geometry("500x300")

    # Esta clase 
    def show(self):

        title = tkinter.Label(self.windows, text="Peajes DORA")
        title.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        btnPeaje = tkinter.Button(self.windows, text="Peajes",command=self.__Toll)
        btnPeaje.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnPeaje.place(relx=0.07,rely=0.25, relwidth=0.25, relheight=0.3)

        btnAuto = tkinter.Button(self.windows, text="Auto",command=self.__Auto)
        btnAuto.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnAuto.place(relx=0.39,rely=0.25, relwidth=0.25, relheight=0.3)

        btnTree = tkinter.Button(self.windows, text="Arbol",command=self.__Toll)
        btnTree.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnTree.place(relx=0.7,rely=0.25, relwidth=0.25, relheight=0.3)

        self.windows.mainloop()

    # Abrirá el Formulario para Los peajes
    def __Toll(self):
        instanceTollIndex = tollIndex(self.Tree)
        self.windows.destroy()
        instanceTollIndex.show()

    # Abrirá el Formulario para Los peajes
    def __Auto(self):
        instanceTollIndex = autoIndex()
        self.windows.destroy()
        instanceTollIndex.show()
