class Deportista():
    #constructor
    def __init__(self,deporte,añosPracticando):
        self._deporte=deporte#(String)
        self._añosPracticando=añosPracticando#(Int)

    #getter & setter
    def getDeporte(self):
        return self._deporte
    def setDeporte(self,deporte):
        self._deporte=deporte

    def getAñosPracticando(self):
        return self._añosPracticando
    def setAñosPracticando(self,añosPracticando):
        self._añosPracticando=añosPracticando