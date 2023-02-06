maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Digite o peso da {p}º: '))
    if peso > maior:
        maior = peso
    if peso