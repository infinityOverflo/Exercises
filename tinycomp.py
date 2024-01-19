from lexer.lex import *

def main():
    source = "+ * / - == <= >= != #_random message_\n <= \"Hello\" +-111.122"

    lexer = Lexer(source)

    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        if token.kind == TokenType.STRING:
            print(token.text)
        elif token.kind == TokenType.NUMBER:
            print(token.text)
        token = lexer.getToken()

main()