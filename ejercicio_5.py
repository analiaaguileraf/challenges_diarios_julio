# challenge ---> Camino más corto: Dado un grafo pequeño con 5 nodos y 6 aristas, escribe una función que encuentre el camino más corto entre dos nodos especificados usando cualquier método que prefieras.

import heapq

def dijkstra(grafo, inicio, fin):
    # Inicializamos el diccionario de distancias y el heap (cola de prioridad)
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    cola_prioridad = [(0, inicio)]
    camino = {nodo: None for nodo in grafo}
    
    while cola_prioridad:
        (distancia_actual, nodo_actual) = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            break

        if distancia_actual > distancias[nodo_actual]:
            continue
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                camino[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))

    ruta = []
    nodo = fin
    while nodo is not None:
        ruta.append(nodo)
        nodo = camino[nodo]
    ruta.reverse()
    
    return ruta, distancias[fin]

# Definimos el grafo con 5 nodos y 6 aristas con pesos
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# Especificamos los nodos de inicio y fin
nodo_inicio = 'A'
nodo_fin = 'F'

# Llamamos a la función Dijkstra para encontrar el camino más corto
camino_corto, distancia = dijkstra(grafo, nodo_inicio, nodo_fin)
print(f"El camino más corto de {nodo_inicio} a {nodo_fin} es: {camino_corto} con una distancia de {distancia}")
