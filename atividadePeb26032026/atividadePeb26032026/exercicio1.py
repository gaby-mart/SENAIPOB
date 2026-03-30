import math

h0 = int(input("Digite a altura inicial (h0):"))

if h0 >= 0:
    t = math.sqrt(2*h0/9.8)
    print(f'Tempo: {t:.2f} segundos')
else:
    print("Altura inválida: a altura não pode ser negativa.")

