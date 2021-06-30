import random
global m,s

# Clase NODO --> es la que maneja los datos de cada peaje
class Nodo:
    # Constructor: (llave, valor, hijoIzquierdo, hijoDerecho, padre)
    def __init__(self, nombre, id, valor, nivel,recargoIzquierdo,recargoDerecho,categoria, padre=None, hijoIzquierdo=None, hijoDerecho=None):
        self.nombre = nombre
        self.id = id
        self.valor = valor
        self.nivel = nivel
        self.categoria = categoria
        self.hijoIzquierdo = hijoIzquierdo
        self.hijoDerecho = hijoDerecho
        self.recargoIzquierdo = recargoIzquierdo
        self.recargoDerecho = recargoDerecho
        self.padre = padre
        self.bandera = True
        self.autosPeajes = []

    # Retornar el nodo del hijo izquierdo [None cuando no tiene hijo]
    def ObtenerHijoIzquierdo(self):
        return self.hijoIzquierdo

    # Asignar el nodo del hijo izquierdo
    def PonerHijoIzquierdo(self, hijo):
        self.hijoIzquierdo = hijo

    # Retornar el nodo del hijo derecho [None cuando no tiene hijo]
    def ObtenerHijoDerecho(self):
        return self.hijoDerecho

    # Asignar el nodo del hijo derecho
    def PonerHijoDerecho(self, hijo):
        self.hijoDerecho = hijo

    def ObtenerCategoria(self):
        return self.categoria

    def ObtenerRecargoIz(self):
        return self.recargoIzquierdo

    def ObtenerRecargoDe(self):
        return self.recargoDerecho

    
    def PonerPadre(self, padre):
        self.padre = padre

    def ObtenerPadre(self):
        return self.padre

    # Validar sí el nodo es raíz
    def EsNodoRaiz(self):
        return not self.padre

    # Validar sí el nodo es hoja
    def EsNodoHoja(self):
        return not (self.hijoIzquierdo or self.hijoDerecho)

    # obtener el nivel del nodo
    def ObtenerNivel(self):
        return self.nivel

    def EsHijoIzquierdo(self):
        if (self.padre):
            return self.valor == self.padre.ObtenerHijoIzquierdo().valor

    def EsHijoDerecho(self):
        if (self.padre):
            return self.valor == self.padre.ObtenerHijoDerecho().valor

# Clase AUTO --> es la que maneja los datos de Auto

class Auto:

    def __init__(self, tipoAuto, placa, recargoDia=None, recargoNoche=None, valorPago=None):
        self.tipoAuto = tipoAuto
        self.placa = placa
        self.recargoDia = recargoDia
        self.recargoNoche = recargoNoche
        self.valorPagos = []
        print("se ha crado un auto, el tipo del auto es: ",self.tipoAuto)

    def ObtenerRecargoDia(self):
        return self.recargoDia

    def ObtenerRecargoNoche(self):
        return self.recargoNoche

    def ObtenerPlaca(self):
        return self.placa

    def ObtenertipoAuto(self):
        return self.tipoAuto

# Clase ARBOL PEAJE --> es la que maneja los procesos del programa

