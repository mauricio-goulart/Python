import math

ang = int(input('Ângulo: '))
rad = math.radians(ang)

print(f'{"Ângulo":=^20}')
print(f'Sen:[{math.sin(rad):.3f}]')
print(f'Cos:[{math.cos(rad):.3f}]')
print(f'Tan:[{math.tan(rad):.3f}]')
print('=' * 20)