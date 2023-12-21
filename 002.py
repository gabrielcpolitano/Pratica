#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))
c = ((a**2) + (b**2)) ** (1/2)
print(f'A Hipotenusa desse triângulo retângulo é {c:.2f}')