nome = str(input('Digite o seu nome completo:')).strip()
nome = nome.split()
nome_f = nome[len(nome)-1]
print(f'Seu primeiro nome é = {nome[0]}')
print(f'último = {nome_f}')