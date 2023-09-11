#servicios que se encargan de dar una base para transformar los datos (clases abstractas)
"""
*Si instancio una clase (BaseModel->proveedor) es un objeto tipo BaseModel en ese caso necesito transformarlo en un dict
(Item to row)

*Recibo un dict (row) y lo convierto en un string apto para insertar en la db (row to sql)

*Recibo un dict y lo tranformo en una instancia de BaseModel (row to item)

"""
from abc import ABC
from base.model import BaseModel

class BaseServices(ABC):
    
    def item_to_row(self, item:BaseModel):
        print("p")
    
    def row_to_item(self):
         print("p")
         
    def row_to_item(self):
         print("p")
    
    