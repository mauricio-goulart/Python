cidade = []
lista = []
cont = 1
while True:
    print('-=' * 3, f'{cont}ºLOJA', '-=' * 3)
    cid = str(input('Cidade: ')).capitalize().strip()
    lista.append(cid)
    fatu = float(input('Faturamento: R$'))
    lista.append(fatu)
    cidade.append(lista[:])
    lista.clear()
    cont = cont + 1
    cond = str(input('--> Quer continuar? [S/n]')).strip()
    if cond in 'Nn':
        break

print('-=' * 4, 'ANALISADO', '-=' * 4)
for c in cidade:
    m = 1
    while m < len(c):
        print(f'{c[m -1]} {c[m]}')
        m = m + 1





