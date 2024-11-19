import matplotlib.pyplot as plt
import networkx as nx
import random

def crearGrafo():
    grafo = nx.Graph()
    
    for id in range(100):
        grafo.add_node(id)
        
    return grafo

def agregarConexionesAleatorias(grafo):
    nodos = list(grafo.nodes)
    
    for nodo in nodos:
        conexiones = random.randint(5, 10)
        posiblesAmigos = set(nodos) - {nodo}
        amigos = random.sample(sorted(posiblesAmigos), min(conexiones, len(posiblesAmigos)))
        
        for amigo in amigos:
            grafo.add_edge(nodo, amigo)

def encontrarAmigosComunes(grafo, amigoA, amigoB):
    amigosPersonaA = set(grafo.neighbors(amigoA))
    amigosPersonaB = set(grafo.neighbors(amigoB))
    amigosComunes = amigosPersonaA.intersection(amigosPersonaB)
    
    return amigosComunes

def dibujarGrafoConAmigos(grafo, amigoA, amigoB, amigosComunes):
    plt.figure(figsize=(15, 15))
    pos = nx.spring_layout(grafo)

    coloresNodos = []
    
    for nodo in grafo.nodes:
        if nodo == amigoA or nodo == amigoB:
            coloresNodos.append("green")
            
        elif nodo in amigosComunes:
            coloresNodos.append("orange")
            
        else:
            coloresNodos.append("lightblue")

    coloresAristas = []
    
    for u, v in grafo.edges:
        if (u in amigosComunes and v in amigosComunes) or (u in amigosComunes and (v == amigoA or v == amigoB)) or (v in amigosComunes and (u == amigoA or u == amigoB)):
            coloresAristas.append("red")
            
        else:
            coloresAristas.append("gray")

    nx.draw_networkx_nodes(grafo, pos, node_color=coloresNodos, node_size=900)
    nx.draw_networkx_edges(grafo, pos, edge_color=coloresAristas)
    nx.draw_networkx_labels(grafo, pos, font_size=10)

    plt.title(f"Amigos en común entre {amigoA} y {amigoB}", fontsize=20)
    plt.axis("off")
    plt.show()


grafo = crearGrafo()
agregarConexionesAleatorias(grafo)

amigoA = int(input("Ingrese id de la primera persona (número entre 0 y 99): "))
amigoB = int(input("Ingrese id de la segunda persona (número entre 0 y 99): "))
amigosComunes = encontrarAmigosComunes(grafo, amigoA, amigoB)

print(f"Amigos en común entre {amigoA} y {amigoB}: {amigosComunes}")
dibujarGrafoConAmigos(grafo, amigoA, amigoB, amigosComunes)