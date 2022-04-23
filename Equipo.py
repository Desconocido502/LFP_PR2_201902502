class Equipo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.pts_local = 0
        self.pts_visitante = 0
        self.total_pts = 0
        self.datos_local = DatosEstadisticos()
        self.datos_visitante = DatosEstadisticos()

    def getTotalPts(self):
        return self.total_pts
    
    #*Metodo para calcular todos los partidos jugados
    def pj_total(self):
        total_partidos = self.pg_total() + self.pe_total() + self.pp_total()
        return total_partidos
    
    #*Metodo para calcular todos los partidos ganados
    def pg_total(self):
        total_pg = self.datos_local.getPG() + self.datos_visitante.getPG()
        return total_pg
    
    #*Metodo para calcular todos los partidos empatados
    def pe_total(self):
        total_pe = self.datos_local.getPE() + self.datos_visitante.getPE()
        return total_pe
    
    #*Metodo para calcular todos los partidos perdidos
    def pp_total(self):
        total_pp = self.datos_local.getPP() + self.datos_visitante.getPP()
        return total_pp
    
    #*Metodo para calcular todos los goles a favor
    def gf_total(self):
        total_goles_a_favor = self.datos_local.getGF() + self.datos_visitante.getGF()
        return total_goles_a_favor
    
    #*Metodo para calcular todos los goles en contra
    def gc_total(self):
        total_goles_en_contra = self.datos_local.getGC() + self.datos_visitante.getGC()
        return total_goles_en_contra
    
    #*Metodo para calcular todos los puntos en total
    def pts_total(self):
        total_pts = self.calcular_pts_local() + self.calcular_pts_visitante()
        return total_pts
    
    #*Metodo para calculor los puntos local
    def calcular_pts_local(self):
        self.pts_local = (self.datos_local.getPG()*3) + (self.datos_local.getPE()*1) #*+ los PP pero no le da puntos
        return  self.pts_local
    
    #*Metodo para calculor los puntos visitante
    def calcular_pts_visitante(self):
        self.pts_visitante = (self.datos_visitante.getPG()*3)  + (self.datos_visitante.getPE()*1) #* + los PP pero no le da puntos
        return self.pts_visitante
    
    def __str__(self):
        return f"Nombre: {self.nombre}, \nLocal: {self.datos_local}\nVisitante:{self.datos_visitante}"
    

class DatosEstadisticos():
    def __init__(self):
        self.PJ = 0
        self.PG = 0
        self.PE = 0
        self.PP = 0
        self.GF = 0
        self.GC = 0
    
    #* Metodos setters y Getters de los datos estadisticos
    def setPJ(self, PJ):
        self.PJ = PJ
    
    def getPJ(self):
        return self.PJ
    
    def setPG(self, PG):
        self.PG = PG
    
    def getPG(self):
        return self.PG
    
    def setPE(self, PE):
        self.PE = PE
    
    def getPE(self):
        return self.PE
    
    def setPP(self, PP):
        self.PP = PP
    
    def getPP(self):
        return self.PP
    
    def setGF(self, GF):
        self.GF = GF
    
    def getGF(self):
        return self.GF
    
    def setGC(self, GC):
        self.GC = GC
    
    def getGC(self):
        return self.GC
    
    def __str__(self):
        return f'''Partidos Jugados: {self.PJ}, Partidos Ganados: {self.PG}, Partidos Empatados: {self.PE},
Partidos Perdidos: {self.PP}, Goles a favor: {self.GF}, Goles en contra: {self.GC}'''

# local = DatosEstadisticos()
# visitante = DatosEstadisticos()

# local.setPJ(16)
# local.setPG(11)
# local.setPE(4)
# local.setPP(1)
# local.setGF(34)
# local.setGC(13)

# print(local)

# visitante.setPJ(17)
# visitante.setPG(13)
# visitante.setPE(2)
# visitante.setPP(2)
# visitante.setGF(35)
# visitante.setGC(16)
# print(visitante)

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

# print("Puntos local:",realMadrid.calcular_pts_local())
# print("Puntos visitante:",realMadrid.calcular_pts_visitante())
# print("Total puntos:",realMadrid.pts_total())
# print("Total partidos jugados:", realMadrid.pj_total())
# print("Total partidos ganados:", realMadrid.pg_total())
# print("Total partidos empatados:", realMadrid.pe_total())
# print("Total partidos perdidos:", realMadrid.pp_total())
# print("Total goles a favor:", realMadrid.gf_total())
# print("Total goles en contra:", realMadrid.gc_total())

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

# print("Puntos local:",villaRreal.calcular_pts_local())
# print("Puntos visitante:",villaRreal.calcular_pts_visitante())
# print("Total puntos:",villaRreal.pts_total())
# print("Total partidos jugados:", villaRreal.pj_total())
# print("Total partidos ganados:", villaRreal.pg_total())
# print("Total partidos empatados:", villaRreal.pe_total())
# print("Total partidos perdidos:", villaRreal.pp_total())
# print("Total goles a favor:", villaRreal.gf_total())
# print("Total goles en contra:", villaRreal.gc_total())
# print("------------------------------------------")
# print(villaRreal)
