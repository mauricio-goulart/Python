import math
co = int(input('Digite o Cateto Oposto:'))
ca = int(input('Digite o Cateto Adjaceste:'))
hyp = math.hypot(ca,co)
print(f'{"Calcular Hipotenusa":=^40}')
print(f'Hipotenusa: [{hyp:.0f}]')
print(40 * '=')