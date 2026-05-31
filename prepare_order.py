"""
Ejercicio 1: Sistema de comida rápida
 
Implementar un paquete llamado ‘products' que tiene dos módulos: ‘food_package.py' y ‘product.py', con la siguiente estructura:

products/
        __init__.py
        food_package.py
        product.py

El módulo food_package.py contendrá una clase abstracta denominada 'FoodPackage' con dos funciones abstractas: 'def pack(self)  -> str ' y 'def material(self) -> str '. Esta clase nos permite crear un tipo específico de paquete o envoltura dependiendo del tipo de alimento a empacar, por ejemplo:

Un vaso de soda puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Una hamburguesa puede ser empacada en un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las siguientes clases ‘Wrapping’, ‘Bottle’, ‘Glass’ y ‘Box’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Wrapping’ se puede definir como:

class Wrapping(FoodPackage):  
  def pack(self):
    return "Food Wrap Paper"
  def material(self):
    return "Aluminium" 

El módulo 'product.py’ contendrá una clase abstracta denominada 'Product' con dos funciones abstractas: 'def type(self) -> str' y 'def foodPackage(self)-> FoodPackage. Esta clase nos permita crear un producto específico y relacionarlo con su tipo de empaque por ejemplo:

Un producto con código de barras G1, es una soda Sprite cuyo precio es de 5 euros, pertenece al tipo Soda y puede ser empacado en un paquete tipo vaso y el material puede ser cartón. 
Un producto con código de barras H1, es una hamburguesa Bacon  cuyo precio es de 15 euros, pertenece al tipo Hamburger y puede ser empacado en un paquete un paquete tipo envoltura de papel y el material puede ser aluminio.

En el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Hamburger’, ‘Soda’, ‘Drink’ y ‘HappyMeal’, es decir, de forma parecida al módulo anterior, estas deben implementar los métodos anteriores y devolver un valor. Por ejemplo, la clase ‘Hamburger’, se puede definir como:

class Hamburger(Product):
    def __init__(self, id:str, name:str, price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburger"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
        
Implementar un paquete llamado ‘users' que tiene un módulo ‘user.py', con la siguiente estructura:

users/
        __init__.py
        user.py

El módulo 'user.py' contendrá una clase abstracta denominada ‘User’ que tiene un constructor por defecto para los siguientes datos 'def __init__(self, dni:str, name:str, age:int) ', con una función abstracta: 'def describe(self) '.

Luego en el mismo módulo se deberán incluir las implementaciones concretas para cada una de las clases ‘Cashier’ y ‘Customer’, es decir, estas deben implementar los métodos anteriores y devolver un valor. Adicionalmente, estas clases se diferencian por los parámetros que reciben sus constructores, por tanto, debemos hacer uso de herencia para inicializar el constructor de la clase padre y agregar características propias a cada clase.  

Implementar un paquete llamado 'util' que tiene dos módulos, denominados 'file_manager.py' y 'converter.py’, con la siguiente estructura:

util/
        __init__.py
        file_manager.py
        converter.py

El módulo ‘file_manager.py' contendrá una clase ‘CSVFileManager’ la cual es una implementaciòn libre y debe incluir las funciones:

La función 'def read(self)' lee un archivo en formato CSV y permite exportar su resultado como un Data Frame.
La función 'def write(self, dataFrame)' convierte un Data Frame en un archivo CSV. Esta es una función opcional, se deja al estudiante la implementación.

Los archivos en formato CSV se encuentran en la ruta “data/”, a continuación, se describe el contenido de cada archivo:

cashiers.csv: Información de los cajeros que harán uso del sistema.
customers.csv: Información de los clientes que harán uso del sistema.
drinks.csv: Información de los diferentes tipos de bebidas.
sodas.csv: Información de los diferentes tipos de gaseosas.
hamburgers.csv: Información de los diferentes tipos de hamburguesas.
happyMeal.csv: Información de los diferentes tipos de happy meals.

El módulo 'converter.py' contendrá una clase denominada ‘Converter’ con una función abstracta para convertir las filas de un Data Frame en instancias de objetos. La función sería ‘def convert(self, dataFrame, *args) -> list’. Adicionalmente esta clase debe incluir un método que permite imprimir la información de los objetos ‘def print(self, list)’. En el mismo módulo se deberán incluir las implementaciones específicas que permitan leer los archivos en formato CSV y convertir sus filas en objetos de cada clase utilizando los paquetes product y users.

Implementar un paquete llamado 'orders' que tiene un módulo 'order.py', con la siguiente estructura:

orders/
        __init__.py
        order.py

El módulo 'order.py' contendrá una clase denominada ‘Order’ con un constructor ‘def __init__(self, cashier:Cashier, customer:Customer):’, el cual permite inicializar la clase con los datos del cajero, del cliente y la lista de productos vacía por defecto. Además, debe incluir tres funciones para agregar productos, calcular el total de la orden solicitada y mostrar la información de la orden que está siendo procesada. Las funciones son ‘def add(self, product: Product)', ' def calculateTotal(self) -> float' y ‘def show(self)’, respectivamente.

Finalmente tendremos una clase principal que se llamará ‘PrepareOrder’ en la cual se deberá realizar una implementación que permita integrar los diferentes módulos empleados para leer los archivos en formato CSV y convertirlos en objetos. La implementación de esta clase es libre, es decir, no indicaremos las funciones que debe contener, pero la funcionalidad de la clase debe permitir crear una opción de menú que permita buscar los clientes, los cajeros y los productos para finalmente crear una orden. 

Se sugiere utilizar los métodos de entrada de teclado para leer los datos del dni cajero, cliente e id de los productos. 


A grandes rasgos, la aplicación seguiría los siguientes pasos:

1)	Leer archivos en formato csv: 
a.	Leer cada archivo en formato csv: Utilizar una instancia de la clase 'CSVFileManager' y llamar al método 'read()'.
2)	Convertir a listas de objetos:
a.	Convertir cajeros: Función creada por el alumno  
b.	Convertir clientes: Función creada por el alumno 
c.	Convertir productos: Función creada por el alumno 
3)	Preparar Orden:
a.	Buscar cajero por dni: Función creada por el alumno y debe devolver una instancia de tipo cajero.
b.	Buscar cliente por dni. Función creada por el alumno y debe devolver una instancia de tipo cliente.
c.	Inicializar Orden: Utilizar una instancia la clase 'Order', e inicializar con su constructor por defecto.
d.	Mostrar productos a vender: Función creada por el alumno.
e.	Escoger productos: Función creada por el alumno.
f.	Agregar productos: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'add()'.
4)	Mostrar Orden: Utilizar la instancia la clase 'Order', del paso c y llamar al método 'show()'


"""
#Write your code here
from users import *
from util import *
from products import *
from orders.order import Order
import datetime


