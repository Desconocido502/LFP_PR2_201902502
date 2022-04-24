#* Vista: Es la interfaz de usuario que representa los datos en el modelo.
from tkinter import *
import tkinter as tk
from tkinter import ttk
import time

FONT_BOLD = "Helvetica 13 bold"
FONT_BOLD2 = "Helvetica 12 bold"
BG_BOTTOM = "#140f07"
FG_BOTTOM = "#FBFCFC"

class Vista(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #*Se crean los widgets
        self.create_widgets()
    
    #*Se inicializan los componentes a usar de la ventana
    def create_widgets(self):
        
        self.linea = 0 #*Se usara para llevar el conteo de las lineas del comando
        
        #* Consola donde interactua el usuario y el bot
        self.text_widget = tk.Text(self.parent,bg="#001d36", fg="white", font=FONT_BOLD2)
        self.text_widget.place(x=20, y= 20, width=950, height=500)
        self.text_widget.insert('1.0', "BOT: Bienvenido a La Liga Bot, Ingresa un comando\n\n")
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        #*Scroll bar
        scrollbar = tk.Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.981)
        scrollbar.configure(command=self.text_widget.yview())
        
        #* Bottom bug report
        self.bug_report = tk.Button(self.parent, text="Reporte de errores", bg=BG_BOTTOM, fg=FG_BOTTOM, font=FONT_BOLD, borderwidth=5, command=self.clicked_on_bug_report)
        self.bug_report.place(x=985, y=20, width=200, height=30)
        
        #* Bottom clean log bug
        self.clean_log_bug = tk.Button(self.parent, text="Limpiar log de errores", bg=BG_BOTTOM, fg=FG_BOTTOM, font=FONT_BOLD, borderwidth=5, command=self.clicked_on_clean_log_bug)
        self.clean_log_bug.place(x=985, y= 60, width=200, height=30)

        #* Bottom token report
        self.token_report = tk.Button(self.parent,text="Reporte de tokens", bg=BG_BOTTOM, fg=FG_BOTTOM, font=FONT_BOLD, borderwidth=5, command=self.clicked_on_token_report)
        self.token_report.place(x=985, y= 100, width=200, height=30)
        
        #* Bottom clean log token 
        self.clean_log_token = tk.Button(self.parent, text="Limpiar log de tokens", bg=BG_BOTTOM, fg=FG_BOTTOM, font=FONT_BOLD, borderwidth=5, command=self.clicked_on_clean_log_token)
        self.clean_log_token.place(x=985, y= 140, width=200, height=30)
        
        #* Bottom user manual
        self.user_manual = tk.Button(self.parent, text="Manual de usuario", bg=BG_BOTTOM, fg=FG_BOTTOM, font=FONT_BOLD, borderwidth=5, command=self.clicked_on_user_manual)
        self.user_manual.place(x=985, y= 180, width=200, height=30)
        
        #* Bottom technical manual
        self.technical_manual = tk.Button(self.parent, text="Manual técnico", bg=BG_BOTTOM, fg=FG_BOTTOM, font=FONT_BOLD, borderwidth=5, command=self.clicked_on_technical_manual)
        self.technical_manual.place(x=985, y= 220, width=200, height=30)
        
        #* Bottom send text
        self.send_text = tk.Button(self.parent, text="ENVIAR",bg="#5d2147", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5, command=self.send_data) #, command=self.moveTextToTextArea
        self.send_text.place(x=985, y=530, width=200, height=45)
        
        #* message entry box
        self.msg_var = tk.StringVar()
        self.msg_entry = tk.Entry(self.parent, textvariable=self.msg_var, bg="#121128", fg="#FBFCFC", font=("Helvetica", 12))
        self.msg_entry.place(x=20, y = 530, width=950, height=45)
        
        #*Message
        self.message_label = tk.Label(self.parent, text="", foreground="white", bg="#5e64ad", font=("Helvetica", 12))
        self.message_label.place(x=975, y= 260, width=200, height=40)
        
        #*Establecemos el controlador
        self.controlador = None
        
    def set_controlador(self, controlador):
        #Establecer el controlador
        self.controlador = controlador
    
    def clicked_on_bug_report(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            self.controlador.show_bug_in_html() #*Nos faltaria agregar los errores sintacticos
    
    def clicked_on_clean_log_bug(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            self.controlador.clean_log_bugs() #*Nos faltaria agregar los errores sintacticos
    
    def clicked_on_token_report(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            self.controlador.show_tokens_in_html()
    
    def clicked_on_clean_log_token(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            self.controlador.clean_log_tokens()
    
    def clicked_on_user_manual(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            self.controlador.show_user_manual() #*Se le dice que abra el pdf de manual de usuario
    
    def clicked_on_technical_manual(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            self.controlador.show_technical_manual() #*Se le dice que abra el pdf de manual tecnico
    
    def send_data(self):
        """
        Gestionar evento de clic de botón
        """
        if self.controlador:
            if self.msg_var.get() != "": #*Solo se trabaja si el contenido es diferente de cadena vacia
                msg1 = f"You: {self.msg_var.get()}\n\n" #*Se ordena el comando, para visualizacion
                self.text_widget.configure(state=NORMAL) #*Se prepara la consola para recibir el texto
                self.text_widget.insert(END, msg1) #*Se inserta el comando a la consola
                self.text_widget.configure(state=DISABLED) #* Se cierra para que no se pueda escribir en la consola
                
                self.linea += 2 #*Aumentamos el contador de lineas x2, por cada vez que se ingrese un comando
                #*Se manda el texto ingresado en la caja de texto al controlador, para luego ser analizado en el modelo
                self.controlador.process_data(self.msg_var.get(), self.linea)
                
                self.msg_var.set("")
                
                #*Aqui tendriamos que tener la respuesta del 'bot'
                #*Se tiene que crear otra funcion que sea la que devuelva la salida, y esta es llamada 
                #*Desde el controlador --> funcion => printResponse
            else:
                #print("cadena vacia")
                self.message_label['text'] = "La caja de texto esta vacia!!!\n ingrese un comando!!!"
                self.message_label.after(3000, self.hide_message)
    
    #*Añade respuestas del bot al cuadro de texto
    def printResponse(self, data): #*data puede ser cualquier
        time.sleep(0.3) #* se espera 500 milsemimas de segundo = la mitad de un segundo
        self.text_widget.configure(state=NORMAL) #*Se prepara la consola para recibir el texto
        self.text_widget.insert(END, data) #*Se inserta el comando a la consola
        self.text_widget.configure(state=DISABLED) #* Se cierra para que no se pueda escribir en la consola
    
    def show_msg_open_manual_succesfully(self, message):
        self.message_label['text'] = message
        self.message_label.after(3000, self.hide_message)
        
    #*lIMPIA EL label
    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''
    
    #*Cerrar la ventana
    def quitWindow(self):
        self.parent.quit()