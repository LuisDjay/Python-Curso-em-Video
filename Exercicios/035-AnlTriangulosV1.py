print('=====Desafio 035=====')


num=int(input('Me diga um número qualquer: '))
resultado=num % 2

if resultado == 0:
    print('O número {} é um numero PAR'.format(num))
else:
    print('O número {} é um número IMPAR'.format(num))
