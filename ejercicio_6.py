# challenge --->  Árbol binario de búsqueda (BST): Implementa solo la inserción en un árbol binario de búsqueda para 5 elementos.



class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, valor)
        else:
            if valor > nodo_actual.valor:
                if nodo_actual.derecha is None:
                    nodo_actual.derecha = Nodo(valor)
                else:
                    self._insertar_recursivo(nodo_actual.derecha, valor)

    def imprimir_inorden(self, nodo):
        if nodo is not None:
            self.imprimir_inorden(nodo.izquierda)
            print(nodo.valor)
            self.imprimir_inorden(nodo.derecha)

# Ejemplo de uso:
arbol = ArbolBinarioBusqueda()
valores = [10, 5, 15, 2, 7]

for valor in valores:
    arbol.insertar(valor)

print("Árbol binario de búsqueda en orden:")
arbol.imprimir_inorden(arbol.raiz)
