n1 = int(input('Velocidade do carro: '))
print(f'{"Radar":=^20}')
if n1 > 80 :
    print(f'Multado! Limite [80]Km. Total a Pagar:[{(n1 - 80) * 7}]')
else:
    print(f'Excelente! Tenha um ótimo dia!')
