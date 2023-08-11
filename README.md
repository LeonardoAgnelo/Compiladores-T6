# Trabalho 6 de Compiladores - Linguagem para Planejamento de tarefas tarefas 

Este projeto consiste no desenvolvimento de uma linguagem de programação dedicada ao planejamento de tarefas, permitindo aos usuários definir, organizar e gerenciar suas atividades de maneira eficiente. A linguagem foi projetada para facilitar a criação de planos de projetos, automatizar a alocação de recursos e controlar a interdependência entre as tarefas.

## Funcionalidades Principais

- Definição de tarefas com nome, descrição, data e status.
- Estabelecimento de dependências entre tarefas para garantir uma ordem lógica de execução.
- Atribuição de recursos a tarefas, otimizando o planejamento e a alocação.
- Visualização de tarefas próximas aos prazos ou em andamento.

## Docente
Daniel Lucrédio  

## Discente
Leonardo Nogueira Agnelo - 779801  
João Gabriel Gonçalves - 769690  
Victor Fernandes Dell Elba Gomes - 769839 

### Pré-requisitos
Certifique-se de ter os seguintes requisitos instalados em seu sistema:

Python 3

Java Development Kit (JDK) - versão 8 ou superior

ANTLR4-Tools

ANTLR4 Python Runtime

### COMO EXECUTAR
    # Instale o runtime para python
    $ pip install antlr4-python3-runtime

    # Instale as ferramentas do ANTLR4
    $ pip install antlr4-tools

    # Gerar Lexer
    $ antlr4 -Dlanguage=Python3 Todolist.g4 -o "Parser"

    # Teste
    $ py main.py "teste.txt" "saida.txt"
