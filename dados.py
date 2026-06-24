'''Definição dos módulos, informações referentes aos módulos e os caminhos entre os módulos '''

# Definição da função que contêm os módulos de exploração 
def modulos():
    return ['Habitação', 'Centro de controle', 'Armazenamento de energia', 'Agricultura', 'Laboratório científico', 'Comunicação', 'Suporte médico', 'Produção de oxigênio']# Definição dos módulos

# Definição da função que contêm as informações referentes aos módulos 
def modulos_infos():
   infos = ((30, 10, 5, 60, 25, 8, 15, 40), # Consumo em kW de potência contínua
            (1, 1, 0.75, 0.5, 0.5, 0.75, 1, 1), # Ordem de preioridade dos módulos, sendo 1 o mais crítico
            (5560,200,2000,3300,500,100,200,200), # Armazenamento total dos módulos, podendo ser medidos em kg, tb, kWh 
            (1,1,1,1,1,1,1,1), # Necessidade de comunicação entre os módulos
            (1,1,1,1,1,1,1,1)) # Status operacional do módulo
   return infos

# Definição da função com os caminhos entre os módulos
def conexao_rede():
        return[
        [0, 20, 70, 60, 80, 60, 15, 25],
        [20, 0, 40, 0, 0, 70, 0, 0],
        [70, 40, 0, 45, 95, 110, 100, 110],
        [60, 0, 45, 0, 0, 0, 0, 88],
        [80, 0, 95, 0, 0, 0, 0, 100],
        [60, 70, 110, 0, 0, 0, 0, 30],
        [15, 0, 100, 0, 0, 0, 0, 25],
        [25, 60, 110, 88, 100, 30, 25, 0]]

# Relação legível entre os nomes dos módulos e a matriz de conexões
def relacoes_modulos_conexoes():
    nomes = modulos()
    matriz = conexao_rede()
    return {nome: linha for nome, linha in zip(nomes, matriz)}

# Lista as conexões diretas entre módulos com peso
def conexoes_com_nomes():
    nomes = modulos()
    matriz = conexao_rede()
    conexoes = []
    for i in range(len(nomes)):
        for j in range(i + 1, len(nomes)):
            peso = matriz[i][j]
            if peso != 0:
                conexoes.append((nomes[i], nomes[j], peso))
    return conexoes
