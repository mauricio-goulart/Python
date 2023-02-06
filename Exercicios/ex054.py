maior = int(0)
menor = int(0)
for contador in range(1,8):
    pessoa = int(input(f'Ano de nascimento [{contador}º]Pessoa:'))
    if pessoa >2005:
        maior = maior + 1

    else:
        menor = menor + 1
        print(f'{menor} são maiores de idade')

print(f'{maior} são menores de idade')