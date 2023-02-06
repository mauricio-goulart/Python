m = float(0)
idade = float(0)
soma = float(0)
nomev = ''
maioridadeh = 0
mulherm = 0

c = int(input('Quantas pessoas: '))
for contador in range(1,c + 1):
    print(f'----- {contador}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma = soma + idade

    if contador == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomev = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        mulherm = mulherm + 1

media = idade / 4
print('-=' * 15)
print(f'Media de idade:[{media}]')
print(f'Nome homem mais velho:[{nomev}]')
print(f'Quant. de mulheres menor que 20:[{mulherm}]')