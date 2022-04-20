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
        # self.imprimirDatos() #*Si se suman las cadena de tokens y de errores
        #*Se procede a realizar el analisis sintactico, se obtendra una lista, que puede contener cualquiera de los
        #* datos de los 7 comandos, por eso, se enviara en la primera posicion de la lista, que tipo de gramatica
        #*fue la que se trabajo, por eso hay que validar que informacion se manda a la vista
        analisis_sintactico_comando = AnalizadorSintactico(analisis_lexico_comando.getListaTokens())
        analisis_sintactico_comando.analizarEntrada()
        
        #*Nos faltan las demas gramaticas, hay unas por corregir, pero os vamos a hacer mejor los html de tokens y errores lexicos
        lts_datos = analisis_sintactico_comando.getLtsDatos()#*Se retorna la lista de datos
        if lts_datos == None:
            print("Venia cadena vacia y por tanto <<EOF>>")
        elif lts_datos[0] == "resultado":
            print(lts_datos[1], lts_datos[2], lts_datos[3], lts_datos[4])
        else:
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

# modelo = Modelo("Prueba")
# print(modelo.partidos[0])