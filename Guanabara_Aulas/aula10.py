tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3:
    print('Seu carro é novo!!')
else:
    print('Seu carro é velho')
print('--FIM--')




tempo = int(input('Quantos anos tem seu carro:'))
print('carro novo' if tempo<=3 else'carro velho')
print('--FIM--')


nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Nome esquisito')
else:
    print('Que nome lindo você tem!!')
print(f'Bom dia, {nome}')

print('Nome Esquisito' if nome == 'Pablo' else 'Nome Lindo')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média final foi {:.1f}'.format(m))

if m >= 6.0:
    print('A sua média está boa')
else:
    print('A sua média está ruim')

print('A sua média está boa' if m >= 6 else 'A sua média está ruim')

