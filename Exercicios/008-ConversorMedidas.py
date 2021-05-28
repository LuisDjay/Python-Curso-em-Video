print('=====Desafio 008=====')

m=float(input('Uma distância em metros: '))
km= m*0.001
hm= m*0.01
dam= m*0.1
dm=m*10
cm= m*100
mm= m*1000

print( 'A medida de {} metros corresponde a \n {:.3f} kilômetros \n {:.2f} '
       'hectrometros \n {:.1f} decametros \n {:.0f} decimetros \n {:.0f} '
       'centimetros \n {:.0f} milimetros'.format(m, km, hm, dam, dm, cm, mm, ))

