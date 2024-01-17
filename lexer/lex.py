class Lexer:
    def __init__(self, source):
        self.source = source + '\n'
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nextChar(self):
        self.curPos += 1
        if (self.curPos >= len(self.source)):
            self.curChar = '\0' # EOF
        else:
            self.curChar = self.source[self.curPos]
 
    def peek(self):
        if self.curPos+1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    def abort(self,message):
        pass

    def skipWhitespace(self):
        pass

    def skipComment(self):
        pass

    def getToken(self):
        if self.curChar == '+':
            pass
        elif self.curChar == '-':
            pass
        elif self.curChar == '*':
            pass
        elif self.curChar == '/':
            pass
        elif self.curChar == '\n':
            pass
        elif self.curChar == '\0':
            pass
        else:
            pass

        self.nextChar()

