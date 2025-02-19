"""10 - Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa.
Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas"."""

convidados= int(input("Olá, quantos convidados você deseja convidar para sua festa?"))

if convidados < 10:

    for i in range(convidados):
        nome = input("Qual o nome do {}° convidado:".format(i+1)).title()
        print("{} está convidado(a) para a festa".format(nome))
else:
    print("Muitas pessoas!")


print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")