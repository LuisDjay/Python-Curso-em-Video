print('=====Desafio 068=====')
from random import randint

cont = 0
while True:
    jog = int(input('Diga Um valor: '))
    resp = str(input('Par ou Ímpar? [P/I] ').upper())
    comp = randint(0, 10)
    result = jog + comp
    result2 = result % 2
    if result2 == 0 and resp == 'P':
        print(f'Voce Jogou {jog} e o computador jogou {comp}. O total é {result} Deu PAR')
        print(f'Você Venceu!')
        print(f'Vamos jogar novamente')
    elif result2 == 0 and resp == 'I':
        print(f'Voce Jogou {jog} e o computador jogou {comp}. O total é {result} Deu PAR')
        print(f'Você Perdeu!')
        break
    elif result2 != 0 and resp == 'I':
        print(f'Voce Jogou {jog} e o computador jogou {comp}. O total é {result} Deu IMPAR')
        print(f'Você Venceu!')
        print(f'Vamos jogar novamente')
        cont += 1
    elif result2 != 0 and resp == 'P':
        print(f'Voce Jogou {jog} e o computador jogou {comp}. O total é {result} Deu IMPAR')
        print(f'Você Perdeu!')
        break
    cont += 1
print(f'Você venceu {cont} vezes.')
