from fastapi import FastAPI
from typing import Union
from modulos.proveedores.repository import RepositoryProveedor
from modulos.proveedores.model import Proveedor
from modulos.db.services import DBServices
from modulos.proveedores.services import ProveedorServices
nuevo_proveedor=Proveedor()
nuevo_proveedor.email = "a@a.com"
nuevo_proveedor.nombre="A"
nuevo_proveedor.telefono="123123213"

app = FastAPI()
db_services=DBServices()
db_services.connect_db()
module_services=ProveedorServices()
repository_proveedor=RepositoryProveedor(db_services, module_services)

@app.get("/proveedores")
def read_proveedores():
    proveedores = repository_proveedor.read()
    return proveedores

@app.post("/proveedores")
def create_proveedores(item:Proveedor):
    repository_proveedor.create(item)

@app.put("/proveedores/{id}")
def update_proveedores(id:int,item:Proveedor):
    repository_proveedor.update(id,item)

@app.delete("/proveedores/{id}")
def delete(id:int):
    repository_proveedor.delete(id)