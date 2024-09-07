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

    def insertar_nuevo_nodo(self, valor):  # Método para insertar nodos en la LSLC
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:  # Verificamos si solo hay un nodo, si es asi, este se apunta a si mismo
            self.cabecera = nuevo_nodo
            self.cabecera.siguiete = self.cabecera
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiete is not self.cabecera:  # Buscamos el último nodo y actualizamos los punteros
                nodo_actual = nodo_actual.siguiete
            nodo_actual.siguiete = nuevo_nodo
            nuevo_nodo.siguiete = self.cabecera

    def lista(self):  # Método para extraer los valores de los nodos de una LSLC a un ArrayList
        L = []
        if self.cabecera:
            nodo_actual = self.cabecera
            while True:
                L.append(nodo_actual.valor)  # Agregamos el valor del nodo al ArrayList
                nodo_actual = nodo_actual.siguiete
                if nodo_actual == self.cabecera:
                    break
        return L  # Retornamos el ArrayList con cada uno de los valores de la LSLC

    def ordenamiento_por_insercion(self):
        # Método para ordenar los valores del ArrayList y devuelve la LSLC ordenada
        if self.cabecera:
            lista = self.lista()  # Declaramos una variable igual a nuestro ArrayList con los valores de los nodos

            for i in range(1, len(lista)):  # Método de ordenamiento por inserción
                p = lista[i]
                j = i - 1
                while j >= 0 and p < lista[j]:
                    lista[j + 1] = lista[j]
                    j -= 1
                lista[j + 1] = p

            self.cabecera = None
            for i in lista:  # Insertamos los valores ordenados en la LSLC
                self.insertar_nuevo_nodo(i)

    def imprimir_lista(self):  # Método para imprimir los nodos de la LSLC
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
for i in range(50):  # Generacion de 50 números aleatorios
    lslc.insertar_nuevo_nodo(random.randint(1, 100))

print("Lista original:\n")
lslc.imprimir_lista()

print(
    "\n---------------------------------------------------------------------------------------------------------------------------------------------------\n")

lslc.ordenamiento_por_insercion()

print("Lista ordenada:\n")
lslc.imprimir_lista()
