
sexo=str(input('Informe seu sexo: [M/F]')).upper()[0].strip()
print(sexo)
while sexo not in 'MF':
    sexo=str(input('Dados inválidos. Por favor, informe seu sexo: '))
print('Sexo {} validado'.format(sexo))

