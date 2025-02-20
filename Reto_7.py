from queue import Queue
from collections import namedtuple


class MenuItem():
    def __init__(self, nombre : str, precio : float):
        self.nombre = nombre                           
        self.precio = precio        

    def neto(self):                               
        return self.precio
# Tupla con nombre para representar un libro    
MenuItems = namedtuple("Menuitem", ["Nombre", "Precio", "Adición"])    

class  Almuerzo(MenuItem):
    def __init__(self, nombre : str, precio : float, sopa: bool):  
        super().__init__(nombre, precio)                        
        if sopa == True:                                        
            self.sopa = 'con sopa'
        elif sopa == False:
            self.sopa = 'sin sopa'
            self.precio = self.precio -500

        almuerzo=MenuItems(self.nombre, self.precio, self.sopa)
        self.almuerzo = almuerzo


    def mostrar(self):
        return f"Nombre: {self.almuerzo.Nombre}\n Sopa: {self.almuerzo.Adición}\n Precio: {self.almuerzo.Precio}\n\n" 

class Jugo(MenuItem):
    def __init__(self, nombre: str, precio: float, agua:bool): 
        super().__init__(nombre, precio)                       
        if agua == True:                                       
            self.agua = "En agua"
        elif agua == False:
            self.agua = "En leche"
            self.precio = self.precio +1500
        bebida=MenuItems(self.nombre, self.precio, self.agua)
        self.bebida = bebida
    def mostrar(self):
        return f"\nNombre: {self.bebida.Nombre}\n jugo: {self.bebida.Adición}\n Precio: {self.bebida.Precio}\n\n"
        
    
class Postre(MenuItem):
    def __init__(self, nombre:str, precio: float, extra: bool):   
        super().__init__(nombre, precio)                           
        if extra == False:                                        
            self.extra= "promedio"
        elif extra == True:
            self.extra = "grande"
            self.precio = self.precio +2000
        postre=MenuItems(self.nombre, self.precio, self.extra)
        self.postre = postre
    def mostrar(self):
        return f"Nombre: {self.postre.Nombre}\n postre: {self.postre.Adición}\n Precio: {self.postre.Precio}\n\n"
 
class Order:
    def __init__(self):                       
        self.lista_cuenta = []
        self.items = []
          
    def añadidura(self, item: "MenuItem"):
        self.lista_cuenta.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None
    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        return self.lista_cuenta
    
    def cuenta(self):
        self.total = 0                
        
        for item in self.lista_cuenta:
            self.total += item.neto()

        return self.total       
    
    def item(self):
        for item in self.lista_cuenta:
            self.items.append(item.mostrar())
        lista_items = ( list(map(str, self.items)))
        return (",".join(lista_items))


class ColaFIFO:
  def __init__(self):
    self.items = []

  def encolar(self, elemento):
    self.items.append(elemento)

  def desencolar(self):
    if not self.esta_vacia():
      return self.items.pop(0)
    else:
      return None

  def esta_vacia(self):
    return len(self.items) == 0

mesa = Order()                                             
mesa.añadidura(Jugo("maracuya", 5000, False)) 
mesa.añadidura(Almuerzo("corriente", 12000, False))
mesa.añadidura(Postre("fresas", 6000, True))


mesa1 = Order()                                             
mesa1.añadidura(Jugo("mora", 5000, False))   
mesa1.añadidura(Almuerzo("bandeja paisa", 25000, True))
mesa1.añadidura(Postre("wafles", 2500, True))


mesa2 = Order()                                             
mesa2.añadidura(Jugo("mango", 5000, True))   
mesa2.añadidura(Almuerzo("corriente", 15000, True))
mesa2.añadidura(Postre("brownie", 1000, True))

mesa_1 = ( f"Mesa 1: Son ${mesa1.cuenta()} pesos.\
            \nFactura de lo que ordeno {mesa1.item()}\
            Resultado ${mesa1.cuenta()} pesos.\n")
mesa_2 = ( f"Mesa 2: Son ${mesa2.cuenta()} pesos.\
            \nFactura de lo que ordeno {mesa2.item()}\
            Resultado ${mesa2.cuenta()} pesos.\n")

mesa_0 = (f"Mesa 0: Son ${mesa.cuenta()} pesos.\
            \nFactura de lo que ordeno {mesa.item()}\
            Resultado ${mesa.cuenta()} pesos.\n")
cola = ColaFIFO()
cola.encolar(mesa_0)
cola.encolar(mesa_1)
cola.encolar(mesa_2)

while not cola.esta_vacia():
  print("Atentiendo a la", cola.desencolar())

