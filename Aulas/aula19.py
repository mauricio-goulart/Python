estado = dict()
brasil = list()
for c in range(0,3):
    estado['UF'] = str(input('Digite o nome do estado:'))
    estado['SIGLA'] = str(input('Digite a sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'{k} = {v}', end=' ')
        print()



