# Inicializa uma lista vazia para armazenar as tarefas
tarefas = []

print("--- Gerenciador de Tarefas ---")
print("Digite 'fim' a qualquer momento para sair e ver suas tarefas.")

# Estrutura de repetição: Permite que o programa continue pedindo novas tarefas
while True:
    tarefa = input("\nDigite a sua tarefa: ")
    
    # Estrutura de decisão: Verifica se a palavra de parada foi digitada
    if tarefa.lower() == "fim":
        print("\n--- Saindo do programa ---")
        break  # Encerra o loop e para a repetição
    else:
        tarefas.append(tarefa) # Adiciona a tarefa informada à lista

# Exibe a lista completa de tarefas cadastradas
print("\n=== Suas Tarefas Cadastradas ===")
for t in tarefas:
    print(f"- {t}")