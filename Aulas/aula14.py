#n = 1
#r = 'S'
#while r == 'S':
   # n =  int(input('Digite um valor: '))
   # r = str(input('Quer continuar: [S/N]')).upper()
#print('fim')
impar = int(0)
par = int(0)
n = 1

while n !=0:
    n = int(input('Digite um número: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1

print(f'Voce digitou {par} números pares e {impar} números ímpares')