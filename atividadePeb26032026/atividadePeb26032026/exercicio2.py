import math
a = float(input("Digite o valor do primeiro lado do triângulo: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if a+b < c and b+c < a and a+c < b:
    print("Triângulo inválido")
else:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

maior = max(a, b, c)

if maior == a:
    if a**2 == b**2 + c**2:
        print("Triângulo retângulo também.")
elif maior == b:
    if b**2 == c**2 + a**2:
        print("Triângulo retângulo também.")
else:
    if c**2 == b**2 + a**2:
        print("Triângulo retângulo também.")
