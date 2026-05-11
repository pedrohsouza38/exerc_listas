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
#Usa 'for' novamente para percorrer a lista e mostrar nome por nome
for indice, convidado in enumerate(convidados, start=1):
    print(f"{indice}. {convidado}")

#5. Informar a Quantidade
#Utiliza a função 'len()' para contar quantos elementos existem na lista.
total_convidados = len(convidados)
print("-" * 25)
print(f"Total de convidados: {total_convidados}")
print("---------------------------")

Justificativa das Estruturas Utilizadas

1. Estrutura de Repetição (for + range)
   
Por que usar: O laço for foi escolhido porque o requisito define um número fixo de repetições (5 convidados). O range(1, 6) garante que o loop execute exatamente 5 vezes, facilitando a contagem automática na mensagem de input 1.4.11.

Alternativa: Um while funcionaria, mas exigiria um contador manual (ex: c = 0; while c < 5:), sendo menos eficiente para números de iterações conhecidos 1.4.10.

2. Estrutura de Decisão (if)
   
Por que usar: O if é essencial para validação de dados. Ele impede que nomes vazios (apenas apertar Enter) sejam contabilizados como convidados, garantindo a integridade da lista 1.1.4.

Uso: if nome != "": verifica se a entrada não é nula antes de usar o método append para adicionar à lista.

3. Estrutura de Dados (list + len())

Lista []: Utilizada para armazenar múltiplos strings em uma única variável de forma ordenada.

len(convidados): Função built-in do Python usada para retornar o número de elementos atualmente na lista. É mais eficiente e direto do que criar um contador separado 1.2.4.



Exercício 2 — Controle de preços
     Solicite 5 preços e:
     armazene em uma lista;
     exiba o maior preço;
     exiba o menor preço.
     
#Programa: Analisador de Preços

#1. Inicialização da lista vazia
precos = []

#2. ESTRUTURA DE REPETIÇÃO (for)
#Justificativa: Usa o 'for' com 'range(5)' porque sabe exatamente quantas vezes o código deve rodar (5 vezes). É mais eficiente que um 'while'.
print("Digite 5 preços:")
for i in range(5):
#Solicita o preço e converte para float (número real)
preco = float(input(f"Digite o {i+1}º preço: R$ "))
#Adiciona o preço na lista
precos.append(preco)

#3. EXIBIÇÃO DOS RESULTADOS
#Justificativa: Utiliza as funções embutidas max() e min() para encontrar o maior e menor valor de forma direta e eficiente.
print("-" * 30)
print(f"Lista de preços: {precos}")
print(f"O maior preço é: R$ {max(precos):.2f}")
print(f"O menor preço é: R$ {min(precos):.2f}")
print("-" * 30)

Explicação Detalhada e Justificativas

1. Estrutura de Repetição (for + range)

O que faz: for i in range(5): executa o bloco de código abaixo dele 5 vezes.

Por que usar: Quando sabe o número exato de repetições (neste caso, 5 preços), o laço for é a estrutura mais limpa e legível. Ele evita a necessidade de criar um contador manual e uma condição de parada complexa, como seria em um while.

lista.append(): Essencial para adicionar cada preço inserido pelo usuário ao final da lista precos a cada repetição.

2. Estrutura de Decisão / Funções de Comparação (max e min)

O que fazem: max(precos) e min(precos) percorrem a lista inteira automaticamente para encontrar o maior e o menor valor, respectivamente.

Por que usar: Embora usa um if dentro do loop para verificar o maior/menor valor a cada entrada, as funções nativas max() e min() são mais rápidas, geram um código mais limpo (Pythonico) e reduzem as chances de erro de lógica.

3. Formatação (:.2f)

Usado para garantir que o preço seja exibido com duas casas decimais (ex: 10.50), simulando o formato de moeda brasileiro.



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
