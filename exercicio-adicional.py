import math

# Probabilidade individual e quorum
p = 0.5
k = 1

# Disponibilidades alvo
targets = [0.90, 0.99, 0.999, 0.9999, 0.99999, 0.999999]

# Total de minutos em um ano
MINUTOS_ANO = 365 * 24 * 60


def disponibilidade(n, p):
    """
    Calcula a disponibilidade quando k=1:
    A = 1 - (1-p)^n
    """
    return 1 - (1 - p) ** n


def encontrar_n_minimo(target, p):
    """
    Encontra o número mínimo de servidores necessários
    para atingir a disponibilidade desejada
    """
    n = 1
    while disponibilidade(n, p) < target:
        n += 1
    return n


print("Disponibilidade | n mínimo | Perda anual (min)")
print("---------------|---------|------------------")

for target in targets:

    n = encontrar_n_minimo(target, p)

    perda = (1 - target) * MINUTOS_ANO

    print(f"{target:.6%} | {n:^7} | {perda:>10.4f}")