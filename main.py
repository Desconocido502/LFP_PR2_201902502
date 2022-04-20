from Vista import Vista
from Modelo import Modelo
from Controlador import Controlador
import tkinter as tk

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title("La Liga Bot")
        #*Se crea el modelo
        modelo = Modelo("modelop")
        
        #*Se crea una vista
        vista = Vista(self)
        
        #*Se crea un controlador
        controlador = Controlador(modelo, vista)
        
        #*Se le da un controlador a la vista
        vista.set_controlador(controlador)

if __name__ == "__main__":
    app = App()
    app.geometry("1100x600")
    app.config(bg="#5e64ad")
    app.mainloop()