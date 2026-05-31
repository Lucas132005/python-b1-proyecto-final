from abc import ABC, abstractmethod
import pandas as pd
from users import *
from products.product import *
from util.listas_python import lista_nativa
#Write your code here

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def descripcion(self, objects):         #Cambio el nombre de la función para que sea mas intuitivo para mi.
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):
    lista_indice = list(dataFrame.index)    #Guardo una variable con los indices del dataframe.
    instancias_Cashier = []                 #Almacen de todas las instancias/objetos creados.
    for i in lista_indice:                  #Bucle para iterar sobre cada uno de los indices
      row = lista_nativa(list(dataFrame.loc[i]))          #Acceder a la fila de cada indice convertida en lista
      cajero = Cashier(*row)                
      instancias_Cashier.append(cajero)       #Convertir los atributos de la lista y crear instancia,luego almacenar
    return instancias_Cashier




class CustomerConverter(Converter):
  def convert(self,dataFrame):
    lista_indice = list(dataFrame.index)   
    instancias_Customer = []                  
    for i in lista_indice:               
      row = lista_nativa(list(dataFrame.loc[i]))         
      cliente = Customer(*row)                
      instancias_Customer.append(cliente)      
    return instancias_Customer


class ProductConverter(Converter):
  def convert(self,dataFrame):
    lista_indice = list(dataFrame.index) 
    instancias_Products = []
    id_column = list(dataFrame["id"])
    if id_column[0][0] == "B":
      for i in lista_indice:               
        row = lista_nativa(list(dataFrame.loc[i]))            
        instancias_Products.append(Drink(*row))
    elif id_column[0][0] == "H" and id_column[0][1] != "M":
      for i in lista_indice:               
        row = lista_nativa(list(dataFrame.loc[i]))             
        instancias_Products.append(Hamburger(*row))  
    elif id_column[0][0] == "H" and id_column[0][1] == "M":
      for i in lista_indice:               
        row = lista_nativa(list(dataFrame.loc[i]))             
        instancias_Products.append(HappyMeal(*row))
    elif id_column[0][0] == "G":
      for i in lista_indice:               
        row = lista_nativa(list(dataFrame.loc[i]))             
        instancias_Products.append(Soda(*row))
    return instancias_Products  