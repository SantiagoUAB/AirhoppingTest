class PaymentData:

    def __init__(self, tipo_tarjeta, nombre_titular, num_tarjeta, codigo_seguridad, importe):
        self.tipo_tarjeta = tipo_tarjeta
        self.nombre_titular = nombre_titular
        self.num_tarjeta  = num_tarjeta
        self.codigo_seguridad = codigo_seguridad
        self.importe = importe