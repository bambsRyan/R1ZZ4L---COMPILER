
class Parser:
    def __init__(self,tokens):  
        self.tokens = tokens    #tokens from lexer
        self.max = len(tokens)  #number of tokens
        self.num = -1           #current token index
        self.errors = []        #list of errors
        self.current = ''       #current token
        self.identifier_num = 1 #identifier number
        self.isBody = False     
        self.isIbang = False
        self.isClosed = False
        self.isException = False

# ------------------------ PARSER -------------------------------------
    def parse(self):
        if self.max == 0: return    #if no tokens
        self.next()                 #get the first token
        self.start()                #start parsing
        self.packages()             #check for packages
        self.body()                 #check for body
        if len(self.errors) == 0:   #if no errors
            self.errors.append("Syntax Compiled Successfully") 

    def start(self): #start parsing
        if self.current == 'g.ssSawa':  
            self.match('g.ssSawa')
            if self.current == 'newline':
                self.newline()
            else:
                self.err('newline')
                self.newline()
        elif self.current == 'newline':
            self.newline()
            self.start()
        else: 
            self.err('g.ssSawa')
            self.enter()

    def packages(self):  #check for packages
        if self.current == 'hakot':
            self.match('hakot')
            if self.current == f'Identifier{self.identifier_num}':
                self.id_match()
                if self.current == 'bilang':
                    self.match('bilang')
                    if self.current == f'Identifier{self.identifier_num}':
                        self.id_match()
                    else:
                        self.err('identifier')
                        self.enter()
                elif self.current == 'newline':
                    self.newline()
                else:
                    self.err('"bilang", "newline"')
                    self.enter()
            else:
                self.err('identifier')
                self.enter()
            self.packages()

# -------------------- OTHER FUNCTIONS --------------------------------
    def next(self):     #get the next token
        self.num += 1
        if self.num < self.max: 
            self.current = self.tokens[self.num][1]
            print(f'current:{self.num}- {self.tokens[self.num][1]}')
        else:
            self.current = None
        if self.current in ['space','Line-comment','Block-comment','tab']:
            self.next()
    
    def err(self,expected): #add error to list
        if self.num == self.max:
                self.errors.append(f"Syntax Error on line {self.tokens[self.num-1][2]}: Expected: {expected}")
        else:
            if self.current == 'newline':
                self.errors.append(f"Syntax Error on line {self.tokens[self.num-1][2]}: Expected: {expected}")
            else:  
                if self.current == f'Identifier{self.identifier_num}':
                    self.errors.append(f"Syntax Error on line {self.tokens[self.num][2]}: Unexpected: Identifier, Expected: {expected}")
                else:
                    self.errors.append(f"Syntax Error on line {self.tokens[self.num][2]}: Unexpected: {self.current}, Expected: {expected}")

    def match(self,expected): #match token
        if self.current == expected:
            self.next()

    def id_match(self):     #match identifier
        if self.current == f'Identifier{self.identifier_num}':
            self.match(f'Identifier{self.identifier_num}')
            self.identifier_num += 1

    def enter(self):    #skip tokens until newline
        while self.current != 'newline' and self.num < self.max:
            self.next()
            if self.current == f'Identifier{self.identifier_num}':
                self.identifier_num += 1
    
    def newline(self):  #skip newlines
        while self.current == 'newline' and self.num != self.max:
            self.next()