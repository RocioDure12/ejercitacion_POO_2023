from typing import List
"""
Enunciado del problema:

Se requiere desarrollar un sistema de gestión de una tienda de productos electrónicos.
El sistema debe permitir registrar y administrar los productos disponibles en la tienda.
Cada producto tiene un nombre, una marca, un precio y una cantidad en inventario.
El sistema debe ser capaz de realizar las siguientes operaciones:

1. Registrar un nuevo producto: Se debe poder agregar un nuevo producto al sistema, 
proporcionando su nombre, marca, precio y cantidad inicial en inventario.

2. Actualizar la información de un producto: El sistema debe permitir modificar la información
de un producto existente, como su nombre, marca, precio y cantidad en inventario.

3. Realizar una venta: El sistema debe permitir registrar una venta de un producto específico.
Se debe especificar el nombre del producto vendido y la cantidad vendida. Si hay suficientes unidades 
disponibles en inventario, se debe actualizar la cantidad restante.

4. Realizar un pedido: Si un producto se encuentra agotado, el sistema debe permitir realizar 
un pedido para reponer el inventario. Se debe especificar el nombre del producto y la cantidad solicitada. 
El pedido debe registrarse y se actualizará la cantidad de inventario una vez que llegue el nuevo stock.

5. Consultar disponibilidad: El sistema debe permitir consultar la disponibilidad de un producto en particular, 
proporcionando su nombre. Se mostrará la cantidad disponible en inventario.

6. Mostrar lista de productos: El sistema debe mostrar una lista de todos los productos registrados en la tienda, 
con su nombre, marca, precio y cantidad disponible.

"""


class Producto:
    id: int
    nombre: str
    cantidad: int

    def __init__(self, id: int, nombre: str, cantidad: int):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad


class Tienda:
    id: int
    nombre: str
    direccion: str
    productos: List[Producto] = []

    def __init__(self, id: int, nombre: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion

    def registrar_prod(self, producto: Producto):
        self.productos.append(producto)


    def mostrar_productos(self):
        for producto in self.productos:
            print(f"{producto.id} {producto.nombre} {producto.cantidad}")
    
    def actualizar_prod(self, id: int, nombre: str, cantidad: int):
        for producto in self.productos:
            if producto.id == id:
                producto.id=id
                producto.nombre=nombre
                producto.cantidad=cantidad
    
    def registrar_venta(self, id_producto:int, cantidad_prod:int):
        for producto in self.productos:
            if producto.id == id_producto and producto.cantidad >= cantidad_prod:
                producto.cantidad=producto.cantidad - cantidad_prod
            else:
                print("No hay stock")
                
    def realizar_pedido(self, id:int, cantidad:int):
        for producto in self.productos:
            if producto.id == id and cantidad == 0:
             print(f"Realizar pedido de {producto.nombre}")
    
    def consulta_disponibilidad(self, nombre_prod:str):
        for producto in self.productos:
            if nombre_prod == producto.nombre and producto.cantidad > 0:
                print(f"{producto.nombre} {producto.cantidad}")
            else:
                print(f"no hay {producto.nombre}")
        
                

tienda_1 = Tienda(1 , "Chango+", "Kukex 123")
prod_1 = Producto(1, "papel higienico", 12)
prod_2 = Producto(2, "jabon", 0)
tienda_1.registrar_prod(prod_1)
tienda_1.registrar_prod(prod_2)
tienda_1.registrar_venta(1,10)
tienda_1.mostrar_productos()
tienda_1.realizar_pedido(2,0)
tienda_1.consulta_disponibilidad("jabon")
prod_6=Producto(6,"Shampoo",25)
tienda_1.registrar_prod(prod_6)
tienda_1.mostrar_productos()



