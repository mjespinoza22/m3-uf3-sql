import sqlite3 #importa la libreria

conexion=sqlite3.connect("bd1.db") # coneccion con la bd
codigo=int(input("Ingrese el código de un artículo:")) # variable codigo que inserta el usuario
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, )) # variable cursor que ejecuta una consulta sql
fila=cursor.fetchone() # variable fila que contiene la fila de los resultados de la consulta sql anterior 
if fila!=None: # un if si la fila es igual a None
    print(fila) # imprime fila
else:
    print("No existe un artículo con dicho código.")
conexion.close()
