idade1 = 18
idade = float(input('Informe a idade '))
idade2 =  idade1-idade % 18
if idade >= 18:
 print('Pode dirigir ')
elif idade < 18:
 print(f'Falta {idade2} anos para dirigir')

