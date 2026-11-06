# comentario de una sola linea

"""
Este
es
un
comentario
multilinea
"""

# ¿Qué es python?
"""
python es un lenguaje de programación INTERPRETADO, es decir, que se ejecuta línea 
por línea en tiempo de ejecución.Fue creado por Guido van Rossun y es conocido por 
su sintaxis clara y legible.
Python tiene la filosofia de que el código deber ser legible y sencillo,promoviendo 
la claridad y la simplicidad en la programación.
Fue lanzado en el 1991,tomando popularidad rápidamente debido a lo simple que
era escribir código en el.
Python puede ser utilizado para:
    - Aplicaciones de escritorio
    - Aplicaciones web
    - Ciencia de datos
    - Inteligencia artificial (Agentes como ChatGPT, Gemini,etc. están basados en 
    Python)
    - Automatización de tareas 
"""
# Características de Python
"""
-Python es un lenguaje de programación de alto nivel, interpretado y de propósito
general.
-Es muy conocido en el mercado debido a su sintaxis clara y legible, lo cual facilita
el aprendizaje y la escritura de código eficiente y mantenible.
-Además,cuenta con una amplia biblioteca estándar y una gran comunidad de
desarrolladores que contribuyen con paquetes y módulos adicionales, lo que facilita 
el realizar diversas tareas de programación sin necesidad de reinventar la rueda.
Tambien es conocido por su portabilidad, ya que puede ejecutarse en diferentes
Sistemas Operativos como Windows, Linux, McOS, entre otros, sin necesidad de 
realizar cambios grande en el código fuente.
-De igual forma,Python doporta múltiples paradigmas de programación, entre los que
se encuentra la Programación Orientada a Objetos, la Programación Funcional y la
Programación Imperativa.
-También permite la Programación basada en eventos y la programación concurrente,
lo que lo hace muy versátil para diferentes tipos de apliciones.
-Además,Python cuenta con un sistema de gestión de paquetes eficientes mediante 
herramientas como pip, lo que facilita la instalación y la actualización de bibliotecas
externas.
"""

# Declaración de variables
nombre = "Pedrito Martinez" # Este es un tipo de dato "string"(Cdena de texto)
edad = 8 # Este un tipo de dato "int" (Número entero)
estatura = 1.25 # Este es un tipo de dato "float" (Número decimal)
is_saludable = True # Este es un tipo de dato "bool"(Booleano: True o False)

"""
En Python, los tipos de datos básicos son:
-int: números enteros, como 8 o -3.
-bool: valores booleanos, True o False.
-str: cadenas de texto, como "Hola".
-Float: Números decimales, como 1.25 o -3.5.
"""

# Imprimiendo las variables concatenadas
print("Nombre: ",nombre,)
print("edad: ", edad)
print("estatura: ", estatura)
print("¿Es saludable?: ", is_saludable)
print("Nombre:", nombre, "Edad: ", edad, " Estatura: ", estatura,
"¿Es saludable: ",is_saludable)

# Interpolación de canedas o f-strings (Cadenas formateadas)
print(f"Nombre: {nombre}, Edad: {edad}, Estatura: {estatura}, ¿Es saludable?: { is_saludable}")