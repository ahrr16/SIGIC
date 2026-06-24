from collections import deque
from dados import conexao_rede

def bfs(matriz, V, inicio):
    
    visitado = [False] * V      # Marca quais vértices já foram visitados
    queue = deque()            # Fila para BFS
    ordem = []                 # Armazena a ordem de visita

    visitado[inicio] = True
    queue.append(inicio)

    while queue:
        u = queue.popleft()    # Remove o primeiro da fila
        ordem.append(u)        # Adiciona à ordem de visita

        # Percorre todos os vértices adjacentes
        for v in range(V):
            if matriz[u][v] != 0 and not visitado[v]:
                visitado[v] = True
                queue.append(v)
    
    return ordem

# Python
# parent: lista representando o pai de cada nó no caminho
# s: nó de origem
# t: nó de destino
def print_path(matriz, inicio, fim):
    path = []
    current = fim

    # Percorre os pais de t até s
    while current != -1:
        path.append(current)
        if current == inicio:
            break
        current = fim[current]

    # Verifica se s realmente conecta t
    if path[-1] != inicio:
        print("Não há caminho de", inicio, "para", fim)
        return

    # Inverte e imprime o caminho
    path.reverse()
    print("Caminho de", inicio, "para", fim, ":", ' -> '.join(map(str, path)))


INF = 1_000_000_000

# Retorna o índice do vértice não finalizado com menor distância
def min_dist(dist, used, V):
    best = INF
    idx = -1
    for i in range(V):
        if not used[i] and dist[i] < best:
            best = dist[i]
            idx = i
    return idx

# w[u][v] = peso; 0 significa "sem aresta"
def dijkstra(matriz, V, inicio):
    dist = [INF] * V
    parent = [-1] * V
    used = [False] * V

    dist[inicio] = 0

    for _ in range(V):
        u = min_dist(dist, used, V)
        if u == -1:
            break  # não há mais alcançáveis

        used[u] = True

        # Relaxamento das arestas saindo de u
        for v in range(V):
            if matriz[u][v] > 0 and not used[v]:
                if dist[u] + matriz[u][v] < dist[v]:
                    dist[v] = dist[u] + matriz[u][v]
                    parent[v] = u

    return dist, parent

def print_path_parent(parent, inicio, fim):
    stack = []
    v = fim

    # Monta o caminho de t até s
    while v != -1:
        stack.append(v)
        if v == inicio:
            break
        v = parent[v]

    # Verifica se existe caminho
    if len(stack) == 0 or stack[-1] != inicio:
        print(f"Sem caminho de {inicio} para {fim}.")
        return

    # Imprime o caminho na ordem correta
    for i in range(len(stack) - 1, -1, -1):
        if i > 0:
            print(stack[i], end=" -> ")
        else:
            print(stack[i])

dist, parent = dijkstra(conexao_rede(),7,0)
print(parent)

print(print_path_parent(parent,0,7))

