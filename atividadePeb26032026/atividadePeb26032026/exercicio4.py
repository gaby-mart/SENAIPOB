salarioBruto = float(input("Digite o valor do salário bruto: R$"))

if salarioBruto <= 2000:
    print("Isento")
elif salarioBruto >= 2001 and salarioBruto <= 4000:
    taxa1 = salarioBruto * 0.10
    print(f'A taxa para {salarioBruto} é {taxa1}.')
    print(f'O salário liquido é {salarioBruto - taxa1}')
elif salarioBruto >= 4001 and salarioBruto <= 8000:
    taxa2 =((salarioBruto - 4000)*0.20)+(salarioBruto * 0.10)
    print(f'A taxa para {salarioBruto} é {taxa2}')
    print(f'O salário liquido é {salarioBruto - taxa2}')
else:
    taxa3 = ((salarioBruto - 8000)*0.30)+(salarioBruto * 0.10) + (salarioBruto * 0.20)
    print(f'A taxa para {salarioBruto} é {taxa3}')
    print(f'O salário liquido é {salarioBruto - taxa3}')