class Vehiculo():
    __marca = ''
    __modelo = ''
    __precio = 0

    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def agregaVehiculo(self):
        vehiculos = []

    def __str__(self):
        return f'Marca: {self.get_marca()} // Modelo: {self.get_modelo()} // Precio: ${self.get_precio()}'

    def esLujo(self):
        pass
