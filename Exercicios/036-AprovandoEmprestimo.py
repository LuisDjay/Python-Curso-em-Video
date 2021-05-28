print('=====Desafio 036=====')

valor = float(input('Qual o valor da casa: R$'))
salario = float(input('Qual o salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prest = valor / (anos * 12)
if prest >= salario * 30 /100:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de RS{:.2f}'.format(valor, anos, prest))
    print('EMPRESTIMO NEGADO')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de RS{:.2f}'.format(valor,anos,prest))
    print('EMPRESTIMO LIBERADO')


