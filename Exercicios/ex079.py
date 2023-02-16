numeros = list()
cond = ''
while True:

    for n in numeros:
        numeros.append(int(input('Digite um valor: ')))
        
    cond = str(input('Quer continuar: [S/N] '))
    if cond in 'Nn':
        print('-=' * 15)
        break
print(numeros)
