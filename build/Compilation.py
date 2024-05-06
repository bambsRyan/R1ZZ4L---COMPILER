class Compilation:
    def __init__(self,tokens):  
        self.tokens = tokens    #tokens from lexer
        self.max = len(tokens)  #number of tokens
        self.num = -1           #current token index
        self.errors = []        #list of errors 
        self.current = ''       #current token
        self.values = ''        #values

# ------------------------ PARSER -------------------------------------
    def parse(self):
        for i in self.tokens:
            print(i)
        if self.max == 0:
            self.errors = ["Syntax Error: No tokens found"]
        else:
            self.next()
            self.newline()
            self.program()
            self.packages()
            while self.current != None or self.current == 'gg.ssSawa':
                self.body()
                if self.current not in body and self.current != None:
                    self.err('"yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda", "subok"')

        if self.errors == []:
            self.errors = ["Syntax Completed: No errors found"]
            return 
