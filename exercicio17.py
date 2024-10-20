ladoA = float(input('Informe o lado A '))
ladoB = float(input('Informe o lado B '))
ladoC = float(input('Informe o lado C '))
if ladoA == ladoB == ladoC :
 print('Esse é um triâgulo equilátero ')
elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
 print('Esse triângulo é isósceles')
else:
 print('Esse triângulo é escaleno')