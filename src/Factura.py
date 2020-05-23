class Factura:

    def __init__(self, num_pasajeros=0,  dictDestinos = dict(), dictVehiculos={} ):

        self.num_pasajeros = num_pasajeros
        self.dictDestinos = dictDestinos
        self.dictVehiculo = dictVehiculos


    def set_num_pasajeros(self, num_pasajeros):
        self.num_pasajeros = num_pasajeros

    def add_destino(self, destino, importe):


        self.dictDestinos[str(destino)] = importe

    def eliminar_destino(self, destino):
        del self.dictDestinos[destino]

    def get_total(self):
        total = 0
        for importe in self.dictDestinos.values():
            total = total + (importe * self.num_pasajeros)

        return total
