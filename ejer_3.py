from typing import List
import datetime
"""
Enunciado del problema:

Se necesita desarrollar un sistema de reserva de salas de reuniones en una empresa. 
El sistema debe permitir a los empleados reservar salas para reuniones en diferentes fechas y horarios. 
Cada sala tiene un nombre, una capacidad máxima de personas y una lista de horarios disponibles.

El sistema debe ser capaz de realizar las siguientes operaciones:

1. Consultar disponibilidad de una sala: El sistema debe permitir consultar la disponibilidad de una sala 
en una fecha y hora específica. Se debe mostrar si la sala está disponible o si ya ha sido reservada.

2. Reservar una sala: Los empleados deben poder reservar una sala para una fecha y hora determinada.
Se debe verificar la disponibilidad de la sala y registrar la reserva en caso de que esté disponible.

3. Cancelar una reserva: Si un empleado necesita cancelar una reserva, se debe permitir cancelarla y 
liberar la sala para que esté disponible nuevamente en ese horario.

4. Mostrar horarios disponibles de una sala: El sistema debe mostrar los horarios disponibles de una
sala en particular, indicando las fechas y horas en las que no hay reservas realizadas.

5. Mostrar lista de salas: El sistema debe mostrar una lista de todas las salas disponibles en la empresa, 
con su nombre, capacidad máxima y horarios disponibles.
como 
Diseña y desarrolla un sistema utilizando Programación Orientada a Objetos (POO) que cumpla con los requisitos
mencionados y permita gestionar eficientemente las reservas de salas de reuniones. Utiliza los conceptos de clases, 
objetos, atributos y métodos para crear una solución estructurada y reutilizable. Además, implementa una clase
para manejar las fechas y horarios. Puedes utilizar el lenguaje de programación que prefieras y adaptar el enunciado 
según tus necesidades. ¡Diviértete practicando la POO y la gestión de fechas!
"""


class Reserva:
    fecha_hora: datetime
    sala

    def __init__(self, fecha_hora: datetime, sala):
        self.fecha_hora = fecha_hora
        self.sala = sala


class Sala:
    nombre: str
    capacidad_max: int
    lista_reservas: List[Reserva] = []

    def __init__(self, nombre: str, capacidad_max: int):
        self.nombre = nombre
        self.capacidad_max = capacidad_max


class Empledo:
    id: int
    nombre: str
    apellido: str

    def __init__(self, id: int, nombre: str, apellido: str):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido


class Empresa:
    nombre: str
    lista_salas: List[Sala] = []

    def __init__(self, nombre: str, list_salas: List, list_reservas: List):
        self.nombre = nombre
        self.lista_salas = list_salas
        self.lista_reservas = list_reservas

    def consultar_disponibilidad_sala(self):
        print("l")

    def reservar_sala(self):
        print("l")

    def cancelar_sala(self):
        print("l")

    def mostrar_horarios_disponibles(self):
        print("l")

    def mostrar_lista_salas(self):
        print("l")
