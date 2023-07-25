"""Problema: Registro de ventas

Imagina que tienes una tienda y deseas mantener un registro de las ventas diarias. 
Cada día, la tienda registra el número de unidades vendidas de tres productos diferentes: A, B y C. 
Quieres almacenar esta información en una matriz para poder realizar análisis posteriores.

Escribe un programa en Python que solicite al usuario ingresar las ventas diarias durante una semana (7 días) 
y almacene estos datos en una matriz de 7x3, donde cada fila representa un día y cada columna representa
el número de unidades vendidas de los productos A, B y C, respectivamente.

Después de obtener la matriz de ventas, el programa debe calcular el total de ventas para cada producto y
el total de ventas por día. Luego, muestra los resultados en la consola.
"""

registro_ventas=[
    [],#Lunes
    [],#Martes
    [],#Miercoles
    [],#Jueves
    [],#Viernes
    [],#Sabado
    []#Domingo
]