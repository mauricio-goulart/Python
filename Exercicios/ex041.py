from datetime import date

i = int(input('Ano de Nascimento: '))
idade = date.today().year - i
print('-=' * 15)

if idade <= 9 :
    print(f'Idade:[{idade}]')
    print('Categoria:[Mirim]')
elif idade <= 14 :
    print(f'Idade:[{idade}]')
    print('Categoria:[Infantil]')
elif idade <=19 :
    print(f'Idade:[{idade}]')
    print('Categoria:[Junior]')
elif idade <= 20 :
    print(f'Idade:[{idade}]')
    print('Categoria:[Senior]')
else:
    print(f'Idade:[{idade}]')
    print('Categoria:[Master]')

print('-=' * 15)

