import sqlite3

conexion=sqlite3.connect("bd1.db") # se coneta a la base de datos bd1.db y empieza a insertar valores
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
conexion.commit()
conexion.close()