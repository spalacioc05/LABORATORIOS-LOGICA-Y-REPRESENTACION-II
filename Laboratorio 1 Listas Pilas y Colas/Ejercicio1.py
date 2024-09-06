"""
Ejercicio 1
Utiliza una lista simplemente enlazada para crear una estructura de 25 nodos,
cada uno conteniendo un número aleatorio entre 1 y 30. Una vez generada la lista enlazada,
construye una pila en la que los números pares se coloquen en la parte inferior y los impares en la parte superior. 
"""

import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class LSL:
    def __init__(self):
        self.cabecera = None

    def insertar_valor(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_ultimo(self):
        # Definición de la función eliminar_ultimo que pertenece a la clase LSL.
        
        if self.cabecera is None:
            # Verifica si la lista está vacía (si la cabecera es None).
            return None
            #  Si la lista está vacía, retorna None.
        
        if self.cabecera.siguiente is None:
            # Verifica si la lista tiene solo un nodo (si el siguiente nodo de la cabecera es None).
            valor_eliminar = self.cabecera.valor
            # Guarda el valor del único nodo en la variable valor_eliminar.
            self.cabecera = None
            # Elimina el único nodo estableciendo la cabecera a None.
            return valor_eliminar
            # Retorna el valor del nodo eliminado.
        
        nodo_actual = self.cabecera
        # Inicializa nodo_actual con la cabecera de la lista.
        
        while nodo_actual.siguiente.siguiente is not None:
            # Itera a través de la lista hasta encontrar el penúltimo nodo (el nodo cuyo siguiente nodo es el último).
            nodo_actual = nodo_actual.siguiente
            # Avanza al siguiente nodo en la lista.
        
        valor_eliminar = nodo_actual.siguiente.valor
        # Guarda el valor del último nodo en la variable valor_eliminar.
        nodo_actual.siguiente = None
        # Elimina el último nodo estableciendo el siguiente del penúltimo nodo a None.
        return valor_eliminar
        # Retorna el valor del nodo eliminado.

    def imprimir_lista(self):
        nodo_actual = self.cabecera
        while nodo_actual is not None:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")


class Pila:
    def __init__(self, tam):
        self.V = LSL()
        self.tope = -1
        self.tam = tam
        
    def pila_vacia(self):
        return self.tope < 0

    def pila_llena(self):
        return self.tope == self.tam - 1

    def apilar(self, valor):
        if self.pila_llena():
            print("La pila esta llena, solo podemos apilar 25 objetos a la vez.")
            raise ValueError("Error")
        else:
            self.tope = self.tope + 1
            self.V.insertar_valor(valor)
    
    def desapilar(self):
        if self.pila_vacia():
            print("La pila está vacía")
            return None
        valor_eliminar = self.V.eliminar_ultimo()
        self.tope = self.tope - 1
        return valor_eliminar

    def imprimir_pila(self):
        while not self.pila_vacia():
            valor = self.desapilar()
            if valor is not None:
                print(f"| {valor} |")
                print(" --- ")


lista = LSL()
for i in range(25): 
    lista.insertar_valor(random.randint(1, 30))

print("Lista Simplemente Enlazada")
lista.imprimir_lista()
print("------------------------------------------------------------------------------------------------------------------------------------------------")

pila = Pila(25)
nodo_actual = lista.cabecera

try:
    while nodo_actual is not None:
        if nodo_actual.valor % 2 == 0:
            pila.apilar(nodo_actual.valor)
        nodo_actual = nodo_actual.siguiente

    nodo_actual = lista.cabecera

    while nodo_actual is not None:
        if nodo_actual.valor % 2 != 0:
            pila.apilar(nodo_actual.valor)
        nodo_actual = nodo_actual.siguiente

    print("Pila (numeros pares abajo, impares arriba):")
    pila.imprimir_pila()

except:
    print("Pila (numeros pares abajo, impares arriba):")
    pila.imprimir_pila()