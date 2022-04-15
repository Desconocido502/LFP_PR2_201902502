from Token import Token
from Error import Error

class AnalizadorLexico():
    
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
    
    #* Se tendran que pasar el numero de linea, 
    def analizarEntrada(self, entrada, linea):
        # * Se genera el analisis general del archivo de entrada
        buffer = ""  # *Alamacenara de forma un caracter o una cadena de caracteres
        centinela = "#"  # * Nos ayuda a saber cuando es EOF (End OF File)
        entrada += centinela  # * Se agrega el centinela a la entrada
        columna = 1  # * Servira para saber en que columna se encuentra el caracter del archivo
        print(entrada)
        
        # * Estados
        estado = 0  # * Nos servira para saber en que estado nos encontramos y a que estado vamos

        # * Indice -> nos servira para recorrer en la cadena de entrada, caracter por caracter
        index = 0
        
        # * Vamos a recorrer todo el archivo de entrada
        while index < len(entrada):
            if index == 1 and entrada[index] == centinela: #* En caso de que en la cadena solo venga el centinela --> #
                return False
            if estado == 0:
                #*Guion bajo
                if (entrada[index] == "-"):
                    index -= 1 #* Se retrocede una posicion, para que en el siguiente estado sea aceptado
                    estado = 1
                #*Palabras reservadas --> Estas van todas en mayusculas ya que no es lo mismo TEMPORADA que temporada
                elif(is_letter(entrada[index])):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    estado = 2  # * Se cambia el estado en caso de ser necesario
                #*Numeros enteros
                elif(is_number(entrada[index])):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    estado = 3  # * Se cambia el estado en caso de ser necesario
                #*Signos
                elif (entrada[index] == "<"):
                    index -= 1 #* Se retrocede una posicion, para que en el siguiente estado sea aceptado
                    estado = 4
                elif (entrada[index] == ">"):
                    index -= 1 #* Se retrocede una posicion, para que en el siguiente estado sea aceptado
                    estado = 4
                #*Identificadores
                elif (is_letter2(entrada[index])):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    estado = 5  # * Se cambia el estado en caso de ser necesario
                #*Cadenas
                elif entrada[index] == '"':
                    columna += 1
                    buffer += entrada[index]
                    estado = 6
                # * espacios y tabs
                elif entrada[index] == " " or entrada[index] == "\t":
                    columna += 1
                    estado = 0
                # * centinela
                elif(entrada[index] == centinela):
                    columna += 1
                    buffer += entrada[index]
                    if index == (len(entrada)-1):
                        token = Token("<<EOF>>", buffer, linea, columna)
                        self.listaTokens.append(token)
                        print("Analisis Lexico completado con exito")
                    else:
                        error = Error("Error Lexico", buffer, linea, columna)
                        self.listaErrores.append(error)
                    buffer = ""
                    estado = 0
                # * errores
                else:
                    columna += 1
                    buffer += entrada[index]
                    error = Error("Error lexico", buffer, linea, columna)
                    self.listaErrores.append(error)
                    buffer = ""
                    estado = 0
            elif estado == 1:
                #* Guion
                if (entrada[index] == "-" and is_number(entrada[index+1])):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    token = Token("GUION", buffer, linea, columna) #* Se crea el token
                    self.listaTokens.append(token)
                    buffer = ""  # * Se limpia el buffer
                    estado = 0  # * Se cambia el estado en caso de ser necesario
                    #print(entrada[index])
                #* Banderas
                elif (entrada[index] == "-" and entrada[index+1] == "f"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4
                elif (entrada[index] == "-" and entrada[index+1] == "n"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                elif (entrada[index] == "-" and entrada[index+1] == "j"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 7  # * Se cambia el estado en caso de ser necesario
            elif estado == 2:
                if is_letter(entrada[index]):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    estado = 2  # * Se cambia el estado en caso de ser necesario
                else:
                    # *Se hace una validacion por cada palabra reservada (total:13)
                    if buffer == "RESULTADO":
                        token = Token("RESULTADO", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "VS":
                        token = Token("VS", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "TEMPORADA":
                        token = Token("TEMPORADA", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "JORNADA":
                        token = Token("JORNADA", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "GOLES":
                        token = Token("GOLES", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "LOCAL":
                        token = Token("LOCAL", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "VISITANTE":
                        token = Token("VISITANTE", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "TOTAL":
                        token = Token("TOTAL", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "TABLA":
                        token = Token("TABLA", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "TOP":
                        token = Token("TOP", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "SUPERIOR":
                        token = Token("SUPERIOR", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "INFERIOR":
                        token = Token("INFERIOR", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "ADIOS":
                        token = Token("ADIOS", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif buffer == "PARTIDOS":
                        token = Token("PARTIDOS", buffer, linea, columna)
                        self.listaTokens.append(token)
                    else:
                        error = Error("Error léxico",buffer, linea, columna)
                        self.listaErrores.append(error)
                    buffer = "" #*Se limpia el buffer
                    index -= 1  # *Retroceso de indice
                    estado = 0  # * Retornamos al estado inicial
            elif estado == 3:
                if is_number(entrada[index]):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    estado = 3  # * Se cambia el estado en caso de ser necesario
                else:
                    token = Token("ENTERO", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = "" #*Se limpia el buffer
                    index -= 1  # *Retroceso de indice
                    estado = 0  # * Retornamos al estado inicial
            elif estado == 4:
                #*BANDERAS
                #*Bandera -f y -jf
                if (entrada[index] == "f"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                #*Bandera -n
                elif (entrada[index] == "n"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                #*Bandera -ji
                elif (entrada[index] == "i"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                #* Signos
                elif(entrada[index] == "<"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                elif(entrada[index] == ">"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                elif(entrada[index] == '"'):
                    columna += 1
                    buffer += entrada[index]
                    token = Token("CADENA", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                else:
                    #* Se validan las banderas
                    if (buffer == "-f"):
                        #print(buffer)
                        token = Token("BANDERAEXPORTAR", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif (buffer == "-n"):
                        #print(buffer)
                        token = Token("BANDERATOP", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif (buffer == "-ji"):
                        #print(buffer)
                        token = Token("BANDERAINICIAL", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif (buffer == "-jf"):
                        #print(buffer)
                        token = Token("BANDERAFINAL", buffer, linea, columna)
                        self.listaTokens.append(token)
                    #* Se validan los signos
                    elif (buffer == "<"):
                        #print(buffer)
                        token = Token("MENORQUE", buffer, linea, columna)
                        self.listaTokens.append(token)
                    elif (buffer == ">"):
                        #print(buffer)
                        token = Token("MAYORQUE", buffer, linea, columna)
                        self.listaTokens.append(token)
                    else:
                        error = Error("Error lexico",buffer, linea, columna)
                        self.listaErrores.append(error)
                    buffer = ""
                    index-=1
                    estado = 0
            elif estado == 5:
                if is_identifier(entrada[index]):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index]  # * Agregar caracter al buffer
                    estado = 5  # * Se cambia el estado en caso de ser necesario
                else:
                    token = Token("IDENTIFICADOR", buffer, linea, columna)
                    self.listaTokens.append(token)
                    buffer = ""
                    index -= 1 
                    estado = 0
            elif estado == 6:
                if entrada[index] == '"':
                    index -= 1
                    estado = 4
                else:
                    columna += 1
                    buffer += entrada[index]
                    estado = 6
            elif estado == 7:
                #*BANDERAS 
                if (entrada[index] == "j" and entrada[index+1] == "i"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
                if (entrada[index] == "j" and entrada[index+1] == "f"):
                    columna += 1  # * Se suma uno a la columna
                    buffer += entrada[index] # * Agregar caracter al buffer
                    estado = 4  # * Se cambia el estado en caso de ser necesario
            index += 1
            
            #token = Token("BANDERAEXPORTAR", buffer, linea, columna)
    
    def imprimirDatos(self):
        print("\n\n\n")
        print("********************* Lista Tokens")
        for token in self.listaTokens:
            print(token.getInfo())
        print("\n\n\n")
        print("********************* Lista Errores")
        for error in self.listaErrores:
            print(error.getInfo())

    #*Se dejo a las palabras reservadas del lenguaje con mayusculas, por tanto solo se evaluan las mayusculas y no las minusculas
    #*ya que la combinacion de ambas es para los identificadores.
def is_letter (caracter):
    mayusculas =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú"]
    
    if caracter in mayusculas:
        return True
    else:
        return False
    
def is_letter2 (caracter):
    mayusculas =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú"]
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
    mayusculas =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","Á","É","Í","Ó","Ú"]
    minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú"]
    guionbajo =["_"]

    if caracter in numeros or caracter in mayusculas or caracter in minusculas or caracter in guionbajo:
        return True
    else:
        return False

"""
        RESULTADO "Real Madrid" vs "Villareal" TEMPORADA <2019-2020>
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
cadena = 'PARTIDOS "Real Madrid" TEMPORADA <1999-2000> -f reporteEspanol -ji 1 -jf 18'
analisis_cadena = AnalizadorLexico()
analisis_cadena.analizarEntrada(cadena, 1)
analisis_cadena.imprimirDatos()