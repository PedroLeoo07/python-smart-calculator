import math

def mostrar_menu():
    """Exibe o menu de opções da calculadora"""
    print("\n" + "="*40)
    print("         CALCULADORA")
    print("="*40)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz quadrada")
    print("7 - Sair")
    print("="*40)

def obter_numero(mensagem):
    """Solicita e valida a entrada de um número"""
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("❌ Erro: Por favor, digite um número válido!")

def soma(a, b):
    """Realiza a soma de dois números"""
    return a + b

def subtracao(a, b):
    """Realiza a subtração de dois números"""
    return a - b

def multiplicacao(a, b):
    """Realiza a multiplicação de dois números"""
    return a * b

def divisao(a, b):
    """Realiza a divisão de dois números"""
    if b == 0:
        return None
    return a / b

def potencia(a, b):
    """Calcula a potência de um número"""
    return a ** b

def raiz_quadrada(a):
    """Calcula a raiz quadrada de um número"""
    if a < 0:
        return None
    return math.sqrt(a)

def calculadora():
    """Função principal da calculadora"""
    print("\n🔢 Bem-vindo à Calculadora!")
    
    while True:
        mostrar_menu()
        
        # Obtém a opção do usuário
        try:
            opcao = int(input("\nEscolha uma opção (1-7): "))
        except ValueError:
            print("\n❌ Erro: Digite um número válido entre 1 e 7!")
            continue
        
        # Opção para sair
        if opcao == 7:
            print("\n👋 Obrigado por usar a calculadora! Até logo!")
            break
        
        # Validar opção
        if opcao < 1 or opcao > 7:
            print("\n❌ Erro: Opção inválida! Escolha um número entre 1 e 7.")
            continue
        
        # Operações que precisam de dois números
        if opcao in [1, 2, 3, 4, 5]:
            print("\n")
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            if opcao == 1:
                resultado = soma(num1, num2)
                print(f"\n✅ Resultado: {num1} + {num2} = {resultado}")
            
            elif opcao == 2:
                resultado = subtracao(num1, num2)
                print(f"\n✅ Resultado: {num1} - {num2} = {resultado}")
            
            elif opcao == 3:
                resultado = multiplicacao(num1, num2)
                print(f"\n✅ Resultado: {num1} × {num2} = {resultado}")
            
            elif opcao == 4:
                resultado = divisao(num1, num2)
                if resultado is None:
                    print("\n❌ Erro: Não é possível dividir por zero!")
                else:
                    print(f"\n✅ Resultado: {num1} ÷ {num2} = {resultado}")
            
            elif opcao == 5:
                resultado = potencia(num1, num2)
                print(f"\n✅ Resultado: {num1} elevado a {num2} = {resultado}")
        
        # Operação de raiz quadrada (um número apenas)
        elif opcao == 6:
            print("\n")
            num = obter_numero("Digite o número: ")
            resultado = raiz_quadrada(num)
            
            if resultado is None:
                print("\n❌ Erro: Não é possível calcular raiz quadrada de número negativo!")
            else:
                print(f"\n✅ Resultado: √{num} = {resultado}")
        
        # Perguntar se deseja continuar
        print("\n" + "-"*40)
        continuar = input("Deseja realizar outra operação? (s/n): ").lower().strip()
        
        if continuar != 's' and continuar != 'sim':
            print("\n👋 Obrigado por usar a calculadora! Até logo!")
            break

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
