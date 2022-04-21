from Partido import Partido
from os import startfile
import webbrowser
from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico

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
            found_partido = self.result_of_a_match(equipo_local, equipo_visitante, anio_inicial, anio_final) #*Devuelve un objeto Partido
            #print(found_partido)
            #*Se arma la respuesa texto, para ser enviada a la vista
            txt_response = f"BOT: El resultado de este partido fue: {found_partido.getEquipoLocal()} {found_partido.getGolesLocal()} - {found_partido.getEquipoVisitante()} {found_partido.getGolesLocal()}\n\n"
            return txt_response #*Se retorna la respuesta del 'bot'
            #print(txt_response)
            #print(equipo_local, equipo_visitante, anio_inicial, anio_final)
        elif self.lts_datos[0] == "jornada-c": #*Para el caso donde el archivo html se le de un nombre en especifico
            print(self.lts_datos[1], self.lts_datos[2], self.lts_datos[3], self.lts_datos[4])
        elif self.lts_datos[0] == "jornada-i": #*Para el caso donde el archivo html tendra un nombre por default
            print(self.lts_datos[1], self.lts_datos[2], self.lts_datos[3])
        elif self.lts_datos[0] == "goles":
            print(self.lts_datos[1], self.lts_datos[2], self.lts_datos[3], self.lts_datos[4])
        elif self.lts_datos[0] == "tabla-c": #*Para el caso donde el archivo html se le de un nombre en especifico
            print(self.lts_datos[1], self.lts_datos[2], lts_datos[3])
        elif self.lts_datos[0] == "tabla-i": #*Para el caso donde el archivo html tendra un nombre por default
            print(self.lts_datos[1], self.lts_datos[2])
        elif self.lts_datos[0] == "partidos-f": #*Para el caso donde el archivo html se le de un nombre en especifico
            print(self.lts_datos[1], self.lts_datos[2], lts_datos[3], lts_datos[4])
        elif self.lts_datos[0] == "partidos-i": #*Para el caso donde el archivo html tendra un nombre por default
            print(self.lts_datos[1], self.lts_datos[2], lts_datos[3], lts_datos[4], lts_datos[5])
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
    
    #*Retorna un partido
    def sear_for_team(self, lts_season, team1, team2):
        #print(lts_season[0], team1, team2)
        for season in lts_season:
            #print(season.getEquipoLocal(), ",",season.getEquipoVisitante())
            if(team1 == season.getEquipoLocal() and team2 == season.getEquipoVisitante()):
                return season
        return None

# modelo = Modelo("Prueba")
# print(modelo.partidos[0])