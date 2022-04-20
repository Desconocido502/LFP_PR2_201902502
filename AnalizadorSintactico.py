from Error import Error
class AnalizadorSintactico():
    def __init__(self, tokens: list):
        self.listaErrores = []
        self.tokens = tokens
        self.lts_datos = [] #*Lista de datos, variara segun la gramatica en que este
    
    def getLtsDatos(self):
        return self.lts_datos
    
    def agregarError(self, tipo, lexema, linea, columna):
        error = Error(tipo, lexema, linea, columna)
        self.listaErrores.append(error)
    
    def imprimirDatos(self):
        print("\n\n\n")
        print("********************* Lista Errores Sintacticos")
        for error in self.listaErrores:
            print(error.getInfo())
    
    def sacarToken(self):
        #* Saca el primer token y lo quita de la lista
        try:
            return self.tokens.pop(0)
        except:
            return None
    
    def verToken(self):
        #* Saca el primer token mas no lo quita de la lista, solo se muestra
        try:
            return self.tokens[0]
        except:
            return None
    
    def analizarEntrada(self):
        self.S() #*Estado inicial de la gramatica
    
    def S(self):
        self.INICIO()
    
    def INICIO(self):
        #*Se observa el primer elemento para decididir a que parte de la gramatica ir
        temporal = self.verToken()
        if temporal is None:
            #Da error por que viene una cadena vacia
            error = Error("error sintactico", "<<EOF>>", "", "")
            self.listaErrores.append(error)
        elif temporal.tipo == "resultado":
            self.RESULTADO()
        elif temporal.tipo == "jornada":
            self.JORNADA()
        elif temporal.tipo == "goles":
            self.GOLES()
        elif temporal.tipo == "tabla":
            self.TABLA()
        elif temporal.tipo == "partidos":
            self.PARTIDOS()
        elif temporal.tipo == "top":
            self.TOP()
        elif temporal.tipo == "adios":
            self.ADIOS()
        else:
            error = Error("error sintactico", temporal.lexema, temporal.linea, temporal.columna)
            self.listaErrores.append(error)
    
    def RESULTADO(self):
        #* Comando devulve el resultado de un partido
        '''Produccion 
            RESULTADO ::= resultado cadena vs cadena temporada menorque entero guion entero mayorque'''
        
        equipo_local = ""
        equipo_visitante = ""
        anio_inicial = ""
        anio_final = ""
        #* Sacar token --- Se espera la palabra reservada ->resultado<-
        token = self.sacarToken()
        if token.tipo == "resultado":
            #* Sacar token --- Se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "CADENA":
                equipo_local = token.lexema
                #* Sacar otro token --- Se espera la palabra reservada ->vs<-
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return
                elif token.tipo == "vs":
                    #* Sacar otro token --- Se espera cadena
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return
                    elif token.tipo == "CADENA":
                        equipo_visitante = token.lexema
                        #* Sacar otro token --- Se espera la palabra reservada ->temporada<-
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                            return
                        elif token.tipo == "temporada":
                            #* Sacar otro token --- Se espera menorque
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                return
                            elif token.tipo == "MENORQUE":
                                #* Sacar otro token --- Se espera entero
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                                    return
                                elif token.tipo == "ENTERO":
                                    anio_inicial = token.lexema
                                    #* Sacar otro token --- Se espera guion
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                                        return
                                    elif token.tipo == "GUION":
                                        #* Sacar otro token --- Se espera entero
                                        token = self.sacarToken()
                                        if token is None:
                                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                                            return
                                        elif token.tipo == "ENTERO":
                                            anio_final = token.lexema
                                            #* Sacar otro token --- Se espera mayorque
                                            token = self.sacarToken()
                                            if token is None:
                                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                                return
                                            elif token.tipo == "MAYORQUE":
                                                #* Se llama a la funcionalidad
                                                print("Analis sintactico de la primer gramatica completada con exito!!")
                                                #print(equipo_local, equipo_visitante, anio_inicial, anio_final)
                                                self.lts_datos = ["resultado",equipo_local, equipo_visitante, anio_inicial, anio_final]
                                            else:
                                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                                #Venia algo mas que no era entero
                                        else:
                                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                            #Venia algo mas que no era entero
                                    else:
                                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                        #Venia algo mas que no era guion
                                else:
                                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                    #Venia algo mas que no era entero
                            else:
                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                #Venia algo mas que no era menorque
                        else:
                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                            #Venia algo mas que no era temporada
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era cadena
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna) 
                    #Venia algo mas que no era vs
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era cadena
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era resultado
    
    def JORNADA(self):
        #Observar el primer elemento para decidir hacia donde ir
        '''Produccion
            JORNADA ::= jornada entero temporada menorque entero guion entero mayorque BANDERAEXPORTAR 
        '''
        num_jornada = ""
        anio_inicial = ""
        anio_final = ""
        identificador = ""
        #*Sacar token --- se espera la palabra reservada ->jornada<-
        token = self.sacarToken()
        if token.tipo == "jornada":
            #* Sacar otro token --- se espera un entero
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "ENTERO":
                num_jornada = token.lexema
                #* Sacar otro token --- se espera la palabra reservada ->temporada<-
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return
                elif token.tipo == "temporada":
                    #* Sacar otro token --- se espera menorque
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return
                    elif token.tipo == "MENORQUE":
                        #* Sacar otro token --- se espera entero
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                            return
                        elif token.tipo == "ENTERO":
                            anio_inicial = token.lexema
                            #* Sacar otro token --- se espera GUION
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                return
                            elif token.tipo == "GUION":
                                #* Sacar otro token --- se espera ENTERO
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                                    return
                                elif token.tipo == "ENTERO":
                                    anio_final = token.lexema
                                    #* Sacar otro token --- se espera mayorque
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                                        return
                                    elif token.tipo == "MAYORQUE":
                                        #* Despues de mayor que se espera BANDERAEXPORTAR o Epsilon, las validaciones
                                        #*respectivas se haran en la funcion de BANDERAEXPORTAR
                                        identificador = self.BANDERAEXPORTAR()
                                        #* Se llama a la funcionalidad
                                        print("Analis sintactico de la segunda gramatica completada con exito!!")
                                        print(num_jornada, anio_inicial, anio_final, identificador)
                                    else:
                                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                        #Venia algo mas que no era mayorque
                                else:
                                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                    #Venia algo mas que no era entero
                            else:
                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                #Venia algo mas que no era guion
                        else:
                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                            #Venia algo mas que no era entero
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era menorque
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                    #Venia algo mas que no era temporada
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era entero
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era jornada
    
    def BANDERAEXPORTAR(self):
        '''Produccion
            BANDERAEXPORTAR ::= banderaexportar identificador
                            | BANDERAIJ
                            | Epsilon
        '''
        identificador = ""
        #* Sacar token --- Se espera la palabra reservada banderaexportar
        token = self.verToken()
        if token is None:
            #* Como en esta produccion es posible esperar Epsilon
            #* Se retorna una cadena vacia en caso de que token.tipo
            #* no sea una banderaexportar, esto para simular el Epsilon.
            return identificador
        elif token.tipo == "banderaexportar":
            #* Ya se que es una banderaexportar, entonces si lo saco
            token = self.sacarToken()
            
            #* Sacar otro token --- se espera identificador
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return 
            elif token.tipo == "IDENTIFICADOR":
                identificador = token.lexema
                return identificador
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era identificador
        elif token.tipo == "banderainicial":
            return ""
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era banderaexportar
    
    def BANDERAIJ(self):
        '''Produccion
        BANDERAIJ ::= banderainicial entero banderafinal entero
            | Epsilon (<<EOF>>)
        '''
        #*Nos quedamos aqui nos faltan dos variables y seguir
        numero_inicial = ""
        numero_final = ""
        
        #* Sacar token --- se espera banderainicial
        token = self.sacarToken()
        if token.tipo == "banderainicial":
            #* Sacar otro token --- se espera entero
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "ENTERO":
                numero_inicial = token.lexema
                #* Sacar otro token --- se espera banderafinal
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return
                elif token.tipo == "banderafinal":
                    #* Sacar otro token --- se espera entero
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return
                    elif token.tipo == "ENTERO":
                        #*Regreso los numeros encontrados
                        numero_final = token.lexema
                        numeros = [numero_inicial, numero_final]
                        return numeros
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era entero
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                    #Venia algo mas que no era banderafinal
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era entero
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era banderainicial
    
    def BANDERATOP(self):
        '''Produccion
            BANDERATOP ::= banderatop entero 
                        | Epsilon (<<EOF>>)
        '''
        num_equipos = ""
        #* Sacar token --- se espera banderatop
        token = self.sacarToken()
        if token.tipo == "banderatop":
            #* Sacar otro token --- se espera entero
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "ENTERO":
                num_equipos = token.lexema
                return num_equipos
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era entero
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era banderatop
    
    def GOLES(self):
        '''Produccion
            GOLES ::= goles CONDICIONG cadena temporada menorque entero guion entero mayorque
        '''
        
        condiciong = ""
        name_equipo = ""
        anio_inicial = ""
        anio_final = ""
        
        #* Sacar token --- se espera la palabra reservada ->goles<-
        token = self.sacarToken()
        if token.tipo == "goles":
            #* Sacar otro token --- Se espera CONDICIONG --> (local|visitante|total)
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "local" or token.tipo == "visitante" or token.tipo == "total":
                condiciong = token.lexema
                #* Sacar 0tro token --- Se espera una cadena
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return                                               
                elif token.tipo == "CADENA":
                    name_equipo = token.lexema
                    #* Sacar 0tro token --- Se espera la palabra reservada ->temporada<-
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return                                               
                    elif token.tipo == "temporada":
                        #* Sacar 0tro token --- Se espera menorque
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                            return                                               
                        elif token.tipo == "MENORQUE":
                            #* Sacar 0tro token --- Se espera entero
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                return                                               
                            elif token.tipo == "ENTERO":
                                anio_inicial = token.lexema
                                #* Sacar 0tro token --- Se espera guion
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                                    return                                               
                                elif token.tipo == "GUION":
                                    #* Sacar 0tro token --- Se espera entero
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                                        return                                               
                                    elif token.tipo == "ENTERO":
                                        anio_final = token.lexema
                                        #* Sacar 0tro token --- Se espera mayorque
                                        token = self.sacarToken()
                                        if token is None:
                                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                                            return                                               
                                        elif token.tipo == "MAYORQUE":
                                            #*Se llama a la funcionalidad
                                            print("Analis sintactico de la tercera gramatica completada con exito!!")
                                            print(condiciong, name_equipo, anio_inicial, anio_final)
                                            pass                                                                                            
                                        else:
                                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                            #Venia algo mas que no era mayorque                                               
                                    else:
                                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                        #Venia algo mas que no era entero                                              
                                else:
                                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                    #Venia algo mas que no era guion                                                  
                            else:
                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                #Venia algo mas que no era entero                                              
                        else:
                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                            #Venia algo mas que no era menorque                                              
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era temporada                                                       
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                    #Venia algo mas que no era cadena                                        
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era  ni local, ni visitante ni total 
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era goles

    def TABLA(self):
        '''Produccion
            TABLA ::= tabla temporada menorque entero guion entero mayorque BANDERAEXPORTAR
        '''
        
        anio_inicial = ""
        anio_final = ""
        identificador = ""
        
        #* Sacar un token --- se espera la palabra reservada ->tabla<-
        token = self.sacarToken()
        if token.tipo == "tabla":
            #* Sacar otro token --- se espera la palabra ->temporada<-
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return    
            elif token.tipo == "temporada":
                #* Sacar otro token --- se espera menorque
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return    
                elif token.tipo == "MENORQUE":
                    #* Sacar otro token --- se espera entero
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return    
                    elif token.tipo == "ENTERO":
                        anio_inicial = token.lexema
                        #* Sacar otro token --- se espera guion
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                            return    
                        elif token.tipo == "GUION":
                            #* Sacar otro token --- se espera entero
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                return    
                            elif token.tipo == "ENTERO":
                                anio_final = token.lexema
                                #* Sacar otro token --- se espera mayorque
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                                    return    
                                elif token.tipo == "MAYORQUE":
                                    #* Despues de mayor que se espera BANDERAEXPORTAR o Epsilon, las validaciones
                                    #*respectivas se haran en la funcion de BANDERAEXPORTAR
                                    identificador = self.BANDERAEXPORTAR()
                                    #* Se llama a la funcionalidad
                                    print("Analis sintactico de la cuarta gramatica completada con exito!!")
                                    print(anio_inicial, anio_final, identificador)
                                    pass
                                else:
                                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                    #Venia algo mas que no era mayorque
                            else:
                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                #Venia algo mas que no era entero
                        else:
                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                            #Venia algo mas que no era guion
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era entero
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                    #Venia algo mas que no era menorque
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era temporada
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era tabla
    
    def PARTIDOS(self):
        '''Produccion 
            PARTIDOS ::= partidos cadena temporada menorque entero guion entero mayorque BANDERAEXPORTAR BANDERAIJ
        '''
        
        name_equipo = ""
        anio_inicial = ""
        anio_final = ""
        identificador = ""
        jornada_inicial = ""
        jornada_final = ""
        
        #*Sacar token --- se espera palabra reservada partidos
        token = self.sacarToken()
        if token.tipo == "partidos":
            #* Sacar otro token --- se espera una cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "CADENA":
                name_equipo = token.lexema
                #* Sacar otro token --- se espera palabra reservada temporada
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return
                elif token.tipo == "temporada":
                    #* Sacar otro token --- se espera menorque
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return
                    elif token.tipo == "MENORQUE":
                        #* Sacar otro token --- se espera entero
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                            return
                        elif token.tipo == "ENTERO":
                            anio_inicial = token.lexema
                            #* Sacar otro token --- se espera guion
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                return
                            elif token.tipo == "GUION":
                                #* Sacar otro token --- se espera entero
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                                    return
                                elif token.tipo == "ENTERO":
                                    anio_final = token.lexema
                                    #* Sacar otro token --- se espera mayorque
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                                        return
                                    elif token.tipo == "MAYORQUE":
                                        #* Despues de mayor que se espera BANDERAEXPORTAR o Epsilon, las validaciones
                                        #*respectivas se haran en la funcion de BANDERAEXPORTAR
                                        identificador = self.BANDERAEXPORTAR()
                                        #*Nos falta hacer las validaciones de si vienen vacios o no en las banderas
                                        lts_indices = self.BANDERAIJ() #* Nos devuelve los indices en caso de que existan
                                        #jornada_inicial = lts_indices[0]
                                        #jornada_final = lts_indices[1]
                                        print(name_equipo, anio_inicial, anio_final, identificador)
                                        #print(name_equipo, anio_inicial, anio_final, jornada_inicial, jornada_final)
                                        
                                        pass
                                    else:
                                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                        #Venia algo mas que no era mayorque
                                else:
                                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                    #Venia algo mas que no era entero
                            else:
                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                #Venia algo mas que no era guion
                        else:
                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                            #Venia algo mas que no era entero
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era menorque
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                    #Venia algo mas que no era temporada
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era cadenas
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era partidos
    
    def TOP(self):
        '''Produccion 
            TOP ::= top (superior|inferior) temporada menorque entero guion entero mayorque BANDERATOP
        '''
        condicion = ""
        anio_inicial = ""
        anio_final = ""
        num_equipos = ""
        
        #* Sacar token --- se espera la palabra reservada ->top<-
        token = self.sacarToken()
        if token.tipo == "top":
            #* Sacar otro token --- se espera CONDICIONT (superior|inferior)
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "superior" or token.tipo == "inferior":
                condicion = token.lexema
                #* Sacar otro token --- se espera temporada
                token = self.sacarToken()
                if token is None:
                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                    return
                elif token.tipo == "temporada":
                    #* Sacar otro token --- se espera menorque
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                        return
                    elif token.tipo == "MENORQUE":
                        #* Sacar otro token --- se espera entero
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("error sintactico", "<<EOF>>", "", "")
                            return
                        elif token.tipo == "ENTERO":
                            anio_inicial = token.lexema
                            #* Sacar otro token --- se espera guion
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("error sintactico", "<<EOF>>", "", "")
                                return
                            elif token.tipo == "GUION":
                                #* Sacar otro token --- se espera entero
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("error sintactico", "<<EOF>>", "", "")
                                    return
                                elif token.tipo == "ENTERO":
                                    anio_final = token.lexema
                                    #* Sacar otro token --- se espera mayorque
                                    token = self.sacarToken()
                                    if token is None:
                                        self.agregarError("error sintactico", "<<EOF>>", "", "")
                                        return
                                    elif token.tipo == "MAYORQUE":
                                        num_equipos = self.BANDERATOP()
                                        print(condicion, anio_inicial, anio_final, num_equipos)
                                        pass
                                    else:
                                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                        #Venia algo mas que no era mayorque
                                else:
                                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                    #Venia algo mas que no era entero
                            else:
                                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                                #Venia algo mas que no era guion
                        else:
                            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                            #Venia algo mas que no era entero
                    else:
                        self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                        #Venia algo mas que no era menorque
                else:
                    self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                    #Venia algo mas que no era temporada
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era (superior|inferior)
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era top
    
    def ADIOS(self):
        '''Produccion 
            ADIOS ::= adios
        '''
        #* Sacar token --- se espera la palabra reservada adios
        token = self.sacarToken()
        if token.tipo == "adios":
            #* Sacar otro token --- se espera <<EOF>>
            token = self.sacarToken()
            if token is None:
                self.agregarError("error sintactico", "<<EOF>>", "", "")
                return
            elif token.tipo == "<<EOF>>":
                #*Se hace la funcionalidad
                print("Hasta luego...")
            else:
                self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
                #Venia algo mas que no era <<EOF>>
        else:
            self.agregarError(token.tipo, token.lexema, token.linea, token.columna)
            #Venia algo mas que no era adios