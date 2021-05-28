
from random import randint
sorteio = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram: ')
for c in sorteio:
    print(f'{c} ', end= ' ')
print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')