""" ejercicio 2 - copilod"""

class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_start(self):
        if self.head is None:
            print("The list is empty")
            return None
        else:
            value = self.head.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return value

    def is_empty(self):
        return self.head is None

    def print_list(self):
        if self.head is None:
            print("The list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(f"Document: {current_node.value}")
                current_node = current_node.next


class Queue:
    def __init__(self):
        self.dll = DLL()

    def enqueue(self, document):
        if len(document) > 20:
            print("Document exceeds 20 characters limit")
            return
        self.dll.insert_at_end(document)

    def dequeue(self):
        return self.dll.delete_from_start()

    def is_empty(self):
        return self.dll.is_empty()

    def print_queue(self):
        self.dll.print_list()


# Main function to simulate the print queue
def main():
    print_queue = Queue()

    # Enqueue documents
    print_queue.enqueue("Document 1: Hello")
    print_queue.enqueue("Document 2: World")
    print_queue.enqueue("000000")
    print_queue.enqueue("Document 4: Another docasdfghjklasdfghjklokjhgfdstyuiuytr")

    # Print the queue
    print("Print Queue:")
    print_queue.print_queue()

    # Dequeue and process documents
    print("\nProcessing documents:")
    while not print_queue.is_empty():
        doc = print_queue.dequeue()
        print(f"Processing {doc}")

    # Print the queue after processing
    print("\nPrint Queue after processing:")
    print_queue.print_queue()


if __name__ == "__main__":
    main()


""" ejercicio 2 - chat"""

class Nodo:
    def __init__(self, data):
        self.data = data  # Almacena la frase del documento
        self.next = None  # Puntero al siguiente nodo
        self.prev = None  # Puntero al nodo anterior

class LDL:
    def __init__(self):
        self.head = None  # Nodo inicial de la lista
        self.tail = None  # Nodo final de la lista

    def add_last(self, data):
        """Agrega un nuevo nodo al final de la lista"""
        new_node = Nodo(data)
        if not self.head:  # Si la lista está vacía
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node  # Conecta el nodo final actual con el nuevo nodo
            new_node.prev = self.tail  # Conecta el nuevo nodo con el nodo final actual
            self.tail = new_node  # Actualiza el nodo final

    def remove_first(self):
        """Elimina y retorna el primer nodo de la lista"""
        if not self.head:
            return None
        removed_node = self.head
        if self.head == self.tail:  # Si hay un solo nodo en la lista
            self.head = self.tail = None
        else:
            self.head = self.head.next  # Mueve la cabeza al siguiente nodo
            self.head.prev = None  # Elimina la referencia al nodo anterior
        return removed_node.data

    def is_empty(self):
        """Retorna True si la lista está vacía"""
        return self.head is None

class Cola:
    def __init__(self):
        self.ldl = LDL()  # Instancia de la lista doblemente enlazada

    def encolar(self, documento):
        """Agrega un documento a la cola"""
        if len(documento) > 20:
            print("Error: El documento excede los 20 caracteres.")
        else:
            self.ldl.add_last(documento)
            print(f"Documento '{documento}' encolado.")

    def desencolar(self):
        """Procesa y elimina el documento al frente de la cola"""
        if self.ldl.is_empty():
            print("La cola de impresión está vacía.")
        else:
            documento = self.ldl.remove_first()
            print(f"Procesando documento: '{documento}'")

    def imprimir_cola(self):
        """Imprime todos los documentos en la cola"""
        nodo_actual = self.ldl.head
        if not nodo_actual:
            print("La cola de impresión está vacía.")
        else:
            print("Documentos en la cola de impresión:")
            while nodo_actual:
                print(f"- {nodo_actual.data}")
                nodo_actual = nodo_actual.next

# Ejemplo de uso:
cola_impresion = Cola()
cola_impresion.encolar("Documento 1")
cola_impresion.encolar("Documento 2")
cola_impresion.encolar("Un documento largo que no debe ser encolado")  # Este no será encolado
cola_impresion.imprimir_cola()

cola_impresion.desencolar()
cola_impresion.desencolar()
cola_impresion.desencolar()  # No habrá más documentos que procesar
