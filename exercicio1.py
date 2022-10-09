sexo = int(input('Escolha: 1- Sexo Masculino ou 2- Sexo Feminino: '))
altura = float(input('Altura:'))
peso = float(input('Peso:'))

if sexo == 1:
	pesoIdeal = (72.7*altura) - 58
else:
	pesoIdeal = (62.1*altura) - 44.7

if peso == pesoIdeal:
	print('Dentro do peso ideal')

print ('Peso: %.2f atual / Seu peeso ideal é: %.2f' %(peso, pesoIdeal))