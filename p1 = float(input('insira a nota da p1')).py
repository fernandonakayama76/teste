

p1 = float(input('insira a nota da p1: '))
p2 = float(input('insira a nota da p2: '))

def média(p1, p2):
    med = (p1 + p2)
    return med

funcao = média(p1, p2)
print(funcao)


if funcao>=5:
  print('passou')
else:
  print('não passou')

