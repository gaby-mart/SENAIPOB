a = 1000
b = 5000
anos = int(input("Quantos anos deseja analisar? "))
populacaoA = []
populacaoB = []

for i in range(anos):
    a = a + (a * 0.03)
    populacaoA.append(a)

    b = b + (b * 0.015)
    populacaoB.append(b)

print(f"População cidade A em {anos} anos: {populacaoA}")
print(f"População cidade B em {anos} anos: {populacaoB}")