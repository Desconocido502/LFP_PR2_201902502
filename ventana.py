import tkinter as tk
from tkinter import *
from tkinter import ttk
from Partido import Partido
from LectorArchivo import *

global textarea, reporte_errores, clean_log_errors, reporte_tokens, m_u, m_t, send, caja_texto

def moveTextToTextArea():
    global textarea, caja_texto
    ''' 
    Ya no se usara como tal el scrolledtext, en vez de esto se cambiara por un frame, el cual
    almacenara un todos los mensajes que se presentaran al usuario tanto los nombres como
    los comandos.
    '''
    comando = ""
    comando = caja_texto.get()
    if comando != "":
        comando += "\n"
        # lTA = float(len(textarea.get("1.0",'end')))
        # print(lTA)
        # print(textarea.get("1.0",'end'))
        # textarea.config(state='normal')
        # textarea.insert(lTA, comando)
        # textarea.config(state='disabled')
        print(comando)
    else:
        messagebox.showerror("Error!!!","La caja de texto no contiene ningún comando a leer")

def crearVentanaPrincipal():
    global textarea, reporte_errores, clean_log_errors, reporte_tokens, m_u, m_t, send, caja_texto
    #Se crea un objeto ventana
    ventana = tk.Tk()
    
    #*Modificando el tamaño de la ventana
    ancho_ventana = 1200
    alto_ventana = 600
    x_ventana = (ventana.winfo_screenwidth() // 2) - (ancho_ventana//2)
    y_ventana = (ventana.winfo_screenheight() // 2) - (alto_ventana//2)
    posicion = str(ancho_ventana) + "x"+str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.resizable(0, 0)
    ventana.geometry(posicion)
    ventana.config(bg="#5e64ad")
    
    textarea = Frame(ventana) #, state="disabled", fg="white", font=("Arial", 12, "bold")
    reporte_errores = Button(ventana, text="Reporte de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    clean_log_errors = Button(ventana, text="Limpiar log de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 14), borderwidth=5)
    reporte_tokens = Button(ventana, text="Reporte de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    clean_log_tokens = Button(ventana, text="Limpiar log de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    m_u = Button(ventana, text="Manual de usuario",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    m_t = Button(ventana, text="Manual técnico",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    send = Button(ventana, text="ENVIAR",bg="#5d2147", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5, command=moveTextToTextArea)
    caja_texto = Entry(ventana,bg="#121128", fg="#FBFCFC", font=("Helvetica", 12))
    
    textarea.place(x=20, y= 20, width=950, height=500)
    reporte_errores.place(x=985, y=20, width=200, height=30)
    clean_log_errors.place(x=985, y= 60, width=200, height=30)
    reporte_tokens.place(x=985, y= 100, width=200, height=30)
    clean_log_tokens.place(x=985, y= 140, width=200, height=30)
    m_u.place(x=985, y= 180, width=200, height=30)
    m_t.place(x=985, y= 220, width=200, height=30)
    send.place(x=985, y=530, width=200, height=45)
    caja_texto.place(x=20, y = 530, width=950, height=45)
    
    #* Vamos a crear lo restante para que funcione el Frame con la barra de forma correcta
    #*Se crea el lienzo
    mi_canvas = Canvas(textarea)
    mi_canvas.pack(side='left', fill=BOTH, expand=1)
    
    #*Se agrega el scrollbar al lienzo
    mi_scrollbar = ttk.Scrollbar(textarea, orient=VERTICAL, command=mi_canvas.yview)
    mi_scrollbar.pack(side=RIGHT, fill=Y)

    #*Configuro el lienzo
    mi_canvas.configure(yscrollcommand=mi_scrollbar.set)
    mi_canvas.bind("<Configure>", lambda e: mi_canvas.configure(scrollregion=mi_canvas.bbox("all")))
    
    #*Se crea otro frame dentro del lienzo
    textarea2 = Frame(mi_canvas, bg="#121707")
    #*Se agrega este nuevo frame a la ventana en el canvas
    mi_canvas.create_window((0,0), window=textarea2, anchor='nw', width=950)
    
    bienvenida = Label(textarea2, text="Bienvenido a La Liga Bot, Ingrese un comando" ,bg="#121707", fg="#FBFCFC", font=("Helvetica", 11)) #, anchor='e'
    bienvenida.grid(row=0,column=0, sticky="nsew")
    
    salida1 = Label(textarea2, text="generando archivo de resultados de jornada 20 temporada 2015-2016" ,bg="#121707", fg="#FBFCFC", font=("Helvetica", 11)) #, anchor='e'
    salida1.grid(row=2,column=0, sticky="nsew")
    for thing in range(100):
        #Label(textarea2, text="Bienvenido a La Liga Bot, Ingrese un comando").grid(row=thing, column=0, sticky="nsew", pady=10, padx=10)
        Label(textarea2, borderwidth=1 ,relief="raised",text='RESULTADO "Real Madrid" vs "Villareal" TEMPORADA <2019-2020>',bg="#121707", fg="#FBFCFC", font=("Helvetica", 10)).grid(row=thing, column=1, sticky="nsew", pady=10, padx=10)
    
    ventana.mainloop()
