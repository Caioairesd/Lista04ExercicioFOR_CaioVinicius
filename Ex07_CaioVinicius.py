
"""07 - Peça ao usuário para inserir seu nome e um número. Se o número for menor que 10, exiba o nome dele esse número de vezes
caso contrário exiba a mensagem ("Número muito alto(3vzs)"""
try:
    nome = str(input("Insira seu nome:"))
    num = int(input("Insira um número:"))

    if num < 10:
        for i in range(num):
            print(nome)
    else:
        for i in range(3):
            print("Número muito alto!")
except:
    print("Insira valores valídos!")
    