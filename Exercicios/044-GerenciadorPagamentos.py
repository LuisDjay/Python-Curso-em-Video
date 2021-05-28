print('='*10,'D e s a f i o 43','='*9)

print('='*10,'LOJAS GUANABARA','='*10)

preco=float(input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTO 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao=int(input('Qual a opção? '))

if opcao == 1:
    total = preco - (preco * 0.10)
    print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco,total))
elif opcao == 2:
    total = preco - (preco * 5/100)
    print('Preço com desconto {}'.format(preco))
elif opcao == 3:
    total = preco
    print('Preço sem desconto {}'.format(preco))
elif opcao == 4:
    total = preco + (preco * 0.20)
    print('Preço com juros {}'.format(preco))
else:
    total = preco
    print('Opção invalida')
print('Sua compra de {:.2f} vai custar R${:.2f} no final'.format(preco,total))

