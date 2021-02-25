from vehiculo import Vehiculo

class Moto(Vehiculo):
    __cilindrada = 0

    def __init__(self, marca, modelo, precio, cilindrada):
        Vehiculo.__init__(self, marca, modelo, precio)
        self.__cilindrada = cilindrada

    def get_cilindrada(self):
        return self.__cilindrada

    def set_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def __str__(self):
        return f"Marca: {self.get_marca()} // Modelo: {self.get_modelo()} // Puertas: {self.get_cilindrada()} // Precio: ${'{:,.2f}'.format(self.get_precio()).replace(',','~').replace('.',',').replace('~','.')}"

    def __gt__(self, moto):
        return (self.get_precio() > moto.get_precio())
    
    def esLujo(self):
        if int(self.__cilindrada[:3]) >= 150:
            return True
        else:
            return False