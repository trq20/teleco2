import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

def graficar(em, fm, ec, fc):
    
    time = np.linspace(0,5e-3,10000)    # Lista de valores de t para graficar

    # TODO

    plt.xlabel("")  # Etiqueta para el eje X
    plt.ylabel("")  # Etiqueta para el eje Y
    plt.title("")   # Nombre del gráfico
    plt.grid()      # Dibuja la cuadricula en el gráfico
    # Ejemplo de plt.plot, descomenten para probarlo
    # plt.plot([0,1,2,3],[0,1,4,9],label='Esto es un label')
    plt.legend()    # Muestra las leyendas de lo que hayan graficado
    plt.show()      # Muestra el gráfico


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        sliders = [
            {"name" : "em", "from" : 0, "to" : 10, "label" : "Amplitud moduladora", "res" : .5},
            {"name" : "fm", "from" : 0, "to" : 1e3, "label" : "Frecuencia moduladora", "res" : 50},
            {"name" : "ec", "from" : 0, "to" : 10, "label" : "Amplitud portadora", "res" : .5},
            {"name" : "fc", "from" : 0, "to" : 10e3, "label" : "Frecuencia portadora", "res" : 500}
        ]

        for s in sliders:

            slider = tk.Scale(self, from_ = s["from"], to_=s["to"], label=s["label"], resolution=s["res"], orient="horizontal", sliderlength="10px", length="120px")
            setattr(self, s["name"], slider)
            getattr(self, s["name"]).pack()

        self.draw = tk.Button(self, text="Graficar", command=lambda: graficar(self.em.get(), self.fm.get(), self.ec.get(), self.fc.get()))
        self.draw.pack()
        self.quit = tk.Button(self, text="Salir", command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
