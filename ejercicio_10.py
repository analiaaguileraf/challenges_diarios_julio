# challenge ---> Eliminar duplicados: Implementa una función que elimine los elementos duplicados de una lista de 10 enteros.

def eliminar_duplicados(lista):
    return list(set(lista))


lista = [1, 2, 3, 4, 5, 1, 2, 6, 7, 8]
print("Lista original:", lista)

lista_sin_duplicados = eliminar_duplicados(lista)
print("Lista sin duplicados:", lista_sin_duplicados)
