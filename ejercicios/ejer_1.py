"""
Enunciado del problema:

Se necesita desarrollar un sistema para gestionar una biblioteca, donde se puedan registrar y administrar los
libros disponibles. Cada libro tiene un título, un autor, un género y una cantidad de ejemplares disponibles.
El sistema debe permitir realizar las siguientes operaciones:

1. Registrar un nuevo libro: Se debe poder agregar un nuevo libro al sistema,
proporcionando el título, el autor, el género y la cantidad de ejemplares disponibles.

2. Prestar un libro: El sistema debe permitir prestar un libro a un usuario.
Se debe especificar el título del libro a prestar y la cantidad de ejemplares solicitados. Si hay suficientes ejemplares disponibles,
se debe actualizar la cantidad de ejemplares y registrar el préstamo.

3. Devolver un libro: Se debe poder registrar la devolución de un libro prestado.
Se debe especificar el título del libro devuelto y la cantidad de ejemplares devueltos. 
Si la cantidad devuelta es igual a la cantidad prestada, se debe actualizar la cantidad de ejemplares disponibles.

4. Consultar disponibilidad: Se debe poder consultar la disponibilidad de un libro
en particular, proporcionando su título. El sistema debe mostrar la cantidad de ejemplares disponibles.

5. Mostrar lista de libros: El sistema debe mostrar una lista de todos los libros registrados en la biblioteca,
con su título, autor, género y cantidad de ejemplares disponibles.
"""

from typing import List

        
class Libro:
    id:int
    titulo:str
    genero:str
    cantidad:int
    
    def __init__(self, id:int, titulo:str, genero:str, cantidad:int):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.cantidad = cantidad

class Biblioteca:
    id:int
    nombre:str
    direccion:str
    libros:List[Libro] = []
    
    def __init__(self, id, nombre, direccion):
        self.id = id
        self.nombre=nombre
        self.direccion=direccion
        self.libros = []
        
    def registrar_libro(self, libro:Libro):
        self.libros.append(libro)
        
    def prestar_libro(self, id_libro:int, cantidad:int):
        libro_prestar:Libro = None
        
        for libro in self.libros:
            if id_libro == libro.id and libro.cantidad >= cantidad:
                libro_prestar = libro
        
        if libro_prestar == None:
            raise Exception("Libro no disponible")
        
        libro.cantidad = libro.cantidad - cantidad
        
    def mostrar_libros(self):   
        for libro in self.libros:
                print(f"{libro.id}. {libro.titulo} - {libro.genero} ({libro.cantidad} disponibles)")

    
        
    def devolucion_libro(self,id_libro:int,cantidad:int):
        libro_devolucion:Libro=None
        
        for libro in self.libros:
            if id_libro == libro.id:
                libro_devolucion=libro
                
        if libro_devolucion == None:
            raise Exception("el id del libro no existe")
        
        libro.cantidad=libro.cantidad+cantidad
    
      
    def consulta_libro(self, id_libro):
        libro_consultado:Libro=None
        
        for libro in self.libros:
            if id_libro == libro.id:
                libro_consultado=libro
              
        
        if libro_consultado == None:
            raise Exception("No hay disponibilidad")
        
                
            
                    
try:
    
    biblioteca = Biblioteca(1,"Kukelina Books", "Popo 123")

    libro1 = Libro(1,"El fantasma de la ópera","Misterio",25)
    libro2 = Libro(2,"El fantasma","Poesia",15)

    biblioteca.registrar_libro(libro1)
    biblioteca.mostrar_libros()
    biblioteca.prestar_libro(1, 20)
    biblioteca.mostrar_libros()
    biblioteca.devolucion_libro(1,5)
    biblioteca.mostrar_libros()
    biblioteca.consulta_libro(1)
    biblioteca.mostrar_libros()
except Exception as e:
    print(f"Error: {str(e)}")
        