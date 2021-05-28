n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))
opcao=0

while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa ''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('O resultado de {} + {} é {}'.format(n1, n2, n1 + n2))
        print('=-=' * 20)
    elif opcao == 2:
        print('O resultado de {} x {} é {}'.format(n1,n2, n1*n2))
        print('=-='*20)
    elif opcao == 3:
        if n1 > n2:
            maior= n1
        else:
            maior = n2
            print('Entre {} e {} o maior valor é {}'.format(n1,n2, maior))
        print('=-=' * 20)
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 20)
    elif opcao == 5:
        print('Finalizando...')
    else:
        opcao=int(input('Opção inválida. Tente novamente '))
        print('=-=' * 20)
print('Fim do programa! Volte Sempre')