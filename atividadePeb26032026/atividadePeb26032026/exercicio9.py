horaInicial = int(input("Digite a hora inicial:"))
horaFinal = int(input("Digite a hora final:"))
minutoInicial = int(input("Digite a minuto inicial:"))
minutoFinal = int(input("Digite a minuto final:"))

tempoHora = horaFinal - horaInicial
tempoMinuto = minutoFinal - minutoInicial

if tempoHora <= 24 and tempoMinuto <= 1:
    print(f'O jogo durou {tempoHora} horas e {tempoMinuto} minutos.')
else:
    print("Tempo inválido.")



