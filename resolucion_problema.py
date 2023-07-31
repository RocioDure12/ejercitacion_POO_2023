from datetime import datetime
#Representar los dias de la semana y rangos de horario en los que hay funciones 
#de una película a traves de un array multidimensional. 
#Luego, con una funcion, tomar como argumento una fecha y hora
#(objeto datetime),y determinar si hay función en ese horario

horario_funciones=[
    [["09:00","12:00"],["16:00", "20:00"]],#Lunes
    [["09:00","11:00"],["17:00", "20:00"]],#Martes
    [["09:30","12:00"],["15:00", "20:00"]],#Miercoles
    [["10:00","12:00"],["15:30", "20:00"]],#Jueves
    [["10:30","12:00"],["16:30", "20:00"]],#Viernes
    [["10:00","11:30"],["17:30", "20:00"]],#Sabado
    [["09:00","12:00"],["16:00", "20:00"]]#Domingo
]