nome = str(input('Digite uma frase:')).upper().strip()
repet = nome.count('A')
pos = (nome.find('A')+1)
ult_l = (nome.rfind('A')+1)
print('Analisando a frase...')
print(f'A letra [A] aparece {repet} vezes na frase')
print(f'A letra [A] aparece na posição [{pos}] pela primeira vez')
print(f'A última letra [A] apareceu na posição {ult_l}')
