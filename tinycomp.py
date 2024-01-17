from lexer.lex import *

def main():
    source = "+ * / - == <= >= != #_random message_\n <="

    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()

main()