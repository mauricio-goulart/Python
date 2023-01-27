#nome = 'Mauricio'
#print(f'Olá {nome:>20} !')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print(f'A soma entre [{n1}] e [{n2}] é [{s}] e subtração é [{sub}]')
print(f'A multiplição é [{m}] a divisão é [{d:.3f}] a divisão exata é [{di}]')
print(f'A potenciação é [{p}]')