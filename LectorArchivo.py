from Partido import Partido

def leerArchivo(ruta):
    archivo = open(ruta,'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def enviarListaPartidos():
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
        p = Partido(fecha, temporada, jornada, equipoLocal, equipoVisitante, golesLocal, golesVisitante) #* Se crea el objeto Partido
        lista_partidos.append(p) #*Se agrega el objeto a una lista
    
    return lista_partidos

# lts_p = enviarListaPartidos()
# print(lts_p[0])