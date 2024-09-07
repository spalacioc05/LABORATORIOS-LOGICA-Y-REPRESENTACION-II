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

    def imprimir_lista(self):
        if self.cabecera is None:
            print("La lista esta vacia\n")
        else:
            nodo_actual = self.cabecera

            while nodo_actual is not None:
                print(nodo_actual.documento, end=" <-> ")
                nodo_actual = nodo_actual.siguiente
            print("None")


class Cola:
    def __init__(self):
        self.V = []

    def cola_vacia(self):
        return len(self.V) == 0

    def encolar(self, documento):
        documento = str(documento)
        if len(documento) > 20:
            print(f"No pudimos encolar la frase {documento} porque es muy larga, usa un maximo de 20 caracteres.\n")
        else:
            self.V.append(documento)

    def imprimir_cola(self):
        if self.cola_vacia():
            print("No hay elementos en la cola\n")
        else:
            for valor in self.V:
                print(f"Imprimiendo documento... {valor}")


ldl = LDL()
ldl.agregar_al_final("Documentoooooooooooooooooooooooooooooooooooooooo")
ldl.agregar_al_final(855)
ldl.agregar_al_final("Documento 3")
ldl.agregar_al_final("Documento 4")
ldl.agregar_al_final("Documento 5")
ldl.agregar_al_final(543674839445538839256)

print("LDL:\n")
ldl.imprimir_lista()
print(
    "\n---------------------------------------------------------------------------------------------------------------------------------------------------\n")

nodo_actual = ldl.cabecera

cola = Cola()

while nodo_actual is not None:
    cola.encolar(nodo_actual.documento)
    nodo_actual = nodo_actual.siguiente

print("Cola\n")
cola.imprimir_cola()
