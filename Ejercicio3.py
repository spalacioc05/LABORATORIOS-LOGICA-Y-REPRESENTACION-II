''' Ejercicio 3
Utiliza una lista circular para generar 50 números enteros aleatorios en el rango de 1 a 100.
Implementa un método que ordene los nodos de la lista y otro método que muestre
los elementos de la lista resultante ordenada.'''
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularList:
    def __init__(self):
        self.head = None

    def insert(self, valor):
        nuevo_nodo = Node(valor)
        if self.head is None:
            nuevo_nodo.next = nuevo_nodo
            self.head = nuevo_nodo
        else:
            nodo_actual = self.head
            while nodo_actual.next is not self.head:
                nodo_actual = nodo_actual.next
            nuevo_nodo.next = self.head
            nodo_actual.next = nuevo_nodo

    def sort(self):
        if not self.head:
            return
        end = None
        while end != self.head.next:   #self.head.next != None
            p = self.head
            while p.next != end:
                q = p.next
                if p.data > q.data:
                    p.data, q.data = q.data, p.data
                p = p.next
            end = p

        def insert(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = new_node
                new_node.next = self.head
            print(f"Inserted: {data}")
        
        def display(self):
            if not self.head:
                print("List is empty")
                return
            temp = self.head
            index = 0
            while True:
                print(f"Position {index}: {temp.data}")
                temp = temp.next
                index += 1
                if temp == self.head:
                    break
            print()

# Create a circular list
clist = CircularList()

# Insert 50 random integers into the circular list
for _ in range(50):
    clist.insert(random.randint(1, 100))

# Sort the circular list
clist.sort()

# Display the sorted list with positions
clist.display()