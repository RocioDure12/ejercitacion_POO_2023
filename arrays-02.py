#Suma de elementos en posiciones pares:
#Escribe una función que tome una lista de números como entrada y devuelva la suma de los elementos 
# que se encuentran en posiciones pares.

lista_numeros = [2, 2, 3, 4, 5,6,8]  



def suma_elementos_pares(lista):
    suma=0
    for i in range(len(lista)):
        if i % 2 == 0:
            suma=suma+lista[i]
    
    print(suma)
            

suma_elementos_pares(lista_numeros)

#Eliminar elemento específico:
#Escribe una función que tome una lista y un elemento específico como entrada, 
# y elimine todas las ocurrencias de ese elemento en la lista.

def eliminar_elementos(lista, elemento):
    while elemento in lista:
        lista.remove(elemento)

eliminar_elementos(lista_numeros, 2)
print(lista_numeros)
    
#Contar elementos mayores que un valor dado:
#Escribe una función que tome una lista de números y un valor específico como entrada, 
# y devuelva la cantidad de elementos en la lista que son mayores que ese valor.

def contar(lista, elemento):
    contador=0
    for i in lista:
        if i > elemento:
            contador=contador+1
    return contador

print("contador:",contar(lista_numeros, 6))
    