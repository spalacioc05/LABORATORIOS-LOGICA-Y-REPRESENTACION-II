import matplotlib.pyplot as plt
import networkx as nx
import random

# Crear grafo con un ciclo for para agregar nodos
def crear_grafo_con_nodos():
    grafo = nx.Graph()  # Crea un grafo vacío
    for id in range(100):
        grafo.add_node(id)  # Agrega cada id como nodo
    return grafo

grafo = crear_grafo_con_nodos()

def agregar_conexiones_aleatorias(grafo):
    nodos = list(grafo.nodes)

    for nodo in nodos:
        conexiones = random.randint(5, 10)  # Numero aleatorio de conexiones entre 5 y 10
        posibles_amigos = set(nodos) - {nodo}  # Excluir al nodo actual para que no haya relación consigo él mismo)
        amigos = random.sample(sorted(posibles_amigos), min(conexiones, len(posibles_amigos)))  # Elegir nodos aleatorios
        for amigo in amigos:
            grafo.add_edge(nodo, amigo)  # Crear una relacion entre el nodo actual y el amigo seleccionado


agregar_conexiones_aleatorias(grafo)

amigo_a = int(input("Ingrese id de la primera persona (número entre0 y 99): "))
amigo_b = int(input("Ingrese id de la segunda persona (número entre0 y 99): "))


def encontrar_amigos_comunes(grafo, amigo_a, amigo_b):
    amigos_persona_a = set(grafo.neighbors(amigo_a))
    amigos_persona_b = set(grafo.neighbors(amigo_b))


    amigos_comunes = amigos_persona_a.intersection(amigos_persona_b)
    return amigos_comunes

amigos_comunes = encontrar_amigos_comunes(grafo, amigo_a, amigo_b)
print(f"Amigos en común entre {amigo_a} y {amigo_b}: {amigos_comunes}")

nx.draw(grafo, with_labels=True, node_size=700, node_color="lightblue", font_size=10)
plt.show()