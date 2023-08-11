import sys
import logging
from antlr4 import *
from Parser.TodolistLexer import TodolistLexer
from Parser.TodolistParser import TodolistParser
from antlr4.error.ErrorListener import ErrorListener

def main():
    # Obtém o nome do arquivo de entrada e de saída a partir dos argumentos da linha de comando
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    input = FileStream(input_file, encoding='utf-8')
    output = open(output_file, 'w')
    lexer = TodolistLexer(input, output)
    tokens = CommonTokenStream(lexer)
    parser = TodolistParser(tokens, output)
    
    parser.tarefa() 
    output.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        logging.error(error)