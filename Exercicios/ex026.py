frase = str(input('Digite uma frase: ')).lower()

print(f'{"Analisando":=^20}')
print(f'Quantas letras [A]: [{frase.count("a")}]')
print(f'Primeira posição: [{frase.find("a")}]')
print(f'Ultima posição: [{frase.rfind("a")}]')
print('=' * 20)