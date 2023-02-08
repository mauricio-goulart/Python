import random
import time

print('\33[35m-=-' * 20)
print('\33[34mVou pensar em um número de 0 a 10. Tente adivinhar...')
print('\33[35m-=-' * 20)

pc = int(random.randint(0, 10))
h = int(input('\33[34mEm que número eu pensei? : '))
tot = int(0)
print('\33[33mPROCESSANDO...')
time.sleep(0.5)
while pc != h:
    tot = tot + 1
    if pc > h:

        print('\033[31mMais... Tente mais uma vez')
        h = int(input('\033[34mEm que número eu pensei? : '))
        print('\33[33mPROCESSANDO...')
        time.sleep(0.5)
    else:


        print('\033[31mMenos... Tente mais uma vez')
        h = int(input('\033[34mEm que número eu pensei : '))
        print('\33[33mPROCESSANDO...')
        time.sleep(0.5)


print('\033[35m-=' * 30)
print(f'\033[34mPc:[{pc}]|Vc:[{h}]')
print(f'Parabéns você ganhou, com [{tot + 1}] vezes')
print('\033[35m-=' * 30)

fechar = input('Digite enter para fechar')
