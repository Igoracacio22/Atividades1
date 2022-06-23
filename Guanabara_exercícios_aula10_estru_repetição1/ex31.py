dist = float(input('Quantos Km tem a viagem que deseja realizar?'))
dist_perto = 0.50*dist
dist_longe = 0.45*dist
if dist <= 200:
    print('A viagem de {} Km vai custar {} reais'.format(dist, dist_perto))

else:
    print('A viagem de {} Km vai custar {} reais'.format(dist, dist_longe))

# If ternário ou If in line
preço = (0.5*dist if dist <= 200 else 0.45*dist)
print(preço)
