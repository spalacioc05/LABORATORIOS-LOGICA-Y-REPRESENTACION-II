#Clase Nodo sacada de las diapositivas de clase
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    #Método para insertar sacado de las diapositivas de clase
    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            actual = self.raiz
            while actual:
                padre = actual
                if valor < actual.valor:
                    actual = actual.izquierda
                else:
                    actual = actual.derecha
            if valor < padre.valor:
                padre.izquierda = nuevo_nodo
            else:
                padre.derecha = nuevo_nodo

    #Método recorrido_inorden_no_recursivo sacados de las diapositivas
    def recorrido_inorden_no_recursivo(self):
        pila = []
        actual = self.raiz
        valores = []

        while pila or actual:
            if actual:
                pila.append(actual)
                actual = actual.izquierda
            else:
                actual = pila.pop()
                valores.append(actual.valor)
                actual = actual.derecha

        return valores

    #Método recorrido_preorden_no_recursivo sacado de las diapositivas de clase
    def recorrido_preorden_no_recursivo(self):
        if self.raiz is None:
            return

        pila = []
        pila.append(self.raiz)

        while pila:
            nodo = pila.pop()
            print(nodo.valor, end=' ')

            # Agregar el hijo derecho antes del hijo izquierdo en la pila
            if nodo.derecha:
                pila.append(nodo.derecha)
            if nodo.izquierda:
                pila.append(nodo.izquierda)

    #Método para balancear el árbol actual
    def balancear(self):
        valores_ordenados = self.recorrido_inorden_no_recursivo() #primero ordenamos
        self.raiz = self.crear_arbol_balanceado(valores_ordenados)


    #Método para construir el árbol balanceado a partir de la lista con valores ordenados."""
    def crear_arbol_balanceado(self, valores_ordenados):
        if not valores_ordenados:
            return None
        mid = len(valores_ordenados) // 2
        nodo = Nodo(valores_ordenados[mid])
        nodo.izquierda = self.crear_arbol_balanceado(valores_ordenados[:mid])
        nodo.derecha = self.crear_arbol_balanceado(valores_ordenados[mid + 1:])
        return nodo




#Método con menú y acciones a ejecutar
def gestionar_arbol():
    arbol = ArbolBinario() # instanciamos nuestro arbol vacío con todos lo métodos necesario

    while True:
        print("Opciones:")
        print("1. Insertar números en el árbol")
        print("2. Balancear el árbol")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numeros = input("Ingrese una serie de números separados por espacios: ")
            for num in map(int, numeros.split()):
                arbol.insertar(num)
            print("Números insertados en el árbol (sin balancear): ", numeros.split())

        elif opcion == "2":
            arbol.balancear()
            print("Árbol balanceado en recorrido preorden:")
            arbol.recorrido_preorden_no_recursivo()
            print()

        elif opcion == "3":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

gestionar_arbol()

