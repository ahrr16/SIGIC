'''Algoritmos de modelagem matemática para o consumo de energia da colônia'''
from dados import *
from grafos import *


# Função para calcular a perda energética entre dois módulos usando o algoritmo de Dijkstra
def perda_energetica(origem, destino):
    caminho, distancia = dijkstra(origem, destino)
    if caminho is not None:
        perda = distancia * 0.1  # Supondo que a perda energética seja de 10% da distância
        return f'Perda de {perda}% de energia da colônia ao percorrer o caminho de {origem} para {destino}'
    else:
        return None
    
# Função para calcular o consumo total de energia da colônia    
def consumo_total():
    
    total = 0
    consumo = modulos_infos()[0]  # Obtém o consumo de energia dos módulos
    if modulos_infos()[4] is not None:  # Verifica se o status operacional está disponível
        status = modulos_infos()[4]  # Obtém o status operacional dos módulos
        for i in range(len(consumo)):
            if status[i] == 1:  # Considera apenas os módulos operacionais
                total += consumo[i]
    return total

# Função para calcular o crescimento do consumo de energia da colônia ao longo do tempo
def aumento_consumo(taxa, tempo):
    return consumo_total() * taxa * tempo # Calcula o aumento do consumo de energia com base na taxa e no tempo fornecidos

def modelagem(taxa, tempo):
    # Calcula o consumo inicial e o consumo futuro estimado com base na taxa de crescimento e no tempo fornecidos
    consumo = consumo_total()
    resultado = aumento_consumo(taxa, tempo)

    print(f"\nConsumo inicial: {consumo} kW")
    print(f"Taxa de crescimento: {taxa}")
    print(f"Tempo analisado: {tempo}")
    print(f"Consumo futuro estimado: {resultado}")

    # Verifica se o consumo futuro excede o limite de 220 kW e retorna uma mensagem de alerta
    if resultado > 220:
        print("ALERTA: será necessário otimizar o uso de energia.")
    else:
        print("A infraestrutura permanece dentro do limite energético.")

