import math
import random
import matplotlib.pyplot as plt

def calculo_analitico(n, k, p):
    """Implementação da fórmula deduzida no 1.1"""
    a = 0
    for i in range(k, n + 1):
        combinacao = math.comb(n, i)
        a += combinacao * (p**i) * ((1-p)**(n-i))
    return a

def simulador_estocastico(n, k, p, rodadas=10000):
    """Simula o comportamento real do sistema"""
    sucessos = 0
    for _ in range(rodadas):
        servidores_ativos = 0
        for _ in range(n):
            # Gera número aleatório e verifica se o servidor está UP
            if random.random() <= p:
                servidores_ativos += 1
        
        # O serviço está operacional se pelo menos k servidores estão UP
        if servidores_ativos >= k:
            sucessos += 1
            
    return sucessos / rodadas

# --- Execução e Comparação ---
n = 10
p_valores = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99]
casos_k = [1, n//2, n] # k=1 (consulta), k=5 (quórum), k=10 (escrita)

print(f"{'p':<6} | {'k':<4} | {'Analítico':<12} | {'Simulado':<12} | {'Erro'}")
print("-" * 55)

resultados = {k: {"p": [], "ana": [], "sim": []} for k in casos_k}

for k in casos_k:
    for p in p_valores:
        ana = calculo_analitico(n, k, p)
        sim = simulador_estocastico(n, k, p)
        erro = abs(ana - sim)
        
        resultados[k]["p"].append(p)
        resultados[k]["ana"].append(ana)
        resultados[k]["sim"].append(sim)
        
        print(f"{p:<6.2f} | {k:<4} | {ana:<12.6f} | {sim:<12.6f} | {erro:.6f}")

# --- Geração dos Gráficos ---
plt.figure(figsize=(12, 7))

cores = {1: 'blue', n//2: 'green', n: 'red'}
labels = {1: 'k=1 (Consulta)', n//2: f'k={n//2} (Quórum)', n: f'k={n} (Atualização)'}

for k in casos_k:
    # Linha para o analítico
    plt.plot(resultados[k]["p"], resultados[k]["ana"], label=f"{labels[k]} - Teoria", 
             linestyle='-', marker='o', color=cores[k])
    # Pontos para o simulado
    plt.scatter(resultados[k]["p"], resultados[k]["sim"], label=f"{labels[k]} - Simulação", 
                color=cores[k], alpha=0.5)

plt.title(f"Comparação Analítica vs Simulação (n={n} servidores)")
plt.xlabel("Probabilidade de um servidor estar disponível (p)")
plt.ylabel("Disponibilidade do Serviço (A)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig("comparacao_disponibilidade.png")
plt.show()