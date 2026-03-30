senha = input("Digite sua senha: ")

if len(senha) < 8:
    print("Inválida: Menos de 8 caracteres")
else:
    tem_minuscula = any(c.islower() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)

    if senha.isdigit() or senha.isupper():
        print("Senha Fraca.")
    elif senha.isalnum():
        print("Senha Média.")
    elif tem_minuscula and tem_maiuscula and tem_numero and tem_especial:
        print("Senha Forte.")


