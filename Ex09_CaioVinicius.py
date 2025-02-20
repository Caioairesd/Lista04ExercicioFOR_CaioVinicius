
"""09 - Faça um programa que pergunte ao usuário onde deseja apontar, C/c para cima, A/a para baixo. 
a) se ele apontar para cima peça um número superior e conte de 1 até esse número.
b) se ele selecionar para baixo pesa-lhe para inserir um número abaixo de 20 e em seguida faça a contagem regressiva de 20 até esse número
c) se ele inserir uma direção diferente, imprima ("Direção inválida!")"""

direcao = input("Em que posição você deseja apontar?\n C/c para cima, A/a para baixo: ").lower()

if direcao == 'c':
    numeroSuperior = int(input("Insira um número:"))
    for i in range(numeroSuperior):
        print(i+1)
elif direcao == 'a':
    numeroAbaixode20= int(input("Insira um número abaixo de 20:"))
    if numeroAbaixode20 < 20:
        for i in range(20,numeroAbaixode20 -1,-1):
            print(i)
    else:
        print("Seu número não é abaixo de 20.")
else:
    print("Direção inválida!")


    print("----------------------------------------------------")
    print("Programa finalizado!")
    print("Caio Vinicius Aires da Silva")

