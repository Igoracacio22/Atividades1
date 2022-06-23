# len, mostra a quantidade de caracteres que aparece na frase sem contar com o 0 começando de 1 até o final.
frase = 'Curso em Video Python'
print(len(frase)) 
# mostra quantas vezes conta a letra ou o caractere que eu quero aparece.
#se for adicionado outros parâmetros irá mostrar de onde, até aonde que irá procurar os caracteres na frase.
#frase.count('o', 0, 13), primeiro = o que eu quero achar, segundo = De onde eu quuero começar, terceiro = Aonde eu quero terminar, sendo exclisivo o ultimo item.
print(frase.count('o'))
# Vai indicar o momento que começou essa sequencia de caracteres, foi encontrado o 'deo' a partir da posição 11.
print(frase.find('deo'))
# Se for colocado uma string que não existe dentro da frase toda, vai retornar -1:
print(frase.find('Android'))
# Operador 'in' serve para mostrar se existe o item dentro da frase.
print('Curso' in frase)
# Replace substitui o primeiro item pelo segundo.
print(frase.replace('Python', 'Android'))
# transforma todos os itens que estavam em minúsculos, em maiúsculo
print(frase.upper())
# torna todos os itens maiúsculos em minúsculos.
print(frase.lower())
# Coloca todas as letras em minúsculos e a primeira letra fica maiúsculas
print(frase.capitalize())
# Coloca todos os caracteres entre espaços em maiúsculos
print(frase.title())
frase = '   Aprenda Python  '
# Elimina os epaços do inicio e final da frase, 0u da string.
print(frase.strip())
# rstrip remove os espaços a direita da frase, e lfrase remove os epaços a esquerda da frase.
print(frase.rstrip())
# FUNCIONALIDADES EM STRINGS NO PYTHON
# Em espaços separados ele cria listas para esses tipos de strings/ tradução de split = dividir;
# Refaz todos os índices da frase ou da string e em cada palavra criada na lista recebe um index novo.
frase = 'Curso em Video Python'
print(frase.split())
# Une a frase toda pelo separador determinado
print('-'.join(frase))

print(frase[13:])
print(frase[::2])
dividido = frase.split()
print(dividido[2])










