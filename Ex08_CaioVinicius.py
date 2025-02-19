"""08 - Defina uma variável chamada total valendo 0.
peça ao usuário para inserir 5 números, e após cada entrada pergunte se ele deseja que esse número seja incluído ('S' ou 's' ou 'N' ou 'n').
Se ele desejar adicione o número ao total. Se ele não quiser incluí-lo, não adicione ao total, depois de inserir os 5 números de o valor total."""

total = 0 
for i in range(5):
   
    num = int(input("Insira um número:"))
    resposta = input("Deseja adcionar esse número ao total?\n['S' ou 's' para sim ou 'N' ou 'n' para não.]").lower()
    
    if resposta == 's':
        total += num
    
    elif resposta == 'n':
        print("Valor não adicionado!")
    
    else:
        print("Resposta  inválida!")
            
        
print("O total é de: {}".format(total))
    