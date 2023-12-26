#O mesmo professor do desafio 4 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

a = input('Digite o nome do Aluno: ')
b = input('Digite o nome do Aluno: ')
c = input('Digite o nome do Aluno: ')
d = input('Digite o nome do Aluno: ')

alunos = a, b, c, d

ordem = random.sample(alunos, 4)
#ordem = random.sample(alunos, len(alunos))

print(f'Ordem de apresentação: {ordem}')
