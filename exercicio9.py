#VALIDAÇÃO DE ENTRADA GRATUITA
idade = float(input('Qual a sua idade ?\n'))
entradaGratuita = idade
if idade <= 5 or idade >= 60:
 print('Tem direito a entrada gratuita ')
else:
 print('Não tem direito a entrada gratuita')