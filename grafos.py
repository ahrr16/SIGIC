from collections import deque
import heapq
from dados import *

# Definição da função para visualizar a rede de módulos
def visualizar_rede():
    print("\n===== REDE DA COLÔNIA =====")
    for origem, conexoes in grafo().items():
        print(f"\n{origem}:")
        for destino, peso in conexoes:
            print(f"  -> {destino} | peso: {peso}")

# Definição da função para buscar módulos usando BFS (Busca em Largura)
def bfs(inicio):
    
    visitados = [] 
    fila = [inicio]

    while fila:
        atual = fila.pop(0)

        if atual not in visitados:
            visitados.append(atual)

            for vizinho, peso in grafo()[atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)

    return visitados

# Definição da função para buscar módulos usando DFS (Busca em Profundidade)
def dfs(inicio, visitados=None):
    if visitados is None:
        visitados = []

    visitados.append(inicio)

    for vizinho, peso in grafo()[inicio]:
        if vizinho not in visitados:
            dfs(vizinho, visitados)

    return visitados


INF = 1_000_000_000
# Definição da função para buscar o caminho mais curto entre dois módulos usando o algoritmo de Dijkstra
def dijkstra(origem, destino):
    # Inicializa distâncias com infinito e rastreia o módulo anterior no caminho
    distancias = {modulo: INF for modulo in grafo()}
    anteriores = {modulo: None for modulo in grafo()}

    distancias[origem] = 0
    fila = [(0, origem)]  # Fila de prioridade com (distância, módulo)

    # Processa módulos em ordem de distância (processando os mais próximos primeiro)
    while fila:
        distancia_atual, atual = heapq.heappop(fila)

        if atual == destino:
            break

        # Relaxamento das arestas: atualiza distâncias se encontrar caminho melhor
        for vizinho, peso in grafo()[atual]:
            nova_distancia = distancia_atual + peso

            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = atual
                heapq.heappush(fila, (nova_distancia, vizinho))

    # Reconstrói o caminho do destino até a origem
    caminho = []
    atual = destino

    while atual is not None:
        caminho.insert(0, atual)
        atual = anteriores[atual]

    return caminho, distancias[destino]

