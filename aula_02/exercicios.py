import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# n_01 = int(input("Insira o primero numero: "))
# n_02 = int(input("insira o segundo numero: "))
# print(f"Resultado: {n_01 + n_02}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# n = int(input("Insira o número: "))
# d = n % 5
# print(d)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# n1 = int(input("Primeiro valor: "))
# n2 = int(input("Segundo valor: "))
# mult = n1 * n2
# print(mult)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numerador = int(input("Numerador: "))
# denominador =int(input("Denominador: "))
# print(numerador / denominador)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# n1 = int(input('Numero:' ))
# quadrado = n1**2
# print(quadrado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# n_01 = float(input("Insira o primero numero: "))
# n_02 = float(input("insira o segundo numero: "))
# print(f"Resultado: {n_01 + n_02}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# n1 = float(input())
# n2 = float(input())
# media = (n1 + n2) / 2
# print(media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input())
# expo = float(input())
# res = base ** expo
# print(res)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.



# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# r = int(input('Digite o raio: '))
# area = math.pi * r ** 2
# print(f'{area:.1f}')

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# nome = str(input("Digite seu nome: "))
# print(nome.upper())

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = str(input("Digite seu nome completo: "))
# print(nome.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = str(input("Insira uma frase: "))
# frase_sem_espaco = frase.strip()
# print("Frase sem espaços no início e no final:", frase_sem_espaco)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f'O 1 elemento é o: {lista_de_dia_mes_ano[0]}')
# print(f'O 2 elemento é o: {lista_de_dia_mes_ano[1]}')
# print(f'O 3 elemento é o: {lista_de_dia_mes_ano[2]}')

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# n1 = input("Valor 1: ")
# n2 = input("Valor 2: ")
# retorno = n1 + n2
# print(retorno)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# n1 = True
# n2 = True
# resultado = n1 and n2
# print(resultado)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# n1 = False
# n2 = False
# resultado = n1 or n2
# print(resultado)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# n1 = False
# n2 = True
# resultado = not n2
# print(resultado)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# n1 = int(input("Valor 1: "))
# n2 = int(input("Valor 2: "))
# resultado = n1 == n2
# print(resultado)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# n1 = int(input("Valor 1: "))
# n2 = int(input("Valor 2: "))
# resultado = n1 != n2
# print(resultado)

# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     c = float(input("Digite um valor em C° para convertermos para F°: "))
#     f = (c * 9/5) + 32
#     print(f"{c}C° é igual a {f}F°")
# except ValueError:
#     print("Por favor digite um número válido.")

# 22: Verificador de Palíndromo
# entrada = input("Digite uma palavra ou frase: ")

# if isinstance(entrada, str): 
#     formatado = entrada.replace("", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um polídromo.")
#     else:
#         print("Não é um polídromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")
# 23: Calculadora Simples

# 24: Classificador de Números

# 25: Conversão de Tipo com Validação
