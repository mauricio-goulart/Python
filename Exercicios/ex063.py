print('-=' * 15)
print('Sequencia Fibonacci')
print('-=' * 15)
n = int(input('Quantos termos você quer mostrar?: '))
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} > {t2}', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1

print('\nFIM')