print('-=' * 20)
print('\tDIGITE 5 NÚMEROS')
print('-=' * 20)

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
n5 = int(input('Digite outro número: '))
print('-=' * 20)

numeros = [n1, n2, n3, n4, n5]

print(f'O valor [9] apareceu:[{numeros.count(9)}] Vezes')