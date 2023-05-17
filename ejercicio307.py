import sqlite3 # importara libreria sqlite3

conexion=sqlite3.connect("bd1.db") # coneccion con la bbdd
precio=float(input("Ingrese un precio:")) # variable precio que es un float y su valor lo ingresa el usuario
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, )) # variable cursor que ejecuta una consulta sql
filas=cursor.fetchall() # variable fila que contiene la fila de los resultados de la consulta sql anterior 
if len(filas)>0: # si la longitud de fila es mas grande que cero entra 
    for fila in filas: # recorre las filas
        print(fila) # imprime la fila
else: # si no hay regsultado
    print("No existen artículos con un precio menor al ingresado.")
conexion.close() # cerrar coneccion