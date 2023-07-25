from typing import List
from datetime import datetime

class Empleado:
    id:int
    nombre:str
    
    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre
        

class Sala:
    nombre:str
    capacidad:int
    horarios_disponibles:List[]=[]
    
    def __init__(self, nombre, capacidad):
        self.nombre=nombre
        self.capacidad=capacidad

class Reserva:
    empleado:Empleado
    sala:Sala
    
    def __init__(self, empleado, sala)
        self.empleado=empleado
        self.sala=sala
    
    
class Sistema_Reserva_Sala:
    salas:List[Sala]=[]
    reservas:List[Reserva]=[]









"""

    
    def consultar_disponibilidad_sala(self):
        print(l)
    
    def reservar_sala(self):
        print(l)
    
    def cancelar_reserva(self):
        print(l)
    
    def obtener_horarios_disponibles(self):
        print(l)
        

class Reserva:
    sala:Sala_reunion
    fecha_hora:datetime


class Empledo:
    id:int
    nombre:str

class Sistema_reservas:
    salas:List[Sala_reunion]=[]
"""
    
    

    
    
    