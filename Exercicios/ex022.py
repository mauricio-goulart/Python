nome = str(input('Digite o seu nome: '))
n = nome.strip()

print(f'{"Analisando":=^20}')
print(f'Maiúsculo:[{nome.upper()}]')
print(f'Minúsculo:[{nome.lower()}]')
print(f'{len(n)}')
