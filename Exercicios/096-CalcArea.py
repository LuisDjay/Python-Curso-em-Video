


def area(larg , comp):
    a = larg * comp
    print(f'A Area de um terreno {larg}x{comp} é de {a}m2.')

#Programa principal
print('Controle de Terrenos')
print('+*'*30)
l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m):'))
l2 = float(input('LARGURA (m):'))
c2 = float(input('COMPRIMENTO (m):'))

area(l, c)
area(l2,c2)
area(c2,l)

