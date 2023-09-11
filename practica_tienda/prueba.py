from modulos.base.model import BaseModel
import pymysql
from typing import List
from typing import Optional

from pydantic import EmailStr

from fastapi import FastAPI
from typing import Union

class Proveedor(BaseModel):
    nombre:str
    email:EmailStr
    telefono:Optional[str]
'''
nuevo_cliente=Proveedor()
nuevo_cliente.nombre="RicardoMCS"
nuevo_cliente.email="rickyricon@gmail.com"
nuevo_cliente.telefono="343657896"
'''

"""
-insertar en la base de datos
-mostrar resultados
-volver a instanciar lo que me traigo de la base de datos
"""
#base de datos
class DBServices:
    def connect_db(self)-> pymysql.Connection:
        return pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='',
            database='tienda',
            cursorclass=pymysql.cursors.DictCursor

        )
        

    def execute_db(self, sql:str)->int:
        connection = self.connect_db()
        with connection.cursor() as cursor:
                cursor.execute(sql)
        connection.commit()
        return connection.affected_rows()
        
    
    def read_db(self, sql:str)->List[dict]:
       connection = self.connect_db()
       with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    

class BaseRepository():
    
    def Create():
        print("p")
    
    
    def Read(self):
         print("p")
         
    def Update(self):
         print("p")
    
    def Delete(self):
         print("p")
        
data_base=DBServices()
data_base.connect_db()

def create(item:Proveedor):
    sql=f"INSERT INTO proveedores (nombre,email,telefono) VALUES ('{item.nombre}','{item.email}','{item.telefono}')"
    data_base.execute_db(sql)
    
def read()->List[Proveedor]:
    sql=f"SELECT * FROM proveedores"
    results=data_base.read_db(sql)
    items:List[Proveedor]=[]
    for proveedor in results:
        items.append(proveedor)
    return items
    
def update(id:int, item:Proveedor):
    sql=f"UPDATE proveedores SET nombre='{item.nombre}', email='{item.email}', telefono='{item.telefono}' WHERE id={id}"
    data_base.execute_db(sql)
    
    
def delete(id:int):
    sql=f"DELETE FROM proveedores WHERE id={id}"
    data_base.execute_db(sql)
    


app = FastAPI()


@app.get("/api/proveedores")
def read_proveedores():
    proveedores = read()
    return proveedores

@app.post("/api/proveedores")
def create_proveedores(item:Proveedor):
    create(item)

@app.put("/api/proveedores/{id}")
def update_proveedores(id:int,item:Proveedor):
    update(id,item)

@app.delete_proveedores("/api/proveedores/{id}")
def delete(id:int):
    delete(id)