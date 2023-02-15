numeros = list()

for c in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))

print('-=' * 20)
print('Você digitou os números: ', end='')
for n in numeros:
    print(f' {n} ',end='')

print(f'\nMaior número:[{max(numeros)}] nas posições', end='')

for i, v in enumerate(numeros):
    if v == max(numeros):
        print(f' ...{i}', end='')
print(f'\nMenor número:[{min(numeros)}] nas posições', end='')
for i, v in enumerate(numeros):
    if v == min(numeros):
        print(f' ...{i}', end='')
print('-=' * 20)
