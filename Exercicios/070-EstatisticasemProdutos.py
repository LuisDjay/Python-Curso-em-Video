print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATAO'.rstrip()))
print('-'*30)
total= caro = menor = cont =0
barato = ' '
while True:
    prod=str(input('Nome do Produto: '))
    preco=float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        caro += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar: [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print ('FIM DO PROGRAMA')
print(f'O total da compra foi R${total:.2f} ')
print(f'{caro} produtos acima de R$1000 Reais')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')