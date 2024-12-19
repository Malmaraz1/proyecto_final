from funciones_db import *  
from funciones_validacion import *
    
def agregar_producto():
    
    nombre = validar_nombre()
    descripcion = validad_descripcion()
    categoria = validad_categoria()
    cantidad = validar_cantidad()
    precio = validar_precio()
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }
    db_ingresar_producto(producto)    
    
    

def mostrar_producto():
    listaProd = db_get_producto()
    
    if listaProd:
      for producto in listaProd:
        print(producto)
    else:
        print("No hay productos que mostrar")
   
       
def eliminar_producto():
    idproducto = input("id del producto a eliminar: ")
    get_producto =  db_get_id_productro(idproducto)
    if not get_producto:
      print("ERROR: no se ha encontrado ningun producto con el id")
    else:
      print("Se eliminara el siguiente producto")
      print(get_producto)
      confirmacion = input("Ingrese 's' para confirmar o cualquier otro para cancelar: ").lower()
      if confirmacion == "s":
            db_eliminar_producto(idproducto)
            print("Se elimino el producto")
      else:
            print("Operación cancelada.")
      
   
def buscar_producto():
    id_producto = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_get_id_productro(id_producto)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id")
    else:
        print(get_producto)
    
    
def reporte_bajo_stock():
    minimo_stock = int(input("Ingrese el tope de minimo stock: "))
    lista_stock = db_get_minimo_stock(minimo_stock)
    if not lista_stock:
      print("No se ah encontrado ningun producto con el top minimo de stock")
    else:
      for producto in lista_stock:
            print(producto)
    
       
def actualizar_cantidad():
    idproducto = input("Ingrese el id del producto: ")
    get_producto = db_get_id_productro(idproducto)
    if not get_producto:
     print("ERROR: no se ha encontrado ningun producto con la id indiciada")
    else:
     nueva_cantidad = int(input("Nueva cantidad: "))
     db_actualizar_producto(idproducto,nueva_cantidad)
     print("Se actualizo correctamente el producto")
    
  
       
def mostrar_menu():
     print("\n--- Menú de Inventario ---")
     print("1. Agregar producto")
     print("2. Mostrar productos")
     print("3. Actualizar cantidad de producto")
     print("4. Eliminar producto")
     print("5. Buscar producto")
     print("6. Reporte de bajo stock")
     print("7. Salir")    
     opcion = input("Ingrese la opcion deseada: ")
     return opcion
        
                                         
while True:
       
       opcion = mostrar_menu()  # esta aca dentro opcion = input("Elija una opción: ")
       print("Usted selecciono: ", opcion)  # imprime la opción seleccionada por el usuario
      
       if opcion == "1":
         agregar_producto()
       elif opcion == "2":
         mostrar_producto()
       elif opcion == "3":
         actualizar_cantidad()    
       elif opcion == "4":
         eliminar_producto()   
       elif opcion == "5":
         buscar_producto()  
       elif opcion == "6":
         reporte_bajo_stock()  
       elif opcion == "7":  
         print("Adios")
         break
       else:
         print("Opción no válida. Por favor, elija una opción válida.")

         continuar = input(
         "Presione 's' para continuar..."
         ).lower()  
         if continuar == "s":
            break
    



    
    


