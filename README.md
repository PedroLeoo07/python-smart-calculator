# 🧮 Calculadora Inteligente em Python

Uma calculadora interativa e avançada desenvolvida em Python com interface de linha de comando intuitiva, oferecendo operações matemáticas básicas, avançadas e trigonométricas, além de histórico de operações.

## ✨ Funcionalidades

### Operações Básicas
- ➕ **Soma**: Adiciona dois números
- ➖ **Subtração**: Subtrai dois números
- ✖️ **Multiplicação**: Multiplica dois números
- ➗ **Divisão**: Divide dois números (com proteção contra divisão por zero)

### Operações Avançadas
- 🔢 **Potência**: Calcula a potência de um número
- √ **Raiz Quadrada**: Calcula a raiz quadrada de um número (com validação para números negativos)
- % **Porcentagem**: Calcula a porcentagem de um valor
- 📐 **Módulo**: Calcula o resto da divisão entre dois números

### Funções Trigonométricas
- 📊 **Seno**: Calcula o seno de um ângulo em graus
- 📊 **Cosseno**: Calcula o cosseno de um ângulo em graus
- 📊 **Tangente**: Calcula a tangente de um ângulo em graus

### Recursos Extras
- 📜 **Histórico de Operações**: Salva todas as operações realizadas com data e hora
- 🗑️ **Limpar Histórico**: Remove todas as operações salvas
- 🧹 **Limpar Tela**: Limpa a interface do terminal
- ⏰ **Timestamp**: Registra data e hora de cada operação

## 🚀 Como Usar

### Pré-requisitos

- Python 3.x instalado no sistema

### Executando a Calculadora

1. Clone o repositório ou baixe os arquivos
2. Navegue até o diretório do projeto
3. Execute o seguinte comando:

```bash
python calculadora.py
```

### Exemplo de Uso

```text
==================================================
         🧮 CALCULADORA INTELIGENTE 🧮
==================================================
  OPERAÇÕES BÁSICAS:
  1  - ➕ Soma
  2  - ➖ Subtração
  3  - ✖️  Multiplicação
  4  - ➗ Divisão

  OPERAÇÕES AVANÇADAS:
  5  - 🔢 Potência
  6  - √  Raiz quadrada
  7  - %  Porcentagem
  8  - 📐 Módulo (resto da divisão)

  FUNÇÕES TRIGONOMÉTRICAS:
  9  - 📊 Seno
  10 - 📊 Cosseno
  11 - 📊 Tangente

  OUTRAS FUNÇÕES:
  12 - 📜 Ver histórico
  13 - 🗑️  Limpar histórico
  14 - 🧹 Limpar tela
  0  - 🚪 Sair
==================================================
```

Escolha uma opção digitando o número correspondente e siga as instruções na tela.

### Exemplo de Operação

```text
👉 Escolha uma opção: 1
--------------------------------------------------
📝 Digite o primeiro número: 10
📝 Digite o segundo número: 5

✅ Resultado: 10.0 + 5.0 = 15.0
--------------------------------------------------
✨ Pressione Enter para continuar...
```

## 🛡️ Tratamento de Erros

A calculadora inclui validações para:

- ✅ Entrada de dados (aceita apenas números válidos)
- ✅ Divisão por zero
- ✅ Raiz quadrada de números negativos
- ✅ Módulo com divisor zero
- ✅ Opções inválidas no menu
- ✅ Validação de tipos de dados

## 📁 Estrutura do Projeto

```text
python-smart-calculator/
│
├── calculadora.py    # Arquivo principal da calculadora
└── README.md         # Documentação do projeto
```

## 🎯 Funcionalidades Detalhadas

### Histórico de Operações
A calculadora mantém um registro completo de todas as operações realizadas durante a sessão, incluindo:
- Data e hora de cada operação
- Expressão matemática completa
- Resultado obtido

### Interface Intuitiva
- Menu colorido e organizado com emojis
- Mensagens de erro claras e informativas
- Feedback visual para cada operação
- Opção de limpar a tela para melhor visualização

### Precisão Matemática
- Suporte para números decimais
- Cálculos trigonométricos com 6 casas decimais
- Conversão automática de graus para radianos nas funções trigonométricas

## 🔧 Tecnologias Utilizadas

- **Python 3.x**
- Biblioteca `math` (padrão do Python)

## 👨‍💻 Autor

PedroLeoo07

## 📄 Licença

Este projeto está disponível para uso educacional e pessoal.

---

⭐ Se você achou este projeto útil, considere dar uma estrela no repositório!
