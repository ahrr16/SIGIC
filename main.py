from dados import *
from grafos import *

print('Módulos disponíveis para consulta: ' + ', '.join(modulos()))
modulo_selecionado = input("Digite o nome do módulo que deseja consultar: ")
def consultar_modulo():

    nome = modulo_selecionado

    if nome in modulos():
        print("\n===== DADOS DO MÓDULO =====")
        for i in range(len(modulos())):
            if modulos()[i] == nome:
                infos = modulos_infos()
                print(f"Nome: {modulos()[i]}")
                print(f"Consumo de potência contínua (kW): {infos[0][i]}")
                print(f"Ordem de prioridade: {infos[1][i]}")
                print(f"Armazenamento total: {infos[2][i]}")
                print(f"Necessidade de comunicação: {infos[3][i]}")
                print(f"Status operacional: {infos[4][i]}")
    else:
        print("Módulo não encontrado.")
consultar_modulo()

visualizar_rede()

print("\n===== BUSCA EM LARGURA (BFS) =====")
print(bfs(modulo_selecionado))

print("\n===== BUSCA EM PROFUNDIDADE (DFS) =====")
print(dfs(modulo_selecionado))

print("\n===== CAMINHO MAIS CURTO (DIJKSTRA) =====")
destino = input("Digite o nome do módulo de destino: ")
print(dijkstra(modulo_selecionado, destino))

while True:
        while True:
            print("\n===== SIGIC - AURORA SIGER =====")
            print("1 - Visualizar rede da colônia")
            print("2 - Consultar módulo")
            print("3 - Executar BFS")
            print("4 - Executar DFS")
            print("5 - Calcular caminho mínimo com Dijkstra")
            print("6 - Simular energia da colônia")
            print("7 - Modelagem matemática")
            print("8 - Detectar conexões críticas")
            print("9 - Ver matriz de adjacência")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                visualizar_rede()

            elif opcao == "2":
                consultar_modulo()

            elif opcao == "3":
                inicio = input("Digite o módulo inicial: ")
                if inicio in grafo:
                    print("BFS:", bfs(inicio))
                else:
                    print("Módulo inválido.")

            elif opcao == "4":
                inicio = input("Digite o módulo inicial: ")
                if inicio in grafo:
                    print("DFS:", dfs(inicio))
                else:
                    print("Módulo inválido.")

            elif opcao == "0":
                print("Encerrando o SIGIC...")
                break

            else:
                print("Opção inválida.")