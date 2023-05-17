# Se importa la librería sqlite3 para conectarse a una base de datos SQLit
import sqlite3

# Se establece la conexión a la base de datos "bd1.db" (o se crea si no existe)
conexion = sqlite3.connect("bd1.db")

try:
    # Se intenta crear una tabla llamada "articulos" con 3 columnas
    conexion.execute("""CREATE TABLE articulos (
                              codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                              descripcion TEXT,
                              precio REAL
                        )""")
    # Si la tabla se crea con éxito, se imprime un mensaje indicando que se creó la tabla
    print("Se creó la tabla 'articulos' con éxito.")
                        
except sqlite3.OperationalError:
    # Si la tabla ya existe, se maneja la excepción y se imprime un mensaje indicando que la tabla ya existe
    print("La tabla 'articulos' ya existe en la base de datos.")
