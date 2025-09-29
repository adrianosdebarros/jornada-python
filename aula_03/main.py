# print('--- Entendendo o que é debugar ---\n')

# print('Primeiro comando')
# print('Segundo comando')
# print('Terceiro comando')
# x = 3
# print(x)

# print('--- Controle de fluxo ---\n')

# numero = int(input("Insira um número e lhe direi se ele é positivo ou negativo: "))

# if numero < 0:
#     print(f'O número que você digitou foi {numero} e ele é negativo.')
# elif numero == 0: 
#     print(f'O número que você digitou foi {numero} e ele é nulo.')
# else:
#     print(f'O número que você digitou foi {numero} e ele é positivo.')

# 1°)

# temperatura = float(input('Temperatura atual: '))

# if temperatura < 18:
#     print(f'A temperatura atual de {temperatura} graus é considerada baixa.')
# elif temperatura >= 18 and temperatura <= 26:
#     print(f'A temperatura atual de {temperatura} graus está no nível normal.')
# else:
#     print(f'A temperatura atual de {temperatura} graus é considerada alta.')


# lista_de_alunos = ["adriano", "taires", "alice"]

# for aluno in lista_de_alunos:
#     print(aluno)

import time

condicao = True

while condicao:
    print("Execute minha ETL")
    time.sleep(5)