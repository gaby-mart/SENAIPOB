dia = int(input("Qual seu dia de nascimento: "))
mes = int(input("Qual seu mes de nascimento: "))
ano = int(input("Qual seu ano de nascimento: "))

if 1900 <= ano <= 2026:
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    if 1 <= mes <= 12:

        if mes == 2:
            if bissexto:
                if 1 <= dia <= 29:
                    print("Data válida no calendário gregoriano.")
                else:
                    print("Data inválida no calendário gregoriano.")
            else:
                if 1 <= dia <= 28:
                    print("Data válida no calendário gregoriano.")
                else:
                    print("Data inválida no calendário gregoriano.")

        elif mes in [4, 6, 9, 11]:
            if 1 <= dia <= 30:
                print("Data válida no calendário gregoriano.")
            else:
                print("Data inválida no calendário gregoriano.")

        else:
            if 1 <= dia <= 31:
                print("Data válida no calendário gregoriano.")
            else:
                print("Data inválida no calendário gregoriano.")

    else:
        print("Mês inválido")

else:
    print("Ano inválido")