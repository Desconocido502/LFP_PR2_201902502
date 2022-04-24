class Partido():
    def __init__(self, fecha, temporada, jornada, equipoLocal, equipoVisitante, golesLocal, golesVisitante):
        self.fecha = fecha
        self.temporada = temporada
        self.jornada = jornada
        self.equipoLocal = equipoLocal
        self.equipoVisitante = equipoVisitante
        self.golesLocal = golesLocal
        self.golesVisitante = golesVisitante
    
    def getFecha(self):
        return self.fecha
    
    def getTemporada(self):
        return self.temporada
    
    def getJornada(self):
        return self.jornada
    
    def getEquipoLocal(self):
        return self.equipoLocal
    
    def getEquipoVisitante(self):
        return self.equipoVisitante
    
    def getGolesLocal(self):
        return self.golesLocal
    
    def getGolesVisitante(self):
        return self.golesVisitante
    
    def __str__(self):
        return f"""Fecha: {self.fecha}, Temporada: {self.temporada}, Jornada: {self.jornada}, Equipo Local: {self.equipoLocal}, 
Equipo Visitante: {self.equipoVisitante}, Goles Local: {self.golesLocal}, Goles Visitante : {self.golesVisitante}
"""