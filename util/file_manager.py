import pandas as pd
import os
class CSVFileManager:
  def __init__(self,path: str):
    base = os.path.dirname(os.path.dirname(__file__))                   # Esto sirve para extraer la carpeta base donde se aloja todo el programa.
    self.path = os.path.join(base, path)                                # Para no crear problemas y generar un camino entre el path del argumento y pueda funcionar da igual donde se encuentre la terminal.
  def read(self) -> str:
    return pd.read_csv(self.path)

def escritura_csv(dataFrame):                                           # Esta es la función de write
  base_1 = os.path.dirname(os.path.dirname(__file__))                   # Contiene un if/elif segund exista o no el archivo para crearlo y añadir datos con o sin header.
  camino = os.path.join(base_1,"data/order_done.csv")
  if os.path.exists(camino) == False:
    dataFrame.to_csv(camino, index = False)
  elif os.path.exists(camino) == True:
    dataFrame.to_csv(camino, index = False, mode = "a", header = False)  #Escribimos un nuevo archivo(argumento=nombre del nuevo archivo)
    
"""
Esto son pruebas que he hecho yo meramente para comprobar


lectura = CSVFileManager("data/cashiers.csv")
dataframe_prueba = lectura.read()
index_dataframe = list(dataframe_prueba.index)

#print(dataframe_prueba["name"])
#print(dataframe_prueba)

lista_prueba = list(dataframe_prueba.loc[1])

lista_limpia = []
for elemento in lista_prueba:
  if "int" in type(elemento).__name__:
    lista_limpia.append(int(elemento))
  elif "float" in type(elemento).__name__:
    lista_limpia.append(float(elemento))
  else:
    lista_limpia.append(elemento)
print(lista_limpia)

#print(lista_prueba)
#print(type(lista_prueba[2]))

#print(index_dataframe)

"""