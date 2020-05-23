class Flights:



    def __init__(self, lCodigos=[], lDestiancions=[], num_pasajeros=0):

        self.lCodios = lCodigos
        self.lDestiancions = lDestiancions
        self.num_pasajeros = num_pasajeros

        self.dictDestinos = {}
        self.importe = 0

    def set_num_pasajeros(self, num_pasajeros: int) -> None:
        self.num_pasajeros = num_pasajeros

    def get_num_pasajeros(self) -> int:
        return self.num_pasajeros

    def add_vuelo(self, codigo_vuelo : int):
        self.lCodios.append(codigo_vuelo)

    def eliminar_vuelo(self, codigo_vuelo: int):
        self.lCodios.remove(codigo_vuelo)

    def existen_Destinos(self) -> bool:
        if len(self.lDestiancions) <= 0:
            return False # no existen destinos
        else:
            return False
    def existen_Vuelos(self) -> bool:
        if len(self.lCodios) <= 0:
            return False # no existen vuelos
        else:
            return True

    def get_destinos(self) -> list:
        return list(self.dictDestinos.keys())

    def get_vuelos(self):
        return self.lCodios

    def add_destino(self, destino, importe):

        self.dictDestinos[str(destino)] = importe

    def eliminar_destino(self, destino):
        del self.dictDestinos[destino]

    def get_total(self):
        total = 0
        for importe in self.dictDestinos.values():
            total = total + (importe * self.num_pasajeros)

        return total
