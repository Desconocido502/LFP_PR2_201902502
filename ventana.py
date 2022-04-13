import tkinter as tk
from tkinter import Label, Button, Entry, Frame, scrolledtext, messagebox

global textarea, reporte_errores, clean_log_errors, reporte_tokens, m_u, m_t, send, caja_texto

def moveTextToTextArea():
    global textarea, caja_texto
    comando = ""
    comando = caja_texto.get()
    print(comando)
    if comando != "":
        comando += "\n"
        lTA = float(len(textarea.get("1.0",'end')))
        print(lTA)
        print(textarea.get("1.0",'end'))
        textarea.config(state='normal')
        textarea.insert(lTA, comando)
        textarea.config(state='disabled')
    else:
        messagebox.showerror("Error!!!","La caja de texto no contiene ningún comando a leer")



def crearVentanaPrincipal():
    global textarea, reporte_errores, clean_log_errors, reporte_tokens, m_u, m_t, send, caja_texto
    #Se crea un objeto ventana
    ventana = tk.Tk()
    
    #*Modificando el tamaño de la ventana
    ancho_ventana = 1000
    alto_ventana = 600
    x_ventana = (ventana.winfo_screenwidth() // 2) - (ancho_ventana//2)
    y_ventana = (ventana.winfo_screenheight() // 2) - (alto_ventana//2)
    posicion = str(ancho_ventana) + "x"+str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.resizable(0, 0)
    ventana.geometry(posicion)
    ventana.config(bg="#5e64ad")
    
    textarea = scrolledtext.ScrolledText(ventana, bg="#121707", fg="white", font=("Arial", 12, "bold")) #, state="disabled"
    reporte_errores = Button(ventana, text="Reporte de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    clean_log_errors = Button(ventana, text="Limpiar log de errores",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 14), borderwidth=5)
    reporte_tokens = Button(ventana, text="Reporte de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    clean_log_tokens = Button(ventana, text="Limpiar log de tokens",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    m_u = Button(ventana, text="Manual de usuario",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    m_t = Button(ventana, text="Manual técnico",bg="#140f07", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5)
    send = Button(ventana, text="ENVIAR",bg="#5d2147", fg="#FBFCFC", font=("Helvetica", 15), borderwidth=5, command=moveTextToTextArea)
    caja_texto = Entry(ventana,bg="#121128", fg="#FBFCFC", font=("Helvetica", 12))
    
    textarea.insert(0.0,"Bot: Bienvenido a La Liga Bot, Ingrese un comando\n")
    textarea.config(state='disabled')
    
    textarea.place(x=20, y= 20, width=750, height=500)
    reporte_errores.place(x=785, y=20, width=200, height=30)
    clean_log_errors.place(x=785, y= 60, width=200, height=30)
    reporte_tokens.place(x=785, y= 100, width=200, height=30)
    clean_log_tokens.place(x=785, y= 140, width=200, height=30)
    m_u.place(x=785, y= 180, width=200, height=30)
    m_t.place(x=785, y= 220, width=200, height=30)
    send.place(x=785, y=530, width=200, height=45)
    caja_texto.place(x=20, y = 530, width=750, height=45)

    ventana.mainloop()
