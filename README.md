# Reto 7
## estructura de datos python y queues.
En este reto ponemos en practica los temas vistos en clase acerca de tuplas, listas, añadir y sacar información de las clases, entre otros.

primero  :
```python
class Order:                   #clase order con la que iniciamos
    def __init__(self):        #funcion donde se almacenarán los datos.         
        self.lista_cuenta = []    
        self.items = []
       
 # meter y sacar    
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
    
    def cuenta(self):                # función que nos dara la cuenta total
        self.total = 0                
        
        for item in self.lista_cuenta:
            self.total += item.neto()  

        return self.total       
    
    def item(self):                       #Función que nos dara todos los datos almacenados
        for item in self.lista_cuenta:
            self.items.append(item.mostrar())
        lista_items = ( list(map(str, self.items)))
        return (",".join(lista_items))
```
En esta parte, vemos diferentes cosas, por ejemplo; "la añadidura, desencolar, item"... en pocas palabras, los que nos darán el almacenamiento, la eliminación y nos muestra 
los diferentes items.

En otra parte:
```python
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
```
En esta parte vemos una nueva clase, esta nos dara la posibilidad de tener varias... *ordenes* (por así decirlo), de añadir oredenes y eliminar ordenes.

## "Practica" 
Bueno... esto unido seria: 
Los pedidos (mesas) se le añaden diferentes productos (cuantos quieran),  se dividen cada una entre la cantidad de mesas (por ejemplo; acá son tres mesas), luego hice un pedido 2.0
(como una mesa pero con información de más) llamado como la mesa y el numero pero separado por un **"_"**, esto nos servira para usarlo en las colas y demás.
```python
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
```

Ahora Vamos a usar las mesas 2.0 y las vamos a imprimir, dando el resultado del total del dinero, del total de items y su precio cada uno, con sus añadiduras, dividido cada una 
por sus mesas... en pocas palabras como una factura.
```python
cola = ColaFIFO()
cola.encolar(mesa_0)
cola.encolar(mesa_1)
cola.encolar(mesa_2)

while not cola.esta_vacia():
  print("Atentiendo a la", cola.desencolar())
```
y así tendriamos..... momento! 

vamos también a meter nombre de tuplas, y esto se consigue muy facilmente, solo con import y añadimos una variable con el nombre tuple.

```python
from collections import namedtuple  #la importación.... (ja)

class MenuItem():                                         # Una clase ...
    def __init__(self, nombre : str, precio : float):
        self.nombre = nombre                           
        self.precio = precio        
    def neto(self):                               
        return self.precio

# Tupla con nombre para representar las caracteristicas que tendran todas las clases de aqui en adelante.    
MenuItems = namedtuple("Menuitem", ["Nombre", "Precio", "Adición"])
```
Bueno....y ahora que?
Aunque pareciera que ahí ya acabo y cumple la función de existir, pues no. 
Anteriormente habia usado una funcion *x* llamada mostrar, solo para mostrar mientras programaba, pero esta vez hice un gran cambio,
pues ahora esta es visible y esta es util para el espectador, pues al final cuando se tenga todo, la función llamara a mostrar y mostrar lo que se pidió, y aquí 
es dónde brilla nuestro nombre tupla. 

 ``` python
class  Almuerzo(MenuItem):                  # clase ....almuerzo
    def __init__(self, nombre : str, precio : float, sopa: bool):  
        super().__init__(nombre, precio)                        
        if sopa == True:                                        
            self.sopa = 'con sopa'              # Cosas
        elif sopa == False:
            self.sopa = 'sin sopa'
            self.precio = self.precio -500       #cosas

        # aqui creamos una variable llamada almuerzo (ahora que lo pienso...¿no es mucho texto?), esta trae a la funcion tuplenombre y....
          #        Llama    remplaza   y la usa según esta clase 
        almuerzo=MenuItems(self.nombre, self.precio, self.sopa)
        self.almuerzo = almuerzo


    def mostrar(self):  #    pues lo nombra y lo trae..... 
        return f"Nombre: {self.almuerzo.Nombre}\n Sopa: {self.almuerzo.Adición}\n Precio: {self.almuerzo.Precio}\n\n" 
    # y así por 2 más
class Jugo(MenuItem):
  ...
  ...
  def mostrar(self):
        return f"\nNombre: {self.bebida.Nombre}\n jugo: {self.bebida.Adición}\n Precio: {self.bebida.Precio}\n\n"
class postre(MenuItem):
  ...
  ...
  def mostrar(self):
        return f"\nNombre: {self.postre.Nombre}\n jugo: {self.postre.Adición}\n Precio: {self.postre.Precio}\n\n"
# Ahora que lo pienso... creo que se podria poner todas en una sola clase o en un "def" de tal manera que no se necesite poner una por una... sino traerla...
```
Bueno ahora si, esto que mostre aca con "mostrar" es lo que se ve como print al final entre otras cosas no muy significativas.

## llegamos !
Bueno ya para concluir, creo que lo de las tuplas nombre me gusto peeero no le vi mucha utilidad hasta.... hace 10 segundos... pero lo de las colas y demas me gusto bastante,
al inicio queria ponerle limite de mesas y que fuera sacando de acuerdo a la cantidad de cosas que añadio... como en la vida real, 
pero cuando lo puse no supe como quitar datos y sacarlos a mi antojo. y pues eso me obligaba que funcionara siempre al limite o menos
y pues en realidad no supé como hacer ahi, por que cada vez  que se excedia mi computador se trababa, así que preferi algo mas sencillito comó lo que pudimos ver.
el programa corre bien, añade, quita, muestra... ¡que más se le puede sacar al pobre! (todo sobrexplotado el pobre... bueno no tanto como Shape).
## Palabras finales.
la verdad lo que modifique solo fue lo que mostre acá, el código no es muy complejo pero es completo. 
Y en pocas palabras lo que hice fue :  que le pasen una datos eso lo toma como una factura, si se añaden por aparte este la toma nueva como otra mesa y al final hace una recopilación de 
todo lo que conoce y sabe, si tiene 20 facturas con 40 productos cada uno... pued bueno le corre esas vainas.
Espero que el que vea esto almenos me perdone mi ortografia, y que almenos le alla ...(:b)  (no mentiras)... que le haya sacado asi sea una sonrisa.


