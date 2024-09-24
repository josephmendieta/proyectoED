# Modelo de Oferta y Demanda con Ecuaciones Diferenciales

Este proyecto implementa un modelo basado en ecuaciones diferenciales para analizar la relación entre oferta, demanda y precios en el contexto de las industrias manufactureras. Utiliza Python y las bibliotecas `numpy` y `scipy` para resolver la ecuación diferencial y simular el comportamiento del precio a lo largo del tiempo.

## Descripción del Proyecto

El modelo se basa en la siguiente ecuación diferencial:

\[ a_1 p'(t) + b_1 p(t) = a_3 - b_3 \]

Donde:
- \( p(t) \) es el precio en función del tiempo.
- \( p'(t) \) es la tasa de cambio del precio.
- \( a_1, b_1, a_3, b_3 \) son constantes que definen la oferta y demanda.

El prototipo permite simular y visualizar cómo varía el precio en función del tiempo, proporcionando una herramienta útil para la toma de decisiones en la gestión de la producción e inventarios.

## Avances

En esta sección se presentan los avances realizados en el desarrollo del prototipo del modelo basado en ecuaciones diferenciales, diseñado para analizar la relación entre oferta, demanda y precios en el contexto de las industrias manufactureras.

El prototipo implementado en Python utiliza la biblioteca `scipy` para resolver una ecuación diferencial que describe cómo el precio cambia con el tiempo, en función de la oferta y la demanda. Este modelo proporciona una herramienta analítica que permite simular el comportamiento del precio, facilitando el estudio del equilibrio de precios y su impacto en la gestión de la producción e inventarios.

El código del prototipo está disponible en el siguiente repositorio de GitHub:

[Repositorio del Prototipo en GitHub](https://github.com/usuario/proyecto-ejemplo)

Este enlace lleva al repositorio donde se puede acceder al código fuente, así como a las instrucciones necesarias para la instalación y ejecución del modelo. Se planean futuras mejoras y funcionalidades para continuar avanzando en la optimización de la producción e inventarios en industrias manufactureras.

## Navegación al Directorio del Proyecto

Para navegar al directorio del proyecto después de clonar el repositorio, utiliza los siguientes comandos en la terminal:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/usuario/proyecto-ejemplo.git

## Instalación de Dependencias

pip install numpy scipy matplotlib

## Uso

Para ejecutar el modelo, puedes usar el siguiente comando en la terminal: 

python modelo.py