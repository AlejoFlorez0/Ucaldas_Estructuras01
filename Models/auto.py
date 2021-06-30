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

