num = int(input('Digite um Número: '))

for contador in range(1, num + 1):

    if num % contador == 0:
        print('\033[34m', end=' ')
    else:
        print('\033[m', end=' ')

    print(contador, end=' ')