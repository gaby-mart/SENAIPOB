import numpy as np

matriz = np.random.uniform(50, 200, (4, 3))

total = np.sum(matriz, axis=1)
totalcolunas = np.sum(matriz, axis=0)

for i, total2 in enumerate(total):
    print(f"A produção total da máquina {i + 1} foi de {total2:.2f}.")

for j, valor in enumerate(totalcolunas):
    print(f"Total no {j + 1}° turno é: {valor:.2f}")