# exerc_listas
Exercícios de Lógica com Listas

Exercício 1 — Lista de convidados
Crie um programa que:
     Cadastre 5 convidados;
     Exiba todos os convidados;
     Informe quantos convidados existem.

#Programa de Cadastro de Convidados

#1. Inicialização da Lista
#Utiliza uma lista vazia [] para armazenar os nomes.
#Listas são ideais para coleções ordenadas que podem mudar de tamanho.
convidados = []

print("--- Sistema de Cadastro de Convidados (5 vagas) ---")

#2. Estrutura de Repetição (for + range)
#O laço 'for' com 'range(5)' é ideal porque sabe exatamente quantas vezes quer repetir o cadastro (5 vezes).
for i in range(1, 6):
#Solicita o nome e remove espaços em branco extras
nome = input(f"Digite o nome do convidado {i}: ").strip()

#3. Estrutura de Decisão (if)
#Verifica se o usuário digitou algo antes de adicionar
    if nome != "":
        convidados.append(nome) # Adiciona o nome à lista
    else:
        print("Nome inválido. Convidado ignorado.")

#4. Exibição dos Dados
print("\n--- Lista de Convidados ---")
#Usamos 'for' novamente para percorrer a lista e mostrar nome por nome
for indice, convidado in enumerate(convidados, start=1):
    print(f"{indice}. {convidado}")

#5. Informar a Quantidade
#Utiliza a função 'len()' para contar quantos elementos existem na lista.
total_convidados = len(convidados)
print("-" * 25)
print(f"Total de convidados: {total_convidados}")
print("---------------------------")

Exercício 2 — Controle de preços
     Solicite 5 preços e:
     armazene em uma lista;
     exiba o maior preço;
     exiba o menor preço.

Exercício 3 — Lista de tarefas
     Crie um programa que:
     permita cadastrar tarefas;
     finalize quando o usuário digitar “fim”;
     exiba todas as tarefas.

Exercício 4 - Controle de temperaturas
     Solicite temperaturas em graus Celsius até o usuário digitar "sair";
     Converta as temperaturas da lista em graus Celsius para uma nova lista de temperaturas em graus Fahrenheit;
     Calcule e exiba as médias de ambas as temperaturas.

Exercício 5: Lista de compras
     Exibir um menu de opções para esta lista de compras: 

             1 - Adicionar a lista 
             2 - Pesquisar item 
             3 - Remover item
             4 - Alterar item
             5 - Listar produtos
             6 - Sair

     para a opção 1 solicitar ao usuário digitar produtos para compra até digitar a palavra "sair"
     para a opção 2 solicitar um produto a ser pesquisado na lista. se encontrar o produto, exibir o mesmo senão exibir produto não encontrado;
     para  a opção 3 solicitar o nome do produto a ser removido da lista. se encontrar, exibir na tela "produto encontrado" senão exibir "produto não encontrado";
     para a opção 4 solicitar o nome do produto a ser alterado. se encontrar exibir na tela "produto alterado com sucesso" senão exibir "produto não encontrado"
     para a opção 5 listar todos os produtos cadastrados. se não houver produtos cadastrados, exibir a mensagem "Lista vazia" senão exibir os produtos cadastrados.
     para a opção 6 sair do programa e exibir na tela "Programa encerrado com sucesso!".

Todos os produtos deverão ser cadastrados, pesquisados, removidos e alterados em letras minúsculas.
