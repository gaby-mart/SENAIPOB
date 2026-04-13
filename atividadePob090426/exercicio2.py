num = int(input("Digite um número:"))
par = []
impar = []



if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
    par.append(num)
    print(f'{num} é par.')

    while num != 1:
        num = num // 2
        par.append(num)

    print(f'Sequência em números pares:{par}')

else:
    impar.append(num)
    print(f'{num} é impar.')

    while num != 1:
        num = num * 3 + 1
        impar.append(num)
        
    print(f'Sequência em números impares: {impar}')








