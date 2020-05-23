class Coche:
    def __init__(self):
        self.codigo = 0
        self.marca = ''
        self.lugar_recogida = ''
        self.nDias_reserva = 0
        self.precio = 0

    def crear_coche(self, cod, mar, lr, dias, precio):
        self.codigo = cod
        self.marca = mar
        self.lugar_recogida = lr
        self.nDias_reserva = dias
        self.precio = precio

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codi):
        self.codigo = codi

    def get_precio(self):
        return self.precio

    def set_precio(self, preu):
        self.precio = preu

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_dias_reserva(self):
        return self.nDias_reserva

    def set_dias_reserva(self, dias):
        self.nDias_reserva = dias

    def get_lugar_recogida(self):
        return self.lugar_recogida

    def set_lugar_recogida(self, lr):
        self.lugar_recogida = lr
