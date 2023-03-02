from datetime import date
trabalhador = dict()
print('-=' * 12)
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Idade'] = int(input('Ano nascimento: '))
trabalhador['Idade'] = date.today().year - trabalhador['Idade']
c = int(input('Número Carteira de Trabalho: '))
if c != 0:
    trabalhador['Ctps'] = c
    trabalhador['Contratação'] = int(input('Ano da Contratação: '))
    trabalhador['Salario'] = float(input('Salário: '))
    trabalhador['Idade aposentadoria'] = trabalhador['Idade'] + ((trabalhador['Contratação'] + 35) - date.today().year)
else:
    trabalhador['Ctps'] = 'Desempregado'
print('-=' * 12)
for k,v in trabalhador.items():
    print(f'{k} = {v}')
print('-=' * 12)
