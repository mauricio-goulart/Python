
lista = [[], []]
cont = 1
while True:
    print('-=' * 3, f'{cont}ºLOJA', '-=' * 3)
    cid = str(input('Cidade: ')).capitalize().strip()
    lista[0].append(cid)
    fatu = float(input('Faturamento: R$'))
    lista[1].append(fatu)
    cont = cont + 1
    cond = str(input('--> Quer continuar? [S/n]')).strip()
    if cond in 'Nn':
        break

print(lista)

