import math
import os
from datetime import datetime

# Histórico de operações
historico = []

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Exibe o menu de opções da calculadora"""
    print("\n" + "="*50)
    print("         🧮 CALCULADORA INTELIGENTE 🧮")
    print("="*50)
    print("  OPERAÇÕES BÁSICAS:")
    print("  1  - ➕ Soma")
    print("  2  - ➖ Subtração")
    print("  3  - ✖️  Multiplicação")
    print("  4  - ➗ Divisão")
    print("\n  OPERAÇÕES AVANÇADAS:")
    print("  5  - 🔢 Potência")
    print("  6  - √  Raiz quadrada")
    print("  7  - %  Porcentagem")
    print("  8  - 📐 Módulo (resto da divisão)")
    print("\n  FUNÇÕES TRIGONOMÉTRICAS:")
    print("  9  - 📊 Seno")
    print("  10 - 📊 Cosseno")
    print("  11 - 📊 Tangente")
    print("\n  OUTRAS FUNÇÕES:")
    print("  12 - 📜 Ver histórico")
    print("  13 - 🗑️  Limpar histórico")
    print("  14 - 🧹 Limpar tela")
    print("  0  - 🚪 Sair")
    print("="*50)

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

def porcentagem(valor, percentual):
    """Calcula a porcentagem de um valor"""
    return (valor * percentual) / 100

def modulo(a, b):
    """Calcula o módulo (resto da divisão)"""
    if b == 0:
        return None
    return a % b

def seno(angulo_graus):
    """Calcula o seno de um ângulo em graus"""
    return math.sin(math.radians(angulo_graus))

def cosseno(angulo_graus):
    """Calcula o cosseno de um ângulo em graus"""
    return math.cos(math.radians(angulo_graus))

def tangente(angulo_graus):
    """Calcula a tangente de um ângulo em graus"""
    return math.tan(math.radians(angulo_graus))

def adicionar_historico(operacao, resultado):
    """Adiciona uma operação ao histórico"""
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historico.append({
        'timestamp': timestamp,
        'operacao': operacao,
        'resultado': resultado
    })

def mostrar_historico():
    """Exibe o histórico de operações"""
    if not historico:
        print("\n📭 O histórico está vazio!")
        return
    
    print("\n" + "="*50)
    print("         📜 HISTÓRICO DE OPERAÇÕES")
    print("="*50)
    for i, item in enumerate(historico, 1):
        print(f"{i}. [{item['timestamp']}]")
        print(f"   {item['operacao']} = {item['resultado']}")
        print("-"*50)

def limpar_historico():
    """Limpa o histórico de operações"""
    global historico
    historico = []
    print("\n🗑️  Histórico limpo com sucesso!")

def calculadora():
    """Função principal da calculadora"""
    print("\n🔢 Bem-vindo à Calculadora Inteligente!")
    print("📅 Data: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    
    while True:
        mostrar_menu()
        
        # Obtém a opção do usuário
        try:
            opcao = int(input("\n👉 Escolha uma opção: "))
        except ValueError:
            print("\n❌ Erro: Digite um número válido!")
            input("Pressione Enter para continuar...")
            continue
        
        # Opção para sair
        if opcao == 0:
            print("\n" + "="*50)
            print("👋 Obrigado por usar a Calculadora Inteligente!")
            print(f"📊 Total de operações realizadas: {len(historico)}")
            print("="*50)
            break
        
        # Opção para ver histórico
        if opcao == 12:
            mostrar_historico()
            input("\nPressione Enter para continuar...")
            continue
        
        # Opção para limpar histórico
        if opcao == 13:
            limpar_historico()
            input("Pressione Enter para continuar...")
            continue
        
        # Opção para limpar tela
        if opcao == 14:
            limpar_tela()
            continue
        
        # Validar opção
        if opcao < 0 or opcao > 14:
            print("\n❌ Erro: Opção inválida!")
            input("Pressione Enter para continuar...")
            continue
        
        # Operações que precisam de dois números
        if opcao in [1, 2, 3, 4, 5, 7, 8]:
            print("\n" + "-"*50)
            num1 = obter_numero("📝 Digite o primeiro número: ")
            num2 = obter_numero("📝 Digite o segundo número: ")
            
            if opcao == 1:
                resultado = soma(num1, num2)
                operacao = f"{num1} + {num2}"
                print(f"\n✅ Resultado: {operacao} = {resultado}")
                adicionar_historico(operacao, resultado)
            
            elif opcao == 2:
                resultado = subtracao(num1, num2)
                operacao = f"{num1} - {num2}"
                print(f"\n✅ Resultado: {operacao} = {resultado}")
                adicionar_historico(operacao, resultado)
            
            elif opcao == 3:
                resultado = multiplicacao(num1, num2)
                operacao = f"{num1} × {num2}"
                print(f"\n✅ Resultado: {operacao} = {resultado}")
                adicionar_historico(operacao, resultado)
            
            elif opcao == 4:
                resultado = divisao(num1, num2)
                operacao = f"{num1} ÷ {num2}"
                if resultado is None:
                    print("\n❌ Erro: Não é possível dividir por zero!")
                else:
                    print(f"\n✅ Resultado: {operacao} = {resultado}")
                    adicionar_historico(operacao, resultado)
            
            elif opcao == 5:
                resultado = potencia(num1, num2)
                operacao = f"{num1}^{num2}"
                print(f"\n✅ Resultado: {operacao} = {resultado}")
                adicionar_historico(operacao, resultado)
            
            elif opcao == 7:
                resultado = porcentagem(num1, num2)
                operacao = f"{num2}% de {num1}"
                print(f"\n✅ Resultado: {operacao} = {resultado}")
                adicionar_historico(operacao, resultado)
            
            elif opcao == 8:
                resultado = modulo(num1, num2)
                operacao = f"{num1} mod {num2}"
                if resultado is None:
                    print("\n❌ Erro: Não é possível calcular módulo com divisor zero!")
                else:
                    print(f"\n✅ Resultado: {operacao} = {resultado}")
                    adicionar_historico(operacao, resultado)
        
        # Operação de raiz quadrada
        elif opcao == 6:
            print("\n" + "-"*50)
            num = obter_numero("📝 Digite o número: ")
            resultado = raiz_quadrada(num)
            operacao = f"√{num}"
            
            if resultado is None:
                print("\n❌ Erro: Não é possível calcular raiz quadrada de número negativo!")
            else:
                print(f"\n✅ Resultado: {operacao} = {resultado}")
                adicionar_historico(operacao, resultado)
        
        # Funções trigonométricas
        elif opcao in [9, 10, 11]:
            print("\n" + "-"*50)
            angulo = obter_numero("📝 Digite o ângulo em graus: ")
            
            if opcao == 9:
                resultado = seno(angulo)
                operacao = f"sen({angulo}°)"
                print(f"\n✅ Resultado: {operacao} = {resultado:.6f}")
                adicionar_historico(operacao, f"{resultado:.6f}")
            
            elif opcao == 10:
                resultado = cosseno(angulo)
                operacao = f"cos({angulo}°)"
                print(f"\n✅ Resultado: {operacao} = {resultado:.6f}")
                adicionar_historico(operacao, f"{resultado:.6f}")
            
            elif opcao == 11:
                resultado = tangente(angulo)
                operacao = f"tan({angulo}°)"
                print(f"\n✅ Resultado: {operacao} = {resultado:.6f}")
                adicionar_historico(operacao, f"{resultado:.6f}")
        
        # Aguardar antes de continuar
        print("\n" + "-"*50)
        input("✨ Pressione Enter para continuar...")

# Executar a calculadora
if __name__ == "__main__":
    calculadora()
