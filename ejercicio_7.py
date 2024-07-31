# challenge ---> Piloto de eventos (Priority Queue): Implementa una cola de prioridad utilizando una lista para insertar y eliminar 5 elementos.

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item):
        self.queue.append(item)
        self.queue.sort() 

    def remove(self):
        if not self.is_empty():
            return self.queue.pop(0) 
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        return ' '.join(map(str, self.queue))


pq = PriorityQueue()
elementos = [20, 15, 10, 5, 30]

print("Insertando elementos:")
for elem in elementos:
    pq.insert(elem)
    print(f"Insertado {elem}, cola actual: {pq}")

print("\nEliminando elementos:")
while not pq.is_empty():
    eliminado = pq.remove()
    print(f"Eliminado {eliminado}, cola actual: {pq}")
