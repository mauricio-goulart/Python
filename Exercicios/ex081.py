lista = []
cond = ''
while True:
    lista.append(int(input('Digite um valor: ')))
    cond = str(input('Quer continuar: [S/N] '))
    if cond in 'Nn':
        break
print('-=' * 30)
print(f'Elementos:[{len(lista)}]')
lista.sort(reverse=True)
print(f'Ordem decrescente:{lista}')
if 5 in lista:
    print(f'Não teve números 5')
else:
    print(f'O valor [5] faz parte da lista')