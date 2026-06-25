from dados import *
from grafos import *
from modelagem import *


def consultar_modulo(): # Função para consultar informações de um módulo específico

    nome = modulo_selecionado

    if nome in modulos(): # Verifica se o módulo existe na lista de módulos
        print("\n===== DADOS DO MÓDULO =====") # Exibe os dados do módulo
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

# Menu simples de interação no terminal para o usuário escolher as opções disponíveis no SIGIC

while True:
    # Menu principal
    print("\n===== SIGIC - AURORA SIGER =====")
    print("1 - Visualizar rede da colônia")
    print("2 - Consultar módulo")
    print("3 - Executar BFS")
    print("4 - Executar DFS")
    print("5 - Calcular caminho mínimo com Dijkstra")
    print("6 - Perda de energia da colônia")
    print("7 - Consumo total de energia da colônia")
    print("8 - Crescimento do consumo de energia da colônia")
    print("9 - Modelagem matemática do consumo de energia da colônia")
    print("0 - Sair")

    # Solicita ao usuário que escolha uma opção do menu
    opcao = input("Escolha uma opção: ")
    
    # Executa a ação correspondente à opção escolhida pelo usuário
    match opcao:
        case "1":
            visualizar_rede()
                
        case "2":
            print('Módulos disponíveis para consulta: ' + ', '.join(modulos()))
            modulo_selecionado = input("Digite o nome do módulo que deseja consultar: ")
            consultar_modulo()


        case "3":
            print("\n===== BUSCA EM LARGURA (BFS) =====")
            print('Módulos disponíveis para consulta: ' + ', '.join(modulos()))
            inicio = input("Digite o módulo de inicio: ")
            if inicio in grafo():
                print("BFS:", bfs(inicio))
            else:
                print("Módulo inválido.")

        case "4":
            print("\n===== BUSCA EM PROFUNDIDADE (DFS) =====")
            print('Módulos disponíveis para consulta: ' + ', '.join(modulos()))
            inicio = input("Digite o módulo de inicio inicial: ")
            if inicio in grafo():
                print("DFS:", dfs(inicio))
            else:
                print("Módulo inválido.")
        case "5":
            print("\n===== CAMINHO MÍNIMO COM DIJKSTRA =====")
            print('Módulos disponíveis para consulta: ' + ', '.join(modulos()))
            origem = input("Digite o módulo de origem: ")
            destino = input("Digite o módulo de destino: ")
            if origem in grafo() and destino in grafo():
                caminho, distancia = dijkstra(origem, destino)
                if caminho is not None:
                    print(f"Caminho mais curto de {origem} para {destino}: {' -> '.join(caminho)} | Distância total: {distancia}")
                else:
                    print(f"Não há caminho entre {origem} e {destino}.")
            else:
                        print("Módulo inválido.")

        case "6":
            print("\n===== PERDA DE ENERGIA DA COLÔNIA =====")
            print('Módulos disponíveis para consulta: ' + ', '.join(modulos()))
            origem = input("Digite o módulo de origem: ")
            destino = input("Digite o módulo de destino: ")
            print(perda_energetica(origem, destino))
                
        case "7":
            print("\n===== CONSUMO TOTAL DE ENERGIA DA COLÔNIA =====")
            print("Consumo total de energia da colônia:", consumo_total(), "kW")    
                
        case "8":
            print("\n===== CRESCIMENTO DO CONSUMO DE ENERGIA =====")
            tempo = float(input("Digite o tempo (em unidades): "))
            taxa = float(input("Digite a taxa de crescimento (em %): "))
            print("Crescimento do consumo de energia da colônia:", aumento_consumo(taxa, tempo), "kW")

        case "9":
            print("\n===== MODELAGEM MATEMÁTICA DO CONSUMO DE ENERGIA DA COLÔNIA =====")
            print("Função usada: C(t) = C0 + k.t")
            print("C(t): consumo no tempo")
            print("C0: consumo inicial")
            print("k: taxa de crescimento")
            print("t: tempo")
            tempo = float(input("Digite o tempo (em unidades): "))
            taxa = float(input("Digite a taxa de crescimento (em %): "))
            modelagem(taxa, tempo)

        case "0":
            print("SIGIC encerrado.")
            break

        case _:
            print("Opção inválida.")
