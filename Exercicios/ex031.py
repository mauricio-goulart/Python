viagem = float(input('Distância da viagem em KM: '))
print(f'{"Passagem":=^20}')

if viagem >= 200:
    print(f'Valor passagem:[{viagem * 0.45}]')
else:
    print(f'Valor passagem:[{viagem * 0.50}]')


print('=' * 20)