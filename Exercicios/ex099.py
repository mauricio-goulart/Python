def maior(*list):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados ...')
    for n in list:
        print(f'{n}', end=' ')
    print(f'Foram informados {len(list)} números')
    if cont == 0:
        maior = n
    else:
        if n > maior:
            maior = n
    cont = cont + 1
    print(f'Maior número = [{maior}]')
    print('-=' * 20)


maior(1,4,3)