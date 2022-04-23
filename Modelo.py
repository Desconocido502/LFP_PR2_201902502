from Partido import Partido
from os import startfile
import webbrowser
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico
from Equipo import Equipo
from Clasificacion import Clasificacion

class Modelo(): #*Tiene toda la logica del negocio osea el backend
    def __init__(self, name):
        self.name = name
        #*Se inicializan algunos metodos como la carga de los partidos
        self.partidos : list = self.leerArchivo() #*Retorna la lista de los partidos
        self.lts_tokensG = []
        self.lts_erroresG = []
        self.lts_tokens_tmp = None #*Contendra la lista de tokens por cada vuelta(es una lista de tokens temporal)
        self.lts_datos = None #* Contendra cualquiera de los datos de las 7 gramaticas
    
    def clean_lts_bugs(self):
        self.lts_erroresG = []
    
    def clean_lts_tokens(self):
        self.lts_tokensG = []
    
    def leerArchivo(self):
        lista_partidos = []
        contenido = ""
        with open('LaLigaBot-LFP.csv', encoding="utf-8") as file:
            contenido = file.read()
        partidos = contenido.split("\n")
        partidos.pop(0)
        
        for partido in partidos:
            datos = partido.split(',')
            fecha = datos[0]
            temporada = datos[1]
            jornada = datos[2]
            equipoLocal = datos[3]
            equipoVisitante = datos[4]
            golesLocal = datos[5]
            golesVisitante = datos[6]
            #* Se crea el objeto Partido
            p = Partido(fecha, temporada, jornada, equipoLocal, equipoVisitante, golesLocal, golesVisitante) 
            lista_partidos.append(p) #*Se agrega el objeto a una lista
        
        return lista_partidos

    def analisisLexico(self, entrada, linea):
        analisis_lexico_comando = AnalizadorLexico()
        analisis_lexico_comando.analizarEntrada(entrada, linea)
        #*Se suma cada nueva lista de tokens a la lista de tokens general
        self.lts_tokensG += analisis_lexico_comando.getListaTokens()
        #*Se suma cada nueva lista de errores lexicos a la lista de errores general
        self.lts_erroresG += analisis_lexico_comando.getListaErrores()
        self.lts_tokens_tmp = analisis_lexico_comando.getListaTokens() #*lista de tokens temporal
        
    def analisisSintactico(self):
        # self.imprimirDatos() #*Si se suman las cadena de tokens y de errores
        #*Se procede a realizar el analisis sintactico, se obtendra una lista, que puede contener cualquiera de los
        #* datos de los 7 comandos, por eso, se enviara en la primera posicion de la lista, que tipo de gramatica
        #*fue la que se trabajo, por eso hay que validar que informacion se manda a la vista
        analisis_sintactico_comando = AnalizadorSintactico(self.lts_tokens_tmp) #*Lista temporal de tokens
        analisis_sintactico_comando.analizarEntrada()
        
        #*Nos faltan las demas gramaticas, hay unas por corregir, pero os vamos a hacer mejor los html de tokens y errores lexicos
        self.lts_datos = analisis_sintactico_comando.getLtsDatos()#*Se retorna la lista de datos
        #!Nos quedamos aqui
    def returnResponse(self):
        if self.lts_datos == None:
            print("Venia cadena vacia y por tanto <<EOF>>")
        elif self.lts_datos[0] == "resultado":
            equipo_local = self.lts_datos[1].replace('"', '') 
            equipo_visitante = self.lts_datos[2].replace('"', '')
            anio_inicial = self.lts_datos[3]
            anio_final = self.lts_datos[4]
            
            bandera_inicial = self.validate_year_initial(anio_inicial)
            bandera_final = self.validate_year_final(anio_final)
            if (bandera_inicial == "a"): #*No se hace nada
                pass
            elif (bandera_inicial == "nfr"):
                txt_response = "BOT: El número inicial se encuentra fuera del rango aceptable (1979-2019)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_inicial == "nm"):
                txt_response = "BOT: El número inicial contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if (bandera_final == "a"): #*No se hace nada
                pass
            elif (bandera_final == "nfr"):
                txt_response = "BOT: El número final se encuentra fuera del rango aceptable (1980-2020)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_final == "nm"):
                txt_response = "BOT: El número final contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            found_partido = self.result_of_a_match(equipo_local, equipo_visitante, anio_inicial, anio_final) #*Devuelve un objeto Partido
            #print(found_partido)
            if (found_partido == None):
                txt_response = "BOT: Equipos no encontrados, revise que esten escritos los equipos!!!\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            #*Se arma la respuesa texto, para ser enviada a la vista
            txt_response = f"BOT: El resultado de este partido fue: {found_partido.getEquipoLocal()} {found_partido.getGolesLocal()} - {found_partido.getEquipoVisitante()} {found_partido.getGolesLocal()}\n\n"
            return txt_response #*Se retorna la respuesta del 'bot'
            #print(txt_response)
            #print(equipo_local, equipo_visitante, anio_inicial, anio_final)
        elif self.lts_datos[0] == "jornada-c": #*Para el caso donde el archivo html se le de un nombre en especifico
            num_jornada = self.lts_datos[1]
            anio_inicial = self.lts_datos[2]
            anio_final = self.lts_datos[3]
            identificador = self.lts_datos[4]
            
            bandera_inicial = self.validate_year_initial(anio_inicial)
            bandera_final = self.validate_year_final(anio_final)
            bandera_numero = self.validate_number_day(num_jornada)
            if (bandera_inicial == "a"): #*No se hace nada
                pass
            elif (bandera_inicial == "nfr"):
                txt_response = "BOT: El número inicial se encuentra fuera del rango aceptable (1979-2019)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_inicial == "nm"):
                txt_response = "BOT: El número inicial contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if (bandera_final == "a"): #*No se hace nada
                pass
            elif (bandera_final == "nfr"):
                txt_response = "BOT: El número final se encuentra fuera del rango aceptable (1980-2020)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_final == "nm"):
                txt_response = "BOT: El número final contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if(bandera_numero == "nm"):
                txt_response = "BOT: El número de jornada contiene más de 2 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            self.result_of_a_day(num_jornada, anio_inicial, anio_final, identificador)
            txt_response = f"BOT: Generando archivo de resultados jornada {num_jornada} temporada {anio_inicial}-{anio_final}\n\n"
            return txt_response
            print(num_jornada, anio_inicial, anio_final, identificador)
        elif self.lts_datos[0] == "jornada-i": #*Para el caso donde el archivo html tendra un nombre por default
            num_jornada = self.lts_datos[1]
            anio_inicial = self.lts_datos[2]
            anio_final = self.lts_datos[3]
            
            bandera_inicial = self.validate_year_initial(anio_inicial)
            bandera_final = self.validate_year_final(anio_final)
            bandera_numero = self.validate_number_day(num_jornada)
            if (bandera_inicial == "a"): #*No se hace nada
                pass
            elif (bandera_inicial == "nfr"):
                txt_response = "BOT: El número inicial se encuentra fuera del rango aceptable (1979-2019)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_inicial == "nm"):
                txt_response = "BOT: El número inicial contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if (bandera_final == "a"): #*No se hace nada
                pass
            elif (bandera_final == "nfr"):
                txt_response = "BOT: El número final se encuentra fuera del rango aceptable (1980-2020)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_final == "nm"):
                txt_response = "BOT: El número final contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if(bandera_numero == "nm"):
                txt_response = "BOT: El número de jornada contiene más de 2 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            self.result_of_a_day(num_jornada, anio_inicial, anio_final, None)
            txt_response = f"BOT: Generando archivo de resultados jornada {num_jornada} temporada {anio_inicial}-{anio_final}\n\n"
            #print(num_jornada, anio_inicial, anio_final)
            return txt_response
        elif self.lts_datos[0] == "goles":
            condiciong = self.lts_datos[1]
            name_equipo = self.lts_datos[2].replace('"', '') 
            anio_inicial = self.lts_datos[3]
            anio_final = self.lts_datos[4]
            
            bandera_inicial = self.validate_year_initial(anio_inicial)
            bandera_final = self.validate_year_final(anio_final)
            
            if (bandera_inicial == "a"): #*No se hace nada
                pass
            elif (bandera_inicial == "nfr"):
                txt_response = "BOT: El número inicial se encuentra fuera del rango aceptable (1979-2019)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_inicial == "nm"):
                txt_response = "BOT: El número inicial contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if (bandera_final == "a"): #*No se hace nada
                pass
            elif (bandera_final == "nfr"):
                txt_response = "BOT: El número final se encuentra fuera del rango aceptable (1980-2020)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_final == "nm"):
                txt_response = "BOT: El número final contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            
            resultado = self.team_goals_in_a_season(condiciong, name_equipo, anio_inicial, anio_final) #*Retorna una cantidad en str o ERROR
            print(condiciong, name_equipo, anio_inicial, anio_final)
            if resultado != "Error":
                txt_response = f"BOT: Los goles anotados por el {name_equipo} en {condiciong} en la temporada {anio_inicial}-{anio_final} fueron {resultado}\n\n"
                return txt_response
            else:
                txt_response = "BOT: Error en la condicion, no es ni local, ni visitante, ni total!!!\n\n"
                return txt_response
        elif self.lts_datos[0] == "tabla-c": #*Para el caso donde el archivo html se le de un nombre en especifico
            anio_inicial = self.lts_datos[1]
            anio_final = self.lts_datos[2]
            identificador = self.lts_datos[3]            
            
            bandera_inicial = self.validate_year_initial(anio_inicial)
            bandera_final = self.validate_year_final(anio_final)
            
            if (bandera_inicial == "a"): #*No se hace nada
                pass
            elif (bandera_inicial == "nfr"):
                txt_response = "BOT: El número inicial se encuentra fuera del rango aceptable (1979-2019)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_inicial == "nm"):
                txt_response = "BOT: El número inicial contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if (bandera_final == "a"): #*No se hace nada
                pass
            elif (bandera_final == "nfr"):
                txt_response = "BOT: El número final se encuentra fuera del rango aceptable (1980-2020)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_final == "nm"):
                txt_response = "BOT: El número final contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            self.leaderboard(anio_inicial, anio_final, identificador)
            txt_response = f"BOT: Generando archivo de clasificación de temporada {anio_inicial}-{anio_final}\n\n"
            return txt_response
            #print(anio_inicial, anio_final, identificador)
        elif self.lts_datos[0] == "tabla-i": #*Para el caso donde el archivo html tendra un nombre por default
            anio_inicial = self.lts_datos[1]
            anio_final = self.lts_datos[2]
            
            bandera_inicial = self.validate_year_initial(anio_inicial)
            bandera_final = self.validate_year_final(anio_final)
            
            if (bandera_inicial == "a"): #*No se hace nada
                pass
            elif (bandera_inicial == "nfr"):
                txt_response = "BOT: El número inicial se encuentra fuera del rango aceptable (1979-2019)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_inicial == "nm"):
                txt_response = "BOT: El número inicial contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            if (bandera_final == "a"): #*No se hace nada
                pass
            elif (bandera_final == "nfr"):
                txt_response = "BOT: El número final se encuentra fuera del rango aceptable (1980-2020)\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            elif (bandera_final == "nm"):
                txt_response = "BOT: El número final contiene más de 4 digitos\n\n"
                return txt_response #*Se retorna la respuesta del 'bot'
            
            self.leaderboard(anio_inicial, anio_final, None)
            txt_response = f"BOT: Generando archivo de clasificación de temporada {anio_inicial}-{anio_final}\n\n"
            return txt_response
            #print(anio_inicial, anio_final)
        elif self.lts_datos[0] == "partidos-f": #*Para el caso donde el archivo html se le de un nombre en especifico
            name_equipo = self.lts_datos[1].replace('"', '')
            anio_inicial = self.lts_datos[2]
            anio_final = self.lts_datos[3]
            identificador = self.lts_datos[4]
            
            self.a_teams_season(name_equipo, anio_inicial, anio_final, identificador, None, None)
            
            print(name_equipo, anio_inicial, anio_final, identificador)
        elif self.lts_datos[0] == "partidos-i": #*Para el caso donde el archivo html tendra un nombre por default
            print(self.lts_datos[1], self.lts_datos[2], self.lts_datos[3], self.lts_datos[4], self.lts_datos[5])
        elif self.lts_datos[0] == "top-c": #*Para el caso donde se da un numero de equipos en especifico a mostrar
            print(self.lts_datos[1], self.lts_datos[2], self.lts_datos[3], self.lts_datos[4])
        elif self.lts_datos[0] == "top-i": #*Para el caso donde no se da un numero de equipos en especifico a mostrar
            print(self.lts_datos[1], self.lts_datos[2], self.lts_datos[3])
        elif self.lts_datos[0] == "adios": 
            print("adios")
        else: #*Si no es ninguno de los tokens inciales, viene un token que no es parte del inicio de una gramatica
            pass
    
    #*Se crea el reporte de Tokens
    def reporteTokensHTML(self):
        if self.lts_tokensG != None:
            doc_str = """
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="./css/style.css">
                    <title>Reporte de tokens</title>
                </head>
                <body>
                    <h1>Reporte de Tokens</h1>
                <div class="container">
                <table>
                    <thead class="container_encabezado">
                        <tr>
                            <td>TIPO</td>
                            <td>LEXEMA</td>
                            <td>FILA</td>
                            <td>COLUMNA</td>
                        </tr>
                    </thead>
                <tbody class="container_cuerpo">
            """
            cuerpo = ""  # *Tocamos el codigo en la parte del tipo ya que se ha de confundir con <<EOF>>
            for token in self.lts_tokensG:
                tipoToken = token.getTipo()
                if token.getTipo() == "<<EOF>>":
                    tipoToken = f"&lt;&lt;EOF&gt;&gt;"
                cuerpo += f""" 
                    <tr>
                        <td>  {tipoToken} </td>
                        <td> {token.getLexema()} </td>
                        <td> {token.getLinea()} </td>
                        <td> {token.getColumna()} </td>
                    </tr>\n    
                """
            cuerpo += """ 
                    </tbody>
                </table>
                </div>
                <footer class="datos">
                <p>Carlos E. Soto M. - 201902502 - Proyecto 2</p>
                </footer>
            </body>
            </html>
            """
            doc_str += cuerpo
            # Fin del reporte de lista de tokens
            nombreHTML = "lista_tokens.html"
            try:
                file = open(nombreHTML, "w")
                file.write(doc_str)
            except:
                print("Error al crear el HTML")
            finally:
                file.close()
                webbrowser.open_new_tab(nombreHTML)
                print("Reporte de tokens finalizado con Exito")
        else:
            print("No hay informacion con que crear el HTML")
    
    #*Se crea el reporte de errores
    def reporteErroresHTML(self):
        if self.lts_erroresG != None:
            doc_str = """
                <!DOCTYPE html>
                <html lang="es">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link rel="stylesheet" href="./css/style.css">
                    <title>Lista de errores</title>
                </head>
                <body>
                    <h1>Reporte de Errores</h1>
                <div class="container">
                <table>
                    <thead class="container_encabezado">
                        <tr>
                            <td>TIPO</td>
                            <td>LEXEMA</td>
                            <td>FILA</td>
                            <td>COLUMNA</td>
                        </tr>
                    </thead>
                <tbody class="container_cuerpo">
            """
            cuerpo = ""  # *Tocamos el codigo en la parte del tipo ya que se ha de confundir con <<EOF>>
            for error in self.lts_erroresG:
                tipoToken = error.getTipo()
                if error.getTipo() == "<<EOF>>":
                    tipoToken = f"&lt;&lt;EOF&gt;&gt;"
                cuerpo += f""" 
                    <tr>
                        <td>  {tipoToken} </td>
                        <td> {error.getLexema()} </td>
                        <td> {error.getLinea()} </td>
                        <td> {error.getColumna()} </td>
                    </tr>\n    
                """
            cuerpo += """ 
                    </tbody>
                </table>
                </div>
                <footer class="datos">
                <p>Carlos E. Soto M. - 201902502 - Proyecto 2</p>
                </footer>
            </body>
            </html>
            """
            doc_str += cuerpo
            # Fin del reporte de lista de tokens
            nombreHTML = "lista_errores.html"
            try:
                file = open(nombreHTML, "w")
                file.write(doc_str)
            except:
                print("Error al crear el HTML")
            finally:
                file.close()
                webbrowser.open_new_tab(nombreHTML)
                print("Reporte de errores finalizado con Exito")
        else:
            print("No hay informacion con que crear el HTML")
    
    def result_of_a_match(self, equipo_local, equipo_visitante, anio_inicial, anio_final):
        #print(equipo_local, equipo_visitante, anio_inicial, anio_final)
        #*Primero se tendra que buscar por temporada, y guardarlos en una lista
        #*Luego buscar en esa lista, los nombres de los equipos
        #*Por ultimo, ya se manda a mostrar los datos
        temporada = anio_inicial+"-"+anio_final
        lts_season = self.search_for_season(temporada)
        partido = self.sear_for_team(lts_season, equipo_local, equipo_visitante)
        return partido
    
    #* Crea un html de los resultados de una jornada
    def result_of_a_day(self, num_jornada, anio_inicial, anio_final, identificador):
        #lts_days = self.search_for_day(day)
        #*Primero se tendra que buscar por temporada y guardar los datos en una Lista
        #*Luego se busca en esa lista por el numero de jornada los partidos y retorna una lista con la jornada dada
        #*Por ultimo con esa lista de jornada, se crea un archivo html
        temporada = anio_inicial+"-"+anio_final
        lts_season = self.search_for_season(temporada) #*Busca por temporada y devulve una lista de los partidos de esa temporada
        lts_days = self.search_for_day(lts_season, num_jornada) #*Busca el numero de jornada en la lista de temporada especificada
        print("Identificador:", identificador)
        if (identificador == None):
            identificador = "jornada"
            print("Identificador renombrado:", identificador)
        #* Aqui ya se manda la lista de los partidos en cierta jornada para crear el html
        self.create_html_for_day(num_jornada, anio_inicial, anio_final, identificador, lts_days)
    
    def team_goals_in_a_season(self, condiciong, name_equipo, anio_inicial, anio_final):
        #*Primero se busca por temporada, se retorna una lista de temporada
        #*Luego en la lista de temporada temporal, dependiendo de la condicion, se buscaran, la cantidad
        #*De goles para el equipo ingresado
        temporada = anio_inicial+"-"+anio_final
        lts_season = self.search_for_season(temporada) #*Busca por temporada y devulve una lista de los partidos de esa temporada
        if (condiciong == "LOCAL"):
            local = 0
            for partido in lts_season:
                if (partido.getEquipoLocal() == name_equipo):
                    local += int(partido.getGolesLocal())
            return str(local)
        elif (condiciong == "VISITANTE"):
            visitante = 0
            for partido in lts_season:
                if (partido.getEquipoVisitante() == name_equipo):
                    visitante += int(partido.getGolesVisitante())
            return str(visitante)
        elif (condiciong == "TOTAL"):
            total : int = 0
            for partido in lts_season:
                if (partido.getEquipoLocal() == name_equipo):
                    total += int(partido.getGolesLocal())
                elif (partido.getEquipoVisitante() == name_equipo):
                    #print(partido, partido.getGolesVisitante())
                    total += int(partido.getGolesVisitante())
            return str(total)
        else:
            #*EN caso de que no sea ni local, ni visitante, ni total, retorna un mensaje de error
            return "Error"

    def open_user_manual(self):
        startfile("Manual de Usuario.pdf")
    
    def open_technical_manual(self):
        startfile("Manual Tecnico.pdf")
    
    def imprimirDatos(self):
        print("\n\n\n")
        print("********************* Lista Tokens")
        for token in self.lts_tokensG:
            print(token.getInfo())
        print("\n\n\n")
        print("********************* Lista Errores")
        for error in self.lts_erroresG:
            print(error.getInfo())
    
    #*Retorna una lista con la temporada buscada
    def search_for_season(self, season):
        lts_season = []
        #print(len(self.partidos))
        #print(self.partidos[0].getTemporada())
        for partido in self.partidos:
            if (partido.getTemporada() == season):
                #print(partido)
                lts_season.append(partido)
        return lts_season
    
    #*Retorna una lista con la jornada buscada
    def search_for_day(self, lts_season, day):
        lts_days = []
        for partido in lts_season:
            if (partido.getJornada() == day):
                #print(partido)
                lts_days.append(partido)
        return lts_days
    
    #*Retorna un partido
    def sear_for_team(self, lts_season, team1, team2):
        #print(lts_season[0], team1, team2)
        for season in lts_season:
            #print(season.getEquipoLocal(), ",",season.getEquipoVisitante())
            if(team1 == season.getEquipoLocal() and team2 == season.getEquipoVisitante()):
                return season
        return None
    
    #* Crea el html con la informacion requerida
    def create_html_for_day(self, num_jornada, anio_inicial, anio_final, identificador, lts_days):
        doc_str = f""" 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./css/estilos.css" />
    <title>Tabla de jornadas</title>
  </head>
  <body>
    <h1>Jornada {num_jornada}, temporada: {anio_inicial}-{anio_final}</h1>
    <table class="jornada" border="1">
      <thead>
        <th>Fecha</th>
        <th>Temporada</th>
        <th>Jornada</th>
        <th>Equipo Local</th>
        <th>Equipo Visitante</th>
        <th>Goles Local</th>
        <th>Goles Visitante</th>
      </thead>
      <tbody>
        """
        cuerpo = ""
        #*El cuerpo del html
        for partido in lts_days:
            cuerpo += "<tr>\n" 
            cuerpo += f"<td>{partido.getFecha()}</td>\n"
            cuerpo += f"<td>{partido.getTemporada()}</td>\n"
            cuerpo += f"<td>{partido.getJornada()}</td>\n"
            cuerpo += f"<td>{partido.getEquipoLocal()}</td>\n"
            cuerpo += f"<td>{partido.getEquipoVisitante()}</td>\n"
            cuerpo += f"<td>{partido.getGolesLocal()}</td>\n"
            cuerpo += f"<td>{partido.getGolesVisitante()}</td>\n"
            cuerpo += "</tr>\n"
        
        cuerpo += """ 
        </tbody>
    </table>
    <div id="footer">Carlos E. Soto M. - 201902502 - Proyecto 2</div>
  </body>
</html>
"""
        doc_str += cuerpo #*Se concatena el resto de informacion
        identificador = identificador+".html"
        try:
            file = open(identificador, "w", encoding="utf-8")
            file.write(doc_str)
        except:
            print("Error al crear el archivo html")
        finally:
            file.close()
            webbrowser.open_new_tab(identificador)
            print("Reporte de resultados de una jornada finalizado con exito")
