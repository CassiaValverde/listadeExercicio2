#desconto de compra
valor = float(input('Qual o valor a ser descontados ? \n'))
porcentagem = 100*0.10

if valor >= 100:
 print(valor-porcentagem)
else:
 print(valor)