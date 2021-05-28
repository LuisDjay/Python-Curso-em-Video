from random import randint
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi???''')
tot=1
n1=int(input('Qual será o seu palpite? '))
resp = randint(0, 10)

while n1 != resp:
    tot += 1
    if n1 > resp:
        n1=int(input('Menos... Tente novamente: '))
    if n1 < resp:
        n1=int(input('Mais... mais uma vez: '))
print('Voce me venceu em {} tentativas! escolhi o numero {}'.format(tot, resp))
