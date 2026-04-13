import random

num = list(range(1,101))

escolha = random.choice(num)

for tentativa in range(1, 11):
    chute = int(input("Digite um numero de 1 a 101: "))
    print(f"É a tentativa {tentativa}")
    tentativa += 1

    if chute == 1 and chute <= 100:
        if chute >= escolha + 20:
            print(f"{chute} é muito alto")
            print(f"Tente novamente")
        elif chute >= escolha + 10:
            print(f"{chute} é alto")
            print(f"Tente novamente")
        elif chute <= escolha - 20:
            print(f"{chute} é muito baixo")
            print(f"Tente novamente")
        elif chute <= escolha - 10:
            print(f"{chute} é baixo.")
            print(f"Tente novamente")
        else:
            print(f"Você Conseguiu!!")
            print(f"Usou {tentativa} tentativas.")
    else:
        print("Número invalido")