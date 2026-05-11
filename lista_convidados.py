# Programa de Cadastro de Convidados

# 1. Inicialização da Lista
# Utiliza uma lista vazia [] para armazenar os nomes.
# Listas são ideais para coleções ordenadas que podem mudar de tamanho.
convidados = []

print("--- Sistema de Cadastro de Convidados (5 vagas) ---")

# 2. Estrutura de Repetição (for + range)
# O laço 'for' com 'range(5)' é ideal porque sabe exatamente quantas vezes quer repetir o cadastro (5 vezes).
for i in range(1, 6):
    # Solicita o nome e remove espaços em branco extras
    nome = input(f"Digite o nome do convidado {i}: ").strip()
    
    # 3. Estrutura de Decisão (if)
    # Verifica se o usuário digitou algo antes de adicionar
    if nome != "":
        convidados.append(nome) # Adiciona o nome à lista
    else:
        print("Nome inválido. Convidado ignorado.")

# 4. Exibição dos Dados
print("\n--- Lista de Convidados ---")
# Usa 'for' novamente para percorrer a lista e mostrar nome por nome
for indice, convidado in enumerate(convidados, start=1):
    print(f"{indice}. {convidado}")

# 5. Informar a Quantidade
# Utiliza a função 'len()' para contar quantos elementos existem na lista.
total_convidados = len(convidados)
print("-" * 25)
print(f"Total de convidados: {total_convidados}")
print("---------------------------")