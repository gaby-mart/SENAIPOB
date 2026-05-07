import numpy as np

a = np.random.uniform(0, 100, 3)
b = np.random.uniform(0, 100, 3)

euclidiana = np.linalg.norm(a - b)

print(f"A posição do Drone A: {a}")
print(f"A posição do Drone B: {b}")
print(f"Os drone estão a {euclidiana:.2f} metros")

if euclidiana < 2.5:
    print(f"Alerta de Colisão")
else:
    print("Drones em distância segura.")