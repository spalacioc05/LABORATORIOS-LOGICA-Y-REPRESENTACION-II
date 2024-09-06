"""
Ejercicio 3
Utiliza una lista circular para generar 50 números enteros aleatorios en el rango de 1 a 100.
Implementa un método que ordene los nodos de la lista y otro método que muestre
los elementos de la lista resultante ordenada.
"""

import random

class Nodo:
    def __init__(self, parametro):
        self.valor = parametro
        self.siguiete = None

class LSLC:
    def __init__(self):
        self.cabecera = None

    def insertar_nuevo_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabecera:
            self.cabecera = nuevo_nodo
            self.cabecera.siguiete = self.cabecera
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiete is not self.cabecera:
                nodo_actual = nodo_actual.siguiete
            nodo_actual.siguiete = nuevo_nodo
            nuevo_nodo.siguiete = self.cabecera

    def to_list(self):
        result = []
        if self.cabecera:
            nodo_actual = self.cabecera
            while True:
                result.append(nodo_actual.valor)
                nodo_actual = nodo_actual.siguiete
                if nodo_actual == self.cabecera:
                    break
        return result

    def organizar(self):
        if self.cabecera:
            lst = self.to_list()
            lst.sort()
            self.cabecera = None
            for item in lst:
                self.insertar_nuevo_nodo(item)

    def imprimir_lista(self):
        if self.cabecera is None:
            print("La lista esta vacia")
        else:
            nodo_actual = self.cabecera
            while True:
                print(nodo_actual.valor, end=" ")
                if nodo_actual.siguiete is self.cabecera:
                    break
                else:
                    nodo_actual = nodo_actual.siguiete
                    
# Generar 50 números enteros aleatorios en el rango de 1 a 100
circular_list = LSLC()
for i in range(50):
    circular_list.insertar_nuevo_nodo(random.randint(1, 100))

print("Lista original:")
circular_list.imprimir_lista()

# Ordenar la lista
circular_list.organizar()

print("\nLista ordenada:")
circular_list.imprimir_lista()
