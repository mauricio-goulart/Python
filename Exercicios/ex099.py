def maior(*list):
    maior = 0
    print('-=' * 20)
    print('Analisando os valores passados ...')
    for n in list:
        print(f'{n}', end=' ')
    print(f'Foram informados {len(list)} números')
    if n > maior:
        maior = n
    print(f'Maior número = [{maior}]')
    print('-=' * 20)


maior(1,4,3)