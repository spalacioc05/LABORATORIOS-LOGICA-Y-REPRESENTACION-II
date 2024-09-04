''' Ejercicio 2

Simula una cola de impresión para una impresora compartida utilizando una lista doblemente enlazada.
Cada documento en la cola debe contener una frase de hasta 20 caracteres.
Los documentos deben ser procesados en el orden en que fueron encolados, respetando su secuencia de llegada. '''


class Node:
    def __init__(self, doc):
        self.next = None
        self.prev = None
        self.doc = doc


class PrintQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty_queue(self):
        return self.head is None

    def enqueue(self, doc):
        doc = str(doc)
        if len(doc) > 20:
            print(f"We couldn't queue the sentence {doc} because it's too long, use a maximum of 20 characters.")
            return

        new_node = Node(doc)

        if self.empty_queue():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def procesing(self):
        if self.empty_queue():
            print("There's no elements in the queue")
            return

        actual_node = self.head

        while actual_node:
            print(f"Printing document... {actual_node.doc}")
            actual_node = actual_node.next


queue = PrintQueue()
queue.enqueue("Documentoooooooooooooooooooooooooooooooooooooooo")
queue.enqueue(855)
queue.enqueue("Documento 3")
queue.enqueue("Documento 4")
queue.enqueue("Documento 5")

queue.procesing()
