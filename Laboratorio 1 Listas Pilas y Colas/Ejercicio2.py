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

    def longitud(self):
        count = 0
        nodo_actual = self.cabecera
        while nodo_actual is not None:
            count += 1
            nodo_actual = nodo_actual.siguiente
        return count

class ColaNoCircular:
    def __init__(self, m):
        self.capacidad = m
        self.V = LDL()
        
    def cola_vacia(self):
        return self.V.longitud() == 0

    def cola_llena(self):
        return self.V.longitud() == self.capacidad

    def encolar(self, documento):
        documento = str(documento)
        if self.cola_llena():
            print(" Cola llena ")
        elif len(documento) > 20:
            print(f"Error: El documento: {documento} excede los 20 caracteres.")
        else:
            self.V.agregar_al_final(documento)

    def desencolar(self):
        if self.cola_vacia():
            print(" Cola vacía ")
            return None
        else:
            nodo_actual = self.V.eliminar_cabecera()
            return nodo_actual.documento

    def imprimir_cola(self):
        while not self.cola_vacia():
            documento = self.desencolar()
            if documento is not None:
                print(f"Imprimiendo documento... {documento}")

# Ejemplo de uso
cola = ColaNoCircular(5)

cola.encolar("Documento 3")
cola.encolar("Documentoooooooooooooooooooooooooooooooooooooooo")
cola.encolar(567890)
cola.encolar("Documento 4")
cola.encolar("Documento 5")

cola.imprimir_cola()