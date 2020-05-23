class Factura:

    def __init__(self, dictDestinos = dict(), num_pasajeros=0):

        self.num_pasajeros = num_pasajeros
        self.dictDestinos = dictDestinos


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
