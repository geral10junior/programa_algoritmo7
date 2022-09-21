#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato

p1 = float(input('Informe o valor do primeiro produto: R$ '))
p2 = float(input('Informe o valor do segundo produto: R$ '))
p3 = float(input('Informe o valor do terceiro produto: R$ '))

print('O valor mais barato é:')

if p1 > p2 > p3:
    print(p3)
elif p1 > p3 > p2:
    print(p2)
elif p2 > p1 > p3:
    print(p3)
elif p2 > p3 > p1:
    print(p1)
elif p3 > p1 > p2:
    print(p2)
elif p3 > p2 > p1:
    print(p1)
