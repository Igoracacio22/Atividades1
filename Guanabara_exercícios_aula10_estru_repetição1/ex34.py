salario = float(input('Digite o Salário do funcionário:'))

if salario > 1250:
    aumento = salario*1.1
else:
    aumento = salario*1.15

print(f'O salário do funcionário com aumento é de {aumento:.2f}')