lista = []
listapar = []
listaimpar = []
cond = ''

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    cond = str(input('Quer continuar: [S/N] '))
    print('-=' * 15)
    if cond in 'Nn':
        break
print(f'Lista completa:{lista}')
print(f'Lista pares:{listapar}')
print(f'Lista impares:{listaimpar}')
print('-=' * 15)
