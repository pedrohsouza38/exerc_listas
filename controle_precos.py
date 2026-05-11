# Programa: Analisador de Preços

# 1. Inicialização da lista vazia
precos = []

# 2. ESTRUTURA DE REPETIÇÃO (for)
# Justificativa: Usa o 'for' com 'range(5)' porque sabe exatamente quantas vezes o código deve rodar (5 vezes). É mais eficiente que um 'while'.
print("Digite 5 preços:")
for i in range(5):
    # Solicita o preço e converte para float (número real)
    preco = float(input(f"Digite o {i+1}º preço: R$ "))
    # Adiciona o preço na lista
    precos.append(preco)

# 3. EXIBIÇÃO DOS RESULTADOS
# Justificativa: Utiliza as funções embutidas max() e min() para encontrar o maior e menor valor de forma direta e eficiente.
print("-" * 30)
print(f"Lista de preços: {precos}")
print(f"O maior preço é: R$ {max(precos):.2f}")
print(f"O menor preço é: R$ {min(precos):.2f}")
print("-" * 30)