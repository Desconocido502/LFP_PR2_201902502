from Modelo import Modelo
from Vista import Vista
from threading import Timer

class Controlador():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    #*Se trae el texto ingresa a la caja de texto
    def process_data(self, data, linea):
        #print(data, linea)
        self.modelo.analisisLexico(data, linea)
        #*Se tendria que colocar luego el analizador lexico e igualarlo a un identificador
        #*Asi por ultimo se pasa a la vista los datos obtenidos del analizador sintactico
        self.modelo.analisisSintactico()
        data = self.modelo.returnResponse() #*Devuelve la respuesta segun el comando en una cadena de texto
        self.vista.printResponse(data)
        self.vista.show_msg_open_manual_succesfully("Comando leído sin \nningún problema...")
        
        if(data == "BOT: \t\tADIOS"):
            t = Timer(0.6, self.stopProcess)
            t.start()

    
    def stopProcess(self):
        self.vista.quitWindow()#*Cierra la ventana
    
    #*Funcion para crear el html de los errores
    def show_bug_in_html(self):
        self.modelo.reporteErroresHTML()
        self.modelo.reporteErroresSHTML()
        self.vista.show_msg_open_manual_succesfully("Creando reporte de\nErrores Léxicos y Sintacticos")
    
    #*Funcion para limpiar el log de los errores
    def clean_log_bugs(self):
        self.modelo.clean_lts_bugs()
        self.vista.show_msg_open_manual_succesfully("Se ha limpiado el \nlog de errores")
    
    #*Funcion para crear el html de los tokens
    def show_tokens_in_html(self):
        self.modelo.reporteTokensHTML()
        self.vista.show_msg_open_manual_succesfully("Creando el archivo \nHTML de TOKENS")
    
    #*Funcion para limpiar el log de los tokens
    def clean_log_tokens(self):
        self.modelo.clean_lts_tokens()
        self.vista.show_msg_open_manual_succesfully("Se ha limpiado el \nlog de tokens")
    
    def show_user_manual(self):
        self.modelo.open_user_manual()
        self.vista.show_msg_open_manual_succesfully("Abriendo el Manual \nde Usuario...")
    
    def show_technical_manual(self):
        self.modelo.open_technical_manual()
        self.vista.show_msg_open_manual_succesfully("Abriendo el Manual \nTécnico...")