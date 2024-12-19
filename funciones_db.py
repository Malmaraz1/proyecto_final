import sqlite3
def generar_tabla():
 try:
    conexion = sqlite3.connect("proyectoFinal/Inventario.db")
    cursor = conexion.cursor()
    cursor.execute(
       '''CREATE TABLE IF NOT EXISTS productos(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       nombre TEXT NOT NULL,
       descripcion TEXT,
       categoria TEXT NOT NULL,
       cantidad INTEGER NOT NULL,
       Precio REAL NOT NULL
       )'''
       )
    conexion.commit()    
       
 except sqlite3.Error as error:
        print(f"Eror al crear la tabla: {error}")
        
 finally:
     conexion.close()
 
def  db_ingresar_producto(producto):
     conexion = sqlite3.connect("proyectoFinal/Inventario.db")
     cursor = conexion.cursor()   
     cursor.execute("INSERT INTO productos (nombre , descripcion , categoria , cantidad , precio) VALUES (?,?,?,?,?)",   
          (producto["nombre"] , producto["descripcion"] , producto["categoria"] , producto["cantidad"] ,producto["precio"] )
          )
     conexion.commit()
     conexion.close()
 
def  db_get_producto():
     conexion = sqlite3.connect("proyectoFinal/Inventario.db")
     cursor = conexion.cursor()
     cursor.execute("SELECT * FROM productos")
     listProducto = cursor.fetchall()
     conexion.close()
     return listProducto
def  db_get_id_productro(idproducto):
    conexion = sqlite3.connect("proyectoFinal/Inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id =?",
    (idproducto,)
    )
    producto = cursor.fetchone()
    conexion.close()
    return producto 
def db_actualizar_producto(idproducto,nuevaCantidad):
    
    conexion = sqlite3.connect("proyectoFinal/Inventario.db")
    cursor = conexion.cursor()
    
    cursor.execute("UPDATE productos SET cantidad = ? WHERE id =?",
    (nuevaCantidad,idproducto)
    )
    conexion.commit()
    conexion.close() 
def db_eliminar_producto(idproducto):
    conexion = sqlite3.connect("proyectoFinal/Inventario.db")
    cursor = conexion.cursor()
    
    cursor.execute("DELETE FROM productos WHERE id =?",
    (idproducto,)
    )
    conexion.commit()
    conexion.close()
def db_get_minimo_stock(minimo_stock):
    conexion = sqlite3.connect("proyectoFinal/Inventario.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad < ? ",
    (minimo_stock,)
    )
    listproducto  = cursor.fetchall()
    conexion.close()
    return listproducto   