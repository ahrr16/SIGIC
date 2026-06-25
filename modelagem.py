from dados import *
from grafos import *



def perda_energetica(origem, destino):
    caminho, distancia = dijkstra(origem, destino)
    if caminho is not None:
        perda = distancia * 0.1  # Supondo que a perda energética seja de 10% da distância
        return f'Perda de {perda}% de energia da colônia ao percorrer o caminho de {origem} para {destino}'
    else:
        return None
    
def consumo_total():
    
    total = 0
    consumo = modulos_infos()[0]  # Obtém o consumo de energia dos módulos
    if modulos_infos()[4] is not None:  # Verifica se o status operacional está disponível
        status = modulos_infos()[4]  # Obtém o status operacional dos módulos
        for i in range(len(consumo)):
            if status[i] == 1:  # Considera apenas os módulos operacionais
                total += consumo[i]
    return total

def crescimento_consumo(taxa, tempo):
    return consumo_total() * taxa * tempo # Supondo um crescimento de 5% no consumo total de energia da colônia por unidade de tempo

def simulacao_modelagem(taxa, tempo):
    


    # Calcula projeção de consumo para os próximos períodos
    consumo = consumo_total()
    taxa = 8  # Unidades de energia por período
    tempo = 5  # Períodos futuros

    resultado = crescimento_consumo(taxa, tempo)

    print(f"\nConsumo inicial: {consumo} kW")
    print(f"Taxa de crescimento: {taxa}")
    print(f"Tempo analisado: {tempo}")
    print(f"Consumo futuro estimado: {resultado}")

    # Avisa se a projeção exceder capacidade de geração
    if resultado > 220:
        print("ALERTA: será necessário otimizar o uso de energia.")
    else:
        print("A infraestrutura permanece dentro do limite energético.")

