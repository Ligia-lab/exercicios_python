#quantos dolares da pra comprar com o dinheiro que voce tem? (dol 3,27)

c = float(input('Quanto dinheiro você tem na carteira? R$ '))
d = c / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}.'.format(c, d))
