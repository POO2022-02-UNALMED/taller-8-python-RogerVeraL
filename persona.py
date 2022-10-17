class Persona():
    #constructor
    def __init__(self,nombre,edad,altura,sexo):
        self._nombre=nombre#(String)
        self._edad=edad#(Int)
        self._altura=altura#(String)
        self._sexo=sexo#(String)

    #getter & setter
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre

    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad=edad

    def getAltura(self):
        return self._altura
    def setAltura(self,altura):
        self._altura=altura

    def getSexo(self):
        return self._sexo
    def setSexo(self,sexo):
        self._sexo=sexo