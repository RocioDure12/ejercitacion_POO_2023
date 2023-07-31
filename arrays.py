peliculas=[
    ["Lo que el viento se llevó",240,["Acción","Suspenso","Terror"]]
]

print(peliculas[0][2])

#Suma de elementos:
#Escribe una función que tome una lista de números como entrada y devuelva la suma de todos los elementos en la lista.

def suma_numeros(lista):
    suma=0
    for numero in lista:
        suma=suma+numero
    return(suma)
    
    
lista_numeros = [1, 2, 3, 4, 5]  
suma_numeros(lista_numeros)

#Encontrar el valor máximo:
#Escribe una función que tome una lista de números como entrada y devuelva el valor máximo dentro de la lista.

def valor_maximo(lista):
    maximo=lista[0]
    
    for numero in lista:
        if numero > maximo:
            maximo=numero
    return maximo
    

print(valor_maximo(lista_numeros))


#Eliminar duplicados:
#Escribe una función que tome una lista como entrada y devuelva una nueva lista sin elementos duplicados.

vocales=["a","e","i","e","a","o","u"]

def eliminar_duplicados(lista):
    nueva_lista=[]
    for letra in vocales:
        if letra not in nueva_lista:
            nueva_lista.append(letra)
    return nueva_lista

    
print(eliminar_duplicados(vocales))

#Ordenar la lista:
#Escribe una función que tome una lista de números como entrada y devuelva una nueva lista ordenada de forma ascendente.
def ordenar_lista(lista):
    lista.sort()
    return lista

lista_num = [66, 22, 33, 44, 55] 
print(ordenar_lista(lista_num))

numbers=[2,9,8,7,5,0]
for i in numbers:
    print(i)
    
empleados=[
    ["Lucas", 25, "Marketing"],
    ["Joaquin", 50,"Ventas"],
    ["Luana",32,"Diseño"],
    
]

for empleado in empleados:
        for i in empleado:
            print(i)

abecedario=[
    [["A","B","C"],["D","E","F"],["G","H","I"]],
    [["J","K"],["L"],["M","N","O"]],
    [["P"],["Q","R","S"],["T","U"]],
    [["V", "W"],["X","Y"],["Z"]]
]


for conjunto_letras in abecedario:
    for letras in conjunto_letras :
        for i in letras:
            print(i)
      
      
print(abecedario[0][0][0])
print(abecedario[3][2][0])

