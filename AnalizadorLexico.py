from Token import Token
from Error import Error

class AnalizadorLexico():
    
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
    
    def getListaTokens(self):
        return self.listaTokens
    
    def getListaErrores(self):
        return self.listaErrores
    
    #* Se tendran que pasar el numero de linea
    def analizarEntrada(self, entrada, linea):
        self.listaErrores = []
        self.listaTokens = []
        
        #* buffer, centinela y concatenar centinela
        
        buffer = ""
        centinela = "#"
        entrada += centinela
        #print(entrada)
        
        #*Columna
        columna = 1
        
        #*Estado
        estado = 0
        
        #*Iterar caracter por caracter
        index = 0
        while index < len(entrada):
            c = entrada[index]
            if estado == 0:
                #*Signos
                if c == "<":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    token = Token("MENORQUE", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
                elif c == ">":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    token = Token("MAYORQUE", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
                #*Guion y banderas
                elif c == "-":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    estado = 1
                #*Identificadores y Palabras reservadas
                elif is_letter(c):
                    columna += 1
                    buffer += c
                    estado = 2
                #*Enteros
                elif is_number(c):
                    #* Sumar a la columna
                    #* Agregar al buffer
                    #* modificar el estado
                    columna += 1
                    buffer += c
                    estado = 4
                #*Cadenas
                elif c == "\"":
                    columna += 1
                    buffer += c
                    estado = 5
                #*Espacios y tabs
                elif c == " " or c == "\t":
                    columna += 1
                    estado = 0
                elif c == centinela:
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    if index == (len(entrada) - 1) :
                        token = Token("<<EOF>>", buffer, linea, columna)
                        self.listaTokens.append(token)
                        # print("Analisis exitoso")
                        # return self.listaTokens
                    else:
                        error = Error("Error Lexico", buffer, linea, columna)
                        self.listaErrores.append(error)
                    buffer = ""
                    estado = 0
                #*Errores
                else:
                    columna += 1
                    buffer += c
                    error = Error("Error Lexico", buffer, linea, columna)
                    self.listaErrores.append(error)
                    buffer = ''
                    estado = 0
            elif estado == 1: #*Si el caracter c es un numero quiere decir que el anterior caracter fijo era un guion
                if c == "f":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    token = Token("banderaexportar", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
                elif c == "n":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    token = Token("banderatop", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
                elif c == "j":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* modificar el estado
                    columna += 1
                    buffer += c
                    estado = 3
                #*Guion
                else:
                    #* no sumar a la columna  [ reconocer el token del buffer ]
                    #* no agregar al buffer
                    #* crear el token
                    #* agregar a la lista el token 
                    #* limpiar el buffer
                    #* retroceder el index
                    #* cambiar el estado
                    token = Token("GUION", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    index -= 1
                    estado = 0
            elif estado == 2:
                if is_identifier(c):
                    #print(c, end="")
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* modificar el estado
                    columna += 1
                    buffer += c
                    estado = 2
                else:
                    #* no sumar a la columna  [ reconocer el token del buffer ]
                    #* no agregar al buffer
                    #* obtener el tipo de token
                    #* crear el token
                    #* agregar a la lista el token 
                    #* limpiar el buffer
                    #* retrocede el index
                    #* modificar estado
                    tipoToken = ""#* Se hace una validadacion por cada palabra reservada
                    if buffer == "PARTIDOS":
                        tipoToken = "partidos"
                    elif buffer == "RESULTADO":
                        tipoToken = "resultado"
                    elif buffer == "VS":
                        tipoToken = "vs"
                    elif buffer == "TEMPORADA":
                        tipoToken = "temporada"
                    elif buffer == "JORNADA":
                        tipoToken = "jornada"
                    elif buffer == "GOLES":
                        tipoToken = "goles"
                    elif buffer == "LOCAL":
                        tipoToken = "local"
                    elif buffer == "VISITANTE":
                        tipoToken = "visitante"
                    elif buffer == "TOTAL":
                        tipoToken = "total"
                    elif buffer == "TABLA":
                        tipoToken = "tabla"
                    elif buffer == "TOP":
                        tipoToken = "top"
                    elif buffer == "SUPERIOR":
                        tipoToken = "superior"
                    elif buffer == "INFERIOR":
                        tipoToken = "inferior"
                    elif buffer == "ADIOS":
                        tipoToken = "adios"
                    else:
                        tipoToken = "IDENTIFICADOR"
                    token = Token(tipoToken, buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    index -= 1
                    estado = 0
            elif estado == 3:
                if c == "i":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    token = Token("banderainicial", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
                elif c == "f":
                    #* Sumar 1 a la columna
                    #* Agregar al buffer
                    #* Creo el token
                    #* agrego a la lista de tokens
                    #* limpiar el buffer
                    #* cambiar estado si es necesario
                    columna += 1
                    buffer += c
                    token = Token("banderafinal", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
            elif estado == 4:
                #*Digito
                if is_number(c):
                    #* Sumar a la columna
                    #* Agregar al buffer
                    #* modificar el estado
                    columna += 1
                    buffer += c
                    estado = 4
                else:
                    #* no sumar a la columna  [ reconocer el token del buffer ]
                    #* no agregar al buffer
                    #* crear el token
                    #* agregar a la lista el token 
                    #* limpiar el buffer
                    #* retroceder el index
                    #* cambiar el estado
                    token = Token("ENTERO", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    index -= 1
                    estado = 0
            elif estado == 5:
                if c == "\"":
                    columna += 1
                    buffer += c
                    token = Token("CADENA", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    estado = 0
                else:
                    columna += 1
                    buffer += c
                    estado = 5
            index += 1
    
    def imprimirDatos(self):
        print("\n\n\n")
        print("********************* Lista Tokens")
        for token in self.listaTokens:
            print(token.getInfo())
        print("\n\n\n")
        print("********************* Lista Errores")
        for error in self.listaErrores:
            print(error.getInfo())

def is_letter(caracter):
    mayusculas =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú"]
    if caracter in mayusculas or caracter in minusculas:
        return True
    else:
        return False

def is_number(caracter):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]

    if caracter in numeros:
        return True
    else:
        return False
    
def is_identifier(caracter):
    numeros = ["0","1","2","3","4","5","6","7","8","9"]
    mayusculas =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú"]
    guionbajo =["_"]

    if caracter in numeros or caracter in mayusculas or caracter in minusculas or caracter in guionbajo:
        return True
    else:
        return False

"""
    Error-> RESULTADO "Real Madrid" VS "Villareal" TEMPORADA <2019-2020> | buena --> RESULTADO "Levante" VS "Espanyol" TEMPORADA <2017-2018>
        JORNADA 1 TEMPORADA <1996-1997> -f jornada1Reporte | JORNADA 12 TEMPORADA <1996-1997>
        GOLES TOTAL "Valencia" TEMPORADA <1998-1999> | GOLES LOCAL "Zaragoza" TEMPORADA <1998-1999>
        TABLA TEMPORADA <2018-2019> | TABLA TEMPORADA <1996-1997> -f reporteGlobal1
        PARTIDOS "Real Madrid" TEMPORADA <1999-2000> -ji 1 -jf 18 | PARTIDOS "Español" TEMPORADA <1999-2000> -f reporteEspanol
        TOP SUPERIOR TEMPORADA <2000-2001> | TOP INFERIOR TEMPORADA <1999-2000> -n 3
        ADIOS
        
        generando archivo de resultados de jornada 20 temporada 2015-2016
        En la temporada 2019-2020 el Levante anoto 15 goles de local
        generando archivo de clasificacion temporada 2019-2020
"""  
# cadena = 'PARTIDOS "Real ñ Madrid" TEMPORADA <1999-2000> $ -fa2 reporteEspanol* ;ñ -ji 1 -jf 18'
# cadena2 = 'PARTIDOS "Español" TEMPORADA <1999-2000> -f reporteEspanol'
# analisis_cadena = AnalizadorLexico()
# analisis_cadena.analizarEntrada(cadena2, 1)
# analisis_cadena.imprimirDatos()