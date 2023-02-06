maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}º: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
         maior = peso
        if peso < menor:
            menor = peso
print('-=' * 15)
print(f'Menor peso:[{menor}]')
print(f'Maior peso:[{maior}]')
print('-=' * 15)
