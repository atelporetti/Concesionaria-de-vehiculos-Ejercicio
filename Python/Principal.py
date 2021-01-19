class Vehiculo():
    marca = ''
    modelo = ''
    precio = 0

    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def agregaVehiculo(self):
        vehiculos = []

    def __str__(self):
        return f'Marca: {self.marca} // Modelo: {self.modelo} // Precio: ${self.precio}'

    def esLujo(self):
        pass

class Auto(Vehiculo):
    puertas = 0

    def __init__(self, marca, modelo, precio, puertas):
        Vehiculo.__init__(self, marca, modelo, precio)
        self.puertas = puertas

    def __str__(self):
        return f"Marca: {self.marca} // Modelo: {self.modelo} // Puertas: {self.puertas} // Precio: ${'{:,.2f}'.format(self.precio).replace(',','~').replace('.',',').replace('~','.')}"

    def __gt__(self, auto):
        return (self.precio > auto.precio)

class AutoElectrico(Auto):
    voltaje = ""

    def __init__(self, marca, modelo, precio, puertas, voltaje):
        Auto.__init__(self, marca, modelo, precio, puertas)
        self.voltaje = voltaje

    def __str__(self):
        return f"Marca: {self.marca} // Modelo: {self.modelo} // Puertas: {self.puertas} // Precio: ${'{:,.2f}'.format(self.precio).replace(',','~').replace('.',',').replace('~','.')} // Voltaje: {self.voltaje}"

    def __gt__(self, auto):
        return (self.precio > auto.precio)
    
    def esLujo(self):
        if int(self.voltaje[:3]) >= 240:
            return True
        else:
            return False

class Moto(Vehiculo):
    cilindrada = 0

    def __init__(self, marca, modelo, precio, cilindrada):
        Vehiculo.__init__(self, marca, modelo, precio)
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.marca} // Modelo: {self.modelo} // Puertas: {self.cilindrada} // Precio: ${'{:,.2f}'.format(self.precio).replace(',','~').replace('.',',').replace('~','.')}"

    def __gt__(self, moto):
        return (self.precio > moto.precio)
    
    def esLujo(self):
        if int(self.cilindrada[:3]) >= 150:
            return True
        else:
            return False

def contiene_letra(vehiculos):
    for vehiculo in vehiculos:
        if('Y' in vehiculo.modelo):
            print(
                f"Vehículo que contiene en el modelo la letra 'Y': {vehiculo.marca} {vehiculo.modelo} ${'{:,.2f}'.format(vehiculo.precio).replace(',','~').replace('.',',').replace('~','.')}")

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
        f'Vehículo más caro: {(max(vehiculos)).marca} {(max(vehiculos)).modelo}')
    print(
        f'Vehículo más barato: {(min(vehiculos)).marca} {(min(vehiculos)).modelo}')
    contiene_letra(vehiculos)
    print('=============================')


def imprime_vehiculos_ordenados_precio(vehiculos):
    vehiculos.sort(reverse=True)
    print('Vehículos ordenados por precio de mayor a menor:')
    for vehiculo in vehiculos:
        print(f'{vehiculo.marca} {vehiculo.modelo}')
    print('=============================')

def imprime_vehiculos_lujo(vehiculos):
    print('Vehiculos de lujo:')
    for vehiculo in vehiculos:
        if vehiculo.esLujo():
            print(f'{vehiculo.marca} {vehiculo.modelo}')

###############################################################################################################
###############################################################################################################


vehiculos = carga_vehiculos()
imprime_vehiculos(vehiculos)
imprime_vehiculo_caro_barato(vehiculos)
imprime_vehiculos_ordenados_precio(vehiculos)
imprime_vehiculos_lujo(vehiculos)
