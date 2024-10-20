altura = float(input('Informe a sua altura '))
peso = float(input('Informe o seu peso '))
calculo = peso/(altura**2)
print(f'O seu IMC é {calculo:.2f}')

if calculo < 18.5:
 print('Você está abaixo do peso ')
elif calculo >= 18.5 and calculo < 25:
 print('Você está com o peso normal')
elif calculo >= 25:
 print('Você está acima do peso')