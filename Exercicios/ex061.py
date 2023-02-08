print('-=' * 15)
print('\t10 TERMOS DE UMA PA')
print('-=' * 15)

primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
cont = 1
termo = primeiro
while cont <= 10:
    print(f'{termo}', end=' ')
    termo = termo + razao
    cont = cont + 1
print('FIM')