print('=====Desafio 049=====')

cont = 0
while True:
    num = int(input('Quer Ver a Tabuada de Qual Valor? '))
    if num < 0:
        break
    print('=' * 25)
    for c in range (1, 11):
        print(f'{num}  X {c} = {num*c}')
    print('=' * 25)
print('Programa de Tabuada Encerrado!')
print('Volte Sempre!')


