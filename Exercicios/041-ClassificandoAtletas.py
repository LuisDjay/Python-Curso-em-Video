print('=====Desafio 041=====')
from datetime import date
atual = date.today().year
ano=int(input("Ano de Nascimento: "))
idade= atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria: Mirim')
elif idade <=14:
    print('Categoria: Infantil')
elif idade <=19:
    print('Categoria: Júnior')
elif idade <=25:
    print('Categoria: Sênior')
elif idade >25:
    print('Categoria: Master')


