#Challenge ---> Ordenamiento simple: Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).

# Metodo burbuja

# Definimos la función llamada 'ordenar_lista_burbuja' que recibe una lista de 5 enteros
def ordenar_lista_burbuja(lista):
    n = len(lista)  # Obtenemos la longitud de la lista
    for i in range(n):  # Bucle que se repetirá tantas veces como elementos hay en la lista
        for j in range(0, n-i-1):  # Bucle interno para comparar elementos adyacentes
            if lista[j] > lista[j+1]:  # Si el elemento actual es mayor que el siguiente
                # Intercambiamos los elementos
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista  # Devolvemos la lista ordenada

# Ejemplo de uso:
lista_de_ejemplo = [64, 34, 25, 12, 22]
lista_ordenada = ordenar_lista_burbuja(lista_de_ejemplo)
print("Lista ordenada:", lista_ordenada)

