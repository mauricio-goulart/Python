num = int(input('Digite um Número: '))
tot = int(0)
print('-=' * 20)
for contador in range(1, num + 1):

    if num % contador == 0:
        print('\033[34m', end=' ')
        tot = tot + 1
    else:
        print('\033[m', end=' ')

    print(f'{contador}',end=' ')

print('\n\033[m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

if tot > 2:
    print(f'[PRIMO:[NÃO]')

