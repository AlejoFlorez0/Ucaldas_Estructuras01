import os
import json

from Models.Toll import Toll
from Models.Nodo import Nodo

class Tree:

    # Constructor ([listaNodosIniciales], [raiz])
    def __init__(self):
        self.Autos = []
        self.raiz = None
        self.peso = 0
        self.altura = 0
        self.loadTree()

    #Cargará los peajes existentes
    def loadTree(self):
        if os.path.exists("File/Toll"):
            contentPath = os.listdir("File/Toll")
            for file in contentPath:
                instanceToll = Toll()
                instanceToll.loadFromFile(file)
                self.AgregarPeaje(instanceToll.getName(),instanceToll.getId(),instanceToll.getValueBase(),instanceToll.getIncreLeft(),instanceToll.getIncreRight(),instanceToll.getCategory())

        #self.imprimir_pre_order(self.raiz)

        return True

    #Define un nodo como raiz
    def PonerRaiz(self, raiz):
        self.raiz = raiz

    #Obtiene el peso del arbol
    def ObtenerPeso(self):
        return self.peso

    #Validará la existencia de un nodo raiz
    # En caso de que exista ya un valor raiz, agregará un nodo
    def AgregarPeaje(self, nombre, id, valueBase,increLeft,increRight,category):
        if self.raiz:
            # agregar nodo nuevo al árbol
            self._AgregarPeaje(nombre, id, valueBase,increLeft,increRight,category, self.raiz)
        else:
            # agregar el nuevo nodo como raíz
            self.raiz = Nodo(nombre,id, valueBase, 1,increLeft,increRight,category)
            self.peso += 1

            print("Se ha agregado como raiz de el peaje de ", nombre, ",valor",valueBase)

        return True

    # Validará un nuevo nodo
    # Validará el nodo actual y agregará un peaje dentro de los hijos sí es necesario
    def _AgregarPeaje(self, nombre, id, valueBase,increLeft,increRight,category, nodo):

        nodo.valor = int(nodo.valor)
        valueBase = int(valueBase)
        
        # verificar sí es menor o mayor para ir por la izq o derecha respectivamente
        if nodo.valor > valueBase:
            # verifica si tiene hijo izq
            if (nodo.ObtenerHijoIzquierdo()):
                #print("El hijo izquierdo es ",nodo.ObtenerHijoIzquierdo().valor)
                # se llama recursivamente al hijo implicado
                self._AgregarPeaje(nombre, id, valueBase,increLeft,increRight,category, nodo.ObtenerHijoIzquierdo())
            else:
                
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(nombre,id, valueBase, 1,increLeft,increRight,category, nodo)
                nodo.PonerHijoIzquierdo(nuevoNodo)
                self.peso += 1
                if (self.altura < nuevoNodo.ObtenerNivel()):
                    self.altura = nuevoNodo.ObtenerNivel()
                    
                print("Se ha agregado como Peaje izquierdo de ", nodo.nombre, " al peaje de ", nuevoNodo.nombre, " en el valor",nuevoNodo.getValue(),"padre:",nodo.valor)
        else:
            
            if (nodo.ObtenerHijoDerecho()):  # verifica si tiene hijo derecho
                # se llama recursivamente al hijo implicado
                self._AgregarPeaje(nombre, id, valueBase,increLeft,increRight,category, nodo.ObtenerHijoDerecho())
            else:
                    
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(nombre,id, valueBase, 1,increLeft,increRight,category, nodo)
                nodo.PonerHijoDerecho(nuevoNodo)
                self.peso += 1
                if (self.altura < nuevoNodo.ObtenerNivel()):
                    self.altura = nuevoNodo.ObtenerNivel()
                print("Se ha agregado como Peaje derecho de ", nodo.nombre, " al peaje de ", nuevoNodo.nombre, " en el valor",nuevoNodo.getValue(),"padre:",nodo.valor)

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo, isSon = "Raiz",isFather=0):
        if (nodo):
            print(isSon)
            print(isFather)
            print(f"- Peaje: {nodo.nombre} , - nombre: {nodo.nombre} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}, -Recargo por Derecha {nodo.ObtenerRecargoDe()}, -Categoria {nodo.categoria}.")
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo(),"Izquierdo",nodo.valor)
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho(),"Derecho",nodo.valor)