from auto import Auto

class AutoElectrico(Auto):
    __voltaje = ""

    def __init__(self, marca, modelo, precio, puertas, voltaje):
        Auto.__init__(self, marca, modelo, precio, puertas)
        self.__voltaje = voltaje

    def get_voltaje(self):
        return self.__voltaje

    def set_voltaje(self, voltaje):
        self.__voltaje = voltaje

    def __str__(self):
        return f"Marca: {self.get_marca()} // Modelo: {self.get_modelo()} // Puertas: {self.get_puertas()} // Precio: ${'{:,.2f}'.format(self.get_precio()).replace(',','~').replace('.',',').replace('~','.')} // Voltaje: {self.get_voltaje()}"

    def __gt__(self, auto):
        return (self.get_precio() > auto.get_precio())
    
    def esLujo(self):
        if int(self.get_voltaje()[:3]) >= 240:
            return True
        else:
            return False