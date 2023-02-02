print('Pares multiplos de 3')
s = int(0)
c = int(0)
print('-=' * 15)

for contador in range(0,501):
    if contador % 3 == 0 and contador % 2 != 0:
        s = s + contador
        c = c + 1

print(f'Todos os números multiplos de 3 são [{c}]\nE somados são [{s}]')
print('-=' * 15)
