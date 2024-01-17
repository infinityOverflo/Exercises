from lexer.lex import *

def main():
    source = "LET foobar = 1234"

    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()

main()