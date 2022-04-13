from tkinter import Tk as tk 
from tkinter import Label, Button, Entry, Frame, messagebox
from tkinter import ttk

class ventanaPrincipal(tk):

    def __init__(self):
        super().__init__()
        self.title("La Liga Bot")
        
        ancho_ventana = 1100
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
        lcomando = len(comando) 
        if comando != "":
            print(comando)
            self.texto_ingresado = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado.grid(row=1,column=1, sticky='nsew', padx=5)
            
            self.texto_ingresado2 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado2.grid(row=2,column=0, sticky='nsew')
            
            self.texto_ingresado3 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado3.grid(row=3,column=1, sticky='nsew')
            
            self.texto_ingresado4 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado4.grid(row=4,column=0, sticky='nsew')
            
            self.texto_ingresado5 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado5.grid(row=5,column=1, sticky='nsew')
            
            self.texto_ingresado6 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado6.grid(row=6,column=0, sticky='nsew')
            
            self.texto_ingresado7 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado7.grid(row=7,column=1, sticky='nsew')
            
            self.texto_ingresado8 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado8.grid(row=8,column=0, sticky='nsew')
            
            self.texto_ingresado9 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado9.grid(row=9,column=1, sticky='nsew')
            
            self.texto_ingresado10 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado10.grid(row=10,column=0, sticky='nsew')
            
            self.texto_ingresado11 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado11.grid(row=11,column=1, sticky='nsew')
            
            self.texto_ingresado12 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado12.grid(row=12,column=0, sticky='nsew')
            
            self.texto_ingresado13 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado13.grid(row=13,column=1, sticky='nsew')
            
            self.texto_ingresado14 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado14.grid(row=14,column=0, sticky='nsew')
            
            self.texto_ingresado15 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado15.grid(row=15,column=1, sticky='nsew')
            
            self.texto_ingresado16 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado16.grid(row=16,column=0, sticky='nsew')
            
            self.texto_ingresado17 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado17.grid(row=17,column=1, sticky='nsew')
            
            self.texto_ingresado18 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado18.grid(row=18,column=0, sticky='nsew')
            
            self.texto_ingresado19 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado19.grid(row=19,column=1, sticky='nsew')
            
            self.texto_ingresado20 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado20.grid(row=20,column=0, sticky='nsew')
            
            self.texto_ingresado21 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado21.grid(row=21,column=1, sticky='nsew')
            
            self.texto_ingresado22 = Label(self.textarea, text=comando, bg="#121707", fg="#FBFCFC", font=("Helvetica", 10))
            self.texto_ingresado22.grid(row=22,column=0, sticky='nsew')
        else:
            messagebox.showerror("Error!!!","La caja de texto no contiene ningún comando a leer")
    
    #*Se inicializan los componentes a usar de la ventana
    def create_widgets(self):
        
        self.textarea = Frame(self, bg="#001d36") #, bg="#121707", fg="white", font=("Arial", 12, "bold"), state="disabled"
        self.scrollbar =  ttk.Scrollbar(self.textarea, orient='vertical', command=self.textarea) #!Nos quedamos aqui
        self.reporte_errores = Button(self, text="Reporte de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.clean_log_errors = Button(self, text="Limpiar log de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 14), borderwidth=5)
        self.reporte_tokens = Button(self, text="Reporte de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.clean_log_tokens = Button(self, text="Limpiar log de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.m_u = Button(self, text="Manual de usuario",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.m_t = Button(self, text="Manual técnico",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
        self.send = Button(self, text="ENVIAR",bg="#5d2147", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5, command=self.moveTextToTextArea)
        self.caja_texto = Entry(self,bg="#121128", fg="#FBFCFC", font=("Helvetica", 12))
        self.bienvenida = Label(self.textarea, text="Bienvenido a La Liga Bot, Ingrese un comando" ,bg="#121707", fg="#FBFCFC", font=("Helvetica", 12)) #, anchor='e'
        
        # self.textarea.insert(0.0,"Bot: Bienvenido a La Liga Bot, Ingrese un comando\n")
        # self.textarea.config(state='disabled')
        #* hola soy un nuevo posible comando a utilizar
        """
        RESULTADO "Real Madrid" vs "Villareal" TEMPORADA <2019-2020>
        JORNADA 1 TEMPORADA <1996-1997> -f jornada1Reporte | JORNADA 12 TEMPORADA <1996-1997>
        GOLES TOTAL “Valencia” TEMPORADA <1998-1999> | GOLES LOCAL “Zaragoza” TEMPORADA <1998-1999>
        TABLA TEMPORADA <2018-2019> | TABLA TEMPORADA <1996-1997> -f reporteGlobal1
        PARTIDOS “Real Madrid” TEMPORADA <1999-2000> -ji 1 -jf 18 | PARTIDOS “Español” TEMPORADA <1999-2000> -f reporteEspanol
        TOP SUPERIOR TEMPORADA <2000-2001> | TOP INFERIOR TEMPORADA <1999-2000> -n 3
        ADIOS
        """ 
        
        self.textarea.place(x=20, y= 20, width=850, height=500)
        self.bienvenida.grid(row=0,column=0, sticky="nsew")
        self.scrollbar.place(x=835, y=0, height=500)
        
        self.reporte_errores.place(x=885, y=20, width=200, height=30)
        self.clean_log_errors.place(x=885, y= 60, width=200, height=30)
        self.reporte_tokens.place(x=885, y= 100, width=200, height=30)
        self.clean_log_tokens.place(x=885, y= 140, width=200, height=30)
        self.m_u.place(x=885, y= 180, width=200, height=30)
        self.m_t.place(x=885, y= 220, width=200, height=30)
        self.send.place(x=885, y=530, width=200, height=45)
        self.caja_texto.place(x=20, y = 530, width=850, height=45)
        
        #*Hover en python
        self.send.config(activeforeground="#5d2147", activebackground="#FBFCFC")
