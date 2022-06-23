from datetime import date
nascimento = int(input('Digite o seu ano de nascimento:'))
ano_atual = date.today().year
idade = (ano_atual) - (nascimento)
falta_p_alistar = 18-idade
passou_alista = idade-18

print(f'Quem nasceu em {nascimento} tem {idade} anos em {(ano_atual)}')
if idade < 18:
    print(f'Você tem {idade} e faltam {falta_p_alistar} anos para você se alistar.')
    print(f'Seu alistamento será em {ano_atual + falta_p_alistar}')
elif idade == 18:
    print(f'Está na hora de se alistar imediatamente')
if idade > 18:
    print(f'O tempo de alistamento passou {passou_alista} anos')
    print(f'O seu alistamento foi em {ano_atual - passou_alista}')

