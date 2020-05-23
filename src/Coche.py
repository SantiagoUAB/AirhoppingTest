class Coche:
    def __init__(self, codigo=-1, marca="", lugarRecogida="", nDias_reserva=-1, precio=-1):
        self.codigo = codigo
        self.marca = marca
        self.lugar_recogida = lugarRecogida
        self.nDias_reserva = nDias_reserva
        self.precio = precio


    def get_precio(self):
        return self.precio




