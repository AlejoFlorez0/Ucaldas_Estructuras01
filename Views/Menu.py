
import tkinter
from Views.Toll.index import tollIndex

class Menu:

    def __init__(self):
        pass

    # Esta clase 
    def show(self):
        windows = tkinter.Tk()
        windows.geometry("500x300")

        title = tkinter.Label(windows, text="Peajes DORA")
        title.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        btnPeaje = tkinter.Button(windows, text="Peajes",command=self.__Toll)
        btnPeaje.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnPeaje.place(x=40,y=120, relwidth=0.3, relheight=0.3)

        windows.mainloop()

    # Abrirá el Formulario para Los peajes
    def __Toll(self):
        instanceTollIndex = tollIndex()
        instanceTollIndex.show()