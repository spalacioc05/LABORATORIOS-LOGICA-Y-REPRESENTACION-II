"""
Ejercicio 2

Simula una cola de impresión para una impresora compartida utilizando una lista doblemente enlazada.
Cada documento en la cola debe contener una frase de hasta 20 caracteres.
Los documentos deben ser procesados en el orden en que fueron encolados, respetando su secuencia de llegada. 
"""


class Nodo:
    def __init__(self, documento):
        self.anterior = None
        self.siguiente = None
        self.documento = documento


class LDL:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def agregar_al_final(self, documento):
        nuevo_nodo = Nodo(documento)

        if self.cola is None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo


class ImprimirCola:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def cola_vacia(self):
        return self.cabecera is None

    def encolar(self, doc):
        doc = str(doc)
        if len(doc) > 20:
            print(f"No pudimos encolar la frase {doc} porque es muy larga, usa un maximo de 20 caracteres.")
            return

        nuevo_nodo = Nodo(doc)

        if self.cola_vacia():
            self.cabecera = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def proceso(self):
        if self.cola_vacia():
            print("No hay elementos en la cola")
            return

        valor_actual = self.cabecera

        while valor_actual:
            print(f"Printing document... {valor_actual.documento}")
            valor_actual = valor_actual.siguiente


lista = LDL()
lista.agregar_al_final("Documentoooooooooooooooooooooooooooooooooooooooo")
lista.agregar_al_final(855)
lista.agregar_al_final("Documento 3")
lista.agregar_al_final("Documento 4")
lista.agregar_al_final("Documento 5")

nodo_actual = lista.cabecera

cola = ImprimirCola()

while nodo_actual is not None:
    cola.encolar(nodo_actual.documento)
    nodo_actual = nodo_actual.siguiente

cola.proceso()
