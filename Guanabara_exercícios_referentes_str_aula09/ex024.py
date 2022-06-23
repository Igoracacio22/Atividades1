# Modo 1
cidade = (input('Digite o nome da sua cidade:')).upper().split()
comeca = 'SANTO' in cidade[0]
print(comeca)
# Modo 2
cid = str(input('Digite o nome da sua cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
