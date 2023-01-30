import math
co = float(input('Digite o Cateto Oposto:'))
ca = float(input('Digite o Cateto Adjaceste:'))
hyp = math.hypot(ca,co)
print(f'{"Calcular Hipotenusa":=^40}')
print(f'Hipotenusa: [{hyp:.2f}]')
print(40 * '=')