from ..base.services import BaseServices
from .model import Proveedor

class ProveedorServices(BaseServices):
    def __init__(self):
        pass
    
    def item_to_row(self,item:Proveedor) -> dict:
        data = BaseServices.item_to_row(self,item)
        data['nombre'] = f"'{item.nombre}'"
        data['email'] = f"'{item.email}'"
        data['telefono'] = f"{item.telefono}"
        return data



    '''
    def row_to_item(self,row:dict) -> Proveedor:

        item = BaseServices.row_to_item(self,row)
        item.nombre = row['nombre']
        item.email = row['email']
        item.telefono = row['telefono']
        
        
        return item
    '''
    
    def row_to_item(self,row:dict) -> Proveedor:

        item:Proveedor =  Proveedor(
            id = row['id'],
            nombre = row['nombre'],
            email= row['email'],
            telefono= row['telefono']
        )
        
        
        return item