''' 
Ejercicio 2

Simula una cola de impresión para una impresora compartida utilizando una lista doblemente enlazada.
Cada documento en la cola debe contener una frase de hasta 20 caracteres.
Los documentos deben ser procesados en el orden en que fueron encolados, respetando su secuencia de llegada. 
'''

class Node:
    def __init__(self, doc):
        self.next = None
        self.prev = None
        self.doc = doc

class LDL:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def append(self, doc):
        new_node = Node(doc)

        if self.empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop_head(self):
        if self.empty():
            return None
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return node.doc

    def print_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.doc, end=" <-> ")
            actual_node = actual_node.next
        print("None")

class Tail:
    def __init__(self):
        self.queue = LDL()

    def enqueue(self, doc):
        doc = str(doc)
        if len(doc) > 20:
            print(f"We couldn't queue the sentence '{doc}' because it's too long, use a maximum of 20 characters.")
            return
        self.queue.append(doc)

    def procesing(self):
        if self.queue.empty():
            print("There's no elements in the queue")
            return

        while not self.queue.empty():
            doc = self.queue.pop_head()
            print(f"Printing document... {doc}")

# Example usage
queue = Tail()
queue.enqueue("Documentoooooooooooooooooooooooooooooooooooooooo")
queue.enqueue(855)
queue.enqueue("Documento 3")
queue.enqueue("Documento 4")
queue.enqueue("Documento 5")

queue.procesing()