import Moeda

p= float(input('Digite o preco: R$ '))
print(f'A metade de {p} é R${Moeda.metade(p)}')
print(f'O dobro de {p} é R${Moeda.dobro(p)}')
print(f'Aumentando 10%, temos {Moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {Moeda.diminuir(p, 13)}')