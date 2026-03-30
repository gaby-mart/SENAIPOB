a = int(input("Digite o coeficiente a: "))
b = int(input("Digite o coeficiente b: "))
c = int(input("Digite o coeficiente c: "))

if a != 0:
    delta = b * b - 4 * a * c
    if delta > 0:
        raiz1 = (-b + delta) / (2 * a)
        raiz2 = (-b - delta) / (2 * a)
        print(f'As raizes são {raiz1} e {raiz2}')
    elif delta == 0:
        raiz1 = (-b + delta) / (2 * a)
        print(f'A raiz é {raiz1}.')
    else:
        print("Delta inálido")
else:
    print("Coeficiente 'a' é inválido.")

