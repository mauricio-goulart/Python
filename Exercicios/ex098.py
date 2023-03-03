def cont(c1,c2,c3):
    for con in range(c1,c2 + 1,c3):
        print(f'{con}', end=' ')
    print('FIM!')


print('-=' * 20)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1,11):
    print(f'{c}', end=' ')
print('FIM!')
print('-=' * 20)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10,-1,-2):
    print(f'{c}', end=' ')
print('FIM!')
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
c1 = int(input(f'Incio:  '))
c2 = int(input(f'Fim:    '))
c3 = int(input(f'Passo:  '))
cont(c1,c2,c3)
print('-=' * 20)

