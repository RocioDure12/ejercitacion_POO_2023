from ..base.model import BaseModel
from typing import Optional
from pydantic import EmailStr

class Proveedor(BaseModel):
    nombre:str=None
    email:EmailStr=None
    telefono:Optional[str]=None