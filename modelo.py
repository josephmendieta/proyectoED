import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función del modelo
def model(p, t, a1, b1, a3, b3):
    dpdt = (a3 - b3 - b1 * p) / a1
    return dpdt

# Función para actualizar la gráfica
def actualizar_grafica():
    # Obtención de los parámetros desde la interfaz
    a1 = float(entry_a1.get())
    b1 = float(entry_b1.get())
    a3 = float(entry_a3.get())
    b3 = float(entry_b3.get())
    p0 = float(entry_p0.get())
    tiempo_max = float(entry_tiempo.get())

    # Definición del tiempo
    t = np.linspace(0, tiempo_max, 100)

    # Resolución de la ecuación diferencial
    p = odeint(model, p0, t, args=(a1, b1, a3, b3))

    # Actualización de la gráfica
    ax.clear()
    ax.plot(t, p, label='Precio')
    ax.set_title('Modelo de Oferta y Demanda')
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Precio (p)')
    ax.grid()
    canvas.draw()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Simulación del Modelo de Oferta y Demanda")

# Etiquetas y entradas para los parámetros
tk.Label(ventana, text="a1 (Tasa de cambio)").grid(row=0, column=0)
entry_a1 = ttk.Entry(ventana)
entry_a1.insert(0, "0.5")
entry_a1.grid(row=0, column=1)

tk.Label(ventana, text="b1 (Precio actual)").grid(row=1, column=0)
entry_b1 = ttk.Entry(ventana)
entry_b1.insert(0, "1.2")
entry_b1.grid(row=1, column=1)

tk.Label(ventana, text="a3 (Nivel de oferta)").grid(row=2, column=0)
entry_a3 = ttk.Entry(ventana)
entry_a3.insert(0, "100")
entry_a3.grid(row=2, column=1)

tk.Label(ventana, text="b3 (Nivel de demanda)").grid(row=3, column=0)
entry_b3 = ttk.Entry(ventana)
entry_b3.insert(0, "20")
entry_b3.grid(row=3, column=1)

tk.Label(ventana, text="p0 (Precio inicial)").grid(row=4, column=0)
entry_p0 = ttk.Entry(ventana)
entry_p0.insert(0, "5.0")
entry_p0.grid(row=4, column=1)

tk.Label(ventana, text="Tiempo máximo").grid(row=5, column=0)
entry_tiempo = ttk.Entry(ventana)
entry_tiempo.insert(0, "10")
entry_tiempo.grid(row=5, column=1)

# Botón para actualizar la gráfica
boton_actualizar = ttk.Button(ventana, text="Actualizar Gráfica", command=actualizar_grafica)
boton_actualizar.grid(row=6, column=0, columnspan=2)

# Configuración de la figura de matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().grid(row=7, column=0, columnspan=2)

# Ejecución de la ventana principal
ventana.mainloop()
