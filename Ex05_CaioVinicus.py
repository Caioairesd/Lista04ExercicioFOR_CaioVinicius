
"""05 - Peça ao usuário para inserir um número que deseja a tabuada, e em seguida exiba a tabuada para esse número."""

num = int(input("Insira o valor que deseja saber a tabuada:"))

for i in range(11):
    multiplicacao = num * i
    print("{} X {} = {}".format(num,i,multiplicacao))


print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")