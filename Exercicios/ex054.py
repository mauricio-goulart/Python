maior = int(0)
menor = int(0)
print('-=' * 15)
for contador in range(1,3):
    pessoa = int(input(f'Ano de nascimento [{contador}º]Pessoa:'))
    if pessoa >2005:
        maior = maior + 1

    else:
        menor = menor + 1
print('-=' * 15)
print(f'{maior} são menores de idade')
print(f'{menor} são maiores de idade')
print('-=' * 15)