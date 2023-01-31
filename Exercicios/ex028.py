import random
import time

print('\33[35m-=-' * 20)
print('\33[34mVou pensar em um número de 0 a 5. Tente adivinhar...')
print('\33[35m-=-' * 20)

pc = int(random.randint(0, 5))
h = int(input('\33[34mEm que número eu pensei? :'))
print('\33[33mPROCESSANDO...')
time.sleep(2)

if h == pc :
    print(f'\33[32mParabens!!! Você ganhou eu pensei no {pc}')
else:
    print(f'\33[31mPerdeu!!! Você errou eu pensei no {pc}')
print('\33[35m=' * 40)

input('\33[mdigite enter para encerrar')
