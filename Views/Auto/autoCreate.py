import tkinter

from tkinter import *
from Models.Auto import Auto

class autoCreate:

    def __init__(self):

        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Peajes Dora - Alejandro González Flórez - Marlon Aristizabal Herrea")

        # Define el tipo del vehiculo
        self.autoType = Entry(self.windows)

        # Define la placa
        self.licensePlate = Entry(self.windows)

        # Define el recargo de Dia
        self.daySurcharge = Entry(self.windows)

        # Define el recargo de Noche
        self.nightSurcharge = Entry(self.windows)

    #Mostrar interfaz grafica
    def show(self):

        title = Label(self.windows, text="Peajes DORA")
        title.config(bg="#C861D3", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        b = Label(self.windows ,text = "Tipo de Vehiculo",borderwidth=2, relief="groove")
        b.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        b.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.1)

        self.autoType = Entry(self.windows,textvariable=self.autoType)
        self.autoType.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.1)

        c = Label(self.windows ,text = "Placa",borderwidth=2, relief="groove")
        c.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        c.place(relx=0,rely=0.3,relwidth=0.5,relheight=0.1)

        self.licensePlate = Entry(self.windows,textvariable=self.licensePlate)
        self.licensePlate.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.1)

        d = Label(self.windows ,text = "Recargo de Día",borderwidth=2, relief="groove")
        d.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        d.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.1)

        self.daySurcharge = Entry(self.windows,textvariable=self.daySurcharge)
        self.daySurcharge.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.1)

        e = Label(self.windows ,text = "Recargo de Noche",borderwidth=2, relief="groove")
        e.config(bg="#5bc0de", fg="white", font=("Comic Sans", 12))
        e.place(relx=0,rely=0.5,relwidth=0.5,relheight=0.1)

        self.nightSurcharge = Entry(self.windows,textvariable=self.nightSurcharge)
        self.nightSurcharge.place(relx=0.5,rely=0.5,relwidth=0.5,relheight=0.1)

        btnSave = Button(self.windows,text="Guardar",relief="groove",cursor="hand2",command=self.__save)
        btnSave.config(bg="#5cb85c", fg="white", font=("Comic Sans", 18))
        btnSave.place(relx=0.35,rely=0.7, relwidth=0.3, relheight=0.1)

        self.windows.mainloop()

    # Creará una instancia de la clase Toll
    def __save(self):
        
        instaceAuto = Auto()
        instaceAuto.setAutoType(self.autoType.get())
        instaceAuto.setLicensePlate(self.licensePlate.get())
        instaceAuto.setDaySurcharge(self.daySurcharge.get())
        instaceAuto.setNightSurcharge(self.nightSurcharge.get())
        
        if instaceAuto.save():
            self.windows.destroy()
