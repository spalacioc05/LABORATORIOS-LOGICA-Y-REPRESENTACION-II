''' 
Ejercicio 1
Utiliza una lista simplemente enlazada para crear una estructura de 25 nodos,
cada uno conteniendo un número aleatorio entre 1 y 30. Una vez generada la lista enlazada,
construye una pila en la que los números pares se coloquen en la parte inferior y los impares en la parte superior. 
'''

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LSL:
    def __init__(self):
        self.head = None

    def insert_value(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next is not None:
                actual_node = actual_node.next
            actual_node.next = new_node

    def print_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.value, end=" -> ")
            actual_node = actual_node.next
        print("None")


class Stack:
    def __init__(self, size):
        self.V = []
        self.top = -1
        self.size = size

    def full_stack(self):
        return self.top == self.size - 1

    def stacking(self, value):
        if self.full_stack():
            print("La pila está llena, sólo podemos apilar 25 objetos a la vez.")
            raise ValueError("Error")
        else:
            self.top = self.top + 1
            self.V.append(value)
 

    def print_stack(self):
        for V in reversed(self.V):
            print(V, end=" -> ")
        print("None")


lsl = LSL()
for i in range(25): 
    lsl.insert_value(random.randint(1, 30))

print("LSL")
lsl.print_list()
print("--------------------------------------------------------------------------------------")

stack = Stack(25)
actual_node = lsl.head

try:
    while actual_node is not None:
        if actual_node.value % 2 == 0:
            stack.stacking(actual_node.value)
        actual_node = actual_node.next

    actual_node = lsl.head

    while actual_node is not None:
        if actual_node.value % 2 != 0:
            stack.stacking(actual_node.value)
        actual_node = actual_node.next

    print("Pila (números pares abajo, impares arriba):")
    stack.print_stack()

except:
    print("Pila (números pares abajo, impares arriba):")
    stack.print_stack()


