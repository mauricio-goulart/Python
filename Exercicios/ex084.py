cond = ''
pessoas = list()
t = list()
mai = men = 0

c = 0

while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(int(input('Peso: ')))
    c = c + 1
    if len(t) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    t.append(pessoas[:])
    pessoas.clear()
    cond = input('Quer continuar: [S/N] ')
    if cond in 'Nn':
        break
print('-=' * 30)
print(f'Você cadastrou {len(t)} pessoas. Peso de ', end='')
print(f'O maior peso foi de {mai}Kg')
for c in t:
    if c[1] == mai:
        print(c[0])
print(f'O menor peso foi de {men}Kg')



