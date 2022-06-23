nome = str(input('Digite seu nome completo:')).strip()

nome_maiu = nome.upper()
nome_minu = nome.lower()
nome_novo = nome.replace(' ', '')
nome_s_espaco = len(nome_novo)
nome = nome.split()
letras_primeiro_nome = len(nome[0])


print(f'O seu nome maúsculo é: {nome_maiu}')
print(f'O seu nome minúsculo é: {nome_minu}')
print(f'O seu  nome possui {nome_s_espaco} letras')
print(f'O seu nome {nome[0]} possui {letras_primeiro_nome} letras no primeiro nome')
