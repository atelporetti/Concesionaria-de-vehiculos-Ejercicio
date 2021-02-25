from auto import Auto
from moto import Moto
from auto_electrico import AutoElectrico

def contiene_letra(vehiculos):
    for vehiculo in vehiculos:
        if('Y' in vehiculo.get_modelo()):
            print(
                f"Vehículo que contiene en el modelo la letra 'Y': {vehiculo.get_marca()} {vehiculo.get_modelo()} ${'{:,.2f}'.format(vehiculo.get_precio()).replace(',','~').replace('.',',').replace('~','.')}")

def carga_vehiculos():
    auto1 = Auto("Peugeot", "206", 200000.00, "4")
    moto1 = Moto("Honda", "Titan", 60000.00, "125cc")
    auto2 = Auto("Peugeot", "208", 250000.00, "5")
    moto2 = Moto("Yamaha", "YBR", 80500.50, "160cc")
    autoE = AutoElectrico("Toyota", "Prius", 350000.00, "5", "240V")
    vehiculos = [auto1, moto1, auto2, moto2, autoE]
    return vehiculos

def imprime_vehiculos(vehiculos):
    for vehiculo in vehiculos:
        print(vehiculo)
    print('=============================')


def imprime_vehiculo_caro_barato(vehiculos):
    print(
        f'Vehículo más caro: {(max(vehiculos)).get_marca()} {(max(vehiculos)).get_modelo()}')
    print(
        f'Vehículo más barato: {(min(vehiculos)).get_marca()} {(min(vehiculos)).get_modelo()}')
    contiene_letra(vehiculos)
    print('=============================')


def imprime_vehiculos_ordenados_precio(vehiculos):
    vehiculos.sort(reverse=True)
    print('Vehículos ordenados por precio de mayor a menor:')
    for vehiculo in vehiculos:
        print(f'{vehiculo.get_marca()} {vehiculo.get_modelo()}')
    print('=============================')

def imprime_vehiculos_lujo(vehiculos):
    print('Vehiculos de lujo:')
    for vehiculo in vehiculos:
        if vehiculo.esLujo():
            print(f'{vehiculo.get_marca()} {vehiculo.get_modelo()}')

###############################################################################################################
###############################################################################################################

if __name__ == "__main__":
    vehiculos = carga_vehiculos()
    imprime_vehiculos(vehiculos)
    imprime_vehiculo_caro_barato(vehiculos)
    imprime_vehiculos_ordenados_precio(vehiculos)
    imprime_vehiculos_lujo(vehiculos)