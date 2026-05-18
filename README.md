# exerc_listas
Exercícios de Lógica com Python

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

#Inicializa uma lista vazia para armazenar as tarefas
tarefas = []

print("--- Gerenciador de Tarefas ---")
print("Digite 'fim' a qualquer momento para sair e ver suas tarefas.")

#Estrutura de repetição: Permite que o programa continue pedindo novas tarefas
while True:
    tarefa = input("\nDigite a sua tarefa: ")
    
    #Estrutura de decisão: Verifica se a palavra de parada foi digitada
    if tarefa.lower() == "fim":
        print("\n--- Saindo do programa ---")
        break  # Encerra o loop e para a repetição
    else:
        tarefas.append(tarefa) # Adiciona a tarefa informada à lista

#Exibe a lista completa de tarefas cadastradas
print("\n=== Suas Tarefas Cadastradas ===")
for t in tarefas:
    print(f"- {t}")

Explicação das Estruturas Utilizadas

Estrutura de Repetição while True:

Uso: Cria um laço infinito que continuará rodando continuamente, recebendo entradas do usuário de forma ininterrupta.

Justificativa: Como não sabe quantas tarefas o usuário vai adicionar, não pode fixar um limite (ex: 10 vezes). O laço fica ativo até que uma condição de parada obrigue a sua interrupção.

Estrutura de Decisão if / else:

Uso: Avalia a entrada do usuário. O if testa se a palavra digitada foi "fim" e o else captura as demais frases como sendo tarefas reais.

Justificativa: O programa precisa agir de maneiras diferentes dependendo da intenção do usuário: parar o sistema ou salvar uma tarefa na lista.

Comando break: Utilizado dentro do bloco if para "quebrar" o laço de repetição while e finalizar o programa.

Exercício 4 - Controle de temperaturas
     Solicite temperaturas em graus Celsius até o usuário digitar "sair";
     Converta as temperaturas da lista em graus Celsius para uma nova lista de temperaturas em graus Fahrenheit;
     Calcule e exiba as médias de ambas as temperaturas.

#Listas para armazenar as temperaturas
temp_celsius = []
temp_fahrenheit = []

#Estrutura de repetição: Permite a inserção contínua de valores até que o usuário digite "sair"
while True:
    entrada = input("Digite a temperatura em graus Celsius (ou 'sair' para encerrar): ").strip().lower()
    
    #Estrutura de decisão: Verifica se o comando de saída foi acionado
    if entrada == 'sair':
        print("Encerrando a entrada de dados...")
        break
    
    #Estrutura de decisão: Tenta converter o texto para número e ignora valores inválidos
    try:
        valor_celsius = float(entrada)
        temp_celsius.append(valor_celsius)
        
        #Converte para Fahrenheit usando a fórmula: F = C * (9/5) + 32
        valor_fahrenheit = valor_celsius * (9/5) + 32
        temp_fahrenheit.append(valor_fahrenheit)
        
        print(f"{valor_celsius}°C convertido para {valor_fahrenheit}°F.")
        
    except ValueError:
        print("Valor inválido. Digite apenas um número ou 'sair'.")

#Estrutura de decisão: Executa o cálculo e exibição apenas se a lista não estiver vazia
if len(temp_celsius) > 0:
    media_celsius = sum(temp_celsius) / len(temp_celsius)
    media_fahrenheit = sum(temp_fahrenheit) / len(temp_fahrenheit)
    
    print("\n--- Resultados Finais ---")
    print(f"Temperaturas em Celsius: {temp_celsius}")
    print(f"Média das temperaturas em Celsius: {media_celsius:.2f}°C")
    print(f"Temperaturas em Fahrenheit: {temp_fahrenheit}")
    print(f"Média das temperaturas em Fahrenheit: {media_fahrenheit:.2f}°F")
else:
    print("Nenhuma temperatura foi inserida no programa.")

Explicação e Justificativa das Estruturas Utilizadas

Para atender aos requisitos exigidos, o código faz uso combinado de estruturas de controle de fluxo e repetição:

1. Estrutura de Repetição (while True)

Uso: É utilizada no início do programa para manter o sistema rodando continuamente.
   
Justificativa: Como não sabe de antemão quantas temperaturas o usuário vai querer registrar, o loop while garante que o bloco de comandos seja repetido até que uma condição de parada específica aconteça. O True cria um laço infinito que só é interrompido intencionalmente.

2. Estrutura de Decisão (if / elif e break)

Uso: Presente dentro da repetição, testa a variável entrada.

Justificativa: Responsável por checar se o usuário digitou "sair". Se a condição for verdadeira, o comando break é ativado, forçando o programa a sair imediatamente da estrutura de repetição while e seguindo para o cálculo das médias.

Segundo uso (try / except ValueError): Funciona como um mecanismo de validação e controle de erro. Garante que o programa não quebre (feche abruptamente) caso o usuário digite uma letra ou símbolo em vez de um número válido.

Terceiro uso (if len(temp_celsius) > 0): Antes de calcular e exibir as médias, checa se a lista de temperaturas recebeu algum dado. Isso evita o erro de divisão por zero na matemática do script caso o usuário digite "sair" logo na primeira execução.

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
