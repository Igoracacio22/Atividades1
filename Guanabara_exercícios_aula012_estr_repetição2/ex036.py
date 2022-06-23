casa = float(input('Digite o valor da casa que você deseja comprar:'))
salario = float(input('Digite o seu salário:'))
anos = int(input('Digite em quantos anos pretende pagar a casa:'))

prestacao_mensal = casa/(anos*12)
aprovacao = salario*0.3

print(f'Para pagar uma casa de {casa:.2f}, em {anos} anos', end='')
print(f' a prestação será de {prestacao_mensal:.2f}')

if prestacao_mensal > aprovacao:
    print('O emprestimo foi negado')
else:
    print('O emprestimo foi aceito')  

