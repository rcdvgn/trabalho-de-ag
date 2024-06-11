# 1. Importações e Definições Iniciais
import random

def gera_bit():
    return random.choice([0, 1])

def gera_cromossomo(L):
    return [gera_bit() for _ in range(L)]

def gera_populacao_inicial(N, L):
    return [gera_cromossomo(L) for _ in range(N)]


# 2. Fitness e Média de Fitness
def fitness(cromossomo):
    return sum(cromossomo)

def media_fitness(populacao):
    total_fitness = sum(fitness(individuo) for individuo in populacao)
    return total_fitness / len(populacao)


# 3. Seleção
def seleciona_elite(populacao, elite_size):
    populacao.sort(key=lambda x: fitness(x), reverse=True)
    return populacao[:elite_size]


# 4. Cruzamento (Crossover)
def cruzamento(ponto, cromossomo1, cromossomo2):
    c1, c2 = cromossomo1[:ponto], cromossomo1[ponto:]
    c3, c4 = cromossomo2[:ponto], cromossomo2[ponto:]
    return c1 + c3, c2 + c4

def crossover(populacao, ponto_cruzamento):
    if len(populacao) % 2 != 0:
        populacao.append(populacao[-1])

    nova_populacao = []
    for i in range(0, len(populacao), 2):
        c1, c2 = populacao[i], populacao[i+1]
        filho1, filho2 = cruzamento(ponto_cruzamento, c1, c2)
        nova_populacao.extend([filho1, filho2])
    return nova_populacao


# 5. Mutação
def mutacao(populacao, taxa_mutacao):
    nova_populacao = []
    for individuo in populacao:
        novo_individuo = individuo[:]
        for i in range(len(novo_individuo)):
            if random.random() < taxa_mutacao:
                novo_individuo[i] = 1 - novo_individuo[i]
        nova_populacao.append(novo_individuo)
    return nova_populacao


# 6. Loop Principal do Algoritmo Genético
def ag(N, L, ponto_cruzamento, taxa_mutacao, max_geracoes):
    populacao = gera_populacao_inicial(N, L)

    for geração in range(max_geracoes):
        populacao = seleciona_elite(populacao, int(N * 0.1))

        populacao = crossover(populacao, ponto_cruzamento)

        populacao = mutacao(populacao, taxa_mutacao)

        print(f'Geração {geração}: Média de Fitness = {media_fitness(populacao)}')

        if media_fitness(populacao) >= 100:
            break

    return populacao


# Uso
N = 50
L = 100
ponto_cruzamento = 50
taxa_mutacao = 0.01
max_geracoes = 200

solucao_aproximada = ag(N, L, ponto_cruzamento, taxa_mutacao, max_geracoes)
print("Solução aproximada:", solucao_aproximada)
