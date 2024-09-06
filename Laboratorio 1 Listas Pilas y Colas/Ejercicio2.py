"""
Ejercicio 2

Simula una cola de impresión para una impresora compartida utilizando una lista doblemente enlazada.
Cada documento en la cola debe contener una frase de hasta 20 caracteres.
Los documentos deben ser procesados en el orden en que fueron encolados, respetando su secuencia de llegada. 
"""

class Nodo:
    def __init__(self, documento):
        self.documento = documento
        self.anterior = None
        self.siguiente = None

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
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo

    def eliminar_cabecera(self):
        if self.cabecera is None:
            print("La lista esta vacia")
            
        else:
            nodo = self.cabecera
            self.cabecera = self.cabecera.siguiente
            if self.cabecera:
                self.cabecera.anterior = None
            else:
                self.cola = None
            return nodo

class Cola:
    def __init__(self):
        self.lista = LDL()

    def encolar(self, documento):
        documento = str(documento)
        if len(documento) > 20:
            print(f"Error: El documento: {documento} excede los 20 caracteres.")
        else:
            self.lista.agregar_al_final(documento)

    def desencolar(self):
        nodo = self.lista.eliminar_cabecera()
        if nodo:
            return nodo.documento
        else:
            return None

    def imprimir(self):
        nodo_actual = self.lista.cabecera
        
        if nodo_actual is None:
            print("La cola esta vacia")
        else:
            while nodo_actual is not None:
                print(f"Imprimiendo documento... {nodo.documento}")
                nodo = nodo.siguiente


# Ejemplo de uso
cola = Cola()

cola.encolar("Documento 3")
cola.encolar("Documentoooooooooooooooooooooooooooooooooooooooo")
cola.encolar(567890)
cola.encolar("Documento 4")
cola.encolar("Documento 5")


cola.imprimir()