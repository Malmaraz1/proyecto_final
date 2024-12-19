def validar_nombre():
 while True:
       nombre = input("Ingrese el nombre del producto: ").strip()
       if not nombre:
           print("No se admite dato nulo ")
       else:
        return nombre  
         
def validad_descripcion():
 while True :
  descripcion = input("Descripcion: ").strip()
  return descripcion
     
def validad_categoria():  
 while True:
  categoria = input("Categoria : ").strip()
  if not categoria:
   print("No se admite dato nulo " )
  else:
   return categoria 

def validar_cantidad():       
  while True:
   try:
     cantidad = int(input("Cantidad: ").strip())
     if not cantidad:
      print("No se admite dato nulo ")
     elif cantidad < 0:
      print("La cantidad debe ser mayor a 0 " )
     else:
      return cantidad   
   except ValueError:
     print(" Error , Tipo de dato no valido ") 
     
def validar_precio():    
  while True:
   try:
     precio = float(input("Precio: ").strip())
     if not precio:
      print("No se admite dato nulo ")
     elif precio < 0:
      print("La precio debe ser mayor a 0 " )
     else:
      return precio   
   except ValueError:
     print(" Error , Tipo de dato no valido ") 
   