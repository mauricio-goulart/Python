lista = []
citys = []
cont = 1
while True:
    print('-=' * 3, f'{cont}ÂºLOJA', '-=' * 3)
    cid = str(input('Cidade: ')).capitalize().strip()
    citys.append(cid)
    fatu = float(input('Faturamento: R$'))
    citys.append(fatu)
    lista.append(citys[:])
    citys.clear()
    cont = cont + 1
    cond = str(input('--> Quer continuar? [S/n]')).strip()
    if cond in 'Nn':
        break

print(lista)