# modelo = Modelo("Prueba")
# print(modelo.partidos[0])

    #*VALIDA QUE SEAN NUMEROS DE 4 DIGITOS QUE SEA MAYOR O IGUAL A 1979 
    def validate_year_initial(self, num_inicial):
        if (len(num_inicial) <= 4):
            num_inicial = int(num_inicial)
            if (num_inicial >= 1979 and num_inicial <= 2019):
                return "a" #*En caso de que se cumplan las dos validaciones
            else:
                return "nfr" #*En caso de que el numero este fuera del rango
        else:
            return "nm"#* En caso de que el numero sea mayor a 4 digitos
    
    #*VALIDA QUE SEAN NUMEROS DE 4 DIGITOS QUE SEA MENOR O IGUAL A 2020
    def validate_year_final(self, num_final):
        if (len(num_final) <= 4):
            num_final = int(num_final)
            if(num_final >= 1980 and num_final <= 2020):
                return "a" #*En caso de que se cumplan las dos validaciones
            else:
                return "nfr" #*En caso de que el numero este fuera del rango
        else:
            return "nm" #* En caso de que el numero sea mayor a 4 digitos
    
    #*VALIDA QUE SEAN NUMEROS DE DOS DIGITOS COM MAXIMO
    def validate_number_day(self, num):
        if (len(num) <= 2):
            return "a" #*En caso de que se cumplan las dos validaciones
        else:
            return "nm" #* En caso de que el numero sea mayor a 2 digitos
    
    
    #*---------------------------Aqui van todos los metodos para crear el archivo de clasificatoria----------------------------
    #*Se nos da las temporada, a partir de ahi, se tiene una lista ya que el metodo esta creado ya
    #*A partir de aqui, se recorre la lista de la temporada, listando todos los equipos encontrados,
    #*Se compararan con una lista, y asi se iran agrengando a una lista de solo equipos.
    #*Luego de esto, se recorrera la lista de equipos junto con la lista de la temporada
    #*De esta forma va recolectando la informacion necesaria para cada equipo, y luego ya crear un objeto
    #*De tipo Partido, y almacenarlo en una lista, dicha lista sera un atributo del objeto Clasificacion
    #*Esto para un mejor manejo de la informacion
    def leaderboard(self, anio_inicial, anio_final, identificador):
        name_equipos = []
        temporada = anio_inicial+"-"+anio_final
        lts_season = self.search_for_season(temporada) #*Busca por temporada y devulve una lista de los partidos de esa temporada
        for partido in lts_season:
            if not str(partido.getEquipoLocal()) in name_equipos:
                name_equipos.append(str(partido.getEquipoLocal()))#*Se listan todos los equipos de la temporada
            #*Se empieza a recorrer la lista de temporada, para saber que equipos participaron en dicha temporada
            #*Se ira viendo por el lado de los equipos locales, daria igual que fuera con los equipos visitantes,
            #*entonces lo primero que hacemos al comenzar la iteracion de la temporada es, jalar el nombre del 
            #*equipo local, y se manda a comparar con la lista que contendra los nombres de los equipos 
            #*en caso de que el nombre no aparezca en la lista se agrega a la lista, si ya existe no se agrega 
            #*a la lista asi nos aseguramos de no meter duplicados a la lista.
        #print(len(name_equipos))
        # for equipo in name_equipos:
        #     print(equipo)
        
        clasificacion = Clasificacion(temporada)
        #*Hasta aqui vamos bien con la agrupacion de los nombres de los grupos, ahora toca recorrer ambas listas
        #*la lista de nombres junto con la lista de la temporada, ya que esto es necesario para obtener los datos
        #*estadisticos de cada equipo. primero recorremoos por equipo luego recorremos la temporada.
        for equipo in name_equipos:
            #print(equipo)
            pg_local = 0
            pp_local = 0
            pe_local = 0
            gf_local = 0
            gc_local = 0
            
            pg_visitante = 0
            pp_visitante = 0
            pe_visitante = 0
            gf_visitante = 0
            gc_visitante = 0
            team = Equipo(equipo)
            for partido in lts_season:
                if (equipo == partido.getEquipoLocal()): #*Como es local, solo cosas de local
                    #*Se definen los partidos ganados-perdidos-empatados
                    #print(name_equipos[0], "local")
                    #print(type(int(partido.getGolesLocal())))
                    if (int(partido.getGolesLocal()) > int(partido.getGolesVisitante())):
                        pg_local += 1
                    elif (int(partido.getGolesLocal()) < int(partido.getGolesVisitante())):
                        pp_local += 1
                    else:#*Empate
                        pe_local += 1
                    gf_local += int(partido.getGolesLocal())
                    gc_local += int(partido.getGolesVisitante())
                elif (equipo == partido.getEquipoVisitante()): #*Como es visitante, solo cosas de visitante
                    #print(name_equipos[0], "visitante")
                    if (int(partido.getGolesVisitante()) > int(partido.getGolesLocal())):
                        pg_visitante += 1
                    elif (int(partido.getGolesVisitante()) < int(partido.getGolesLocal())):
                        pp_visitante += 1
                    else:#*Empate
                        pe_visitante += 1
                    gf_visitante += int(partido.getGolesVisitante())
                    gc_visitante += int(partido.getGolesLocal())
            
            team.datos_local.setPG(pg_local)
            team.datos_local.setPE(pe_local)
            team.datos_local.setPP(pp_local)
            team.datos_local.setGF(gf_local)
            team.datos_local.setGC(gc_local)
            team.datos_local.setPJ(pg_local + pe_local + pp_local)
            
            team.datos_visitante.setPG(pg_visitante)
            team.datos_visitante.setPE(pe_visitante)
            team.datos_visitante.setPP(pp_visitante)
            team.datos_visitante.setGF(gf_visitante)
            team.datos_visitante.setGC(gc_visitante)
            team.datos_visitante.setPJ(pg_visitante + pe_visitante + pp_visitante)

            clasificacion.lista_equipos.append(team) #*Se agrega el equipo a la lista de equipos en el objeto clasificacion
        
        #*Si todo sale bien deberiamos ver por ahora los nombres de los equipos
        #clasificacion.mostrarListaEquipos() #* Todo bien hasta el momento
        if (identificador == None):
            identificador = "temporada"
        
        self.create_html_season_table(clasificacion, identificador)
    
    def create_html_season_table(self, clasificacion, identificador):
        clasificacion.bubble_sort_equipos()
        doc_str = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/estilos_cla.css">
    <title>Tabla Clasificatoria {clasificacion.temporada}</title>
