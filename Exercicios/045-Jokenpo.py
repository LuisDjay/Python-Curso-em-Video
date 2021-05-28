print('=====Desafio 043=====')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')


print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)


computador = randint(0, 2)
print('-=' *11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' *11)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:#jogador jogou PEDRA
        print('EMPATE ')
    elif jogador ==1:#jogador jogou PAPEL
        print('Jogador Venceu')
    elif jogador ==2:#jogador jogou TESOURA
        print('Computador Venceu')
    else:
        print('JOGADA INVALIDA')
elif computador == 1:#computador jogou PAPEL
    if jogador == 0:#jogador jogou PEDRA
        print('Computador Venceu')
    elif jogador ==1:#jogador jogou PAPEL
        print('Empate')
    elif jogador ==2:#jogador jogou TESOURA
        print('Jogador Venceu')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:#computador jogou TESOURA
    if jogador == 0:#jogador jogou PEDRA
        print('Jogador Venceu ')
    elif jogador ==1:#jogador jogou PAPEL
        print('Computador Venceu')
    elif jogador ==2:#jogador jogou TESOURA
        print('Empate')
    else:
        print('JOGADA INVALIDA')
