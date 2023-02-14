numero = ['zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte']
n1 = int(input('Digite um número de 0 a 20: '))

while n1 > 20:
    print('Digite um número valído')
    n1 = int(input('Digite um número de 0 a 20: '))

print(f'[{n1}] = [{numero[n1]}]')