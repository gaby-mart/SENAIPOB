import numpy as np

temperaturas = np.random.uniform(1, 100, 30)

maior = np.max(temperaturas)
menor = np.min(temperaturas)
media = np.mean(temperaturas)

print(f"A maior temperatura neste mês é: {maior:.2f}°C")
print(f"A menor temperatura neste mês é:{menor:.2f}°C")
print(f"A media destas temperaturas: {media:.2f}°C")

qtd= len(temperaturas[temperaturas>75])
print(f"A temperatura ultrapassou o recomendado {qtd} vezes")

