from modulos.base.model import BaseModel
from ..db.services import DBServices
from typing import List
from abc import abstractmethod
from abc import ABC
from .services import BaseServices

class BaseRepository(ABC):
    _module_services:BaseServices=None
    _db_services:DBServices=None
    _table_name:str=None
    
    def __init__(self, db_services:DBServices, module_services:BaseServices):
        self._db_services=db_services
        self._module_services=module_services
        
    def create(self,item:BaseModel):
        row=self._module_services.item_to_row(item)
        sql=self._module_services.row_to_sql(row)
        return self._db_services.execute_db(f"INSERT INTO {self._table_name} SET {sql}")
        
    def read(self)->List[BaseModel]:
        sql=f"SELECT * FROM {self._table_name}"
        results=self._db_services.read_db(sql)
        items:List[BaseModel]=[]
        for item in results:
            items.append(self._module_services.row_to_item(item))
        return items
        
    def update(self,id:int, item:BaseModel):
        row=self._module_services.item_to_row(item)
        sql=self._module_services.row_to_sql(row)
        return self._db_services.execute_db(f"UPDATE {self._table_name} SET {sql} WHERE id={id}")
        
        
    def delete(self,id:int):
        return self._db_services.execute_db(f"DELETE FROM {self._table_name} WHERE id={id}")