import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definición de parámetros
a1 = 3.0  # constante que afecta la tasa de cambio del precio
b1 = 6.5  # constante que afecta el precio actual
a3 = 1.0  # constante que representa un nivel de oferta
b3 = 6.0   # constante que representa un nivel de demanda

# Definición de la ecuación diferencial
def model(p, t):
    dpdt = (a3 - b3 - b1 * p) / a1  # Ecuación diferencial
    return dpdt

# Condición inicial
p0 = 5.0  # Precio inicial
t = np.linspace(0, 10, 100)  # Tiempo de 0 a 10

# Resolución de la ecuación diferencial
p = odeint(model, p0, t)

# Gráfica de los resultados
plt.plot(t, p)
plt.title('Modelo de Oferta y Demanda')
plt.xlabel('Tiempo')
plt.ylabel('Precio (p)')
plt.grid()
plt.show()
