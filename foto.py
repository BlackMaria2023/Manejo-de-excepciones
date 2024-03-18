from error import DimensionError

class Foto:
    MAX = 100

    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, value):
        if value < 1 or value > self.MAX:
            raise DimensionError("El valor del alto está fuera de rango.", dimension="Alto", maximo=self.MAX)
        else:
            self._alto = value

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, value):
        if value < 1 or value > self.MAX:
            raise DimensionError("El valor del ancho está fuera de rango.", dimension="Ancho", maximo=self.MAX)
        else:
            self.__ancho = value