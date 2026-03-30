velocidade = int(input('Qual a velocidade do carro?: km/h'))
limiteVia = int(input('Qual o limite da via?: '))

if limiteVia < 100:
    if velocidade > limiteVia + 7:
        if velocidade == 107:
            print("Isento")
        elif velocidade < limiteVia + limiteVia * 0.20:
            print("Multa Média")
        elif velocidade > limiteVia + limiteVia * 0.20 and velocidade < limiteVia + limiteVia * 0.50:
            print("Multa Grave")
        else:
            print("Multa Gravíssima + Suspensão")
else:
    if velocidade > limiteVia + limiteVia * 0.07:
        if velocidade == limiteVia + limiteVia * 0.07:
            print("Isento")
        elif velocidade <= limiteVia + limiteVia * 0.20:
            print("Multa Média")
        elif velocidade > limiteVia + limiteVia * 0.20 and velocidade < limiteVia + limiteVia * 0.50:
            print("Multa Grave")
        else:
            print("Multa Gravíssima + Suspensão")
