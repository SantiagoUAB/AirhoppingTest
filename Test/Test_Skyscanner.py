import unittest
from unittest.mock import patch

from src.User import User
from src.Flights import Flights
from src.Skyscanner import Skyscanner
from src.PaymentData import PaymentData
from src.Factura import Factura


# from src.User import User
# from src.Flights import Flights
# from src.Skyscanner import Skyscanner


nombres = ["Ana", "Bernardo", "Ramirez"]
apellidos = ["Hurtado Hurtado", "Chaves Chaves", "Mateos"]
DNI = ["08075225V", "02604904Q", "03897631M"]

numTarjeta = 5581238443939998
cvv = 117  # codigo seguridad tarjeta
costeViaje = 0

datosPago = PaymentData("VISA", nombres[0], numTarjeta, cvv, costeViaje)

# user2 = User(nombres[1], apellidos[1], DNI[1] )
# user3 = User(nombres[2], apellidos[2], DNI[2] )

lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
lCodigo_vuelos = [741, 852, 963]
num_pasajeros = 3


def Test_Viaje_Numero_pasajeros():
    lVuelos = Flights(num_pasajeros = 3)

    assert lVuelos.get_num_pasajeros() == 3  # numero de paajeros esperados
    print("Test_Viaje_Numero_pasajeros ok")


def Test_Viase_Sin_Destinos():

    lVuelos = Flights()
    assert lVuelos.existen_Destinos() == False
    print("Test_Viase_Sin_Destinos ok")


def Test_Viase_Sin_Vuelos():

    lVuelos = Flights()

    assert lVuelos.existen_Vuelos() == False
    print("Test_Viase_Sin_Vuelos ok")


def Test_Viaje_Precio_Cero():
    datosPago = PaymentData()

    assert datosPago.get_importe() == 0  # coste de viaje 0
    print("Test_Viaje_Precio_Cero ok")


def Test_destinos_esperados():

    lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
    lVuelos = Flights(lDestiancions=lDestinacion_vuelos)

    assert lVuelos.get_destinos() == lDestinacion_vuelos
    print("Test_destinos_esperados ok")


def Test_vuelos_esperados():

    lCodigo_vuelos = [741, 852, 963]
    lVuelos = Flights(lCodigos=lCodigo_vuelos)

    assert lVuelos.get_vuelos() == lCodigo_vuelos
    print("Test_vuelos_esperados ok ")


def test_precio_cero():

    importe = 0
    datosPago = PaymentData(importe=importe)

    assert datosPago.datosPago.get_importe() == 0  # coste de viaje 0
    print("Test_Viaje_Precio_Cero ok")


def Test_precio_viaje_esperado() -> None:

    importe = 0
    num_pasajeros = 3
    datosPago = PaymentData("VISA", nombres[0], numTarjeta, cvv, importe)

    lPrecios = [30, 30, 30]
    for precioDestino in lPrecios:
        datosPago.add_importe(precioDestino * num_pasajeros)
    importeEsperado = sum(lPrecios) * num_pasajeros

    assert datosPago.get_importe() == importeEsperado
    print("Test_precio_viaje_esperado ok")


def Test_precio_viaje_esperado_nuevos_destinos() -> None:
    importe = 0
    num_pasajeros = 3
    datosPago = PaymentData("VISA", nombres[0], numTarjeta, cvv, importe)

    lPrecios = [30, 30, 30]
    # se sumna el coste de cada destino en funcion del numero de pasajeos
    for precioDestino in lPrecios:
        datosPago.add_importe(precioDestino * num_pasajeros)

    # se suman 2 nuevos destinos
    datosPago.add_importe(30 * num_pasajeros)
    datosPago.add_importe(30 * num_pasajeros)

    lPrecios.append(30)
    lPrecios.append(30)

    importeEsperado = sum(lPrecios) * num_pasajeros

    assert datosPago.get_importe() == importeEsperado
    print("Test_precio_viaje_esperado_nuevos_destinos ok")


def Test_viaje_eliminar_destinos() -> None:
    lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]

    num_pasajeros = 3

    lVuelos = Flights()
    lVuelos.set_num_pasajeros(num_pasajeros)

    for destino in lDestinacion_vuelos:
        lVuelos.add_destino(destino)


    # eliminar de listado de vuelos
    lVuelos.eliminar_destino("Metropolis")
    lVuelos.eliminar_destino("Dinamarcia")

    # resultado esperado
    lDestinacion_vuelos.remove("Metropolis")
    lDestinacion_vuelos.remove("Dinamarcia")

    assert lDestinacion_vuelos == lVuelos.get_destinos()

    print("Test_viaje_eliminar_destinos ok")


def Test_viaje_eliminar_vuelos() -> None:
    lCodigo_vuelos = [741, 852, 963]

    num_pasajeros = 3

    lVuelos = Flights()
    lVuelos.set_num_pasajeros(num_pasajeros)

    for vuelo in lCodigo_vuelos:
        lVuelos.add_vuelo(vuelo)

    # eliminar de listado de vuelos
    lVuelos.eliminar_vuelo(lCodigo_vuelos[0])
    lVuelos.eliminar_vuelo(lCodigo_vuelos[1])

    # resultado esperado
    lCodigo_vuelos.remove(741)
    lCodigo_vuelos.remove(852)

    assert lCodigo_vuelos == lVuelos.get_vuelos()

    print("Test_viaje_eliminar_vuelos ok")


def Test_precio_viaje_esperado_eliminar_destinos() -> None: #volveremos

    num_pasajeros = 3
    lPrecios = [30, 30, 30]
    lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
    factura = Factura()

    factura.set_num_pasajeros(num_pasajeros)

    for destino, precio in zip(lDestinacion_vuelos, lPrecios):
        factura.add_destino(destino, precio)

    # se descuetnan 2 destinos
    lPrecios = [30, 0, 0]
    importeEsperado = sum(lPrecios) * num_pasajeros

    factura.eliminar_destino("Dinamarcia")
    factura.eliminar_destino("Suecia")

    assert factura.get_total() == importeEsperado

    print("Test_precio_viaje_esperado_eliminar_destinos")


def Test_pago_correcto() -> None:
    user1 = User(nombres[0], apellidos[0], DNI[0])

    lDestinacion_vuelos = ["Metropolis", "Dinamarcia", "Suecia"]
    lCodigo_vuelos = [741, 852, 963]


    lVuelos = Flights(lCodigo_vuelos, lDestinacion_vuelos, 3)

    interfazSkyscanner = Skyscanner()

    assert interfazSkyscanner.confirm_reserve(user1, lVuelos) == True


def Test_conrimrar_reserva_error():


    with patch('src.Skyscanner') as mock_get:
        mock_get.confirm_reserve.return_value = False
    assert mock_get.confirm_reserve() == False
    print("Test_conrimrar_reserva_error")


Test_Viaje_Numero_pasajeros()
Test_Viase_Sin_Destinos()
Test_Viase_Sin_Vuelos()
Test_Viaje_Precio_Cero()
Test_destinos_esperados()
Test_vuelos_esperados()
Test_precio_viaje_esperado()
Test_precio_viaje_esperado_nuevos_destinos()
Test_viaje_eliminar_destinos()
Test_viaje_eliminar_vuelos()
Test_precio_viaje_esperado_eliminar_destinos()

Test_pago_correcto()
Test_conrimrar_reserva_error()

print("ok")
