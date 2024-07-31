# challenge ---> Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos.

from collections import deque

# Función BFS
def bfs(grafo, nodo_inicial):
    visitados = set()  # Conjunto para almacenar los nodos visitados
    cola = deque([nodo_inicial])  # Cola para el BFS, inicializada con el nodo inicial

    while cola:
        nodo = cola.popleft()  # Sacamos el primer nodo de la cola
        if nodo not in visitados:
            print(nodo)  # Imprimimos el nodo (o lo procesamos de otra forma)
            visitados.add(nodo)  # Marcamos el nodo como visitado

            # Añadimos todos los nodos adyacentes a la cola
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

# Definimos el grafo con 5 nodos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Llamamos a la función BFS
nodo_inicial = 'A'
bfs(grafo, nodo_inicial)
