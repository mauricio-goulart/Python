from random import randint

n = [randint(0,5), randint(0,5), randint(0,5), randint(0,5), randint(0,5)]

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Número sorteados: ', end='')
for numero in n:
    print(f'{numero}', end=' ')

print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'Maior valor:[{max(n)}]')
print(f'Menor valor:[{min(n)}]')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')


