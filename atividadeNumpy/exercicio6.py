import numpy as np

matriz = np.random.randint(0,255,(8,8))


imagemCentro = matriz[2:6, 2:6]

media = np.mean(imagemCentro)

if media > 120:
    print("Engrenagem centralizada dectectada")
else:
    print("Aréa vazia  ou peça desalinhada")