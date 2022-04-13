class Error():
    def __init__(self, tipo, lexema, linea, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
    
    def getTipo(self):
        return self.tipo
    
    def getLexema(self):
        return self.lexema
    
    def getLinea(self):
        return self.linea
    
    def getColumna(self):
        return self.columna
    
    def getInfo(self):
        print("**** **** ****")
        info = f""" 
        Tipo: {self.tipo}, Lexema: {self.lexema}, Linea: {self.linea}, Columna: {self.columna}
        """