from datetime import date
print('Alistamento Militar')
print('-=' * 15)

i = int(input('Data de nascimento: '))

if date.today().year - i == 18 :
    print(f'Idade:[{date.today().year - i}]')
    print(f'Está na hora de se ALISTAR')
elif date.today().year - i < 18 :
    print(f'Idade:[{date.today().year - i}]')
    print(f'Ainda não está na hora')
    print(f'Falta:[{ 18-(2023 - i )}] Anos')
elif date.today().year - i > 18 :
    print(f'Você está [{(2023 - i) - 18}] anos atrasado')

print('=-' * 15)