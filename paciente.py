class Paciente:
    def __init__(self, codigo, nombre, edad):
        self._codigo=codigo
        self._nombre=nombre
        self._edad=edad

    #Getters
    @property
    def codigo(self):
        return self._codigo
    @property
    def nombre(self):
        return self._nombre
    @property
    def edad(self):
        return self._edad
    

    #Setters
    @codigo.setter
    def codigo(self,codigo):
        self._codigo = codigo
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    @edad.setter
    def edad(self,edad):
        self._edad = edad


    def resumen(self):
        return f"{self._codigo}-{self._nombre}-{self._edad}"