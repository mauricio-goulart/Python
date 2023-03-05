def votar(idade):
    nasc = 2023 - idade
    cond = ''
    if 18 <= nasc < 65:
        cond = 'Voto Obrigatorio'
        return cond
    elif nasc == 16 or nasc == 17 or nasc > 65:
        cond ='Voto Opcional'
        return cond
    else:
        cond = 'Não Vota'
        return cond


print('-=' * 15)
ano = int(input('Ano Nascimento: '))
vota = votar(ano)
print('-=' * 15)
print(f'Idade: {2023 - ano}')
print(vota)
print('-=' * 15)