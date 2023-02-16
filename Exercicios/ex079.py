numeros = list()
cond = ''
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado a lista')
    else:
        print('Número duplicado, não adicionado...')
    print('-=' * 15)
    cond = str(input('Quer continuar: [S/N] '))
    print('-=' * 15)
    if cond in 'Nn':
        break
print('Números da lista: ', end='')
for n in numeros:
    print(f'{n} ', end='')
