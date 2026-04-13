num = int(input("Digite um número inteiro:"))
soma = 0

for i in range(1, num):
    if num % i == 0:
        soma += i

if soma == num:
    print(f"{num} é um número perfeito.")
else:
    print(f"{num} não é um numero perfeito.")