dataframe_cashiers = CSVFileManager("data/cashiers.csv").read()             #Lee todos los archivos csv
dataframe_customers = CSVFileManager("data/customers.csv").read()
dataframe_drinks = CSVFileManager("data/drinks.csv").read()
dataframe_hamburgers = CSVFileManager("data/hamburgers.csv").read()
dataframe_happyMeal = CSVFileManager("data/happyMeal.csv").read()
dataframe_sodas = CSVFileManager("data/sodas.csv").read()



lista_cashiers = CashierConverter().convert(dataframe_cashiers)             # Convierte los dataframes en listas de objetos
lista_customers = CustomerConverter().convert(dataframe_customers)          # En cada caso los objetos son, clientes,cajeros,etc
lista_drinks =  ProductConverter().convert(dataframe_drinks)
lista_hamburgers =  ProductConverter().convert(dataframe_hamburgers)
lista_happyMeal = ProductConverter().convert(dataframe_happyMeal)
lista_sodas = ProductConverter().convert(dataframe_sodas)
lista_productos = lista_drinks + lista_sodas + lista_hamburgers +  lista_happyMeal      # Creo una lista donde estan todos los productos juntos en forma de objetos


class PrepareOrder:
    def dni_cost (self,DNI):                           # Creo la clase principal que prepara la orden con sus funciones
        cliente = None                                 # Las 2 primeras funciones hacen lo mismo pero con los clientes y cajeros.
        for i in lista_customers:                      # Sirven para comprobar si los DNI que el usuario da existen en nuestras bases de datos.
            if i.dni == DNI:
                cliente = i
                return cliente
    def dni_cash (self,DNI):
        cajero = None
        for i in lista_cashiers:
            if i.dni == DNI:
                cajero = i
                return cajero
    def seleccion (self,pedido:object):                     # La función de selección es todo el ciclo que pregunta por los productos
        ProductConverter().descripcion(lista_productos)     # Hay una consecución de 2 whiles anidados en 1 general.
        flag = True                 
        lista_id = []
        while flag == True:                                                                                      # El while general marca el ciclo principal para repetir todas las acciones
            flag_2 = False                                                                                       # Esto segun el usuario responda si o no a la pregunta de querer añadir mas productos.
            while flag_2 == False:                          
                producto = input("Elija un producto de la lista, escribe el id del producto que desee:")         # Los otros dos while manejan la posibilidad de que las contestaciones a los inputs demandados sean validas.
                if producto in [str(i.id) for i in lista_productos]:
                    lista_id.append(producto)
                    flag_2 = True
                else:
                    print("No se encuentra el id en la base de datos, vuelva a escribir un id valido.")
            flag_3 = False
            while flag_3 == False:
                marcador = input("Desea algun otro producto?:")
                if "si" in marcador.lower():
                    flag = True
                    flag_3 = True
                elif "no" in marcador.lower():
                    flag = False
                    flag_3 = True
                else:
                    print("Escriba una respuesta que contenga si o no.")
        for i in lista_id:                                                  # Finalmente añade todos los productos de la lista de productos seleccionada en la instancia del pedido.
            for u in lista_productos:
                if i == u.id:
                    pedido.add(u)


