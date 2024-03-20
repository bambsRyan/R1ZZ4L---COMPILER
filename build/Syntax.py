
class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.max = len(tokens)
        self.num = -1
        self.errors = []
        self.current = ''
        self.identifier_num = 1
        self.after = ''
        self.isBody = False
        self.isIbang = False
        self.isClosed = False
        self.isException = False

# ------------------------ PARSER -------------------------------------
    def parse(self):
        if self.max == 0 : return
        self.next()
        self.start()
        self.hakot()
        while self.current != 'gg.ssSawa' and self.num < self.max:
            if self.current == 'newline':
                self.newline() 
            if self.current not in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
                if self.isBody:
                    self.err('"gg.ssSawa", "sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"') #done
                    self.enter()
                    self.newline()
                else:
                    self.err('"gg.ssSawa", "hakot", "sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "newline"') #done
                    self.enter()
                    self.newline()
            else:
                self.isBody = True
                self.body()
        self.end()
        if self.current != self.max:
            if self.current == 'newline':
                self.newline()
            if self.current != None:
                self.errors.append(f"Line {self.tokens[self.num][2]}: Unexpected line of Code after gg.ssSawa") #done
        if len(self.errors) == 0:
            self.errors.append("Syntax Compiled Successfully") #done
# -------------------------- CFG --------------------------------------
    def start(self):
        if self.current == 'newline':
            self.newline()
            self.start()
        elif self.current == 'g.ssSawa':
            self.match('g.ssSawa')
            if self.current != 'newline':
                self.err('"newline"') #done
                self.enter()
            self.newline()
        else:
            self.err("\'g.ssSawa\'") #done
            self.enter()

    def hakot(self):
        if self.current == 'hakot':
            self.match('hakot') 
            if self.current == f'Identifier{self.identifier_num}':
                self.module_identifier()
            else:
                self.err('"Identifier"') #done
                self.enter()

    def module_identifier(self):
        if self.current == f'Identifier{self.identifier_num}':
            self.id_match()
            if self.current == 'bilang':
                self.match('bilang')
                if self.current == f'Identifier{self.identifier_num}':
                    self.id_match()
                    if self.current == 'newline':
                        self.newline()
                    else:
                        self.err('"newline"') #done
                        self.enter()
                else:   
                    self.err('"Identifier"') #done
                    self.enter()
            elif self.current == 'newline':
                self.newline()
            elif self.num == self.max:
                self.err('"newline"')
            else:
                self.err('"bilang", "newline"') #done
                self.enter()
        self.hakot()

    def body(self):
            self.statement()
            
    def statement(self):
        if self.current == f'Identifier{self.identifier_num}':
            self.id()
            self.body()
        elif self.current == 'sulat':
            self.outputting()
            self.body()
        elif self.current in ["kung", "pili"]:
            self.conditional()
            self.body()
        if self.current in ["para","habang","gawin"]:
            self.loop()
            self.body()
        if self.current == 'takda':
            self.function()
            self.body()
        if self.current == 'subok':
            self.subok()
            self.body()
        if self.current in ["laktaw","tapos","bura"]:
            self.other()
            self.body()
        else:
            if self.current == 'newline':
                self.newline()
            # if self.block == True:
            #     if self.num == self.max-1:
            #         return
            #     if self.current == '}':
            #         return
            #     else:
            #         self.err('"sulat", "kung", "pili", "para", "habang", "gawin", ' +
            #         '"takda", "subok", "laktaw", "tapos", "bura", "Identifier", "}"')
            #         self.enter()

    def id(self):
        self.id_match()
        if self.current in ["-=", "=", "+=", "*=", "/="]:
            self.aop()
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", 
                                "Titik Literal", f"Identifier{self.identifier_num}", "di","(", "[", "{", "~",
                                "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"]:
                self.allowed_aop()
                if self.current != 'newline':
                    self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", "newline"') #done
                    self.enter()
                self.newline()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                          ' "Identifier", "di","(, "[", "{", "~","tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"') #done
                self.enter()
                self.newline()
        elif self.current == '(':
            self.match('(')
            self.arg()
            if self.current == ')':
                self.match(')')
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", "Identifier", "di", "[", "{", "~", "tala" "diks", "yunit", "punto", "bool",  "baybay", "titik", ")"') #done
                self.enter()
            if self.current != 'newline':
                self.err('"newline"')
                self.enter()
            self.newline()
        else:
            self.err('"=", "-=", "+=", "*=", "/=", "("') #done
            self.enter()
            self.newline()

    def aop(self):
        if self.current == '=':
            self.match('=')
        elif self.current == '+=':
            self.match('+=')
        elif self.current == '-=':
            self.match('-=')
        elif self.current == '*=':
            self.match('*=')
        elif self.current == '/=':
            self.match('/=')

    def allowed_aop(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
            self.math()
        elif self.current == 'kuha':
            self.inputting()
            if self.current == ')':
                return
            elif self.current == 'newline':
                return
            else:
                self.err('")", "newline"')


    def math(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "[", "{", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
            self.math_value()
            if self.current in ["-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay"]:
                self.math_continue()
        elif self.current == '~':
            self.match('~')
            if self.current == '(':
                self.match('(')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.math()
                    if self.current == ')':
                        self.match(')')
                        if self.current in ["-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay"]:
                            self.math_continue()
                    else:
                        self.err('")"') #done
                        self.enter()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                            ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"') #done
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()
        elif self.current == '(':
            self.match('(')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
                if self.current == ')':
                    self.match(')')
                    if self.current in ["-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay"]:
                        self.math_continue()
                else:
                    self.err('")"') #done
                    self.enter()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                            ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"') #done
                self.enter()
        # else: 
        #     self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
        #     ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
        #     self.enter()

    def math_value(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "[", "{", "tala", "diks"]:
            self.value()
        elif self.current in ["yunit", "punto", "bool",  "baybay", "titik"]:
            self.typecast()
        # else:
        #     self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", "Identifier",' +
        #               ' "di", "[", "{", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
        #     self.enter()
            
    def math_continue(self):
        if self.current in ["-", "+", "*", "/", "%", "**"]:
            self.mop()
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' + #done
                ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                self.enter()
        elif self.current in ["!=", "==", ">", "<", ">=", "<=", "ay"]:
            self.cop()
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' + #done
                ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                self.enter()

    def mop(self):
        if self.current == '+':
            self.match('+')
        elif self.current == '-':
            self.match('-')
        elif self.current == '*':
            self.match('*')
        elif self.current == '/':
            self.match('/')
        elif self.current == '%':
            self.match('%')
        elif self.current == '**':
            self.match('**')
    
    def cop(self):
        if self.current == '==':
            self.match('==')
        elif self.current == '!=':
            self.match('!=')
        elif self.current == '<':
            self.match('<')
        elif self.current == '>':
            self.match('>')
        elif self.current == '<=':
            self.match('<=')
        elif self.current == '>=':
            self.match('>=')
        elif self.current == 'ay':
            self.match('ay')

    def value(self):
        if self.current == 'Totoo':
            self.match('Totoo')
        elif self.current == 'Peke':
            self.match('Peke')
        elif self.current == 'Wala':
            self.match('Wala')
        elif self.current == 'Baybay Literal':
            self.match('Baybay Literal')
        elif self.current == 'Punto Literal':
            self.match('Punto Literal')
        elif self.current == 'Titik Literal':
            self.match('Titik Literal')
        elif self.current == 'Yunit Literal':
            self.match('Yunit Literal')
        elif self.current == f'Identifier{self.identifier_num}':
            self.id_match()
            self.value_id_ext()
        elif self.current == 'di':
            self.no()
        elif self.current in ['tala', '[']:
            self.value_list()
        elif self.current in ['diks','{']:
            self.value_dict()
    
    def value_id_ext(self):
        if self.current in ["[", "("]:
            self.value_id_sub_ext()
        elif self.current == '.':
            self.match('.')
            if self.current ==f'Identifier{self.identifier_num}':
                self.id_match()
                if self.current in ['[','(']:
                    self.value_id_sub_ext()
    
    def value_id_sub_ext(self):
        if self.current == '[':
            self.match('[')
            if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
                self.allowed_value()
                if self.current == ']':
                    self.match(']')
                    if self.current == '[':
                        self.value_index_continue()
                else:
                    self.err('"]"') #done
                    self.enter()
            else:
                self.err('"Yunit Literal", "Baybay Literal", "Identifier"') #done
                self.enter()
        elif self.current == '(':
            self.match('(')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.arg()
                if self.current == ')':
                    self.match(')')
                else:
                    self.err('")"') #done
                    self.enter()
            elif self.current == ')':
                self.match(')')
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                            ' "Identifier", "di", "(",")", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", ")"') #done
                self.enter()
        else:
            self.err('"[", "("') #done
            self.enter()
    
    def allowed_value(self):
        if self.current == 'Yunit Literal':
            self.match('Yunit Literal')
        elif self.current == 'Baybay Literal':
            self.match('Baybay Literal')  
        elif self.current == f'Identifier{self.identifier_num}':
            self.id_match()  

    def value_index_continue(self):
        if self.current == '[':
            self.match('[')
            if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
                self.allowed_value()
                if self.current == ']':
                    self.match(']')
                    if self.current == '[':
                        self.value_index_continue()
                else:
                    self.err('"]"') #done
                    self.enter()
            else:
                self.err('"Yunit Literal", "Baybay Literal", "Identifier"') #done
                self.enter()

    def arg(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
            self.math()
            if self.current == ',':
                self.match(',')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.arg()


    def no(self):
        if self.current == 'di':
            self.match('di')
            if self.current == 'di':
                self.no()
            elif self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                            ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"') #done
                self.enter()

    def value_list(self):
        if self.current == 'tala':
            self.match('tala')
            if self.current == '(':
                self.match('(')
                if self.current == '(':
                    self.match('(')
                    if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                        self.list_content()
                        if self.current == ')':
                            self.match(')')
                            if self.current == ')':
                                self.match(')')
                            else:
                                self.err('")"') #done
                                self.enter()
                        else:
                            self.err('",", ")"') #done
                            self.enter()
                    elif self.current == ')':
                        self.match(')')
                        if self.current == ')':
                            self.match(')')
                        else:
                            self.err('")"') #done
                            self.enter()    
                    else:
                        self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", "," ,")"') #done
                        self.enter()
                else:
                    self.err('"("') #done
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()
        elif self.current == '[':
            self.match('[')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.list_content()
                if self.current == ']':
                    self.match(']')
                else:
                    self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", "," ,"]"') #done
                    self.enter()
            elif self.current == ']':
                    self.match(']')
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                ' "Identifier", "di","(, "[","]", "{", "~","tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"') #done
                self.enter()
    
    def list_content(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
            self.math()
            if self.current == ',':
                self.list_content_continue()

    def list_content_continue(self):
        if self.current == ',':
            self.match(',')
            if self.current == 'newline':
                self.newline()
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.list_content()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +
                ' "Identifier", "di","(, "[", "{", "~","tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"') #done
                self.enter()

    def value_dict(self):
        if self.current == '{':
            self.match('{')
            if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
                self.dict_content()
            if self.current == '}':
                self.match('}')
            else:
                self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", ",", "}"') #done
                self.enter()
        elif self.current == 'diks':
            self.match('diks')
            if self.current == '(':
                self.match('(')
                if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
                    self.diks_content()
                    if self.current == ')':
                        self.match(')')
                    else:
                        self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", ",", ")"') #done
                        self.enter()
                else:
                    self.err('"Yunit Literal", "Baybay Literal", "Identifier"') #done
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()

    def dict_content(self):
        if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
            self.allowed_value()
            if self.current == ';':
                self.match(';')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.math()
                    if self.current == ',':
                        self.value_dict_continue()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' + #done
                    ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                    self.enter()
            else:
                self.err('";"') #done
                self.enter()
    
    def value_dict_continue(self):
        if self.current == ',':
            self.match(',')
            if self.current == 'newline':
                self.newline()
            if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
                self.dict_content()
            else:
                self.err('"Yunit Literal", "Baybay Literal", "Identifier"') #done
                self.enter()
                
    def diks_content(self):
        if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
            self.allowed_value()
            if self.current == '=':
                self.match('=')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.math()
                    if self.current == ',':
                        self.value_diks_continue()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' + #done
                    ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                    self.enter()
            else:
                self.err('"="') #done
                self.enter()
    
    def value_diks_continue(self):
        if self.current == ',':
            self.match(',')
            if self.current == 'newline':
                self.newline()
            if self.current in ['Yunit Literal', 'Baybay Literal', f'Identifier{self.identifier_num}']:
                self.diks_content()
            else:
                self.err('"Yunit Literal", "Baybay Literal", "Identifier"') #done
                self.enter()

    def typecast(self):
        self.type_cast()
        if self.current == '(':
            self.match('(')
            if self.current in["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
                if self.current == ')':
                    self.match(')')
                else:
                    self.err('")"') #done
                    self.enter()
            elif self.current == 'kuha':
                self.inputting()
                if self.current == ')':
                    self.match(')')
                else:
                    self.err('")"') #done
                    self.enter()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +  #done
                ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"')
                self.enter()

    def type_cast(self):
        if self.current == 'yunit':
            self.match('yunit')
        if self.current == 'baybay':
            self.match('baybay')
        if self.current == 'punto':
            self.match('punto')
        if self.current == 'bool':
            self.match('bool')
        if self.current == 'titik':
            self.match('titik')
        
    def inputting(self):
        if self.current == 'kuha':
            self.match('kuha')
            if self.current == '(':
                self.match('(')
                if self.current == 'Baybay Literal':
                    self.match('Baybay Literal') 
                    if self.current == ')':
                        self.match(')')
                    else:
                        self.err('")"')  #done
                        self.enter()
                elif self.current == ')':
                    self.match(')')
                else: 
                    self.err('"Baybay Literal",")"') #done
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()

    def outputting(self):
        if self.current == 'sulat':
            self.match('sulat')
            if self.current == '(':
                self.match('(')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.printable()
                    if self.current == ')':
                        self.match(')')
                        if self.current == 'newline':
                            self.newline()
                        else:
                            self.err('"newline"') #done
                            self.enter()
                    else:   
                        self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", ",", ")"')
                        self.enter()
                elif self.current == ')':
                    self.match(')')
                    if self.current == 'newline':
                        self.newline()
                    else:
                        self.err('"newline"')
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +  #done
                    ' "Identifier", "di","(, ")", "[", "{", "~","tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"')
                    self.enter()
            else:
                self.err('"("')
                self.enter()

    def printable(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
            self.math()
            print(self.current)
            if self.current == ',':
                self.match(',')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.printable()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' +  #done
                    ' "Identifier", "di","(, "[", "{", "~","tala", "diks", "yunit", "punto", "bool",  "baybay", "titik", "kuha"')
                    self.enter()

    def conditional(self):
        if self.current == 'kung':
            self.match('kung')
            if self.current == '(':
                self.match('(')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                                    f"Identifier{self.identifier_num}", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.condition()
                    if self.current == ')':
                        self.match(')')
                        if self.current == 'newline':
                            self.newline()
                        if self.current == '{':
                            self.conditional_block()
                        else:
                            self.err('"{"') #done
                            self.enter()
                    else:
                        self.err('"at", "ay", "o", "-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", ")"') #done
                        self.enter()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", ' + #done
                        '"Identifier", "di", "[", "(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()
        elif self.current == 'pili':
            self.match('pili')
            if self.current =='(':
                self.match('(')
                if self.current in [f"Identifier{self.identifier_num}","Titik Literal","Yunit Literal"]:
                    self.pili_val()
                    if self.current == ')':
                        self.match(')')
                        if self.current == 'newline':
                            self.newline()
                        if self.current == '{':
                            self.match('{')
                            if self.current == 'newline':
                                self.newline()
                                if self.current =='pag':
                                    self.pag_block()
                                    if self.current == 'newline':
                                        self.newline()
                                    if self.current == 'kusa':
                                        self.match('kusa')
                                        if self.current =='newline':
                                            self.newline()
                                        if self.current == '{':
                                            self.match('{')
                                            if self.current == 'newline':
                                                self.newline()
                                                if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", 
                                                    "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}","tapos","laktaw","labas"]:
                                                    self.pili_content()
                                                    if self.current =='newline':
                                                        self.newline()
                                                    if self.current == '}':
                                                        self.match('}')
                                                        if self.current == 'newline':
                                                            self.newline()
                                                            if self.current == '}':
                                                                self.match('}')
                                                                if self.current == 'newline':
                                                                    self.newline()
                                                                else:
                                                                    self.err('"newline"') #done
                                                                    self.enter()
                                                            else:
                                                                self.err('"}"') #done
                                                                self.enter()
                                                        else:
                                                            self.err('"}"') #done
                                                            self.enter()
                                                    else:
                                                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", ' + #done
                                                    '"subok", "laktaw", "tapos", "bura", "Identifier","tapos","laktaw", "labas", "}"')
                                                        self.enter()
                                                else:
                                                    self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", ' + #done
                                                    '"subok", "laktaw", "tapos", "bura", "Identifier","tapos","laktaw", "labas"')
                                                    self.enter()
                                            else:
                                                self.err('"newline"') #done
                                                self.enter()
                                        else:
                                            self.err('"{"') #done
                                            self.enter()
                                    else:
                                        self.err('"pag" ,"kusa"') #done
                                        self.enter()
                                else:
                                    self.err('"pag"') #done
                                    self.enter()
                            else:
                                self.err('"newline"') #done
                                self.enter()
                        else:
                            self.err('"{"') #done
                            self.enter()
                    else:
                        self.err('")"') #done
                        self.enter()
                else:
                    self.err('"Identifier","Titik Literal","Yunit Literal"') #done
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()
        else:
            self.err('"pili"','"kung"') #done
            self.enter()

    def condition(self):
        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "[", "(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
            self.math()
            if self.current in ["at", "o"]:
                self.condition_continue()
                
    def condition_continue(self):
        if self.current == 'at':
            self.match('at')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                                    f"Identifier{self.identifier_num}", "di", "[", "(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.condition()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", ' + #done
                        '"Identifier", "di", "[", "(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                self.enter()
        elif self.current == 'o':
            self.match('o')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                                    f"Identifier{self.identifier_num}", "di", "[", "(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.condition()
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", ' + #done
                            '"Identifier", "di", "[", "(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                self.enter()
    
    def conditional_block(self):
        if self.current == '{':
            self.match('{')
            if self.current == 'newline':
                self.newline()
                if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
                    self.statement()
                    if self.current == 'newline':
                        self.newline()
                    if self.current == '}':
                        self.match('}')
                        if self.current == 'newline':
                            self.newline()
                        else:
                            self.err('"newline"') #done
                            self.enter()
                        if self.current =='kundi':
                            self.conditional_continue()
                        elif self.current == 'edi':
                            self.conditional_end()
                    else:
                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "}"') #done
                        self.enter()
                else:
                    self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"') #done
                    self.enter()
            else:
                self.err('"newline"')

    def conditional_continue(self):
        if self.current == 'kundi':
            self.match('kundi')
            if self.current =='(':
                self.match('(')
                print(self.current)
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                    f"Identifier{self.identifier_num}", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.condition()
                    if self.current == ')':
                        self.match(')')
                        if self.current == 'newline':
                            self.newline()
                        if self.current == '{':
                            self.match('{')
                            if self.current == 'newline':
                                self.newline()
                                if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
                                    self.statement()
                                    if self.current =='}':
                                        self.match('}')
                                        if self.current == 'newline':
                                            self.newline()
                                            if self.current =='kundi':
                                                self.conditional_continue()
                                            elif self.current == 'edi':
                                                self.conditional_end()
                                        else:
                                            self.err('"newline"') #done
                                            self.enter()
                                    else:
                                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "}"') #done
                                        self.enter()
                                else:
                                    self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"') #done
                                    self.enter()
                            else:
                                self.err('"newline"') #done
                                self.enter()
                        else:
                            self.err('"{"') #done
                            self.enter()
                    else:
                        self.err('")"') #done
                        self.enter()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", '+ #done
                    '"Identifier", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()

    def conditional_end(self):
        if self.current == 'edi':
            self.match('edi')
            if self.current == 'newline':
                self.newline()
            if self.current == '{':
                self.match('{')
                if self.current == 'newline':
                    self.newline()
                    if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
                        self.statement()
                        if self.current =='}':
                            self.match('}')
                            if self.current == 'newline':
                                self.newline()
                            else:
                                self.err('"newline"') #done
                                self.enter()
                        else:
                            self.err('"}"') #done
                            self.enter()
                    else:
                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "}"') #done
                        self.enter()
                else:
                    self.err('"newline"') #done
                    self.enter()
            else:
                self.err('"{"') #done
                self.enter()

    def pili_val(self):
        if self.current == f'Identifier{self.identifier_num}':
            self.id_match()
        elif self.current == 'Titik Literal':
            self.match('Titik Literal')
        elif self.current == 'Yunit Literal':
            self.match('Yunit Literal')

    def pag_block(self):
        if self.current =='pag':
            self.match('pag')
            if self.current in ["Yunit Literal", "Titik Literal"]:
                self.pag_val()
                if self.current == 'newline':
                    self.newline()
                if self.current == '{':
                    self.match('{')
                    if self.current == 'newline':
                        self.newline()
                        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", 
                        "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}","tapos","laktaw","labas"]:
                            self.pili_content()
                            if self.current == 'newline':
                                self.newline()
                            if self.current == '}':
                                self.match('}')
                                if self.current == 'newline':
                                    self.newline()
                                else: 
                                    self.err('"newline"') #done
                                    self.enter()
                                if self.current =='pag':
                                    self.pag_block()
                            else:
                                self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", ' + #done
                            '"subok", "laktaw", "tapos", "bura", "Identifier","tapos","laktaw","labas", "}"')
                                self.enter()
                        else:
                            self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", ' +  #done
                            '"subok", "laktaw", "tapos", "bura", "Identifier","tapos","laktaw","labas"')
                            self.enter()
                    else:
                        self.err('"newline"') #done
                        self.enter()
                else:
                    self.err('"{"') #done
                    self.enter()
            else:
                self.err('"Yunit Literal", "Titik Literal"') #done
                self.enter()

    def pag_val(self):
        if self.current == 'Titik Literal':
            self.match('Titik Literal')
        elif self.current == 'Yunit Literal':
            self.match('Yunit Literal')

    def pili_content(self):
        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", 
            "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
            self.statement()
        elif self.current in ["tapos","laktaw","labas"]:
            self.pili_jump()
            if self.current == 'newline':
                self.newline()
            else:
                self.err('"newline"')

    def pili_jump(self):
        if self.current == 'tapos':
            self.match('tapos')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'laktaw':
            self.match('laktaw')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'labas':
            self.match('labas')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()

    def loop(self):
        if self.current == 'para':
            self.match('para')
            if self.current == f'Identifier{self.identifier_num}':
                self.id_match()
                if self.current == 'sa':
                    self.match('sa')
                    if self.current in ["Baybay Literal", "lawak", f"Identifier{self.identifier_num}", "[", "{","tala", "diks"]:
                        self.iterable()
                        if self.current =='newline':
                            self.newline()
                        if self.current == '{':
                            self.match('{')
                            if self.current == 'newline':
                                self.newline()
                                if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", f"Identifier{self.identifier_num}"]:
                                    self.loop_body()
                                    if self.current == 'newline':
                                        self.newline()
                                    if self.current == '}':
                                        self.match('}')
                                        if self.current == 'newline':
                                            self.newline()
                                        else:
                                            self.err('"newline"') #done
                                            self.enter()
                                    else:
                                        self.match('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", "Identifier" ,"}"') #done
                                        self.enter()
                                else:
                                    self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", "Identifier"') #done
                                    self.enter()
                            else:
                                self.err('"newline"') #done
                                self.enter()
                        else:
                            self.err('{') #done
                            self.enter()
                    else:
                        self.err('"Baybay Literal", "lawak", "Identifier", "[", "tala", "diks"') #done
                        self.enter()
                else:
                    self.err('sa') #done
                    self.enter()
            else:
                self.err('"Identifier"') #done
                self.enter()
        elif self.current == 'habang':
            self.match('habang')
            if self.current == '(':
                self.match('(')
                if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                                    f"Identifier{self.identifier_num}", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                    self.condition()
                    if self.current ==')':
                        self.match(')')
                        if self.current == 'newline':
                            self.newline()
                        if self.current == '{':
                            self.match('{')
                            if self.current =='newline':
                                self.newline()
                                if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", f"Identifier{self.identifier_num}"]:
                                    self.loop_body()
                                    if self.current == 'newline':
                                        self.newline()
                                    if self.current == '}':
                                        self.match('}')
                                        if self.current == 'newline':
                                            self.newline() 
                                        else:
                                            self.err('"newline"') #done
                                            self.enter()
                                    else:
                                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", "Identifier", "}"') #done
                                        self.enter()
                                else:
                                    self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", "Identifier"') #done
                                    self.enter()
                            else:
                                self.err('"newline"') #done
                                self.enter()
                        else:
                            self.err('"{"') #done
                            self.enter()
                    else:
                        self.err('")"') #done
                        self.enter()
                else:
                    self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", ' + #done
                            '"Identifier", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()
        elif self.current == 'gawin':
            self.match('gawin')
            if self.current == 'newline':
                self.newline()
            if self.current == '{':
                self.match('{')
                if self.current == 'newline':
                    self.newline()
                    if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", f"Identifier{self.identifier_num}"]:
                        self.loop_body()
                        if self.current == 'newline':
                            self.newline()
                        if self.current == '}':
                            self.match('}')
                            if self.current == 'newline':
                                self.newline()
                                if self.current == 'tuwing':
                                    self.match('tuwing')
                                    if self.current == '(':
                                        self.match('(')
                                        if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                                        f"Identifier{self.identifier_num}", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                                            self.condition()
                                            if self.current == ')':
                                                self.match(')')
                                                if self.current == 'newline':
                                                    self.newline()
                                                else:
                                                    self.err('"newline"') #done
                                                    self.enter()
                                            else:
                                                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", ' +
                                            '"Identifier", "di", "[","(", ")" "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"') #done
                                                self.enter()
                                        else:
                                            self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", ' + #done
                                            '"Identifier", "di", "[","(", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                                            self.enter()
                                    else:
                                        self.err('"("') #done
                                        self.enter()
                                else:
                                    self.err('"tuwing"') #done
                                    self.enter()
                            else:
                                self.err("newline")
                                self.enter()
                        else:
                            self.err('"}"') #done
                            self.enter()
                    else:
                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", "Identifier"') #done
                        self.enter()
                else:
                    self.err('"newline"')
            else:
                self.err('"{"') #done
                self.enter()
                    
    def iterable(self):
        if self.current in ["[","tala"]:
            self.value_list()
        elif self.current in ["{","diks"]:
            self.value_dict()
        elif self.current == f'Identifier{self.identifier_num}':
            self.id_match()
        elif self.current == 'Baybay Literal':
            self.match('Baybay Literal')
        elif self.current == 'lawak':
            self.match('lawak')
            if self.current =='(':
                self.match('(')
                if self.current in ["Yunit Literal", f"Identifier{self.identifier_num}"]:
                    self.lawak_value()
                    if self.current == ',':
                        self.match(',')
                        if self.current in ["Yunit Literal", f"Identifier{self.identifier_num}"]:
                            self.lawak_value()
                            if self.current == ',':
                                self.match(',')
                                if self.current in ["Yunit Literal", f"Identifier{self.identifier_num}"]:
                                    self.lawak_value()
                                    if self.current == ')':
                                        self.match(')')
                                    else:
                                        self.err('")"') #done
                                        self.enter()
                                else:
                                    self.err('"Yunit Literal", "Identifier"') #done
                                    self.enter()
                            else:
                                self.err('","') #done
                                self.enter()
                        else:
                            self.err('"Yunit Literal", "Identifier"') #done
                            self.enter()
                    else:
                        self.err('","') #done
                        self.enter()
                else:
                    self.err('"Yunit Literal", "Identifier"') #done
                    self.enter()
            else:
                self.err('"("') #done
                self.enter()
    
    def lawak_value(self):
        if self.current == 'Yunit Literal':
            self.match('Yunit Literal')
        elif self.current == f'Identifier{self.identifier_num}':
            self.id_match()

    def loop_body(self):
        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", f"Identifier{self.identifier_num}"]:
            self.loop_content()
            if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", f"Identifier{self.identifier_num}"]:
                self.loop_content_continue()

    def loop_content(self):
        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "bura", f"Identifier{self.identifier_num}"]:
            self.statement()
        elif self.current in ["tuloy","labas","laktaw","tapos"]:
            self.loop_jump()
    
    def loop_content_continue(self):
        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "tuloy", "labas", f"Identifier{self.identifier_num}"]:
            self.loop_body()
        
    def loop_jump(self):
        if self.current == 'tuloy':
            self.match('tuloy')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'labas':
            self.match('labas')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'laktaw':
            self.match('laktaw')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'tapos':
            self.match('tapos')
            if self.current == 'newline':
                self.match('newline')
            else:
                self.err('"newline"')
                self.enter()

                
    def function(self):
        if self.current == 'takda':
            self.match('takda')
            if self.current == f'Identifier{self.identifier_num}':
                self.id_match()
                if self.current == '(':
                    self.match('(')
                    if self.current == f'Identifier{self.identifier_num}':
                        self.param()
                        if self.current == ')':
                            self.match(')')
                        else:
                            self.err('"Identifier",")"') #done
                            self.enter()
                    elif self.current == ')':
                        self.match(')')
                    else:
                        self.err('"Identifier",")"') #done
                        self.enter()
                    if self.current == 'newline':
                        self.newline()
                    if self.current == '{':
                        self.match('{')
                        if self.current == 'newline':
                            self.newline()
                            if self.current == 'ibang':
                                self.var_scope()
                                if self.current == 'newline':
                                    self.newline()
                            if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", f"Identifier{self.identifier_num}"]:
                                self.func_content()
                                if self.current == 'newline':
                                    self.newline()
                                if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", f"Identifier{self.identifier_num}"]:
                                    self.func_content_continue()
                                    if self.current == 'newline':
                                        self.newline()
                                if self.current == '}':
                                    self.match('}')
                                    if self.current == 'newline':
                                        self.newline()
                                    else:
                                        self.err('"newline"')
                                else:
                                    if self.isIbang == True:
                                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", "Identifier", "}"') #done
                                        self.enter()
                                    else:
                                        self.err('"ibang", "sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", "Identifier", "}"') #done
                                        self.enter()
                            else:
                                if self.isIbang == True:
                                    self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", "Identifier"') #done
                                    self.enter()
                                else:
                                    self.err('"ibang", "sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", "Identifier"') #done
                                    self.enter()
                        else:
                            self.err('"newline"') #done
                            self.enter()
                    else:
                        self.err('"{"') #done
                        self.enter()
                else:
                    self.err('"("') #done
                    self.enter()
            else:
                self.err('"Identifier"') #done
                self.enter()

    def param(self):
        if self.current == f'Identifier{self.identifier_num}':
            self.id_match()
            if self.current == ',':
                self.param_continue()
            elif self.current == '=':
                self.param_next()
            elif self.current == ')':
                return
            else:
                self.err('"=", ",", ")"')
        
    def param_continue(self):
        if self.current == ',':
            self.match(',')
            if self.current == f'Identifier{self.identifier_num}':
                self.param()
            else:
                self.err('"Identifier"') #done
                self.enter()
        
    def param_next(self):
        if self.current == '=':
            self.match('=')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
                if self.current == ',':
                    self.param_continue()
                elif self.current == ')':
                    return
                else:
                    self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay", ",", ")"')
            else:
                self.err('"Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal",' + #done
                ' "Identifier", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"')
                self.enter()
        elif self.current == ',':
            self.param_continue()
            
    def var_scope(self):
        if self.current == 'ibang':
            self.match('ibang')
            if self.current == f'Identifier{self.identifier_num}':
                self.id_match()
                if self.current == 'newline':
                    self.newline()
                    if self.current == 'ibang':
                        self.var_scope()
                    else:
                        if self.current in ["ibang","sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", f"Identifier{self.identifier_num}", "}"]:
                            return
                        else:
                            self.err('"ibang","sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "balik", "tapos", "Identifier", "}"') #done
                            self.enter()
                else:
                    self.err('"newline"') #done
            else:
                self.err('"Identifier"')#done
                self.enter()
        self.isClosed = False

    def func_content(self):
        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
            self.statement()
        elif self.current in ["balik", "tapos"]:
            self.func_jump()
        self.isIbang = True

    def func_jump(self):
        if self.current == 'tapos':
            self.match('tapos')
            if self.current == 'newline':
                self.newline()
            else:
                self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "balik", "tapos", "}"') #done
                self.enter()
        elif self.current == 'balik':
            self.match('balik')
            if self.current in ["Totoo", "Peke", "Wala", "Baybay Literal", "Yunit Literal", "Punto Literal", "Titik Literal", 
                            f"Identifier{self.identifier_num}", "di", "(", "[", "{", "~", "tala", "diks", "yunit", "punto", "bool",  "baybay", "titik"]:
                self.math()
                if self.current != 'newline':
                    self.err('"-", "+", "*", "/", "%", "**", "!=", "==", ">", "<", ">=", "<=", "ay"')
                    self.enter()
            elif self.current == 'newline':
                self.newline()
            else:
                self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "balik", "tapos", "}"') #done
                self.enter()

    def func_content_continue(self):
        if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "balik", "tapos"]:
            self.func_content()
            self.isIbang = True
            if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "balik", "tapos"]:
                self.func_content_continue()

    def subok(self):
        if self.current == 'subok':
            self.match('subok')
            if self.current == 'newline':
                self.newline()
            if self.current == '{':
                self.match('{')
                if self.current == 'newline':
                    self.newline()
                    if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
                        self.statement()
                        if self.current == 'newline':
                            self.newline()
                        if self.current == '}':
                            self.match('}')
                            if self.current == 'newline':
                                self.newline()
                                if self.current == 'bukod':
                                    self.match('bukod')
                                    if self.current == '(':
                                        self.match('(')
                                        if self.current in ["AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "ValueError", "ZeroDivError"]:
                                            self.exception()
                                        if self.current == ')':
                                            self.match(')')
                                            if self.current == 'newline':
                                                self.newline()
                                            if self.current == '{':
                                                self.match('{')
                                                if self.current == 'newline':
                                                    self.newline()
                                                    if self.current in ["sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", f"Identifier{self.identifier_num}"]:
                                                        self.statement()
                                                        if self.current =='newline':
                                                            self.newline()
                                                        if self.current == '}':
                                                            self.match('}')
                                                            if self.current == 'newline':
                                                                self.newline()
                                                            else:
                                                                self.err('"newline"') #done
                                                                self.enter()
                                                        else:
                                                            self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "}"') #done
                                                            self.enter()
                                                    else:
                                                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"') #done
                                                        self.enter()
                                                else:
                                                    self.err('"newline"')#done
                                            else:
                                                self.err('"{"') #done
                                                self.enter()
                                        else:
                                            self.err('"AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "ValueError", "ZeroDivError", ")"') #done
                                            self.enter()
                                    else:
                                        self.err('"("') #done
                                        self.enter()
                                else:
                                    self.err('"bukod"') #done
                                    self.enter()
                            else:
                                self.err('"newline"') #done
                                self.enter()
                        else:
                            self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier", "}"') #done
                            self.enter()
                    else:
                        self.err('"sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"') #done
                        self.enter()
                else:
                    self.err('"newline"') #done
                    self.enter()
            else:
                self.err('"{"') #done
                self.enter()

    def exception(self):
        if self.current in ["AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "ValueError", "ZeroDivError"]:
            self.error()
            if self.current == ',':
                self.error_continue()
            elif self.current == ')':
                return
            else:
                self.err('",", ")"')

    def error(self):
        if self.current =='AttribError':
            self.match('AttribError')
        elif self.current == 'ExcessError':
            self.match('ExcessError')
        elif self.current == 'ImportError':
            self.match('ImportError')
        elif self.current == 'IndexError':
            self.match('IndexError')
        elif self.current == 'KeyError':
            self.match('KeyError')
        elif self.current == 'MemoryError':
            self.match('MemoryError')
        elif self.current == 'NameError':
            self.match('NameError')
        elif self.current == 'TypeError':
            self.match('TypeError')
        elif self.current == 'ValueError':
            self.match('ValueError')
        elif self.current == 'ZeroDivError':
            self.match('ZeroDivError')

    def other(self):
        if self.current == 'laktaw':
            self.match('laktaw')
            if self.current =='newline':
                self.newline()
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'tapos':
            self.match('tapos')
            if self.current =='newline':
                self.newline()
            else:
                self.err('"newline"')
                self.enter()
        elif self.current == 'bura':
            self.match('bura')
            if self.current == f'Identifier{self.identifier_num}':
                self.id_match()
                if self.current =='[' or self.current == '(':
                    self.value_id_sub_ext()
                    if self.current =='newline':
                        self.newline()
                    else:
                        self.err('"newline"')
                        self.enter()
                elif self.current == 'newline':
                    self.newline()
                else:
                    self.err('"(", "[", "newline"')
            else:
                self.err('"Identifier"')
                self.enter()

    def error_continue(self):
        if self.current == ',':
            self.match(',')
            if self.current in ["AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "ValueError", "ZeroDivError"]:
                self.error()
                if self.current == ',':
                    self.error_continue()
            else:
                self.err('"AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "ValueError", "ZeroDivError"')
                self.enter()

    def end(self):
        if self.current == 'gg.ssSawa':
            self.match('gg.ssSawa')
        else:
            if self.isBody == True:
                self.err('"gg.ssSawa", "sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"')
                self.enter()
            else:
                self.err('"gg.ssSawa", "hakot", "sulat", "kung", "pili", "para", "habang", "gawin", "takda", "subok", "laktaw", "tapos", "bura", "Identifier"')
                self.enter()

# -------------------- OTHER FUNCTIONS --------------------------------
    def next(self):
        self.num += 1
        self.after = self.current
        if self.num < self.max: 
            self.current = self.tokens[self.num][1]
            print(f'current:{self.num}- {self.tokens[self.num][1]}')
        else:
            self.current = None
        if self.current in ['space','Line-comment','Block-comment','tab']:
            self.next()
    
    def err(self,expected):
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

    def match(self,expected):
        if self.current == expected:
            self.next()

    def id_match(self):
        if self.current == f'Identifier{self.identifier_num}':
            self.match(f'Identifier{self.identifier_num}')
            self.identifier_num += 1

    def enter(self):
        while self.current != 'newline' and self.num < self.max:
            self.next()
            if self.current == f'Identifier{self.identifier_num}':
                self.identifier_num += 1
    
    def newline(self):
        while self.current == 'newline' and self.num != self.max:
            self.next()