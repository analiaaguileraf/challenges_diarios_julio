# Challenge ---> Recorrido en profundidad (DFS): Implementa un recorrido DFS para un grafo simple con 5 nodos.

# Función DFS utilizando recursión
def dfs_recursivo(grafo, nodo, visitados):
    visitados.add(nodo)  # Marcamos el nodo como visitado
    print(nodo)  # Imprimimos el nodo (o lo procesamos de otra forma)

    # Recorremos todos los nodos adyacentes
    for vecino in grafo[nodo]:
        if vecino not in visitados:  # Si el vecino no ha sido visitado
            dfs_recursivo(grafo, vecino, visitados)  # Llamamos recursivamente al DFS

# Definimos el grafo con 5 nodos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Llamamos a la función DFS
nodo_inicial = 'A'
visitados = set()  # Creamos un conjunto para almacenar los nodos visitados
dfs_recursivo(grafo, nodo_inicial, visitados)