</head>
<body>
    <h1>Tabla Clasificatoria {clasificacion.temporada}</h1>
    <table class="clasificacion">
        <thead>
            <th>EQUIPOS</th>
            <th>PTS Total</th>
            <th>PJ</th>
            <th>PG</th>
            <th>PE</th>
            <th>PP</th>
            <th>GF</th>
            <th>GC</th>
            <th>PTS Local</th>
            <th>PJ</th>
            <th>PG</th>
            <th>PE</th>
            <th>PP</th>
            <th>GF</th>
            <th>GC</th>
            <th>PTS Visitante</th>
            <th>PJ</th>
            <th>PG</th>
            <th>PE</th>
            <th>PP</th>
            <th>GF</th>
            <th>GC</th>
        </thead>
        <tbody>
"""
        cuerpo = ""
        lista_equipos = clasificacion.getListaEquipos()
        for equipo in lista_equipos:
            equipo.calcular_pts_visitante()
            equipo.calcular_pts_local()
            cuerpo += "<tr>"
            cuerpo += f"""
                <td>{equipo.nombre}</td>
                <td>{equipo.pts_total()}</td>
                <td>{equipo.pj_total()}</td>
                <td>{equipo.pg_total()}</td>
                <td>{equipo.pe_total()}</td>
                <td>{equipo.pp_total()}</td>
                <td>{equipo.gf_total()}</td>
                <td>{equipo.gc_total()}</td>
                <td>{equipo.pts_local}</td>
                <td>{equipo.datos_local.getPJ()}</td>
                <td>{equipo.datos_local.getPG()}</td>
                <td>{equipo.datos_local.getPE()}</td>
                <td>{equipo.datos_local.getPP()}</td>
                <td>{equipo.datos_local.getGF()}</td>
                <td>{equipo.datos_local.getGC()}</td>
                <td>{equipo.pts_visitante}</td>
                <td>{equipo.datos_visitante.getPJ()}</td>
                <td>{equipo.datos_visitante.getPG()}</td>
                <td>{equipo.datos_visitante.getPE()}</td>
                <td>{equipo.datos_visitante.getPP()}</td>
                <td>{equipo.datos_visitante.getGF()}</td>
                <td>{equipo.datos_visitante.getGC()}</td>
        </tr>\n
"""
        cuerpo += """
        </tbody>
    </table>
    <div id="footer">Carlos E. Soto M. - 201902502 - Proyecto 2</div>
</body>
</html>
        """
        doc_str += cuerpo #*Se concatena el resto de informacion
        identificador = identificador+".html"
        try:
            file = open(identificador, "w", encoding="utf-8")
            file.write(doc_str)
        except:
            print("Error al crear el archivo html")
        finally:
            file.close()
            webbrowser.open_new_tab(identificador)
            #print("Reporte de tabla general de temporada finalizado con exito")
    
    def a_teams_season(self, name_equipo, anio_inicial, anio_final, identificador, j_inicial, j_final):
        
        temporada = anio_inicial+"-"+anio_final
        lts_season = self.search_for_season(temporada) #*Busca por temporada y devulve una lista de los partidos de esa temporada
        