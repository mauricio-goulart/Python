cond = 's'.upper()
n = 0
d = 0
maior = 0
menor = 0
soma = 0
quant = 0
while cond == 'S':
    n = float(input('Digite uma nota: '))
    soma = soma + n
    d = d + 1
    cond = str(input('Quer continuar?: [S/N]')).upper().strip()
    quant = quant + 1
    if quant == 1:
        maior = n
        menor = n

    else:
        if maior < n:
            maior = n

        elif menor > n:
            menor = n
print('-=' * 15)
print(f'Você digitou [{d} números]')
print(f'Media:[{soma/d}]')
print(f'Maior número:[{maior}]')
print(f'Menor número:[{menor}]')
print('-=' * 15)


