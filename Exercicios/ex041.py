from datetime import date

i = int(input('Ano de Nascimento: '))
idade = date.today().year - i
print('-=' * 15)

if idade <= 9 :
    print('Mirim')
elif idade <= 14 :
    print('Infantil')
elif idade <=19 :
    print('Junior')
elif idade <= 20 :
    print('Senior')
else:
    print('Senior')

