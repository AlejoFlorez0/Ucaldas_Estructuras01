import os
import json

from Models.Nodo import Nodo

class Tree:

    # Constructor ([listaNodosIniciales], [raiz])
    def __init__(self):
        self.Autos = []
        self.raiz = None
        self.peso = 0
        self.altura = 0

    def PonerRaiz(self, raiz):
        self.raiz = raiz

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
        return True

    # Validará un nuevo nodo
    # Validará el nodo actual y agregará un peaje dentro de los hijos sí es necesario
    def _AgregarPeaje(self, nombre, id, valueBase,increLeft,increRight,category, nodo):

        # verificar sí es menor o mayor para ir por la izq o derecha respectivamente
        if (valueBase < nodo.valor):
            # verifica si tiene hijo izq
            if (nodo.ObtenerHijoIzquierdo()):
                # se llama recursivamente al hijo implicado
                self._AgregarPeaje(nombre, id, valueBase,increLeft,increRight,category, nodo.ObtenerHijoIzquierdo())
            else:
                
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(nombre,id, valueBase, 1,increLeft,increRight,category, nodo)
                nodo.PonerHijoIzquierdo(nuevoNodo)
                self.peso += 1
                if (self.altura < nuevoNodo.ObtenerNivel()):
                    self.altura = nuevoNodo.ObtenerNivel()
                    
                print("Se ha agregado como Peaje izquierdo de ", nodo.nombre, " al peaje de ", nuevoNodo.nombre, " en el nivel",
                      nuevoNodo.ObtenerNivel(),"Recargo por Izquierda: ",nuevoNodo.ObtenerRecargoIz(),"Recargo por Derecha: ",nuevoNodo.ObtenerRecargoDe(),
                      "Categoria: ",nuevoNodo.categoria)
        else:
            if (valueBase > nodo.valor):
                if (nodo.ObtenerHijoDerecho()):  # verifica si tiene hijo derecho
                    # se llama recursivamente al hijo implicado
                    self._AgregarPeaje(self, nombre, id, valueBase,increLeft,increRight,category, nodo.ObtenerHijoDerecho())
                else:
                    
                    # se crea un nuevo nodo y se asigna como hijo
                    nuevoNodo = Nodo(nombre,id, valueBase, 1,increLeft,increRight,category, nodo)
                    nodo.PonerHijoIzquierdo(nuevoNodo)
                    self.peso += 1
                    if (self.altura < nuevoNodo.ObtenerNivel()):
                        self.altura = nuevoNodo.ObtenerNivel()
                    print("Se ha agregado como Peaje derecho de ", nodo.nombre, " al peaje de:  ", nuevoNodo.nombre, " en el nivel",
                          nuevoNodo.ObtenerNivel(),"Recargo por Izquierda: ",nuevoNodo.ObtenerRecargoIz(),"Recargo por Derecha: ",nuevoNodo.ObtenerRecargoDe(),
                      "Categoria: ",nuevoNodo.categoria)

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo):
        if (nodo):
            print(f"- Peaje: {nodo.nombre} , - Id: {nodo.id} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}, -Recargo por Derecha {nodo.ObtenerRecargoDe()}, -Categoria {nodo.categoria}.")
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho())