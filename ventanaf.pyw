from tkinter import Tk as tk 
from tkinter import Label, Button, Entry, Frame, scrolledtext, messagebox

class ventanaPrincipal(tk):

    def __init__(self):
        super().__init__()
        self.title("La Liga Bot")
        
        ancho_ventana = 1000
        alto_ventana = 600
        x_ventana = (self.winfo_screenwidth() // 2) - (ancho_ventana//2)
        y_ventana = (self.winfo_screenheight() // 2) - (alto_ventana//2)
        posicion = str(ancho_ventana) + "x"+str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        self.resizable(0, 0)
        self.geometry(posicion)
        self.config(bg="#5e64ad")
        self.create_widgets()

    #*Mueve el texto de la caja de texto al scrolledText
    def moveTextToTextArea(self):
        comando= ""
        comando = self.caja_texto.get()
        lTA = float(len(self.textarea.get(0.0)))
        #print(comando)
        #print(self.textarea.get(0.0, tk.END))
        if comando != "":
            self.textarea.config(state='normal')
            self.textarea.insert(lTA, comando)
            self.textarea.config(state='disabled')
        else:
            messagebox.showerror("Error!!!","La caja de texto no contiene ningún comando a leer")
    
    #*Se inicializan los componentes a usar de la ventana
    def create_widgets(self):
        
        self.textarea = scrolledtext.ScrolledText(self, bg="#121707", fg="white", font=("Arial", 12, "bold")) #, state="disabled"
        self.reporte_errores = Button(self, text="Reporte de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.clean_log_errors = Button(self, text="Limpiar log de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 14), borderwidth=5)
        self.reporte_tokens = Button(self, text="Reporte de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.clean_log_tokens = Button(self, text="Limpiar log de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.m_u = Button(self, text="Manual de usuario",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.m_t = Button(self, text="Manual técnico",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.send = Button(self, text="ENVIAR",bg="#5d2147", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5, command=self.moveTextToTextArea)
        self.caja_texto = Entry(self,bg="#121128", fg="#FBFCFC", font=("Helvetica", 12))
        
        self.textarea.insert(0.0,"Bot: Bienvenido a La Liga Bot, Ingrese un comando\n")
        self.textarea.config(state='disabled')
        
        self.textarea.place(x=20, y= 20, width=750, height=500)
        self.reporte_errores.place(x=785, y=20, width=200, height=30)
        self.clean_log_errors.place(x=785, y= 60, width=200, height=30)
        self.reporte_tokens.place(x=785, y= 100, width=200, height=30)
        self.clean_log_tokens.place(x=785, y= 140, width=200, height=30)
        self.m_u.place(x=785, y= 180, width=200, height=30)
        self.m_t.place(x=785, y= 220, width=200, height=30)
        self.send.place(x=785, y=530, width=200, height=45)
        self.caja_texto.place(x=20, y = 530, width=750, height=45)
        
        #*Hover en python
        self.send.config(activeforeground="#5d2147", activebackground="#FBFCFC")
