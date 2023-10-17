#servicios que se encargan de dar una base para transformar los datos (clases abstractas)
from abc import abstractmethod
from abc import ABC
from ..base.model import BaseModel
from typing import List


class BaseServices(ABC):

    def row_to_sql(self, item:dict):
        sql = ""
        for key in item:
            sql+=f"{key}={item[key]},"
        return sql.rstrip(",")
    
    @abstractmethod
    def item_to_row(self,item:BaseModel) -> dict:
        data = {}
        return data
    
    '''
    @abstractmethod
    def row_to_item(self,row:dict) -> BaseModel:
        item = BaseModel()
        item.id = row['id']
        return item
    '''