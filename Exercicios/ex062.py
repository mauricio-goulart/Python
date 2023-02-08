print('-=' * 15)
print('\t10 TERMOS DE UMA PA')
print('-=' * 15)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais?: '))
print('FIM')