import numpy as np

matriz = np.random.uniform(-10, 10, (3,3))
print(matriz)

somaDiagonalPrincipal = np.trace(matriz)
print(f"O valor soma da Diagonal Principal é: {somaDiagonalPrincipal}")

somaDiagonalSecundaria = np.sum(np.fliplr(matriz).diagonal())
print(f"O valor soma da Diagonal Secundária é: {somaDiagonalSecundaria}")

matriz[matriz<0] = 0
print(matriz)