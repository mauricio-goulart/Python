n = int(input('Digite um número: '))
print(f'{"Par ou Impar":=^25}')
if n % 2 == 0 :
    print(f'[PAR]')
else:
    print(f'[IMPAR]')
print('=' * 25)