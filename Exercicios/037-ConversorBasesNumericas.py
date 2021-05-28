print('=====Desafio 037=====')

n1= int(input("Digite um numero inteiro: "))
print('Escolha uma das bases para conversão: ')
print('[1]converter para BINÁRIO ')
print('[2]converter para OCTAL ')
print('[3]converter para HEXADECIMAL ')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para Binário é igual a {}'.format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('{} convertido para Octal é igual a {}'.format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção Invalida. Tente Novamente. ')

