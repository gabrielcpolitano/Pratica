#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = float(input('Digite um angulo desejado: '))
radiano = math.radians(a)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'seno = {seno:.4f}')
print(f'cosseno = {cosseno:.4f}')
print(f'tangente = {tangente:.4f}')
