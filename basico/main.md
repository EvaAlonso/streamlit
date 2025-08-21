
def main():
   tu código 

if __name__ == '__main__':
    main()

Este bloque de código se conoce como "entry point" o punto de entrada a tu programa

¿Qué significa __name__?
En python cada archivo (.py) tiene una variable especial llamada __name__.
 - Si ejecutas el archivo directamente (por ejemplo python app.py), entonces __name__=="__main__".
 - Si importas ese archivo como módulo dentro de otro (ejemplo import app), entonces __name__ tomará el nombre del archivo ("app" en este caso).

¿Por qué usarlo en Streamlit?
definimos una función main() que organiza toda la aplicación. Al colocar en entry point hace que el código principal se ejecute sólo cuando ejecutas el archivo directamente y no cuando lo importas desde otro script.

Veamos un ejemplo 

def main():
   print("¡Hola, Mundo!") 

if __name__ == '__main__':
    main()

si ejecutas python app.py se imprime ¡Hola, Mundo!
si desde otro archivo haces import app no se ejecuta automáticamente, pero puedes llamar a app.main()
Evita que tu aplicación se ejecute automáticamente al importar el archivo. Es una buena práctica