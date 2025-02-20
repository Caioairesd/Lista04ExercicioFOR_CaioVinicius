"""Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe.
Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas.
O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não.
No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes.
Desenvolva um programa em Python que:
1.	Solicite ao usuário o número de tarefas a serem inseridas.
2.	Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
3.	Conte e exiba o número de tarefas concluídas e não concluídas."""
    
   
contadorConcluida = 0
contadorNaoConcluida = 0
qtdeTarefas = int(input("Quantas tarefas você tem?"))
tarefas = []
estado = []

for i in range(qtdeTarefas):
    nomeTarefa = input("Qual o nome da {}° tarefa?".format(i + 1))
    tarefas.append(nomeTarefa)

    estadoDeAndamento = input("Qual o estado de andamento dessa tarefa?\n(sim/s para tarefas concluídas ou não/n para tarefas não conluídas):").lower()
    
   

    if estadoDeAndamento == 's' or estadoDeAndamento == 'sim':
        andamento = 'Concluída'
        estado.append(andamento)
        contadorConcluida += 1

    elif estadoDeAndamento == 'não' or estadoDeAndamento == 'n':
        andamento = 'Não concluída'
        estado.append(andamento)
        contadorNaoConcluida += 1

    else:
        print("Estado de andamento inválido!")

print(tarefas)
print(estado)
print("Você tem o total de {} tarefas concluídas e {} tarefas não concluídas".format(contadorConcluida,contadorNaoConcluida))

print("----------------------------------------------------")
print("Programa finalizado!")
print("Caio Vinicius Aires da Silva")
       
   