class ArbolPeajes:
    # Constructor ([listaNodosIniciales], [raiz])
    def __init__(self):
        self.Autos = []
        self.raiz = None
        self.peso = 0
        self.altura = 0

    def ObtenerAutos(self):
        return self.Autos

    def ObtenerPeso(self):
        return self.peso

    def agregarAuto(self, nodo, auto):
        if (not nodo):
            print("Árbol vacío")
        else:

            self._agregarAuto(nodo, auto)

    def _agregarAuto(self, nodo, auto):
        if (nodo.EsNodoHoja()):
            nodo.autosPeajes.append(auto)

            print("El ultimo peaje del auto '", auto.tipoAuto, "' fue el peaje: ", nodo.nombre," - ",nodo.id," - ",nodo.valor,"$")
        else:
            nodo.autosPeajes.append(auto)
            if not (nodo.ObtenerHijoDerecho()):
                print("El auto", auto.tipoAuto," paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:", nodo.valor,"$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                m = int(input(f"Dedea continuar a: {nodo.ObtenerHijoIzquierdo().nombre} ?, valor a pagar: {(nodo.ObtenerRecargoIz()+nodo.valor)}$. (1) para continuar (0) Volver a {nodo.nombre}: "))
                if m == 1:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if dn.lower() == "dia":
                        valorPago = (nodo.ObtenerRecargoDe() + nodo.valor + auto.recargoDia)
                        auto.valorPagos.append(valorPago)
                    else:
                        valorPago = (nodo.ObtenerRecargoDe() + nodo.valor + auto.recargoNoche)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                    print("- El proximo peaje es: ", nodo.ObtenerHijoIzquierdo().nombre)
                    self._agregarAuto(nodo.ObtenerHijoIzquierdo(), auto)
                else:
                    print(f"Volviendo a {nodo.nombre}")
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
            if not (nodo.ObtenerHijoIzquierdo()):
                print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:", nodo.valor,"$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                m = int(input(f"Dedea continuar a: {nodo.ObtenerHijoDerecho().nombre} ?, valor a pagar: {(nodo.ObtenerRecargoDe()+nodo.valor)}$. (1) para continuar (0) Volver a {nodo.nombre}: "))
                if m == 1:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if dn.lower()=="dia":
                        valorPago = (nodo.ObtenerRecargoDe()+nodo.valor+auto.recargoDia)
                        auto.valorPagos.append(valorPago)
                    else:
                        valorPago = (nodo.ObtenerRecargoDe() + nodo.valor + auto.recargoNoche)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                    print("- El proximo peaje es: ", nodo.ObtenerHijoDerecho().nombre)
                    self._agregarAuto(nodo.ObtenerHijoDerecho(), auto)
                else:
                    print(f"Volviendo a {nodo.nombre}")
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
            if nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoIzquierdo():
                print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:", nodo.valor,"$ |||| ",f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                n = int(input(f"desea moverse: (1) -Ir a: {nodo.ObtenerHijoDerecho().nombre}, valor a pagar: {(nodo.ObtenerRecargoDe()+nodo.valor)}$, (2) -ir a: {nodo.ObtenerHijoIzquierdo().nombre}, valor a pagar: {(nodo.ObtenerRecargoIz()+nodo.valor)}$, (0) -Volver a {nodo.nombre}: "))
                if n == 0:
                    print("Listo")
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                if n == 1:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if dn.lower() == "dia":
                        print("-Valor a pagar, ")
                        valorPago = (nodo.ObtenerRecargoDe() + nodo.valor + auto.recargoDia)
                        auto.valorPagos.append(valorPago)
                    else:
                        valorPago = (nodo.ObtenerRecargoDe() + nodo.valor + auto.recargoNoche)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                    self._agregarAuto(nodo.ObtenerHijoDerecho(), auto)
                if n == 2:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if dn.lower() == "dia":
                        valorPago = (nodo.ObtenerRecargoIz() + nodo.valor + auto.recargoDia)
                        auto.valorPagos.append(valorPago)
                    else:
                        valorPago = (nodo.ObtenerRecargoIz() + nodo.valor + auto.recargoNoche)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                    self._agregarAuto(nodo.ObtenerHijoIzquierdo(), auto)

    def AgregarPeaje(self, nombre, id, valor):

        if self.raiz:
            # agregar nodo nuevo al árbol
            self._AgregarPeaje(nombre, id, valor, self.raiz)
        else:
            # agregar el nuevo nodo como raíz

            m=random.randint(1,100)
            n=random.randint(1,100)
            s=random.randint(1,5)
            categoria = ""
            if s == 1:
                categoria = "A"
            if s == 2:
                categoria = "B"
            if s == 3:
                categoria = "C"
            if s == 4:
                categoria = "D"
            self.raiz = Nodo(nombre,id, valor, 1,m,n,categoria)
            self.peso += 1
            print("El Peaje de:  ", nombre, " se ha agregado como Primer peaje en el nivel",f"valor: {valor}", self.raiz.ObtenerNivel(),"Recargo por Izquierda: ",self.raiz.ObtenerRecargoIz(),"Recargo por Derecha: ",self.raiz.ObtenerRecargoDe(),"Categoria: ",self.raiz.categoria)

    def _AgregarPeaje(self, nombre,id ,valor, nodo):
        # verificar sí es menor o mayor para ir por la izq o derecha respectivamente
        if (valor < nodo.valor):
            if (nodo.ObtenerHijoIzquierdo()):  # verifica si tiene hijo izq
                # se llama recursivamente al hijo implicado
                self._AgregarPeaje(nombre ,id , valor, nodo.ObtenerHijoIzquierdo())
            else:
                #Se crean los recargos de Izquierda y derecha
                m = random.randint(1, 100)
                n = random.randint(1, 100)
                s = random.randint(1, 5)
                categoria = ""
                if s == 1:
                    categoria = "A"
                if s == 2:
                    categoria = "B"
                if s == 3:
                    categoria = "C"
                if s == 4:
                    categoria = "D"
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(nombre , id, valor, nodo.ObtenerNivel() + 1,m,n,categoria, nodo)
                nodo.PonerHijoIzquierdo(nuevoNodo)
                self.peso += 1
                if (self.altura < nuevoNodo.ObtenerNivel()):
                    self.altura = nuevoNodo.ObtenerNivel()
                print("Se ha agregado como Peaje izquierdo de ", nodo.nombre, " al peaje de ", nuevoNodo.nombre, " en el nivel",
                      nuevoNodo.ObtenerNivel(),"Recargo por Izquierda: ",nuevoNodo.ObtenerRecargoIz(),"Recargo por Derecha: ",nuevoNodo.ObtenerRecargoDe(),
                      "Categoria: ",nuevoNodo.categoria)
        else:
            if (valor > nodo.valor):
                if (nodo.ObtenerHijoDerecho()):  # verifica si tiene hijo derecho
                    # se llama recursivamente al hijo implicado
                    self._AgregarPeaje(nombre, id, valor, nodo.ObtenerHijoDerecho())
                else:
                    # Se crean los recargos de Izquierda y derecha
                    m = random.randint(1, 100)
                    n = random.randint(1, 100)
                    s = random.randint(1, 5)
                    categoria = ""
                    if s == 1:
                        categoria = "A"
                    if s == 2:
                        categoria = "B"
                    if s == 3:
                        categoria = "C"
                    if s == 4:
                        categoria = "D"

                    # se crea un nuevo nodo y se asigna como hijo
                    nuevoNodo = Nodo(nombre, id, valor, nodo.ObtenerNivel() + 1,m,n,categoria, nodo)
                    nodo.PonerHijoDerecho(nuevoNodo)
                    self.peso += 1
                    if (self.altura < nuevoNodo.ObtenerNivel()):
                        self.altura = nuevoNodo.ObtenerNivel()
                    print("Se ha agregado como Peaje derecho de ", nodo.nombre, " al peaje de:  ", nuevoNodo.nombre, " en el nivel",
                          nuevoNodo.ObtenerNivel(),"Recargo por Izquierda: ",nuevoNodo.ObtenerRecargoIz(),"Recargo por Derecha: ",nuevoNodo.ObtenerRecargoDe(),
                      "Categoria: ",nuevoNodo.categoria)

    def pagoPeaje(self, nodo,cont):

        if (nodo):
            print("------------------------------------------------")
            print("Por el peaje ", nodo.nombre, f" pasaron los autos:")
            for x in nodo.autosPeajes:
                if cont < len(x.valorPagos):
                    print(x.tipoAuto,f"y pagó {x.valorPagos[cont]}")
            print("------------------------------------------------")
            self.pagoPeaje(nodo.ObtenerHijoIzquierdo(),cont+1)
            self.pagoPeaje(nodo.ObtenerHijoDerecho(),cont+1)

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo):
        if (nodo):
            print(f"- Peaje: {nodo.nombre} , - Id: {nodo.id} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}, -Recargo por Derecha {nodo.ObtenerRecargoDe()}.")
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho())

    def buscarNodoPorValor(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorValor(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _buscarNodoPorValor(self, busqueda, nodo):
        if not nodo:
            return None
        if (busqueda == nodo.valor):
            return nodo
        else:
            if (busqueda < nodo.valor):
                return self._buscarNodoPorValor(busqueda, nodo.ObtenerHijoIzquierdo())
            else:
                return self._buscarNodoPorValor(busqueda, nodo.ObtenerHijoDerecho())

    def buscarNodoPorLlave(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorLlave(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    def _buscarNodoPorLlave(self, busqueda, nodo):
        if (nodo):
            if (nodo.nombre.upper() == busqueda.upper() or nodo.id.upper() == busqueda.upper()):
                print("Si se encuentra la llave ", busqueda, f" en el el peaje de -Nombre: {nodo.nombre}, -Id: {nodo.id}")
                return nodo
            return self._buscarNodoPorLlave(busqueda, nodo.ObtenerHijoIzquierdo()) or self._buscarNodoPorLlave(busqueda,nodo.ObtenerHijoDerecho())

    def EliminarNodo(self, busqueda):
        if (self.raiz):
            if isinstance(busqueda, str):
                nodoPorEliminar = self.buscarNodoPorLlave(busqueda)
                if (nodoPorEliminar):
                    self._eliminarNodo(nodoPorEliminar)
            if isinstance(busqueda,int):
                nodoPorEliminar = self.buscarNodoPorValor(busqueda)
                if (nodoPorEliminar):
                    self._eliminarNodo(nodoPorEliminar)

        else:
            print("El árbol está vacío.")

    def _eliminarNodo(self, nodo):
        # caso 1: El nodo es hoja
        if (nodo.EsNodoHoja()):
            if (nodo.EsHijoIzquierdo()):
                nodo.padre.PonerHijoIzquierdo(None)
            else:
                nodo.padre.PonerHijoDerecho(None)
            nodo.PonerPadre(None)
        else:
            # caso 2: tiene un solo hijo
            if (not (nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoIzquierdo())):
                hijo = None
                if (nodo.ObtenerHijoIzquierdo()):
                    hijo = nodo.ObtenerHijoIzquierdo()
                else:
                    hijo = nodo.ObtenerHijoDerecho()
                self.DisminuirNivel(hijo)
                hijo.PonerPadre(nodo.padre)
                if (nodo.EsHijoIzquierdo()):
                    nodo.padre.PonerHijoIzquierdo(hijo)
                else:
                    nodo.padre.PonerHijoDerecho(hijo)
                nodo.PonerHijoDerecho(None)
                nodo.PonerPadre(None)
            else:
                sucesor = self.ObtenerSucesor(nodo.ObtenerHijoDerecho())
                if (sucesor.ObtenerHijoDerecho()):
                    sucesor.ObtenerHijoDerecho().PonerPadre(sucesor.padre)
                    sucesor.padre.PonerHijoIzquierdo(sucesor.ObtenerHijoDerecho())
                sucesor.PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                sucesor.PonerHijoIzquierdo(nodo.ObtenerHijoIzquierdo())
                sucesor.PonerPadre(nodo.padre)
                if (nodo.EsNodoRaiz()):
                    self.raiz = sucesor
                nodo.PonerPadre(None)
                nodo.PonerHijoIzquierdo(None)
                nodo.PonerHijoDerecho(None)

    def ObtenerSucesor(self, nodo):
        while (nodo.ObtenerHijoIzquierdo()):
            nodo = nodo.ObtenerHijoIzquierdo()
        return nodo

    def DisminuirNivel(self, nodo):
        if (nodo):
            nodo.nivel -= 1
            self.DisminuirNivel(nodo.ObtenerHijoIzquierdo())
            self.DisminuirNivel(nodo.ObtenerHijoDerecho())

    def CambiarPeajePos(self, busqueda):

        if (self.raiz):
            if isinstance(busqueda, str):
                nodoPorEliminar = self.buscarNodoPorLlave(busqueda)
                if (nodoPorEliminar):
                    self._CambiarPeajePos(nodoPorEliminar)
            if isinstance(busqueda, int):
                nodoPorEliminar = self.buscarNodoPorValor(busqueda)
                if (nodoPorEliminar):
                    self._CambiarPeajePos(nodoPorEliminar)

        else:
            print("El árbol está vacío.")

    def _CambiarPeajePos(self, nodo):
        # caso 1: El nodo es hoja
        if (nodo.EsNodoHoja()):
            if (nodo.EsHijoIzquierdo()):
                nodo.padre.PonerHijoIzquierdo(None)
            else:
                nodo.padre.PonerHijoDerecho(None)
            nodo.PonerPadre(None)
            m = int(input(f"a donde desea vincular el peaje de {nodo.nombre}"))
            if isinstance(m, str):
                nodoEnlace = self.buscarNodoPorLlave(m)
                if (nodoEnlace):
                    if(nodoEnlace.ObtenerHijoIzquierdo() and nodoEnlace.ObtenerHijoDerecho()):
                        print("el Peaje al cual desea mover tiene los 2 posibles peajes llenos")
            if not (nodoEnlace.ObtenerHijoIzquierdo()):
                if nodo.valor < nodoEnlace.valor:
                    nodoEnlace.PonerHijoIzquierdo(nodo)
                    print(f" ahora el peaje {nodo.nombre} es hijo Izquierdo del peaje {nodoEnlace.nombre}")
                else:
                    print(f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre}")
            if not (nodoEnlace.ObtenerHijoDerecho()):
                if nodo.valor > nodoEnlace.valor:
                    nodoEnlace.PonerHijoDerecho(nodo)
                    print(f" ahora el peaje {nodo.nombre} es hijo Derecho del peaje {nodoEnlace.nombre}")
                else:
                    print(f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre}")
            else:
                print("el Peaje para asignar no esta")
            if isinstance(m, int):
                nodoEnlace = self.buscarNodoPorValor(m)
            if (nodoEnlace):
                if(nodoEnlace.ObtenerHijoIzquierdo() and nodoEnlace.ObtenerHijoDerecho()):
                    print("el Peaje al cual desea mover tiene los 2 posibles peajes llenos")
                if not (nodoEnlace.ObtenerHijoIzquierdo()):
                    if nodo.valor < nodoEnlace.valor:
                        nodoEnlace.PonerHijoIzquierdo(nodo)
                        print(f" ahora el peaje {nodo.nombre} es hijo Izquierdo del peaje {nodoEnlace.nombre}")
                    else:
                        print(f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre}")
            if not (nodoEnlace.ObtenerHijoDerecho()):
                if nodo.valor > nodoEnlace.valor:
                    nodoEnlace.PonerHijoDerecho(nodo)
                    print(f" ahora el peaje {nodo.nombre} es hijo Derecho del peaje {nodoEnlace.nombre}")
                else:
                    print(f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre}")
            else:
                print("el Peaje para asignar no esta")
        else:
            # caso 2: tiene un solo hijo
            if (not (nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoIzquierdo())):
                hijo = None
                if (nodo.ObtenerHijoIzquierdo()):
                    hijo = nodo.ObtenerHijoIzquierdo()
                else:
                    hijo = nodo.ObtenerHijoDerecho()
                self.DisminuirNivel(hijo)
                hijo.PonerPadre(nodo.padre)
                if (nodo.EsHijoIzquierdo()):
                    nodo.padre.PonerHijoIzquierdo(hijo)
                else:
                    nodo.padre.PonerHijoDerecho(hijo)
                nodo.PonerHijoDerecho(None)
                nodo.PonerPadre(None)

            else:
                sucesor = self.ObtenerSucesor(nodo.ObtenerHijoDerecho())
                if (sucesor.ObtenerHijoDerecho()):
                    sucesor.ObtenerHijoDerecho().PonerPadre(sucesor.padre)
                sucesor.padre.PonerHijoIzquierdo(sucesor.ObtenerHijoDerecho())
                sucesor.PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                sucesor.PonerHijoIzquierdo(nodo.ObtenerHijoIzquierdo())
                sucesor.PonerPadre(nodo.padre)
                if (nodo.EsNodoRaiz()):
                    self.raiz = sucesor
                nodo.PonerPadre(None)
                nodo.PonerHijoIzquierdo(None)
                nodo.PonerHijoDerecho(None)
        m = input(f"A Donde desea vincular el peaje de {nodo.nombre}: -")
        if isinstance(m, str):
            nodoEnlace = self.buscarNodoPorLlave(m)
            if (nodoEnlace):
                if (nodoEnlace.ObtenerHijoIzquierdo() and nodoEnlace.ObtenerHijoDerecho()):
                    print("el Peaje al cual desea mover tiene los 2 posibles peajes llenos")
                if not (nodoEnlace.ObtenerHijoIzquierdo()):
                    if nodo.valor < nodoEnlace.valor:
                        nodoEnlace.PonerHijoIzquierdo(nodo)
                        print(f" ahora el peaje {nodo.nombre} es hijo Izquierdo del peaje {nodoEnlace.nombre}")
                    else:
                        print(f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre} al lado Izquierdo")

                if not (nodoEnlace.ObtenerHijoDerecho()):
                    if nodo.valor > nodoEnlace.valor:
                        nodoEnlace.PonerHijoDerecho(nodo)
                        print(f" ahora el peaje {nodo.nombre} es hijo Derecho del peaje {nodoEnlace.nombre}")
                    else:
                        print(f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre} al lado Derecho")
            else:
                print("el Peaje para asignar no esta")

    def EditarNodo(self, busqueda):
        if self.raiz:
            if isinstance(busqueda, str):
                nodoPorEditar = self.buscarNodoPorLlave(busqueda)
                if (nodoPorEditar):
                    self._editarnodo(nodoPorEditar)
            if isinstance(busqueda,int):
                nodoPorEditar = self.buscarNodoPorValor(busqueda)
                if (nodoPorEditar):
                    self._editarnodo(nodoPorEditar)
        else:
            print("El arbol de recorrido esta vacio")

    def _editarnodo(self, nodo):
        if nodo:
            salida=True
            m = random.randint(1, 100)
            n = random.randint(1, 100)
            while salida==True:
                nodo.nombre = input("-Nombre nuevo del peaje: ")
                nodo.id = input("-Id nuevo del peaje: ")
                nodo.valor = self.ValorValido(nodo)
                nodo.recargoIzquierdo = m
                nodo.recargoDerecho = n
                salida= int(input("(1) para salir, (2) para cambiar de nuevo: "))
                if salida==1:
                    salida= False
                else:
                    salida=True
            print(f"El peaje se ha editado: -Nombre: {nodo.nombre}, -Id: {nodo.id}, -Valor del peaje: {nodo.valor}, -Recargo por Izquierda: {nodo.recargoIzquierdo}, -Recargo por Derecha: {nodo.recargoDerecho}")

    def ValorValido(self,nodo):
        if nodo:
            valor = int(input("-valor nuevo del peaje: "))
            if nodo.ObtenerPadre():
                if nodo.EsHijoIzquierdo():
                    if valor > nodo.padre.valor:
                        print(f"El valor no es valido, ya que el valor es mayor al de su padre (el peaje actual es hijo Izquierdo de {nodo.padre.nombre}, valor: {nodo.padre.valor}$)")
                        print("Por favor ingrese un nuevo valor")
                        return self.ValorValido(nodo)
                if nodo.EsHijoDerecho():
                    if valor < nodo.padre.valor:
                        print(f"El valor no es valido, ya que el valor es menor al de su padre (el peaje actual es hijo Derecho de {nodo.padre.nombre}, valor: {nodo.padre.valor}$)")
                        print("Por favor ingrese un nuevo valor")
                        return self.ValorValido(nodo)
                if (nodo.ObtenerHijoIzquierdo() and nodo.ObtenerHijoDerecho()):
                    if valor <= nodo.ObtenerHijoIzquierdo() or valor >= nodo.ObtenerHijoDerecho():
                        print(f"El valor no es valido (el peaje actual es la raiz), porfavor ingrese un nuevo valor del peaje")
                        return self.ValorValido(nodo)
            else:
                if not (nodo.ObtenerHijoIzquierdo()== None and nodo.ObtenerHijoDerecho() == None):
                    if valor <= nodo.ObtenerHijoIzquierdo() or valor >= nodo.ObtenerHijoDerecho():
                        print(f"El valor no es valido (el peaje actual es la raiz), porfavor ingrese un nuevo valor del peaje")
                        return self.ValorValido(nodo)

            print(f"El nuevo valor del Peaje {nodo.nombre} es: {valor}")
            return valor

    def CrearAuto(self):
        tipoAuto = input("tipo de vehiculo: ")
        placa = input("Placa del vehiculo: ")
        recargoDia = int(input("Recargo de Dia: "))
        recargoNoche = int(input("Recargo de noche: "))
        self.Autos.append(Auto(tipoAuto,placa,recargoDia,recargoNoche))
        print(recorrido1.ObtenerAutos())

    def pagoAutos(self, listaAutos,n):
        for i in listaAutos:
            n+=i
        print("total a pagar:",n)
        return n

# PARTE PRINT ---> Hace los llamados de las funciones
recorrido1 = ArbolPeajes()
n=True
while n==True:
    print("PROGRAMA PEAJES COLOMBIA")
    n = input("Desea continuar?. (si) ó (no): ")
    if n=="si":
        n=True
        print(" -Agregar Peaje (1)\n -Crear Auto (2)\n -Editar Peaje (3)\n -Eliminar Peaje (4)\n -Imprimir Peajes (5)\n -Cambiar Peaje de posicion (6)\n -Recorrer Desde la raiz (7)\n -Pagos Por Peaje (8)\n -Pago de cada Vehiculo (9)")
        m=int(input("Que desea Hacer?, por favor escriba el numero: "))
        if m == 1:
            n1= input("Nombre del peaje: ")
            n2 = input("Id del peaje: ")
            n3 = int(input("Valor base del peaje: "))
            recorrido1.AgregarPeaje(n1,n2,n3)
        elif m == 2:
            recorrido1.CrearAuto()
        elif m == 3:
            n4 = input("Nombre ó Id del peaje que desea Editar: ")
            recorrido1.EditarNodo(n4)
        elif m == 4:
            n5 = input("Nombre ó Id del peaje que desea Eliminar: ")
            recorrido1.EditarNodo(n5)
        elif m == 5:
            recorrido1.imprimir_pre_order(recorrido1.raiz)
        elif m == 6:
            n6 = input("Nombre ó Id del peaje que va a cambiar de posicion: ")
            recorrido1.CambiarPeajePos(n6)
        elif m == 7:
            print("Autos:",len(recorrido1.Autos))
            for i in recorrido1.Autos:
                print(i.tipoAuto)
            n7 = int(input("Tipo de Auto que va a hacer el recorrido: "))
            recorrido1.agregarAuto(recorrido1.raiz,recorrido1.Autos[n7-1])
        elif m == 8:
            recorrido1.pagoPeaje(recorrido1.raiz,0)
        elif m == 9:

            for x in recorrido1.Autos:
                n8 = 0
                n9 = 0
                m1 = recorrido1.pagoAutos(x.valorPagos,0)
                if n8 < m1:
                    n8=m1
                    print(f"El auto que mas pago fue {x.tipoAuto}: {n8}$")
                else:
                    print(f"El auto que mas pago fue {x.tipoAuto}: {m1}$")
                print(f"el Auto {x.tipoAuto} pagó: {m1}")

        elif m == 10:
            n=False

    else:
        n=False


# sPDTA: Aun me falta implementar la opcion de poder recorrer desde un nodo que no sea la raiz a otro nodo, de resto creo que todo esta a excepcion de la parte de JSON y la parte GRAFICA, tambien los recargos por izquierda y derecha los hice con un numero random, al igual que la categoria, me falta tambien que imprima el auto que menos gasto y el auto que mas recorrio peajes, posiblemente mañana le pase lo que alcance a adelantar