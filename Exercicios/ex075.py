print('-=' * 20)
print('\tDIGITE 5 NÚMEROS')
print('-=' * 20)
par = 0

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite outro número: ')))
print('-=' * 20)

print(f'O valor 9 apareceu: [{num.count(9)}] Vezes')
if 3 in num:
    print(f'O valor 3 apareceu na: [{num.index(3)}]ª Posição')
else:
    print(f'O valor 3 apareceu não apareceu')
print('Valores pares: ', end='')
for n in num:
    if n % 2 == 0:
        print({n}, end='')






