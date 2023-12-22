#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
a = input('Nome do Aluno: ')
b = input('Nome do Aluno: ')
c = input('Nome do Aluno: ')
d = input('Nome do Aluno: ')

nome = [f'{a}', f'{b}', f'{c}', f'{d}']

nome_selecionado = random.choice(nome)
print(nome_selecionado)
