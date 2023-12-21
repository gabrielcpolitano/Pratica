#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import ceil
a = float(input('Digite um número quebrado: '))
b = ceil(a)
print(f'Esse é o número quebrado: {a}. Esse é o número inteiro {b}')
