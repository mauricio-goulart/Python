m = float(0)
idade = float(0)
soma = float(0)
nomev = ''
for contador in range(1,5):
    print(f'----- {contador}º PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma = soma + idade

media = idade / 4
