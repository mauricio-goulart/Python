nome = str(input('Digite o seu nome: ')).strip()

nm = nome.split()

print(f'{"Analisando":=^20}')
print(f'Maiúsculo:[{nome.upper()}]')
print(f'Minúsculo:[{nome.lower()}]')
print(f'Total Letras:[{len(nome) - nome.count(" ")}]')
print(f'Total Primeiro nome:[{len(nm[0])}]')
print('=' * 20)
