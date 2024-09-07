"""
Ejercicio 3
Utiliza una lista circular para generar 50 números enteros aleatorios en el rango de 1 a 100.
Implementa un método que ordene los nodos de la lista 
y otro método que muestre los elementos de la lista resultante ordenada.
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
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
            self.cabecera.siguiete = self.cabecera
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiete is not self.cabecera:
                nodo_actual = nodo_actual.siguiete
            nodo_actual.siguiete = nuevo_nodo
            nuevo_nodo.siguiete = self.cabecera

    def lista(self):
        L = []
        if self.cabecera:
            nodo_actual = self.cabecera
            while True:
                L.append(nodo_actual.valor)
                nodo_actual = nodo_actual.siguiete
                if nodo_actual == self.cabecera:
                    break
        return L

    def ordenamiento_por_insercion(self):
        if self.cabecera:
            lista = self.lista()
            
            for i in range(1, len(lista)):
                p = lista[i]
                j = i - 1
                while j >= 0 and p < lista[j]:
                    lista[j + 1] = lista[j]
                    j -= 1
                lista[j + 1] = p
            
            self.cabecera = None
            for i in lista:
                self.insertar_nuevo_nodo(i)

    def imprimir_lista(self):
        if self.cabecera is None:
            print("La lista esta vacia")
        else:
            nodo_actual = self.cabecera
            while True:
                print(nodo_actual.valor, end=" -> ")
                if nodo_actual.siguiete is self.cabecera:
                    break
                else:
                    nodo_actual = nodo_actual.siguiete
                    
lslc = LSLC()
for i in range(50):
    lslc.insertar_nuevo_nodo(random.randint(1, 100))

print("Lista original:\n")
lslc.imprimir_lista()

print("\n---------------------------------------------------------------------------------------------------------------------------------------------------\n")


lslc.ordenamiento_por_insercion()

print("Lista ordenada:\n")
lslc.imprimir_lista()
