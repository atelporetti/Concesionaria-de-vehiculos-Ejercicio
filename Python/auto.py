from vehiculo import Vehiculo

class Auto(Vehiculo):
    __puertas = 0

    def __init__(self, marca, modelo, precio, puertas):
        Vehiculo.__init__(self, marca, modelo, precio)
        self.__puertas = puertas

    def get_puertas(self):
        return self.__puertas

    def set_puertas(self, puertas):
        self.__puertas = puertas

    def __str__(self):
        return f"Marca: {self.get_marca()} // Modelo: {self.get_modelo()} // Puertas: {self.get_puertas()} // Precio: ${'{:,.2f}'.format(self.get_precio()).replace(',','~').replace('.',',').replace('~','.')}"

    def __gt__(self, auto):
        return (self.get_precio() > auto.get_precio())