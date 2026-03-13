import math
import matplotlib.pyplot as plt

def calcular_disponibilidade(n, k, p):
    """
    Calcula a disponibilidade A baseada em:
    n: total de servidores
    k: mínimo necessário (quórum)
    p: probabilidade de um servidor estar UP (0.0 a 1.0)
    """
    a = 0
    for i in range(k, n + 1):
        # Fórmula: C(n, i) * p^i * (1-p)^(n-i)
        combinacao = math.comb(n, i)
        a += combinacao * (math.pow(p, i)) * (math.pow(1 - p, n - i))
    return a

# --- GERAÇÃO DE DADOS PARA O RELATÓRIO ---
n_total = 10      # Exemplo com 10 servidores
prob_individual = 0.95 # 95% de disponibilidade individual
ks = list(range(1, n_total + 1))
disponibilidades = [calcular_disponibilidade(n_total, k, prob_individual) for k in ks]

# --- GERAÇÃO DO GRÁFICO ---
plt.figure(figsize=(10, 6))
plt.plot(ks, disponibilidades, marker='o', linestyle='-', color='b')
plt.title(f'Disponibilidade do Sistema (n={n_total}, p={prob_individual})')
plt.xlabel('Mínimo de servidores necessários (k)')
plt.ylabel('Disponibilidade Total (A)')
plt.grid(True)
plt.xticks(ks)

# Salva o gráfico para o repositório
plt.savefig('grafico_disponibilidade.png')
plt.show()

# Exibe os dados formatados
print("k | Disponibilidade (A)")
print("--|-------------------")
for k, disp in zip(ks, disponibilidades):
    print(f"{k} | {disp:.6f}")