#Implementação de um programa que lê uma linha contendo nomes de produtos separados por espaço.
#O script identifica qual produto aparece mais vezes na lista. 
#Se houver empate, retorne o que aparece primeiro na lista. 
#Utilizado apenas estruturas básicas como listas e tuplas para resolver o problema.

entrada = input('Digite os produtos: ')
produtos = entrada.split()

mais_aparece = ""
maior_contagem = 0

for produto in produtos: #aqui eu pego um produto 
    contagem = 0

    for item in produtos: #aqui serve pra olhar a lista toda, se for igual soma 1, guarda o total
        if produto == item:
            contagem += 1

    if contagem > maior_contagem:
        maior_contagem = contagem
        mais_aparece = produto

print(f'O produto que apareceu mais vezes (ou por empate) é: {mais_aparece}')