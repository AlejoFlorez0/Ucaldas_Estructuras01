
import tkinter

class treeNode:

    def __init__(self,Node):
        self.Node = Node
        self.windows = tkinter.Tk()
        self.windows.geometry("500x600")
        self.windows.title("Peajes Dora - Alejandro González Flórez - Marlon Aristizabal Herrea")
        self.__config()

    # Configuración de la vista principal
    def __config(self):
        return True

    # Mostrará la interfaz gráfica
    def show(self):

        title = tkinter.Label(self.windows, text="Peajes DORA")
        title.config(bg="#C861D3", fg="white", font=("Comic Sans", 18))
        title.place(x=0,y=0,relwidth=1,relheight=0.2)

        btnPeaje = tkinter.Label(self.windows, text=self.Node.nombre)
        btnPeaje.config(bg="#0275d8", fg="white", font=("Comic Sans", 18))
        btnPeaje.place(relx=0.35,rely=0.25, relwidth=0.3, relheight=0.3)

        if self.Node.ObtenerHijoIzquierdo():

            nodeLeft = self.Node.ObtenerHijoIzquierdo()

            btnleftNode = tkinter.Button(self.windows, text=nodeLeft.nombre,command=lambda: self.__showNode(nodeLeft))
            btnleftNode.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
            btnleftNode.place(relx=0,rely=0.6, relwidth=0.25, relheight=0.3)

        if self.Node.ObtenerHijoDerecho():

            nodeRight = self.Node.ObtenerHijoDerecho()

            btnRightNode = tkinter.Button(self.windows, text=nodeRight.nombre,command=lambda: self.__showNode(nodeRight))
            btnRightNode.config(bg="#5bc0de", fg="white", font=("Comic Sans", 18))
            btnRightNode.place(relx=0.75,rely=0.6, relwidth=0.25, relheight=0.3)

        self.windows.mainloop()

    def __showNode(self,node):
        print(node.nombre)
        instenceNode = treeNode(node)
        instenceNode.show()
        pass
    