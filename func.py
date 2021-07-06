import random
global m,s

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
        self.pagos = []

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
            if self.padre.ObtenerHijoIzquierdo():
                return self.valor == self.padre.ObtenerHijoIzquierdo().valor

    def EsHijoDerecho(self):
        if (self.padre):
            if self.padre.ObtenerHijoDerecho():
                return self.valor == self.padre.ObtenerHijoDerecho().valor

class Auto:

    def __init__(self, tipoAuto, placa, valorPagar=None  ,recargoNoche=None, valorPagos=None):
        self.tipoAuto = tipoAuto
        self.placa = placa
        self.valorPagar = valorPagar
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

class ArbolPeajes:
    # Constructor ([listaNodosIniciales], [raiz])
    def __init__(self):
        self.Autos = []
        self.raiz = None
        self.peso = 0
        self.altura = 0

    def PonerRaiz(self, raiz):
        self.raiz = raiz

    # Obtiene los autos del arbol
    def ObtenerAutos(self):
        return self.Autos

    # Obtiene el peso total del arbol
    def ObtenerPeso(self):
        return self.peso

    # Recorre desde cualquier nodo
    def agregarRecorrido1(self, nodo, auto):
        if (not nodo):
            print("No hay ningun peaje disponible por ahora")
        else:

            self._agregarRecorrido1(nodo, auto)

    # Recorre desde cualquier nodo recursivamente
    def _agregarRecorrido1(self, nodo, auto):
        if nodo:
            # caso 1: cuando el nodo es raiz
            if nodo.EsNodoRaiz():
                print(f"Primer peaje se nestro sistema de Peajes: {nodo.nombre}")
                if not (nodo.ObtenerHijoIzquierdo() or nodo.ObtenerHijoDerecho()):
                    print(
                        "Solo tenemos este peaje en nuestro sistema, Puede recorrerlo para salir de el o volver a su origen")
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if "d" in dn.lower():
                        valorPago = (((auto.valorPagar * nodo.valor) / 100))
                        auto.valorPagos.append(valorPago)
                    if "n" in dn.lower():
                        valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                    nodo.autosPeajes.append(auto)
                    nodo.pagos.append(valorPago)
                elif not (nodo.ObtenerHijoIzquierdo() and nodo.ObtenerHijoDerecho()):
                    if nodo.ObtenerHijoIzquierdo():
                        print("El auto", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:",
                              nodo.valor, "$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ",
                              nodo.autosPeajes)
                        m = int(input(
                            f"Dedea continuar a: {nodo.ObtenerHijoIzquierdo().nombre} ?, valor a pagar: {(nodo.ObtenerRecargoIz() + nodo.valor)}$. (1) para continuar, (0) Quedarse en {nodo.nombre}: "))
                        if m == 1:
                            dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                            if "d" in dn.lower():
                                valorPago = (nodo.ObtenerRecargoIz() + ((auto.valorPagar * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            if "n" in dn.lower():
                                valorPago = (nodo.ObtenerRecargoIz() + ((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                            print("-El proximo peaje es: ", nodo.ObtenerHijoIzquierdo().nombre)
                            nodo.autosPeajes.append(auto)
                            nodo.pagos.append(valorPago)
                            self._agregarRecorrido1(nodo.ObtenerHijoIzquierdo(), auto)
                        else:
                            print(f"Volviendo a {nodo.nombre}")
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                    else:
                        print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:",
                              nodo.valor, "$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ",
                              nodo.autosPeajes)
                        m = int(input(f"Dedea Ir a: {nodo.ObtenerHijoDerecho().nombre}?, valor a pagar: {(nodo.ObtenerRecargoDe() + nodo.valor)}$. (1)para continuar, (0)Volver a {nodo.nombre}: "))
                        if m == 1:
                            dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                            if "d" in dn.lower():
                                valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            if "n" in dn.lower():
                                valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                            print("- El proximo peaje es: ", nodo.ObtenerHijoDerecho().nombre)
                            nodo.autosPeajes.append(auto)
                            nodo.pagos.append(valorPago)
                            self._agregarRecorrido(nodo.ObtenerHijoDerecho(), auto)
                        else:
                            print(f"Volviendo a {nodo.nombre}")
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                elif (nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoIzquierdo()):
                    print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:",
                          nodo.valor, "$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ",
                          nodo.autosPeajes)
                    n = int(input(
                        f"Donde desea Ir: (1)-Ir a: {nodo.ObtenerHijoDerecho().nombre}, valor a pagar: {(nodo.ObtenerRecargoDe() + nodo.valor)}$, (2)-ir a: {nodo.ObtenerHijoIzquierdo().nombre}, valor a pagar: {(nodo.ObtenerRecargoIz() + nodo.valor)}$, (0)-Volver a {nodo.nombre}: "))
                    if n == 1:
                        dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                        if "d" in dn.lower():
                            print("-Valor a pagar, ")
                            valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor) / 100))
                            auto.valorPagos.append(valorPago)
                        if "n" in dn.lower():
                            valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                            auto.valorPagos.append(valorPago)
                        print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                        nodo.autosPeajes.append(auto)
                        nodo.pagos.append(valorPago)
                        self._agregarRecorrido1(nodo.ObtenerHijoDerecho(), auto)
                    if n == 2:
                        dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                        if "d" in dn.lower():
                            valorPago = (nodo.ObtenerRecargoIz() + ((auto.valorPagar * nodo.valor) / 100))
                            auto.valorPagos.append(valorPago)
                        if "n" in dn.lower():
                            valorPago = (nodo.ObtenerRecargoIz() + ((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                            auto.valorPagos.append(valorPago)
                        print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                        nodo.autosPeajes.append(auto)
                        nodo.pagos.append(valorPago)
                        self._agregarRecorrido1(nodo.ObtenerHijoIzquierdo(), auto)
                    else:
                        print("Listo")
                        print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")

            # caso 2: cuando el nodo tiene un padre
            elif nodo.ObtenerPadre():
                if nodo.EsNodoHoja():
                    print("Este es uno de los ultimos peajes de nuestro Sistema")
                    m = int(input(
                        f"Dedea salir de {nodo.nombre}, valor a pagar: {(nodo.valor)}$, (1) Ir a: {nodo.ObtenerPadre().nombre} (0) Volver a {nodo.nombre}: "))
                    if m == 1:
                        dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                        if "d" in dn.lower():
                            valorPago = (((auto.valorPagar * nodo.valor) / 100))
                            auto.valorPagos.append(valorPago)
                        if "n" in dn.lower():
                            valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                            auto.valorPagos.append(valorPago)
                        print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                        nodo.autosPeajes.append(auto)
                        nodo.pagos.append(valorPago)
                        self._agregarRecorrido1(nodo.ObtenerPadre(), auto)
                    if m == 0:
                        print(f"Volviendo a {nodo.nombre}")
                        print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                else:
                    if not (nodo.ObtenerHijoIzquierdo() and nodo.ObtenerHijoDerecho()):
                        if nodo.ObtenerHijoIzquierdo():
                            print("El auto", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id,
                                  " -Valor:", nodo.valor, "$ |||| ",
                                  f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                            m = int(input(
                                f"Dedea continuar a: {nodo.ObtenerHijoIzquierdo().nombre} ?, valor a pagar: {(nodo.ObtenerRecargoIz() + nodo.valor)}$. (1) para continuar, (2)Ir a: {nodo.ObtenerPadre().nombre}, valor a pagar: {nodo.ObtenerPadre().valor}$ (0) Quedarse en {nodo.nombre}: "))
                            if m == 1:
                                dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                                if "d" in dn.lower():
                                    valorPago = (nodo.ObtenerRecargoDe() +((auto.valorPagar * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                if "n" in dn.lower():
                                    valorPago = (nodo.ObtenerRecargoDe() +((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                                print("-El proximo peaje es: ", nodo.ObtenerHijoIzquierdo().nombre)
                                nodo.autosPeajes.append(auto)
                                nodo.pagos.append(valorPago)
                                self._agregarRecorrido1(nodo.ObtenerHijoIzquierdo(), auto)
                            if m == 2:
                                dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                                if  "d" in dn.lower():
                                    valorPago = (((auto.valorPagar * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                else:
                                    valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                                nodo.autosPeajes.append(auto)
                                nodo.pagos.append(valorPago)
                                self._agregarRecorrido1(nodo.ObtenerPadre(), auto)
                            else:
                                print(f"Volviendo a {nodo.nombre}")
                                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                        else:
                            print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id,
                                  " -Valor:",
                                  nodo.valor, "$ |||| ",
                                  f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ",
                                  nodo.autosPeajes)
                            m = int(input(
                                f"Dedea Ir a: {nodo.ObtenerHijoDerecho().nombre}?, valor a pagar: {(nodo.ObtenerRecargoDe() + nodo.valor)}$. (1)para continuar, (2)Ir a: {nodo.ObtenerPadre().nombre}, valor a pagar: {nodo.ObtenerPadre().valor}$, (0)Volver a {nodo.nombre}: "))
                            if m == 1:
                                dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                                if "d" in dn.lower():
                                    valorPago = (nodo.ObtenerRecargoDe() +((auto.valorPagar * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                if "n" in dn.lower():
                                    valorPago = (nodo.ObtenerRecargoDe() +((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                                print("- El proximo peaje es: ", nodo.ObtenerHijoDerecho().nombre)
                                nodo.autosPeajes.append(auto)
                                nodo.pagos.append(valorPago)
                                self._agregarRecorrido(nodo.ObtenerHijoDerecho(), auto)
                            if m == 2:
                                dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                                if "d" in dn.lower():
                                    valorPago = (((auto.valorPagar * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                else:
                                    valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                    auto.valorPagos.append(valorPago)
                                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                                print("- El proximo peaje es: ", nodo.ObtenerPadre().nombre)
                                nodo.autosPeajes.append(auto)
                                nodo.pagos.append(valorPago)
                                self._agregarRecorrido(nodo.ObtenerPadre(), auto)
                            else:
                                print(f"Volviendo a {nodo.nombre}")
                                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                    else:
                        print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:",
                              nodo.valor, "$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ",
                              nodo.autosPeajes)
                        n = int(input(
                            f"Donde desea Ir: (1)-Ir a: {nodo.ObtenerHijoDerecho().nombre}, valor a pagar: {(nodo.ObtenerRecargoDe() + nodo.valor)}$, (2)-ir a: {nodo.ObtenerHijoIzquierdo().nombre}, valor a pagar: {(nodo.ObtenerRecargoIz() + nodo.valor)}$, (3)-Ir a {nodo.ObtenerPadre()}, valor a pagar {nodo.ObtenerPadre().valor}:, (0)-Volver a {nodo.nombre}: "))
                        if n == 1:
                            dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                            if "d" in dn.lower():
                                print("-Valor a pagar, ")
                                valorPago = (((auto.valorPagar * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            if "n" in dn.lower():
                                valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                            nodo.autosPeajes.append(auto)
                            nodo.pagos.append(valorPago)
                            self._agregarRecorrido1(nodo.ObtenerHijoDerecho(), auto)
                        if n == 2:
                            dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                            if "d" in dn.lower():
                                valorPago = (((auto.valorPagar * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            if "n" in dn.lower():
                                valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                            nodo.autosPeajes.append(auto)
                            nodo.pagos.append(valorPago)
                            self._agregarRecorrido1(nodo.ObtenerHijoIzquierdo(), auto)
                        if n == 3:
                            dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                            if "d" in dn.lower():
                                valorPago = (((auto.valorPagar * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            if "n" in dn.lower():
                                valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                                auto.valorPagos.append(valorPago)
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                            nodo.autosPeajes.append(auto)
                            nodo.pagos.append(valorPago)
                            self._agregarRecorrido1(nodo.ObtenerPadre(), auto)
                        else:
                            print("Listo")
                            print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")

    # Recorre desde raiz
    def agregarRecorrido(self, nodo, auto):
        if (not nodo):
            print("No hay ningun peaje disponible en nuestro sistema")
        else:

            self._agregarRecorrido(nodo, auto)

    # Recorre desde raiz recursivamente
    def _agregarRecorrido(self, nodo, auto):
        if (nodo.EsNodoHoja()):
            print("Este es uno de los ultimos peajes de nuestro Sistema")
            m = int(input(f"Dedea salir de {nodo.nombre}, valor a pagar: {(nodo.valor)}$. (1) para continuar (0) Volver a {nodo.nombre}: "))
            if m == 1:
                dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                if "d" in dn.lower():
                    valorPago = (((auto.valorPagar * nodo.valor) / 100))
                    nodo.pagos.append(valorPago)
                    auto.valorPagos.append(valorPago)
                if "n" in dn.lower():
                    valorPago = (((auto.valorPagar * nodo.valor) / 100))+(((auto.recargoNoche * nodo.valor) / 100))
                    nodo.pagos.append(valorPago)
                    auto.valorPagos.append(valorPago)
                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                print("El ultimo peaje del auto '", auto.tipoAuto, "' fue el peaje: ", nodo.nombre," - ",nodo.id," - ",nodo.valor,"$")
            else:
                print(f"Volviendo a {nodo.nombre}")
                print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
        else:
            if not (nodo.ObtenerHijoDerecho()):
                print("El auto", auto.tipoAuto," paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:", nodo.valor,"$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                m = int(input(f"Dedea continuar a: {nodo.ObtenerHijoIzquierdo().nombre} ?, valor a pagar: {(nodo.ObtenerRecargoIz()+nodo.valor)}$. (1) para continuar (0) Volver a {nodo.nombre}: "))
                if m == 1:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if "d" in dn.lower():
                        valorPago = (nodo.ObtenerRecargoDe() + ((auto.recargoDia * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    if "n" in dn.lower():
                        valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor)/ 100))+(((auto.recargoNoche * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                    print("-El proximo peaje es: ", nodo.ObtenerHijoIzquierdo().nombre)
                    nodo.autosPeajes.append(auto)
                    self._agregarRecorrido(nodo.ObtenerHijoIzquierdo(), auto)
                else:
                    print(f"Volviendo a {nodo.nombre}")
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
            if not (nodo.ObtenerHijoIzquierdo()):
                print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:", nodo.valor,"$ |||| ", f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                m = int(input(f"Dedea Ir a: {nodo.ObtenerHijoDerecho().nombre}?, valor a pagar: {(nodo.ObtenerRecargoDe()+nodo.valor)}$. (1)para continuar (0)Volver a {nodo.nombre}: "))
                if m == 1:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if "d" in dn.lower():
                        valorPago = (nodo.ObtenerRecargoDe()+((auto.valorPagar * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    if "n" in dn.lower():
                        valorPago = (nodo.ObtenerRecargoDe()+((auto.valorPagar * nodo.valor)/ 100))+(((auto.recargoNoche * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                    print("- El proximo peaje es: ", nodo.ObtenerHijoDerecho().nombre)
                    nodo.autosPeajes.append(auto)
                    self._agregarRecorrido(nodo.ObtenerHijoDerecho(), auto)
                else:
                    print(f"Volviendo a {nodo.nombre}")
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
            if nodo.ObtenerHijoDerecho() and nodo.ObtenerHijoIzquierdo():
                print("El auto ", auto.tipoAuto, " paso al peaje:", nodo.nombre, " -Id:", nodo.id, " -Valor:", nodo.valor,"$ |||| ",f"por el peaje '{nodo.nombre}' han pasado los siguientes autos: ", nodo.autosPeajes)
                n = int(input(f"Donde desea Ir: (1)-Ir a: {nodo.ObtenerHijoDerecho().nombre}, valor a pagar: {(nodo.ObtenerRecargoDe()+nodo.valor)}$, (2)-ir a: {nodo.ObtenerHijoIzquierdo().nombre}, valor a pagar: {(nodo.ObtenerRecargoIz()+nodo.valor)}$, (0)-Volver a {nodo.nombre}: "))
                if n == 0:
                    print("Listo")
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}")
                if n == 1:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if "d" in dn.lower():
                        print("-Valor a pagar, ")
                        valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    if "n" in dn.lower():
                        valorPago = (nodo.ObtenerRecargoDe() + ((auto.valorPagar * nodo.valor)/ 100))+(((auto.recargoNoche * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                    nodo.autosPeajes.append(auto)
                    self._agregarRecorrido(nodo.ObtenerHijoDerecho(), auto)
                if n == 2:
                    dn = input(f"-El viaje es de dia o noche (dia) ó  (noche): ")
                    if "d" in dn.lower():
                        valorPago = (nodo.ObtenerRecargoIz() +((auto.valorPagar * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    else:
                        valorPago = (nodo.ObtenerRecargoIz() + ((auto.valorPagar * nodo.valor)/ 100))+(((auto.recargoNoche * nodo.valor)/ 100))
                        nodo.pagos.append(valorPago)
                        auto.valorPagos.append(valorPago)
                    print(f"el auto {auto.tipoAuto} debe pagar: {auto.valorPagos}$")
                    nodo.autosPeajes.append(auto)
                    self._agregarRecorrido(nodo.ObtenerHijoIzquierdo(), auto)

    # Agregará un nodo al arbol
    def AgregarPeaje(self, nombre, id, valor):

        if self.raiz:
            # agregar nodo nuevo al árbol
            self._AgregarPeaje(nombre, id, valor, self.raiz)
        else:
            # agregar el nuevo nodo como raíz

            m=random.randint(1,50)
            n=random.randint(1,50)
            recIz = (valor * m) / 100
            recDe = (valor * n) / 100
            s=random.randint(1,4)
            categoria = ""
            if s == 1:
                categoria = "A - Blanco"
            if s == 2:
                categoria = "B - Verde"
            if s == 3:
                categoria = "C - Azul"
            if s == 4:
                categoria = "D - Rojo"
            self.raiz = Nodo(nombre,id, valor, 1,recIz,recDe,categoria)
            self.peso += 1
            print("El Peaje de:  ", nombre, " se ha agregado como Primer peaje en el nivel" ,self.raiz.ObtenerNivel(),f"valor: {valor}","Recargo por Izquierda: ",self.raiz.ObtenerRecargoIz(),"Recargo por Derecha: ",self.raiz.ObtenerRecargoDe(),"Categoria: ",self.raiz.categoria)

    # Agregará unnodo al arbol recursivamente
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
                recIz = (valor * m) / 100
                recDe = (valor * n) / 100
                s = random.randint(1, 4)
                categoria = ""
                if s == 1:
                    categoria = "A - Blanco"
                if s == 2:
                    categoria = "B - Verde"
                if s == 3:
                    categoria = "C - Azul"
                if s == 4:
                    categoria = "D - Rojo"
                # se crea un nuevo nodo y se asigna como hijo
                nuevoNodo = Nodo(nombre , id, valor, nodo.ObtenerNivel() + 1,recIz,recDe,categoria, nodo)
                nodo.PonerHijoIzquierdo(nuevoNodo)
                self.peso += 1
                if (self.altura < nuevoNodo.ObtenerNivel()):
                    self.altura = nuevoNodo.ObtenerNivel()
                print("Se ha agregado como Peaje izquierdo de", nodo.nombre, " al peaje de ", nuevoNodo.nombre, "en el nivel",
                      nuevoNodo.ObtenerNivel(),"Recargo por Izquierda:",nuevoNodo.ObtenerRecargoIz(),"Recargo por Derecha:",nuevoNodo.ObtenerRecargoDe(),
                      "Categoria:",nuevoNodo.categoria)
        else:
            if (valor > nodo.valor or valor == nodo.valor):
                if (nodo.ObtenerHijoDerecho()):  # verifica si tiene hijo derecho
                    # se llama recursivamente al hijo implicado
                    self._AgregarPeaje(nombre, id, valor, nodo.ObtenerHijoDerecho())
                else:
                    # Se crean los recargos de Izquierda y derecha
                    m = random.randint(1, 100)
                    n = random.randint(1, 100)
                    recIz = (valor * m) / 100
                    recDe = (valor * n) / 100
                    s = random.randint(1, 4)
                    categoria = ""
                    if s == 1:
                        categoria = "A - Blanco"
                    if s == 2:
                        categoria = "B - Verde"
                    if s == 3:
                        categoria = "C - Azul"
                    if s == 4:
                        categoria = "D - Rojo"

                    # se crea un nuevo nodo y se asigna como hijo
                    nuevoNodo = Nodo(nombre, id, valor, nodo.ObtenerNivel() + 1,recIz,recDe,categoria, nodo)
                    nodo.PonerHijoDerecho(nuevoNodo)
                    self.peso += 1
                    if (self.altura < nuevoNodo.ObtenerNivel()):
                        self.altura = nuevoNodo.ObtenerNivel()
                    print("Se ha agregado como Peaje derecho de", nodo.nombre, " al peaje de:  ", nuevoNodo.nombre, "en el nivel",
                          nuevoNodo.ObtenerNivel(),"Recargo por Izquierda:",nuevoNodo.ObtenerRecargoIz(),"Recargo por Derecha:",nuevoNodo.ObtenerRecargoDe(),
                      "Categoria:",nuevoNodo.categoria)

    # Mostrará el pago que se hicieron en cada peaje
    def pagoPeaje(self, nodo):
        total=0
        if (nodo):
            print("------------------------------------------------")
            print("Por el peaje ", nodo.nombre, f" pasaron los autos:")
            for j in nodo.autosPeajes:
                print(f"---------------------------------------------------------------------")
                print(f"el Auto: {j.tipoAuto}")
            if len(nodo.pagos)!=0:
                for i in range(len(nodo.pagos)):

                    total+=nodo.pagos[i]
            print("------------------------------------------------")
            print(f"Pago total realizado en el peaje: {total}$")
            print("------------------------------------------------")
            self.pagoPeaje(nodo.ObtenerHijoIzquierdo())
            self.pagoPeaje(nodo.ObtenerHijoDerecho())
            return total

    # Mostrará el pago total de todo el arbol
    def totalArbol(self,nodo,total):
        if nodo:
            if len(nodo.pagos)!=0:
                totalNodo=0
                for i in nodo.pagos:
                    totalNodo+=i
                total+=totalNodo
        if nodo.ObtenerHijoIzquierdo():
            return self.totalArbol(nodo.ObtenerHijoIzquierdo(),total)
        if nodo.ObtenerHijoDerecho():
            return self.totalArbol(nodo.ObtenerHijoDerecho(),total)
        return total

    def CrearAuto1(self, tipoAuto, placa, valorPagar,recargoNoche):
        self.Autos.append(Auto(tipoAuto,placa,valorPagar,recargoNoche))

    # Pre-order (R-I-D)
    def imprimir_pre_order(self, nodo):
        if (nodo):
            print(f"- Peaje: {nodo.nombre} , - Id: {nodo.id} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}, -Recargo por Derecha {nodo.ObtenerRecargoDe()}, -Categoria {nodo.categoria}.")
            self.imprimir_pre_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_pre_order(nodo.ObtenerHijoDerecho())

    # In-order (I-R-D)
    def imprimir_in_order(self, nodo):
        if (nodo):
            self.imprimir_in_order(nodo.ObtenerHijoIzquierdo())
            print(f"- Peaje: {nodo.nombre} , - Id: {nodo.id} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}$, -Recargo por Derecha {nodo.ObtenerRecargoDe()}$.")
            self.imprimir_in_order(nodo.ObtenerHijoDerecho())

    # Post-order (I-D-R)
    def imprimir_post_order(self, nodo):
        if (nodo):
            self.imprimir_post_order(nodo.ObtenerHijoIzquierdo())
            self.imprimir_post_order(nodo.ObtenerHijoDerecho())
            print(f"- Peaje: {nodo.nombre} , - Id: {nodo.id} , -valor: {nodo.valor}, -Recargo por Izquierda {nodo.ObtenerRecargoIz()}, -Recargo por Derecha {nodo.ObtenerRecargoDe()}.")

    # Recorrido en Amplitud
    def imprimir_amplitud(self, nodo):
        if (nodo):
            cola = [nodo]
            recorrido = []
            while (len(cola) > 0):
                nodoActual = cola.pop(0)
                recorrido.append(nodoActual.valor)
                hijoIzq = nodoActual.ObtenerHijoIzquierdo()
                hijoDer = nodoActual.ObtenerHijoDerecho()
                if (hijoIzq):
                    cola.append(hijoIzq)
                if (hijoDer):
                    cola.append(hijoDer)
            print("El recorrido en amplitud es:")
            print(recorrido)
        else:
            print("El árbol está vacío.")

    # Verifica que un árbol sea impar
    def EsArbolImpar(self, nodo):
        if (nodo):
            cola = [nodo]
            valores = [0 for i in range(self.altura)]
            while (len(cola) > 0):
                nodoActual = cola.pop(0)

                valores[nodoActual.ObtenerNivel() - 1] += nodoActual.valor

                hijoIzq = nodoActual.ObtenerHijoIzquierdo()
                hijoDer = nodoActual.ObtenerHijoDerecho()
                if (hijoIzq):
                    cola.append(hijoIzq)
                if (hijoDer):
                    cola.append(hijoDer)
            print("Los Valores por niveles son:")
            print(valores)
            esImpar = True
            for v in valores:
                if (v % 2 == 0):
                    esImpar = False
                    break;
            if (esImpar):
                print("El árbol es impar")
            else:
                print("El árbol NO es impar")
        else:
            print("El árbol está vacío.")

    # Buscará un nodo en espcifico por el valor
    def buscarNodoPorValor(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorValor(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    # Buscará un nodo en espcifico por el valor recursivamente
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

    # Buscará un nodo en espcifico por una llave
    def buscarNodoPorLlave(self, busqueda):
        if self.raiz:
            # iniciar búsqueda
            return self._buscarNodoPorLlave1(busqueda, self.raiz)
        else:
            print("El árbol está vacio y no se puede buscar.")
            return None

    # Buscará un nodo en espcifico por una llave recursivamente
    def _buscarNodoPorLlave1(self, busqueda, nodo):
        if (nodo):
            if (nodo.nombre.upper() == busqueda.upper() or nodo.id.upper() == busqueda.upper()):
                return nodo
            return self._buscarNodoPorLlave1(busqueda, nodo.ObtenerHijoIzquierdo()) or self._buscarNodoPorLlave1(busqueda,nodo.ObtenerHijoDerecho())

    # Buscará un nodo en espcifico por una llave recursivamente
    def _buscarNodoPorLlave(self, busqueda, nodo):
        if (nodo):
            if (nodo.nombre.upper() == busqueda.upper() or nodo.id.upper() == busqueda.upper()):
                print("Si se encuentra la llave ", busqueda, f" en el el peaje de -Nombre: {nodo.nombre}, -Id: {nodo.id}")
                return nodo
            return self._buscarNodoPorLlave(busqueda, nodo.ObtenerHijoIzquierdo()) or self._buscarNodoPorLlave(busqueda,nodo.ObtenerHijoDerecho())

    # Mostrar peso del árbol por niveles y el total del árbol
    def PesoPorNiveles(self, nodo):
        if (nodo):
            cola = [nodo]
            pesosPorNivel = [0 for i in range(self.altura)]
            while (len(cola) > 0):
                nodoActual = cola.pop(0)
                pesosPorNivel[nodoActual.ObtenerNivel() - 1] += 1
                hijoIzq = nodoActual.ObtenerHijoIzquierdo()
                hijoDer = nodoActual.ObtenerHijoDerecho()
                if (hijoIzq):
                    cola.append(hijoIzq)
                if (hijoDer):
                    cola.append(hijoDer)
            return pesosPorNivel
        else:
            return None

    # Eliminará un nodo en especifico
    def EliminarNodo(self, busqueda):
        if (self.raiz):
            if isinstance(busqueda, str):
                nodoPorEliminar = self.buscarNodoPorLlave(busqueda)
                if (nodoPorEliminar):
                    return self._eliminarNodo(nodoPorEliminar)
            if isinstance(busqueda,int):
                nodoPorEliminar = self.buscarNodoPorValor(busqueda)
                if (nodoPorEliminar):
                    return self._eliminarNodo(nodoPorEliminar)
        else:
            print("El árbol está vacío.")
        return

    # Eliminará un nodo en especifico mientras lo busca
    def _eliminarNodo(self, nodo):
        # caso 1: cuando el nodo, es nodo hoja
        if nodo.EsNodoHoja():
            # pregunto si soy hijo derecho o izquierdo para eliminar el indicado
            if nodo.EsHijoIzquierdo():
                nodo.ObtenerPadre().PonerHijoIzquierdo(None)
            else:
                nodo.ObtenerPadre().PonerHijoDerecho(None)
            nodo.PonerPadre(None)
            if nodo == self.raiz:
                self.raiz = None
        else:
            # caso 2: cuando soy nodo rama (tengo hijo izquierdo o derecho)
            if not (nodo.ObtenerHijoIzquierdo() and nodo.ObtenerHijoDerecho()):
                hijo = None
                if nodo.ObtenerHijoIzquierdo():
                    hijo = nodo.ObtenerHijoIzquierdo()
                else:
                    # hijo derecho
                    hijo = nodo.ObtenerHijoDerecho()
                self.DisminuirNivel(hijo)
                # le asigno a mi hijo izquierdo como padre, a mi padre
                hijo.PonerPadre(nodo.ObtenerPadre())
                # pregunto si soy hijo izquierdo o derecho
                if nodo.EsHijoIzquierdo():
                    # asigno a mi padre, a mi hijo izquierdo
                    nodo.ObtenerPadre().PonerHijoIzquierdo(hijo)
                    nodo.PonerHijoIzquierdo(None)
                if nodo.EsHijoDerecho():
                    nodo.ObtenerPadre().PonerHijoDerecho(hijo)
                    nodo.PonerHijoDerecho(None)
                else:
                    if nodo.EsNodoRaiz():
                        self.PonerRaiz(hijo)
                        nodo.PonerHijoIzquierdo(None)
                        nodo.PonerHijoDerecho(None)
                        print(f"La nueva raiz: {self.raiz.nombre}")
                nodo.PonerPadre(None)
            else:
                # caso 3: cuando el nodo tiene los dos hijos
                sucesor = self.ObtenerSucesor(nodo.ObtenerHijoDerecho())
                if sucesor.ObtenerHijoDerecho():
                    sucesor.ObtenerHijoDerecho().PonerPadre(sucesor.ObtenerPadre())
                    sucesor.ObtenerPadre().PonerHijoDerecho(sucesor.ObtenerHijoDerecho())
                else:
                    sucesor.ObtenerPadre().PonerHijoDerecho(None)
                sucesor.PonerPadre(None)
                sucesor.PonerHijoDerecho(nodo.ObtenerHijoDerecho())
                sucesor.PonerHijoIzquierdo(nodo.ObtenerHijoIzquierdo())
                nodo.PonerPadre(None)
                nodo.PonerHijoIzquierdo(None)
                nodo.PonerHijoDerecho(None)
                if nodo.EsNodoRaiz():
                    self.PonerRaiz(sucesor)
                    nodo.PonerHijoIzquierdo(None)
                    nodo.PonerHijoDerecho(None)
                    print(f"La nueva raiz: {self.raiz.nombre}")
                else:
                    sucesor.PonerPadre(nodo.ObtenerPadre())
                    if nodo.EsHijoIzquierdo():
                        nodo.ObtenerPadre().PonerHijoIzquierdo(sucesor)
                    else:
                        nodo.ObtenerPadre().PonerHijoDerecho(sucesor)
        return nodob

    # Obtendrá el último hijo de la izquierda de la rama derecha
    def ObtenerSucesor(self, nodo):
        while (nodo.ObtenerHijoIzquierdo()):
            nodo = nodo.ObtenerHijoIzquierdo()
        return nodo

    # Regresará a un nivel anterior
    def DisminuirNivel(self, nodo):
        if (nodo):
            nodo.nivel -= 1
            self.DisminuirNivel(nodo.ObtenerHijoIzquierdo())
            self.DisminuirNivel(nodo.ObtenerHijoDerecho())

    # Cambiará la posición de un peaje
    def CambiarPeajePos1(self, nodo):
        self.imprimir_pre_order(self.raiz)
        salida = False
        while salida == False:
            m = input(f"A Donde desea vincular el peaje de {nodo.nombre}: -")
            if isinstance(m, str):
                nodoEnlace = self.buscarNodoPorLlave(m)
                if (nodoEnlace):
                    if (nodoEnlace.ObtenerHijoIzquierdo() and nodoEnlace.ObtenerHijoDerecho()):
                        print("el Peaje al cual desea mover tiene los 2 posibles peajes llenos")
                    elif not (nodoEnlace.ObtenerHijoIzquierdo() and nodoEnlace.ObtenerHijoDerecho()):
                        if nodo.valor > nodoEnlace.valor:
                            if nodoEnlace.ObtenerHijoDerecho():
                                print(f"El nodo tiene un hijo, por lo tanto el enlace se debe hacer con el. -Hijo Derecho {nodoEnlace.ObtenerHijoDerecho().nombre}")
                            else:
                                nodoEnlace.PonerHijoDerecho(nodo)
                                nodo.PonerPadre(nodoEnlace)
                                salida = True
                                print(f" ahora el peaje {nodo.nombre} es hijo Derecho del peaje {nodoEnlace.nombre}")
                        if nodo.valor < nodoEnlace.valor:
                            if nodoEnlace.ObtenerHijoIzquierdo():
                                print(f"El nodo tiene un hijo, por lo tanto el enlace se hara con el. -Hijo Izquierdo {nodoEnlace.ObtenerHijoIzquierdo().nombre}")
                            else:
                                nodoEnlace.PonerHijoIzquierdo(nodo)
                                nodo.PonerPadre(nodoEnlace)
                                salida = True
                                print(f" ahora el peaje {nodo.nombre} es hijo Izquierdo del peaje {nodoEnlace.nombre}")

                    elif (nodoEnlace.ObtenerHijoIzquierdo()):
                        if nodo.valor > nodoEnlace.valor:
                            nodoEnlace.PonerHijoDerecho(nodo)
                            nodo.PonerPadre(nodoEnlace)
                            salida = True
                            print(f" ahora el peaje {nodo.nombre} es hijo Izquierdo del peaje {nodoEnlace.nombre}")
                        else:
                            print(
                                f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre}, su valor: {nodo.valor} el valor de su padre {nodoEnlace.valor}")
                    elif (nodoEnlace.ObtenerHijoDerecho()):
                        if nodo.valor < nodoEnlace.valor:
                            nodoEnlace.PonerHijoIzquierdo(nodo)
                            nodo.PonerPadre(nodoEnlace)
                            salida = True
                            print(f" ahora el peaje {nodo.nombre} es hijo Derecho del peaje {nodoEnlace.nombre}")
                        else:
                            print(
                                f"El peaje {nodo.nombre} no cumple con los requisitos para enlazarlo al peaje {nodoEnlace.nombre}, su valor: {nodo.valor} el valor de su padre {nodoEnlace.valor}")

            else:
                print("el Peaje para asignar no esta")

    # Agregará un nuevo auto
    def CrearAuto(self):
        tipoAuto = input("tipo de vehiculo: ")
        placa = input("Placa del vehiculo: ")
        valorPagar = int(input("Total a pagar: "))
        recargoNoche = int(input("Recargo de noche: "))
        self.Autos.append(Auto(tipoAuto,placa,valorPagar,recargoNoche))

    # Imprimirá los autos almacenados
    def ImprimirAutos(self):
        for x in range(len(self.Autos)):
            print(f"{x+1}- {self.Autos[x].tipoAuto} placa: {self.Autos[x].placa}")
        print("---------------------------------------------------")

    # Mostrará el pago hecho por cada auto
    def pagoAutos(self, listaAutos,n):
        for i in listaAutos:
            n+=i
        return n

    # Mostrará el auto con el pago menor
    def autoMenorPago (self, listaAutos):
        for x in range(len(listaAutos)):
            if x==0:
                menor=listaAutos[0]
            if recorrido1.pagoAutos(menor.valorPagos,0) > recorrido1.pagoAutos(listaAutos[x].valorPagos, 0):
                menor=listaAutos[x]
        return menor

    # Mostrará el auto con el pago mayor
    def autoMayorPago (self, listaAutos):
        for x in range(len(listaAutos)):
            if x==0:
                mayor=listaAutos[0]
            if recorrido1.pagoAutos(mayor.valorPagos,0) < recorrido1.pagoAutos(listaAutos[x].valorPagos, 0):
                mayor=listaAutos[x]
        return mayor

    # Mostrará el auto que paso por más peajes
    def autoMasPEajes (self, listaAutos):
        for x in range(len(listaAutos)):
            if x==0:
                mayor=listaAutos[0]
            if len(mayor.valorPagos) < listaAutos[x].valorPagos:
                mayor=listaAutos[x]
        return mayor

    # Mostrará el peaje con más autos recorridos
    def PeajeMasRecorrido(self, nodo, aux):
        if (nodo):
            if nodo==self.raiz:
                aux=nodo
            if len(nodo.pagos)>len(aux.pagos):
                aux=nodo
                return aux
            return self.PeajeMasRecorrido(nodo.ObtenerHijoIzquierdo(),aux)
            return self.PeajeMasRecorrido(nodo.ObtenerHijoDerecho(),aux)

        return aux

    # Mostrará el peaje con menos autos recorridos
    def PeajeMenosRecorrido(self, nodo, aux1):
        if (nodo):
            if nodo==self.raiz:
                aux1=nodo
            if len(nodo.autosPeajes)<len(aux1.autosPeajes):
                aux1=nodo
                return aux1
            return self.PeajeMenosRecorrido(nodo.ObtenerHijoIzquierdo(),aux1)
            return self.PeajeMenosRecorrido(nodo.ObtenerHijoDerecho(),aux1)

        return aux1

recorrido1 = ArbolPeajes()
retorno=True

recorrido1.AgregarPeaje("MANIZALES","MN2021",25000)
recorrido1.AgregarPeaje("MEDELLIN","MD2021",34500)
recorrido1.AgregarPeaje("BARRANCABERMEJA","BR2021",18700)
recorrido1.AgregarPeaje("PEREIRA","PR2021",27300)
recorrido1.AgregarPeaje("CARTAGO","CRG2021",22400)
recorrido1.AgregarPeaje("ARMENIA","ARM2021",33000)
recorrido1.AgregarPeaje("TOLIMA","TL2021",33000)
recorrido1.AgregarPeaje("CALI","CL2021",32200)
recorrido1.AgregarPeaje("BOGOTA","BG2021",38700)
recorrido1.AgregarPeaje("NEIVA","NV2021",22700)
recorrido1.AgregarPeaje("POPAYAN","PY2021",12500)
recorrido1.AgregarPeaje("PASTO","PS2021",13750)

recorrido1.CrearAuto1("CAMION","CHE - 123",100,7)
recorrido1.CrearAuto1("BUS DE TRANSPORTE PUBLICO","ITN - 311",90,6)
recorrido1.CrearAuto1("CAMIONETA","HTY - 232",60,5)
recorrido1.CrearAuto1("AUTOMOVIL","YTW - 909",50,4)
recorrido1.CrearAuto1("MOTOCICLETA","QMB - 12D",20,3)
recorrido1.CrearAuto1("MOTOCICLETA","NBO - 23S",10,2)

while retorno==True:
    print("PROGRAMA PEAJES COLOMBIA")
    retorno = input("Desea continuar?. (si) ó (no): ")
    if retorno.lower()=="no":
        retorno=False
    else:
        retorno=True
        print(" -Agregar Peaje (1)\n -Crear Auto (2)\n -Editar Peaje (3)\n -Eliminar Peaje (4)\n -Imprimir Peajes (5)\n"
              " -Cambiar Peaje de posicion (6)\n -Recorrer Desde la raiz (7)\n -Recorrer Desde cualquier nodo (8)\n -Pagos Por Peaje (9)\n -Pago de cada Vehiculo (10)\n"
              " -Vehiculo que mas pago (11)\n -Vehiculo que menos pago (12)\n -Peaje con mas transito de vehiculos (13)\n -Peaje con menos transito de vehiculos (14)\n"
              " -Total de pagos realizados en el arbol de peajes (15)\n -Boletin de pagos (16)\n -Salir (17)\n")
        m=int(input("Que desea Hacer?, por favor escriba el numero: "))
        if m == 1:
            n1= input("Nombre del peaje: ")
            n2 = input("Id del peaje: ")
            n3 = int(input("Valor base del peaje: "))
            recorrido1.AgregarPeaje(n1,n2,n3)
        elif m == 2:
            recorrido1.CrearAuto()
            recorrido1.ImprimirAutos()
        elif m == 3:
            m = input("El peaje cambiara de posicion si se Edita, desea editarlo de igual forma??: (si) ó (no): ")
            if "s" in m.lower():
                n4 = input("Nombre ó Id del peaje que desea Editar: ")
                nodoPorEditar = recorrido1.buscarNodoPorLlave(n4)
                if nodoPorEditar:
                    nodoPorEditar1=recorrido1.EliminarNodo(nodoPorEditar.nombre)
                    nodoPorEditar1.nombre = input("- Nombre nuevo del Peaje: ")
                    nodoPorEditar1.id = input("- Id nuevo del Peaje: ")
                    nodoPorEditar1.valor = int(input("- Valor nuevo del Peaje: "))
                    recorrido1.AgregarPeaje(nodoPorEditar1.nombre, nodoPorEditar1.id, nodoPorEditar1.valor)
                    print("El peaje se ha editado")
                else:
                    print("El peaje no se edito")
        elif m == 4:
            n5 = input("Nombre ó Id del peaje que desea Eliminar: ")
            recorrido1.EliminarNodo(n5)
        elif m == 5:
            recorrido1.imprimir_pre_order(recorrido1.raiz)
        elif m == 6:
            n6 = input("Nombre ó Id del peaje que va a cambiar de posicion: ")
            nodoCambio=recorrido1.buscarNodoPorLlave(n6)
            nodoCambio1=0
            if nodoCambio:
                nodoCambio1=recorrido1.EliminarNodo(nodoCambio.nombre)
            recorrido1.CambiarPeajePos1(nodoCambio1)
        elif m == 7:
            print("Autos:",len(recorrido1.Autos))
            if len(recorrido1.Autos)==0:
                print("No es posible hacer un recorrido ya que no hay nigun Auto")
            else:
                for i in range(len(recorrido1.Autos)):
                    print(f"{i+1}- {recorrido1.Autos[i].tipoAuto}")
                n7 = int(input("Tipo de Auto que va a hacer el recorrido, !!por favor elija el numero de la posicion en la que se encuentra!!: "))
                recorrido1.agregarRecorrido(recorrido1.raiz,recorrido1.Autos[n7-1])
        elif m == 8:
            print("Autos:", len(recorrido1.Autos))
            for i in range(len(recorrido1.Autos)):
                print(f"{i+1}- {recorrido1.Autos[i].tipoAuto}")
            n = int(input("Tipo de Auto que va a hacer el recorrido,!!por favor elija el numero de la posicion en la que se encuentra!!: "))
            entrada = input("Desde cual peaje esta comenzando: ")
            nodoInicio = recorrido1.buscarNodoPorLlave(entrada)
            if nodoInicio:
                recorrido1.agregarRecorrido1(nodoInicio,recorrido1.Autos[n-1])
        elif m == 9:
            recorrido1.pagoPeaje(recorrido1.raiz)
        elif m == 10:
            for x in range(len(recorrido1.Autos)):
                auto = recorrido1.Autos[x]
                print(f"---------------------------------------------------------------------")
                print(f"el Auto {auto.tipoAuto} pagó: {recorrido1.pagoAutos(auto.valorPagos,0)}$")
                print("-----------------------------------------------------------------------")
        elif m == 11:
            mayor = recorrido1.autoMayorPago(recorrido1.Autos)
            print(f"el auto que mas pago fue: {mayor.tipoAuto}, {recorrido1.pagoAutos(mayor.valorPagos, 0)}$, En {len(mayor.valorPagos)} peajes")
        elif m == 12:
            menor = recorrido1.autoMenorPago(recorrido1.Autos)
            print(f"el auto que menos pago fue: {menor.tipoAuto}, {recorrido1.pagoAutos(menor.valorPagos, 0)}$, En {len(menor.valorPagos)} peajes")
        elif m == 13:
            mayorP = recorrido1.PeajeMasRecorrido(recorrido1.raiz, 0)
            print(f"el peaje mas transitado fue: {mayorP.nombre}, {len(mayorP.autosPeajes)} autos transitaron este peaje")
        elif m == 14:
            menorP = recorrido1.PeajeMenosRecorrido(recorrido1.raiz, 0)
            print(f"el peaje menos transitado fue: {menorP.nombre}, {len(menorP.autosPeajes)} autos transitaron este peaje")
        elif m == 15:
            print(f"El total recolectado en todo el arbol es de: {recorrido1.totalArbol(recorrido1.raiz,0)}")

        elif m == 16:
            print("BOLETIN")
            mayorP=0
            if recorrido1.Autos:
                mayorP = recorrido1.autoMayorPago(recorrido1.Autos)
                if mayorP !=0:
                    print(f"el auto que mas pago fue: {mayorP.tipoAuto}, {recorrido1.pagoAutos(mayorP.valorPagos, 0)}$, En {len(mayorP.valorPagos)} peajes")
                    print("------------------------------------------------------------------------------------------------------------------")
                    menor1 = recorrido1.autoMenorPago(recorrido1.Autos)
                    print(f"el auto que menos pago fue: {menor1.tipoAuto}, {recorrido1.pagoAutos(menor1.valorPagos, 0)}$, En {len(menor1.valorPagos)} peajes")
                    print("------------------------------------------------------------------------------------------------------------------")
                    mayor1 = recorrido1.autoMayorPago(recorrido1.Autos)
                    print(f"el auto que mas peajes recorrio fue: {mayor1.tipoAuto}, En {len(mayor1.valorPagos)} peajes")
        elif m == 17:
            retorno=False
