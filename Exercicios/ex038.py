n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('-=' * 15)

if n1 > n2 :
    print(f'Maior:[{n1}]')
    print(f'Menor:[{n2}]')

elif n2 > n1 :
    print(f'Maior:[{n1}]')
    print(f'Menor:[{n2}]')

else:
    print('[IGUAIS]')

print('-=' * 15)