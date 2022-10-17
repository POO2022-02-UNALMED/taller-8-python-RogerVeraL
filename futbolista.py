from persona import Persona
from deportista import Deportista

class Futbolista(Persona,Deportista):
    listaFutbolistas=list()
    #constructor
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados=golesMarcados#(Int)
        self._tarjetasRojas=tarjetasRojas#(Int)
        self._piernaHabil=piernaHabil#(String)
        Futbolista.listaFutbolistas.append(self)
    
    #getter & setter
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,golesMarcados):
        self._golesMarcados=golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,piernaHabil):
        self._piernaHabil=piernaHabil

    #metodos
    def __str__(self):
        cad = f"Mi nombre es {Persona.getNombre()} soy profesional en el deporte {Deportista.getDeporte()} Tengo {Persona.getEdad()} años de edad y llevo {Deportista.getAñosPracticando()} años en el deporte"
        return cad
    
