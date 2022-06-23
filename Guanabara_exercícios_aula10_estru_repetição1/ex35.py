print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)

r1 = int(input('Primeiro segmento:'))
r2 = int(input('Segundo segmento:'))
r3 = int(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triângulo')
else:
    print('Os seguimentos acima não podem formar um triângulo')
