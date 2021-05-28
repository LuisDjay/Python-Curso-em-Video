
tupla = (int(input('Digite um valor: ')),int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),int(input('Digite o ultimo valor: ')))
print(f'Você digitou os valores {tupla}')
print(f'O numero 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O numero 3 aparece na {tupla.index(3)+1}ª posição')
else:
    print('o Valor 3  não foi digitado. ')
print(f'Os numeros pares digitados foram',end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')


#print(f'O valor 9 apareceu {} vezes')
