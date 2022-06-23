from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
# ano_atual = date.today().year
ano_atual = 2017
idade = ano_atual - nascimento
print(f'O atleta tem {idade} anos')
if idade <=9:
    print('O atleta irá para caregoria MIRIM')
elif 14 >= idade > 9:
    print('O atleta irá para caregoria INFANTIL')
elif 19 >= idade > 14:
    print('O atleta ira para caregoria JUNIOR')
elif 25 >= idade > 19:
    print('O atleta é SENIOR')
else:
    print('O atleta se encontra na caregoria de MASTER')