nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1+nota2)/2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a media do aluno é {media:.1f}')
if media < 5.0:
    print('O aluno está reprovado')
elif 5.0 <= media < 7:
    print('O aluno está em recuperação')
else:
    print('Aluno Aprovado')