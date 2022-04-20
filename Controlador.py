from Modelo import Modelo
from Vista import Vista

class Controlador():
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
    
    #*Se trae el texto ingresa a la caja de texto
    def process_data(self, data, linea):
        #print(data, linea)
        self.modelo.analisisLexico(data, linea)
    
    #*Funcion para crear el html de los errores
    def show_bug_in_html(self):
        self.modelo.reporteErroresHTML()
        self.vista.show_msg_open_manual_succesfully("Creando el archivo \nHTML de Errores Léxicos")
    
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