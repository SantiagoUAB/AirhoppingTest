import requests

class Cars:

    def __init__(self , codigo, marca, lugar_recogida, nDias_reserva):
        self.codigo = codigo
        self.marca = marca
        self.lugar_recogida = lugar_recogida
        self.nDias_reserva = nDias_reserva


        pass

    @staticmethod
    def download_seat_leon_specifications():
        r = requests.get('http://localhost/dummy_url')
        if r.status_code == 200:
            return r.json()
        return None