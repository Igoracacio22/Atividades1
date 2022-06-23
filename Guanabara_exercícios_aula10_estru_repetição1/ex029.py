velocidade = float(input('Qual a velocidade do seu carro?'))
multa = 7*(velocidade-80)
if velocidade > 80:
    print('você foi multado e ultrapassou os 80Km/h')
    print('A sua multa vai ser de R$: {:.2f}'.format(multa))

print('Tenha um bom dia dirija com segurança')
