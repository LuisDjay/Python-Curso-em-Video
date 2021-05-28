from random import randint

while True:
    jogador = int(input('Diga Um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''

    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
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
