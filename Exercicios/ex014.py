temp = float(input('Temperatura °C:'))
print(f'{"Conversor":=^20}')
print(f'[{temp:6}]°C')
print(f'[{(temp * 1.8) + 32:6}]°F')
print(f'[{temp + 273.15:.2f}]°K')
print(20 * '=')