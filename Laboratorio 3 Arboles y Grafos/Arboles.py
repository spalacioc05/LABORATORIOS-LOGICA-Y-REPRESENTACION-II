import matplotlib.pyplot as plt

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevoNodo = Nodo(valor)
        
        if self.raiz is None:
            self.raiz = nuevoNodo
            
        else:
            actual = self.raiz
            while actual:
                padre = actual
                if valor < actual.valor:
                    actual = actual.izquierda
                    
                else:
                    actual = actual.derecha
                    
            if valor < padre.valor:
                padre.izquierda = nuevoNodo
                
            else:
                padre.derecha = nuevoNodo

    def recorridoInordenNoRecursivo(self):
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

    def recorridoPreordenNoRecursivo(self):
        if self.raiz is None:
            return

        pila = []
        pila.append(self.raiz)

        while pila:
            nodo = pila.pop()
            print(nodo.valor, end=' ')

            if nodo.derecha:
                pila.append(nodo.derecha)
                
            if nodo.izquierda:
                pila.append(nodo.izquierda)

    def balancear(self):
        if not self.estaBalanceado(self.raiz):
            valoresOrdenados = self.recorridoInordenNoRecursivo()
            self.raiz = self.crearArbolBalanceado(valoresOrdenados)

    def crearArbolBalanceado(self, valoresOrdenados):
        if not valoresOrdenados:
            return None
        
        mid = len(valoresOrdenados) // 2
        nodo = Nodo(valoresOrdenados[mid])
        nodo.izquierda = self.crearArbolBalanceado(valoresOrdenados[:mid])
        nodo.derecha = self.crearArbolBalanceado(valoresOrdenados[mid + 1:])
        
        return nodo

    def estaBalanceado(self, nodo):
        if nodo is None:
            return True

        alturaIzquierda = self.altura(nodo.izquierda)
        alturaDerecha = self.altura(nodo.derecha)

        if abs(alturaIzquierda - alturaDerecha) <= 1 and self.estaBalanceado(nodo.izquierda) and self.estaBalanceado(nodo.derecha):
            return True

        return False

    def altura(self, nodo):
        if nodo is None:
            return 0
        
        return max(self.altura(nodo.izquierda), self.altura(nodo.derecha)) + 1

    def graficarArbol(self):
        if not self.raiz:
            print("El árbol está vacío.")
            return

        def recorrerNodos(nodo, x, y, dx, posiciones, conexiones):
            if nodo:
                posiciones[nodo.valor] = (x, y)
                
                if nodo.izquierda:
                    conexiones.append((nodo.valor, nodo.izquierda.valor))
                    recorrerNodos(nodo.izquierda, x - dx, y - 1, dx / 2, posiciones, conexiones)
                    
                if nodo.derecha:
                    conexiones.append((nodo.valor, nodo.derecha.valor))
                    recorrerNodos(nodo.derecha, x + dx, y - 1, dx / 2, posiciones, conexiones)

        posiciones = {}
        conexiones = []
        
        recorrerNodos(self.raiz, 0, 0, 1, posiciones, conexiones)

        for valor, (x, y) in posiciones.items():
            plt.scatter(x, y, s=500, zorder=2)
            plt.text(x, y, str(valor), ha='center', va='center', fontsize=12, zorder=3)

        for de, a in conexiones:
            x1, y1 = posiciones[de]
            x2, y2 = posiciones[a]
            plt.plot([x1, x2], [y1, y2], 'k-', zorder=1)

        plt.axis('off')
        plt.show()

def gestionarArbol():
    arbol = ArbolBinario()

    while True:
        print("Opciones:")
        print("1. Insertar números en el árbol")
        print("2. Balancear el árbol")
        print("3. Graficar árbol")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numeros = input("Ingrese los números separados por espacios: ")
            for num in map(int, numeros.split()):
                arbol.insertar(num)
            print("Números insertados en el árbol (sin balancear): ", numeros.split())

        elif opcion == "2":
            arbol.balancear()
            print("Árbol balanceado en recorrido preorden:")
            arbol.recorridoPreordenNoRecursivo()
            print()

        elif opcion == "3":
            print("\nRepresentación gráfica del árbol:")
            arbol.graficarArbol()

        elif opcion == "4":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


gestionarArbol()