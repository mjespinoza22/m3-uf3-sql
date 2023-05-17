import sqlite3 # importa la librearia sqlite3

conexion=sqlite3.connect("bd1.db") # se conecta a la base de datos bd1.bd 
cursor=conexion.execute("select codigo,descripcion,precio from articulos") # almacena los datos en la variable cursor
for fila in cursor: # un for para recorrerlo 
    print(fila) # imprime las filas 
conexion.close() # se cierra la coneccion