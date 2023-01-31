a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite outro número: '))
print(f'{"Maior ou Menor":=^25}')


#vendo o menor numero
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#vendo maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'Maior número:[{maior}]')
print(f'Menor número:[{menor}]')
print('=' * 25)

