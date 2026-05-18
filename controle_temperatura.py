# Listas para armazenar as temperaturas
temp_celsius = []
temp_fahrenheit = []

# Estrutura de repetição: Permite a inserção contínua de valores até que o usuário digite "sair"
while True:
    entrada = input("Digite a temperatura em graus Celsius (ou 'sair' para encerrar): ").strip().lower()
    
    # Estrutura de decisão: Verifica se o comando de saída foi acionado
    if entrada == 'sair':
        print("Encerrando a entrada de dados...")
        break
    
    # Estrutura de decisão: Tenta converter o texto para número e ignora valores inválidos
    try:
        valor_celsius = float(entrada)
        temp_celsius.append(valor_celsius)
        
        # Converte para Fahrenheit usando a fórmula: F = C * (9/5) + 32
        valor_fahrenheit = valor_celsius * (9/5) + 32
        temp_fahrenheit.append(valor_fahrenheit)
        
        print(f"{valor_celsius}°C convertido para {valor_fahrenheit}°F.")
        
    except ValueError:
        print("Valor inválido. Digite apenas um número ou 'sair'.")

# Estrutura de decisão: Executa o cálculo e exibição apenas se a lista não estiver vazia
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