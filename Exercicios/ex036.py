from time import sleep

print('-=' * 15)
print('Bem-Vindo ao Banco do Brasil')
print('-=' * 15)

v = float(input('Digite o valor da casa: R$'))
s = float(input('Digite o valor do seu Salário: R$'))
a = int(input('Anos financiamento: '))
print('-=' * 15)
print('PROCESSANDO...')
sleep(1)
p = v / (a * 12)
print(f'Valor Prestação: R$[{p:.2f}]')

if p > (s * 30) / 100:
    print('Situação:[NEGADO]')
elif p < (s * 30) / 100:
    print('Situação:[ACEITO]')