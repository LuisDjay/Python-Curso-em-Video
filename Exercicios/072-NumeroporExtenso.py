cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco' , 'Seis' , 'Sete', 'Oito',
            'Nove', 'Dez', 'Onze' , 'Doze' , 'Treze',  'Quatorze',
'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
#resp = ' '
while True:
    while True:
        numero=int(input('Digite um número entre 0 e 20: '))
        if 0 <= numero <= 20:
            break
    print ('Tente novamente.', end=' ')
    print(f'Você digitou o numero {cont[numero]}')
    resp= str(input('Você quer continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break

