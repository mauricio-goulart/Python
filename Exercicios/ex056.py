m = float(0)
idade = float(0)
soma = float(0)
nomev = ''
maioridadeh = 0
mulherm = 0
for contador in range(1,5):
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