CashierConverter().descripcion(lista_cashiers)                          # Aqui muestra la lista de cajeros y pide introducir el dni, y guarda el cajero seleccionado.
respuesta_valida_cash = False                                           # El bucle while maneja la posibilidad de que el input no coincida con ningun DNI de la base de datos.
while respuesta_valida_cash == False:
    DNI_cajero = int(input("Introduzca DNI del cajero:"))
    if DNI_cajero in [int(i.dni) for i in lista_cashiers]:
        cajero_seleccionado = PrepareOrder().dni_cash(DNI_cajero)
        respuesta_valida_cash = True
    else:
        print("No se ha encontrado el cajero en la base de datos, vuelva a introducir un DNI valid.")


CustomerConverter().descripcion(lista_customers)                        # Aqui es el mismo proceso visto anteriormente con los cajeros pero con clientes.
respuesta_valida_cust = False
while respuesta_valida_cust == False:
    DNI_cliente = int(input("Introduzca el dni del cliente:"))
    if DNI_cliente in [int(i.dni) for i in lista_customers]:
        cliente_seleccionado = PrepareOrder().dni_cost(DNI_cliente)
        respuesta_valida_cust = True
    else:
        print("No se ha encontrado el cajero en la base de datos, vuelva a introducir un DNI valid.")

pedido = Order(cajero_seleccionado,cliente_seleccionado)                    # Genera el pedido creando una instacia

PrepareOrder().seleccion(pedido)                                            # Aqui se llama a la función que confecciona todo el pedido
pedido.show()                                                               # Por ultimo se muestra el pedido.

pedido_en_lista = [[pedido.cashier.dni,pedido.customer.dni,datetime.datetime.now(),pedido.calculateTotal()]]                        # En estas ultimas lineas se hace una lista de listas con las variables de interes
df_pedido_en_lista = pd.DataFrame(pedido_en_lista, columns=["DNI CAJERO","DNI CLIENTE","FECHA","PRECIO TOTAL DEL PEDIDO"])          # Para posteriormente convertirlo en un dataframe que podremos llevar a un archivo CSV que se creara en data
escritura_csv(df_pedido_en_lista)