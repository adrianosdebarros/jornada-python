
# nome = "Adriano"

# try:
#     resultado = len(3)
#     print(resultado)
# except TypeError as e:
#     print(e)

numero = int(input('Insira um numero: '))

if isinstance(numero, int):
    print('A variavel é string.')
else:
    print('A varialves não é string.')