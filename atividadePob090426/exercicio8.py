opcoes = [1,2,3]
candidato1 = 0
candidato2 = 0
candidato3 = 0

while True:
    voto = int(input(f"Digite os números {opcoes} para escolher um candidato (ou 0 para encerrar a votação): "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 0:
        break
    else:
        print("Voto inválido")

qtdVotos = candidato1 + candidato2 + candidato3

porcentagemVotos = candidato1 / qtdVotos * 100
porcentagemVotos2 = candidato2 / qtdVotos * 100
porcentagemVotos3 = candidato3 / qtdVotos * 100

if candidato1 > candidato2 and candidato1 > candidato3:
    maior = "Candidato 1"
elif candidato2 > candidato1 and candidato2 > candidato3:
    maior = "Candidato 2"
elif candidato3 > candidato1 and candidato3 > candidato2:
    maior = "Candidato 3"
else:
    maior = "Empate"

print(f'Vencedor: {maior}')

print(f'Candidato 1: {candidato1} votos e {porcentagemVotos:.2f} dos votos totais.')
print(f'Candidato 2: {candidato2} votos e {porcentagemVotos2:.2f} dos votos totais.')
print(f'Candidato 3: {candidato3} votos e {porcentagemVotos3:.2f} dos votos totais.')