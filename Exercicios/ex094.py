pessoas = dict()
lista = list()
p = 1
m = 0
cond = 's'

while True:
    print('-=' * 3, f'{p}ºPessoa', '=-' * 3)
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexo:[M/f]  ')).upper()
    if pessoas['Sexo'] not in 'FfMm':
        while pessoas['Sexo'] not in 'Ffmm':
            pessoas['Sexo'] = str(input('Digite sexo valido:[M/F] '))
    pessoas['Idade'] = int(input('Idade: '))
    m = pessoas['Idade'] + m
    p = p + 1
    lista.append(pessoas.copy())

    cond = str(input(f'-->Quer continuar?[S/N] '))
    if cond in 'Nn':
        break

media = m/(p-1)
print('-=' * 10)
print(f'Pessoas cadastradas: [{len(lista)}]')
print(f'Media idades: [{m/(p-1)}]')
print('Mulheres: ', end='')

for p in lista:
    if p['Sexo'] in 'fF':
        print(p['Nome'])
print('Lista pessoas acima média: ')

for p in lista:
    if p['Idade'] > media:
        print()
        for k,v in p.items():
            print(f'{k} = {v}', end='')
        print()

print('-=' * 10)
