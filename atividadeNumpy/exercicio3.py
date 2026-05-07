import numpy as np

vetor = np.random.randint(1,101, 100)

min = np.min(vetor)
max = np.max(vetor)

vetor_normal = (vetor - min) / (max-min)

print(f"Vetor Original: {vetor}")
print("Vetor normalizado:", np.round(vetor_normal, 2))