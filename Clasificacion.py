from Equipo import Equipo
from Equipo import DatosEstadisticos

class Clasificacion():
    def __init__(self, temporada):
        self.temporada = temporada
        self.lista_equipos = []
    
    def getListaEquipos(self):
        return self.lista_equipos
    
    def setListaEquipos(self, lista_equipos):
        self.lista_equipos = lista_equipos
        
    def mostrarListaEquipos(self):
        for equipo in self.lista_equipos:
            print(equipo)
            print("----------------------------------------------------------------------------\n")
    
    #*Ordena los datos de la lista segun los puntos de mayor a menor cantidad de pts
    def bubble_sort_equipos(self):
        lista = self.getListaEquipos()
        
        for lts in lista:
            lts.calcular_pts_local()
            lts.calcular_pts_visitante()
        
        count = len(lista)
        #print(lista[0].datos_local.getPJ())
        for i in range(0, count):
            for j in range(i+1, count):
                if (lista[i].pts_total() < lista[j].pts_total()):
                    #print(lista[i].getTotalPts())
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
        self.setListaEquipos(lista)
        #print("Equipos ordenados por el total de pts (Global)")

# realMadrid = Equipo("Real Madrid")
# realMadrid.datos_local.setPJ(16)
# realMadrid.datos_local.setPG(11)
# realMadrid.datos_local.setPE(4)
# realMadrid.datos_local.setPP(1)
# realMadrid.datos_local.setGF(34)
# realMadrid.datos_local.setGC(13)

# realMadrid.datos_visitante.setPJ(17)
# realMadrid.datos_visitante.setPG(13)
# realMadrid.datos_visitante.setPE(2)
# realMadrid.datos_visitante.setPP(2)
# realMadrid.datos_visitante.setGF(35)
# realMadrid.datos_visitante.setGC(16)


# villaRreal = Equipo("Villarreal")
# villaRreal.datos_local.setPJ(17)
# villaRreal.datos_local.setPG(10)
# villaRreal.datos_local.setPE(5)
# villaRreal.datos_local.setPP(2)
# villaRreal.datos_local.setGF(38)
# villaRreal.datos_local.setGC(15)

# villaRreal.datos_visitante.setPJ(16)
# villaRreal.datos_visitante.setPG(4)
# villaRreal.datos_visitante.setPE(5)
# villaRreal.datos_visitante.setPP(7)
# villaRreal.datos_visitante.setGF(15)
# villaRreal.datos_visitante.setGC(16)


# sevilla = Equipo("Sevilla")
# sevilla.datos_local.setPJ(16)
# sevilla.datos_local.setPG(11)
# sevilla.datos_local.setPE(4)
# sevilla.datos_local.setPP(1)
# sevilla.datos_local.setGF(34)
# sevilla.datos_local.setGC(16)

# sevilla.datos_visitante.setPJ(17)
# sevilla.datos_visitante.setPG(6)
# sevilla.datos_visitante.setPE(8)
# sevilla.datos_visitante.setPP(3)
# sevilla.datos_visitante.setGF(15)
# sevilla.datos_visitante.setGC(11)

# ligaSantander = Clasificacion("2021-2022")
# ligaSantander.lista_equipos.append(villaRreal)
# ligaSantander.lista_equipos.append(realMadrid)
# ligaSantander.lista_equipos.append(sevilla)
# ligaSantander.bubble_sort_equipos()
# ligaSantander.mostrarListaEquipos()