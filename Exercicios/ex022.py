nome = str(input('Digite o seu nome: '))
n = nome.strip()
nm = n.split()

print(f'{"Analisando":=^20}')
print(f'Maiúsculo:[{nome.upper()}]')
print(f'Minúsculo:[{nome.lower()}]')
print(f'Total Letras:[{len(n) - n.count(" ")}]')
print(f'Total Primeiro nome:[{len(nm[0])}]')
print('=' * 20)
