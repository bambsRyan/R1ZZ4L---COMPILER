program = ["g.ssSawa"]
body = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda"]
statement = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda"]
statement_for_conditional = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili"]
statement_for_looping = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin"]
statement_for_func_dec = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura"]
var_dec = ["yunit", "punto", "baybay", "titik", "bool"]
num_Identifier = ["Identifier"]
num_Identifier_continue = ["=", "["]
num_tala_expression = ["["]
num_ext = [","]
num_tala = ["[", "Identifier"]
num_tala_continue = ["+"]
num_tala_content = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "(", "["]
num_tala_content_continue = [","]
num_content = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "(", "["]
num_tala_concatenate = ["[", "Identifier"]
num_dec_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("]
num_dec_expression_continue = ["+", "-", "*", "/", "%", "**"]
num_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~"]
num_sub_expression = ["Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~"]
num_value = ["Punto Literal", "Yunit Literal", "saYunit", "saPunto"]
mop = ["+", "-", "*", "/", "%", "**"]
baybay_Identifier = ["Identifier"]
baybay_Identifier_continue = ["[", "="]
baybay_tala_expression = ["["]
baybay_ext = [","]
baybay_tala = ["[", "Identifier"]
baybay_tala_continue = ["+"]
baybay_tala_content = ["Identifier", "Baybay Literal", "saBaybay", "(", "["]
baybay_tala_content_continue = [","]
baybay_content = ["Identifier", "Baybay Literal", "saBaybay", "(", "["]
baybay_tala_concatenate = ["[", "Identifier"]
baybay_dec_expression = ["Identifier", "Baybay Literal", "saBaybay", "("]
baybay_dec_expression_continue = ["+"]
baybay_expression = ["Identifier", "Baybay Literal", "saBaybay"]
baybay_sub_expression = ["Baybay Literal", "saBaybay"]
baybay_value = ["Baybay Literal", "saBaybay"]
titik_Identifier = ["Identifier"]
titik_Identifier_continue = ["=", "["]
titik_tala_expression = ["["]
titik_expression = ["Identifier", "Titik Literal", "saTitik"]
titik_sub_expression = ["Titik Literal", "saTitik"]
titik_ext = [","]
titik_tala = ["[", "Identifier"]
titik_content = ["Identifier", "Titik Literal", "saTitik", "["]
titik_tala_continue = ["+"]
titik_tala_content = ["Identifier", "Titik Literal", "saTitik"]
titik_tala_content_continue = [","]
titik_tala_concatenate = ["[", "Identifier"]
bool_Identifier = ["Identifier"]
bool_identifier_continue = ["="]
bool_ext = [","]
condition = ["di"]
cond = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "Totoo", "Peke", "("]
negate = ["di"]
condition_statement = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "Totoo", "Peke"]
condition_id_continue = [">", "<", ">=", "<=", "==", "!="]
condition_sub_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "Totoo", "Peke", "("]
math_tala_dec_expression = ["(", "[", "Identifier"]
math_tala_expression = ["[", "Identifier"]
math_tala = ["[", "Identifier"]
math_tala_content = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(",  "Totoo", "Peke"]
math_tala_content_continue = [","]
math_tala_continue = ["+"]
math_tala_concatenate = ["[", "Identifier"]
condition_continue = ["at", "o"]
cop = [">", "<", ">=", "<=", "==", "!="]
eop = ["==", "!="]
lop = ["at", "o"]
jumps = ["laktaw", "tapos", "bura"]
del_val = ["["]
id = ["Identifier"]
id_continue = ["(", "[", "=", "+=", "-=", "*=", "/="]
aop = ["=", "+=", "-=", "*=", "/="]
allowed_aop = ["di", "kuha"]
math = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"]
math_continue = ["+", "-", "*", "/", "%", "**", ">", "<", ">=", "<=", "==", "!=", "at", "o"]
math_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "Totoo", "Peke"]
math_value_id_expression_continue = [">", "<", ">=", "<=", "==", "!="]
math_num_expression_continue = [">", "<", ">=", "<=", "==", "!="]
math_baybay_expression_continue = ["==", "!="]
math_titik_expression_continue = ["==", "!="]
math_tala_expression_continue = ["==", "!="]
inputting = ["kuha"]
prompt = ["Baybay Literal"]
outputting = ["sulat"]
printable = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"]
printable_continue = [","]
value_id_expression = ["Identifier", "("]
value_id_sub_expression = ["Identifier"]
value_id = ["Identifier"]
value_id_ext = ["[", "("]
allowed_value = ["Yunit Literal", "Identifier"]
value_index_continue = ["["]
arg = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "("]
arg_continue = [","]
value_id_continue = ["+", "-", "*", "/", "%", "**"]
sub_mop = ["-", "*", "/", "%", "**"]
value_id_continue_plus = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "["]
num_typecast = ["saYunit", "saPunto"]
baybay_typecast = ["saBaybay"]
titik_typecast = ["saTitik"]
typecast_value = ["Identifier", "Punto Literal", "Titik Literal", "Baybay Literal", "Yunit Literal"]
titik_typecast_value = ["Identifier", "Titik Literal", "Baybay Literal", "Yunit Literal"]
func_dec = ["takda"]
param = ["yunit", "punto", "baybay", "titik", "bool"]
param_var_dec = ["yunit", "punto", "baybay", "titik", "bool"]
param_num_next = [",", "="]
param_baybay_next = [",", "="]
param_titik_next = [",", "="]
param_bool_next = [",", "="]
param_default_continue = [","]
param_var_dec_default = ["yunit", "punto", "baybay", "titik", "bool"]
global_call = ["global"]
nickname = ["bilang"]
func_content = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"]
func_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"]
return1 = ["balik"]
return_val = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "("]
func_loop = ["para", "habang", "gawin"]
iterable = ["Baybay Literal", "Identifier", "lawak"]
lawak_value = ["Yunit Literal", "Identifier"]
func_loop_body = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "balik", "labas", "tuloy", "kung", "pili"]
func_loop_content = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "balik", "labas", "tuloy", "kung", "pili"]
loop_jumps = ["labas", "tuloy"]
func_loop_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "balik", "labas", "tuloy", "kung", "pili"]
func_loop_conditional = ["kung", "pili"]
func_loop_conditional_continue = ["kundi"]
func_loop_conditional_end = ["edi"]
func_loop_pag_block = ["pag"]
func_loop_pag_continue = ["pag"]
func_conditional = ["kung", "pili"]
func_conditional_continue = ["kundi"]
func_conditional_end = ["edi"]
pili_val = ["Identifier", "Yunit Literal", "Titik Literal"]
func_pag_block = ["pag"]
pag_val = ["Yunit Literal", "Titik Literal"]
func_pili_body = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"]
func_pili_content = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"]
func_pili_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"]
func_pag_continue = ["pag"]
conditional = ["kung", "pili"]
conditional_content = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin",  "kung", "pili"]
conditional_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin",  "kung", "pili"]
conditional_continue = ["kundi"]
conditional_end = ["edi"]
pag_block = ["pag"]
pili_body = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin",  "kung", "pili"]
pili_content = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin",  "kung", "pili"]
pili_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin",  "kung", "pili"]
pag_continue = ["pag"]
loop = ["para", "habang", "gawin"]
loop_body = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili"]
loop_content = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili"]
loop_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili"]
loop_conditional = ["kung", "pili"]
loop_conditional_continue = ["kundi"]
loop_conditional_end = ["edi"]
loop_pag_block = ["pag"]
loop_pag_continue = ["pag"]

class Parser:
    def __init__(self,tokens):  
        self.tokens = tokens    #tokens from lexer
        self.max = len(tokens)  #number of tokens
        self.num = -1           #current token index
        self.errors = []        #list of errors 
        self.current = ''       #current token
        self.values = ''        #values
        self.line = 0

# ------------------------ PARSER -------------------------------------
    def parse(self):

        if self.max == 0:
            self.errors = ["Syntax Error: No tokens found"]
        else:
            self.next()
            self.newline()
            self.program()
            self.newline()
            if self.current == None:    
                self.errors.append(f'Syntax Error on Line {self.line+1}: Unexpected End of line, expected: "yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda", "gg.ssSawa"')
                return
            while self.current != None and self.current != 'gg.ssSawa':
                self.body()
                if self.current not in body and self.current != None:
                    if self.current != 'gg.ssSawa':
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda", "gg.ssSawa"')
                        self.end()
                        self.newline()
            self.newline()
            if self.current == None:
                self.err('newline')
                return
            self.ender()
            self.newline()
            if self.current != None:
                self.errors.append(f"Syntax Error on Line {self.line}: Unexpected lines of codes outside of the gg.ssSawa")
                return
        if self.errors == []:
            self.errors = ["Syntax Completed: No errors found"]
            return 

    def program(self):
        if self.match('g.ssSawa'):
            if self.match('newline'):
                return
            else:
                self.err('"newline"')
        else:
            self.err('"g.ssSawa"')

    def ender(self):
        if self.match('gg.ssSawa'):
            return
        else:
            self.errors.append(f"Syntax Error on Line {self.line + 1}: Unexpected {self.current}, expecting : 'gg.ssSawa'")
               
    def body(self):
        if self.first(statement):
            self.statement()
            if self.first(body):
                self.body()
    
    def statement(self):
        if self.first(statement_for_conditional):
            self.statement_for_conditional()
        elif self.first(func_dec):
            self.func_dec()
            if self.match('newline'):
                self.newline()
            else:
                self.err('"newline"')
        else:
            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda", ')
        self.body()
    
    def statement_for_conditional(self):
        if self.first(statement_for_looping):
            self.statement_for_looping()
        elif self.first(conditional):
            self.conditional()
        else:
            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili"')
        
    def statement_for_looping(self):
        if self.first(statement_for_func_dec):
            self.statement_for_func_dec()
        elif self.first(loop):
            self.loop()
            if self.match('newline'):
                self.newline()
            else:
                self.err('"newline"')
        else:
            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin"')

    def statement_for_func_dec(self):
        if self.first(var_dec):
            self.var_dec()
            if self.match('newline'):
                self.newline() 
            else:
                self.err('"=", "," ,"newline"')
        elif self.first(id):
            self.id()
            if self.match('newline'):
                self.newline()
            else:
                self.err('"newline"')
        elif self.first(outputting):
            self.outputting()
            if self.match('newline'):
                self.newline()
            else:
                self.err('"newline"')
        elif self.first(jumps):
            self.jumps()
            if self.match('newline'):
                self.newline()
            else:
                self.err('"newline"')
        else:
            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura"')

    def var_dec(self):
        if self.match('yunit'):
            if self.match(':'):
                if self.first(num_Identifier):
                    self.num_Identifier()
                else:
                    self.err('"Identifier"')
            else:
                self.err('":"')
        elif self.match('punto'):
            if self.match(':'):
                if self.first(num_Identifier):
                    self.num_Identifier()
                else:
                    self.err('"Identifier"')    
            else:
                self.err('":"')
        elif self.match('baybay'):
            if self.match(':'):
                if self.first(baybay_Identifier):
                    self.baybay_Identifier()
                else:
                    self.err('"Identifier"')
            else:
                self.err('":"')
        elif self.match('titik'):
            if self.match(':'):
                if self.first(titik_Identifier):
                    self.titik_Identifier()
                else:
                    self.err('"Identifier"')
            else:
                self.err('":"')
        elif self.match('bool'):
            if self.match(':'):
                if self.first(bool_Identifier):
                    self.bool_Identifier()
                else:
                    self.err('"Identifier"')
            else:
                self.err('":"')
        
    def num_Identifier(self):   
        if self.match('Identifier'):
            if self.first(num_Identifier_continue):
                self.num_Identifier_continue()
            elif self.first(num_ext):
                self.num_ext()

    def num_Identifier_continue(self):
        if self.match('='):
            if self.first(num_dec_expression):            
                self.num_dec_expression()
                if self.first(num_ext):
                    self.num_ext()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
        elif self.match('['):
            if self.match(']'):
                if self.match('='):
                    if self.first(num_tala_expression):
                        self.num_tala_expression()
                    else:
                        self.err('"["')
                else:
                    self.err('"="')
            else:
                self.err('"]"')
    
    def num_tala_expression(self):
        if self.first(num_tala):
            self.num_tala()
            if self.first(num_tala_continue):
                self.num_tala_continue()

    def num_ext(self):
        if self.match(','):
            if self.first(num_Identifier):
                self.num_Identifier()
                if self.first(num_ext):
                    self.num_ext()
            else:
                self.err('"Identifier"')
    
    def num_tala(self):
        if self.match('['):
            if self.first(num_tala_content):
                self.num_tala_content()
            if self.match(']'):
                return
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "(", "]"')
        elif self.first(value_id):
            self.value_id()


    def num_tala_continue(self):
        if self.match('+'):
            if self.first(num_tala_concatenate):
                self.num_tala_concatenate()
                if self.first(num_tala_continue):
                    self.num_tala_continue()
            else:
                self.err('"Identifier", "["')

    def num_tala_content(self): 
        if self.first(num_content):
            self.num_content()
            if self.first(num_tala_content_continue):
                self.num_tala_content_continue()
        if self.current != ']':
            self.err('"+", "-", "*", "/", "%", "**", "]", ","')

    def num_content(self):
        if self.first(num_dec_expression):
            self.num_dec_expression()
        elif self.first(num_tala):
            self.num_tala()
    
    def num_tala_content_continue(self):
        if self.match(','):
            if self.first(num_tala_content):
                self.num_tala_content()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')

    def num_tala_concatenate(self):
        if self.first(num_tala):
            self.num_tala()
        elif self.first(value_id):
            self.value_id()

    def num_dec_expression(self):
        if self.first(num_expression):
            self.num_expression()
        elif self.match('('):
            if self.first(num_dec_expression):
                self.num_dec_expression()
                if self.match(')'):
                    if self.first(num_dec_expression_continue):
                        self.num_dec_expression_continue()
                else:
                    self.err(' "+", "-", "*", "/", "%", "**"')
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')

    def num_dec_expression_continue(self):
        if self.first(mop):
            self.mop()
            if self.first(num_dec_expression):
                self.num_dec_expression()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
    
    def num_expression(self):
        if self.first(value_id):
            self.value_id() 
            if self.first(num_dec_expression_continue):
                self.num_dec_expression_continue()
        elif self.first(num_sub_expression):
            self.num_sub_expression()

    def num_sub_expression(self):
        if self.first(num_value):
            self.num_value()
            if self.first(num_dec_expression_continue):
                self.num_dec_expression_continue()
        elif self.match('~'):
            if self.match('('):
                if self.first(num_dec_expression):
                    self.num_dec_expression()
                    if self.match(')'):
                        if self.first(num_dec_expression_continue):
                            self.num_dec_expression_continue()
                    else:
                        self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", ")"')
                else:
                    self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
            else:
                self.err('"("')
                
    def num_value(self):
        if self.match('Punto Literal'):
            return
        elif self.match('Yunit Literal'):
            return
        elif self.first(num_typecast):
            self.num_typecast()
        
    def mop(self):
        if self.match('+'):
            return
        elif self.first(sub_mop):
            self.sub_mop()

    def baybay_Identifier(self):
        if self.match('Identifier'):
            if self.first(baybay_Identifier_continue):
                self.baybay_Identifier_continue()
            elif self.first(baybay_ext):
                self.baybay_ext()
    
    def baybay_Identifier_continue(self):
        if self.match('='):
            if self.first(baybay_dec_expression):
                self.baybay_dec_expression()
                if self.first(baybay_ext):
                    self.baybay_ext()
            else:
                self.err('"Identifier", "Baybay Literal", "saBaybay", "("')
        elif self.match('['):
            if self.match(']'):
                if self.match('='):
                    if self.first(baybay_tala_expression):
                        self.baybay_tala_expression()
                    else:
                        self.err('"["')
                else:
                    self.err('"="')
            else:
                self.err('"]"')
    
    def baybay_tala_expression(self):
        if self.first(baybay_tala):
            self.baybay_tala()
            if self.first(baybay_tala_continue):
                self.baybay_tala_continue()      

    def baybay_ext(self):
        if self.match(','):
            if self.first(baybay_Identifier):
                self.baybay_Identifier()
                if self.first(baybay_ext):
                    self.baybay_ext()
            else:
                self.err('"Identifier"')
    
    def baybay_tala(self):
        if self.match('['):
            if self.first(baybay_tala_content):
                self.baybay_tala_content()
            if self.match(']'):
                return
            else:
                self.err('"Identifier", "Baybay Literal", "saBaybay", "(", "]"')
        elif self.first(value_id):
            self.value_id()

    def baybay_tala_continue(self):
        if self.match('+'):
            if self.first(baybay_tala_concatenate):
                self.baybay_tala_concatenate()
                if self.first(baybay_tala_continue):
                    self.baybay_tala_continue()
            else:
                self.err('"Identifier", "["')

    def baybay_tala_content(self):
        if self.first(baybay_content):
            self.baybay_content()
            if self.first(baybay_tala_content_continue):
                self.baybay_tala_content_continue()
        if self.current != ']':
            self.err('"+", "]", ","')

    def baybay_content(self):
        if self.first(baybay_dec_expression):
            self.baybay_dec_expression()
        elif self.first(baybay_tala):
            self.baybay_tala()

    def baybay_tala_content_continue(self):
        if self.match(','):
            if self.first(baybay_tala_content):
                self.baybay_tala_content()
            else:
                self.err('"Identifier", "Baybay Literal", "saBaybay", "("')

    def baybay_tala_concatenate(self):
        if self.first(baybay_tala):
            self.baybay_tala()
        elif self.first(value_id):
            self.value_id()

    def baybay_dec_expression(self):
        if self.first(baybay_expression):
            self.baybay_expression()
        elif self.match('('):
            if self.first(baybay_dec_expression):
                self.baybay_dec_expression()
                if self.match(')'):
                    if self.first(baybay_dec_expression_continue):
                        self.baybay_dec_expression_continue()
                else:
                    self.err('"+", ")"')
            else:
                self.err('"Identifier", "Baybay Literal", "saBaybay"')  

    def baybay_dec_expression_continue(self):
        if self.match('+'):
            if self.first(baybay_dec_expression):
                self.baybay_dec_expression()
            else:
                self.err('"Identifier", "Baybay Literal", "saBaybay", "("')
        
    def baybay_expression(self):
        if self.first(value_id):
            self.value_id()
            if self.first(baybay_dec_expression_continue):
                self.baybay_dec_expression_continue()
        elif self.first(baybay_sub_expression):
            self.baybay_sub_expression()
        
    def baybay_sub_expression(self):
        if self.first(baybay_value):
            self.baybay_value()
            if self.first(baybay_dec_expression_continue):
                self.baybay_dec_expression_continue()

    def baybay_value(self):
        if self.match('Baybay Literal'):
            return   
        elif self.first(baybay_typecast):
            self.baybay_typecast()

    def titik_Identifier(self):
        if self.match('Identifier'):
            if self.first(titik_Identifier_continue):
                self.titik_Identifier_continue()
            if self.first(titik_ext):
                self.titik_ext()

    def titik_Identifier_continue(self):
        if self.match('='):
            if self.first(titik_expression):
                self.titik_expression()
            else:
                self.err('"Identifier", "Titik Literal", "saTitik"')  
        elif self.match('['):
            if self.match(']'):
                if self.match('='):
                    if self.first(titik_tala_expression):
                        self.titik_tala_expression()
                    else:
                        self.err('"["')
                else:
                    self.err('"="')
            else:
                self.err('"]"')

    def titik_tala_expression(self):
        if self.first(titik_tala):
            self.titik_tala()
            if self.first(titik_tala_continue):
                self.titik_tala_continue()

    def titik_expression(self):
        if self.first(value_id):
            self.value_id()
        elif self.first(titik_sub_expression):
            self.titik_sub_expression()

    def titik_sub_expression(self):
        if self.match('Titik Literal'):
            return
        elif self.first(titik_typecast):
            self.titik_typecast()

    def titik_ext(self):
        if self.match(','):
            if self.first(titik_Identifier):
                self.titik_Identifier()
                if self.first(titik_ext):
                    self.titik_ext()
            else:
                self.err('"Identifier"')
    
    def titik_tala(self):
        if self.match('['):
            if self.first(titik_tala_content):
                self.titik_tala_content()
            if self.match(']'):
                return
            else:
                self.err('"Identifier", "Titik Literal", "saTitik", "(", "]"')   
        elif self.first(value_id):
            self.value_id()

    def titik_tala_continue(self):
        if self.match('+'):
            if self.first(titik_tala_concatenate):
                self.titik_tala_concatenate()
                if self.first(titik_tala_continue):
                    self.titik_tala_continue()
            else:
                self.err('"Identifier", "["')
            
    def titik_tala_content(self):
        if self.first(titik_content):
            self.titik_content()
            if self.first(titik_tala_content_continue):
                self.titik_tala_content_continue()
        if self.current != ']':
            self.err('"]", ","')

    def titik_content(self):
        if self.first(titik_expression):
            self.titik_expression()
        elif self.first(titik_tala):
            self.titik_tala()

    def titik_tala_content_continue(self):
        if self.match(','):
            if self.first(titik_tala_content):
                self.titik_tala_content()
            else:
                self.err('"Identifier", "Titik Literal", "saTitik", "("')

    def titik_tala_concatenate(self):
        if self.first(titik_tala):
            self.titik_tala()
        elif self.first(value_id):
            self.value_id()

    def bool_Identifier(self):
        if self.match('Identifier'):
            if self.first(bool_identifier_continue):
                self.bool_identifier_continue()
            if self.first(bool_ext):
                self.bool_ext()
        
    def bool_identifier_continue(self):
        if self.match('='):
            if self.first(condition):
                self.condition()
            elif self.first(cond):
                self.cond()
            else:
                self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "(", "Totoo", "Peke"')
        if self.current not in [ 'newline', ',', 'at', 'o']:
            self.err('"at", "o", ",", "newline"')

    def bool_ext(self):
        if self.match(','):
            if self.first(bool_Identifier):
                self.bool_Identifier()
                if self.first(bool_ext):
                    self.bool_ext()
            else:
                self.err('"Identifier"')

    def condition(self):
        if self.first(negate):
            self.negate()
            if self.first(cond):
                self.cond()
                if self.first(condition_continue):
                    self.condition_continue()
            else:
                self.err('"di", "Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "Totoo", "Peke", "("')

    def cond(self):
        if self.first(condition_statement):
            self.condition_statement()
            self.condition_continue()
        elif self.match('('):
            if self.first(condition):
                self.condition()
                if self.match(')'):
                   if self.first(condition_continue):
                        self.condition_continue()
                else:
                    self.err('")"')
            elif self.first(cond):
                self.cond()
                if self.match(')'):
                    if self.first(condition_continue):
                        self.condition_continue()
                else:
                    self.err('")"')
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "(", "Totoo", "Peke"')
        
    def negate(self):
        if self.match('di'):
            if self.first(negate):
                self.negate()

    def condition_statement(self):
        if self.first(value_id_sub_expression):
            self.value_id_sub_expression()
            if self.first(condition_id_continue):
                self.condition_id_continue()
        elif self.first(num_sub_expression):
            self.num_sub_expression()
            if self.first(cop):
                self.cop()
                if self.first(num_dec_expression):
                    self.num_dec_expression()
                    if self.current != ')':
                        self.err('"at", "o", ")",  "+", "-", "*", "/", "%", "**"')
                else:
                    self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
            else:
                self.err('+", "-", "*", "**", "%", ">", "<", ">=", "<=", "==", "!="')
        elif self.first(baybay_sub_expression):
            self.baybay_sub_expression()
            if self.first(eop):
                self.eop()
                if self.first(baybay_dec_expression):
                    self.baybay_dec_expression()
                    if self.current != ')':
                        self.err('"at", "o", ")", "+"')
                else:
                    self.err('"Identifier", "Baybay Literal", "saBaybay", "("')
            else:
                self.err('"==", "!="')
        elif self.first(titik_sub_expression):
            self.titik_sub_expression()
            if self.first(eop):
                self.eop()
                if self.first(titik_expression):
                    self.titik_expression()
                    if self.current != ')':
                        self.err('"at", "o", ")", "+"')
                else:
                    self.err('"Identifier", "Titik Literal", "saTitik"')
            else:
                self.err('"==", "!="')
        elif self.first(math_tala_expression):
            self.math_tala_expression()
            if self.first(eop):
                self.eop()
                if self.first(math_tala_dec_expression):
                    self.math_tala_dec_expression()
                    if self.current != ')':
                        self.err('"at", "o", ")", "+"')
                else:
                    self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
            else:
                self.err('"==", "!="')
        elif self.match('Totoo'):
            return
        elif self.match('Peke'):
            return

    def condition_id_continue(self):
        if self.first(cop):
            self.cop()
            if self.first(condition_sub_expression):
                self.condition_sub_expression()
            else:
                self.err('"(","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{"')   

    def condition_sub_expression(self):
        if self.match('('):
            if self.first(condition_sub_expression):
                self.condition_sub_expression()
                if self.match(')'):
                    return
                else:
                    self.err('")"')
        elif self.first(value_id_sub_expression):
            self.value_id_sub_expression()
        elif self.first(num_sub_expression):
            self.num_sub_expression()
            if self.current not in ['at', 'o', ')']:
                self.err('"at", "o", ")",  "+", "-", "*", "/", "%", "**"')
        elif self.first(baybay_sub_expression):
            self.baybay_sub_expression()
            if self.current not in ['at', 'o', ')']:
                self.err('"at", "o", ")",  "+"')
        elif self.first(titik_sub_expression):
            self.titik_sub_expression()
            if self.current not in ['at', 'o', ')']:
                self.err('"at", "o", ")"')
        elif self.first(math_tala_expression):
            self.math_tala_expression()
            if self.current not in ['at', 'o', ')']:
                self.err('"at", "o", ")",  "+"')
        elif self.match('Totoo'):
            return
        elif self.match('Peke'):
            return
        
    def math_tala_dec_expression(self):
        if self.first(math_tala_expression):
            self.math_tala_expression()
        elif self.match('('):
            if self.first(math_tala_dec_expression):
                self.math_tala_dec_expression()
                if self.match(')'):
                    return
                else:
                    self.err('"(", "Identifier", "["')
            else:
                self.err('"(", "Identifier", "["')

    def math_tala_expression(self):
        if self.first(math_tala):
            self.math_tala()
            if self.first(math_tala_continue):
                self.math_tala_continue()

    def math_tala(self):
        if self.match('['):
            if self.first(math_tala_content):
                self.math_tala_content()
            if self.match(']'):
                return  
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "(", "]"')  
        elif self.first(value_id):
            self.value_id()

    def math_tala_content(self):
        if self.first(math):
            self.math()
            if self.first(math_tala_content_continue):
                self.math_tala_content_continue()

    def math_tala_content_continue(self):
        if self.match(','):
            if self.first(math):
                self.math()
                if self.first(math_tala_content_continue):
                    self.math_tala_content_continue()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')

    def math_tala_continue(self):
        if self.match('+'):
            if self.first(math_tala_concatenate):
                self.math_tala_concatenate()
                if self.first(math_tala_continue):
                    self.math_tala_continue()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')

    def math_tala_concatenate(self):    
        if self.first(math_tala_expression):
            self.math_tala_expression()
        elif self.first(value_id):
            self.value_id()


    def condition_continue(self):
        if self.first(lop):
            self.lop()
            if self.first(condition):
                self.condition()
            elif self.first(cond):
                self.cond()
            else:
                self.err('"di", "Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "(", "Totoo", "Peke"')
        else:
            if self.current != ')':
                self.err('"at", "o"')

    def cop(self):
        if self.match('>'):
            return
        elif self.match('<'):
            return
        elif self.match('>='):
            return
        elif self.match('<='):
            return
        elif self.first(eop):
            self.eop()
    
    def eop(self):
        if self.match('=='):
            return
        elif self.match('!='):
            return
        
    def lop(self):
        if self.match('at'):
            return
        elif self.match('o'):
            return

    def jumps(self):
        if self.match('laktaw'):
            return
        elif self.match('tapos'):
            return
        elif self.match('bura'):
            if self.match('Identifier'):
                if self.first(del_val):
                    self.del_val()
                if self.current != 'newline':
                    self.err('"Identifier", "[", "newline"')
            else:
                self.err('"Identifier"')
    

    def del_val(self):
        if self.first(value_index_continue):
            self.value_index_continue()
    
    def id(self):
        if self.match('Identifier'):
            if self.first(id_continue):
                self.id_continue()
            else:
                self.err('"=", "+=", "-=", "*=", "/=", "(", "[" ,"newline"')
        
    def id_continue(self):
        if self.match('('):
            if self.first(arg):
                self.arg()
            if self.match(')'):
                return
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", ")"')
            return
        elif self.first(value_index_continue):
            if self.first(value_index_continue):
                self.value_index_continue()
        if self.first(aop):
            self.aop()
            if self.first(allowed_aop):
                self.allowed_aop()
            elif self.first(math):
                self.math()
            else:
                self.err('"di", "Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')
        else:
            self.err('"=", "+=", "-=", "*=", "/="')

    def aop(self):
        if self.match('='):
            return
        elif self.match('+='):
            return
        elif self.match('-='):
            return
        elif self.match('*='):
            return
        elif self.match('/='):
            return
        
    def allowed_aop(self):
        if self.first(negate):
            self.negate()
            if self.first(math):
                self.math()
            else:
                self.err('"di", "Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')
        elif self.first(inputting):
            self.inputting()

    def math(self):
        if self.match('('):
            if self.first(math):
                self.math()
                if self.match(')'):
                    if self.first(math_continue):
                        self.math_continue()
                else:
                    self.err('")", "newline"')
        elif self.first(math_expression):
            self.math_expression()
    
    def math_continue(self):
        if self.first(mop):
            self.mop()
            if self.first(math):
                self.math()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')
        elif self.first(cop):
            self.cop()
            if self.first(math):
                self.math()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')
        elif self.first(lop):
            self.lop()
            if self.first(math):
                self.math()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')
        elif self.match('|'):
            if self.first(math):
                self.math()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')

    def math_expression(self):
        if self.first(value_id_sub_expression):
            self.value_id_sub_expression()
            if self.first(math_value_id_expression_continue):
                self.math_value_id_expression_continue()
        elif self.first(num_sub_expression):
            self.num_sub_expression()
            if self.first(math_num_expression_continue):
                self.math_num_expression_continue()
        elif self.first(baybay_sub_expression):
            self.baybay_sub_expression()
            if self.first(math_baybay_expression_continue):
                self.math_baybay_expression_continue()
        elif self.first(titik_sub_expression):
            self.titik_sub_expression()
            if self.first(math_titik_expression_continue):
                self.math_titik_expression_continue()
        elif self.first(math_tala_expression):
            self.math_tala_expression()
            if self.first(math_tala_expression_continue):
                self.math_tala_expression_continue()
        elif self.match('Totoo'):
            if self.first(condition_continue):
                self.condition_continue()
        elif self.match('Peke'):
            if self.first(condition_continue):
                self.condition_continue()

    def math_value_id_expression_continue(self):
        if self.first(cop):
            self.cop()
            if self.first(condition_sub_expression):
                self.condition_sub_expression()
                if self.first(condition_continue):
                    self.condition_continue()
            else:
                self.first('"(", "Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "Totoo", "Peke"')

    def math_num_expression_continue(self):
        if self.first(cop):
            self.cop()
            if self.first(num_dec_expression):
                self.num_dec_expression()
                if self.first(condition_continue):
                    self.condition_continue()
            else:
                self.err('"Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~"')

    def math_baybay_expression_continue(self):
        if self.first(eop):
            self.eop()
            if self.first(baybay_dec_expression):
                self.baybay_dec_expression()
                if self.first(condition_continue):
                    self.condition_continue()
            else:
                self.err('"Baybay Literal", "saBaybay"')

    def math_titik_expression_continue(self):
        if self.first(eop):
            self.eop()
            if self.first(titik_sub_expression):
                self.titik_sub_expression()
                if self.first(condition_continue):
                    self.condition_continue()
            else:
                self.err('"Titik Literal", "saTitik"')

    def math_tala_expression_continue(self):
        if self.first(eop):
            self.eop()
            if self.first(math_tala_dec_expression):
                self.math_tala_dec_expression()
                if self.first(condition_continue):
                    self.condition_continue()
            else:
                self.err('"(", "[", "Identifier"')

    def inputting(self):
        if self.match('kuha'):
            if self.match('('):
                if self.first(prompt):
                    self.prompt()
                if self.match(')'):
                    return
                else:
                    self.err('"Baybay Literal", ")"')
            else:
                self.err('"("')
        
    def prompt(self):
        if self.match('Baybay Literal'):
            return
    
    def outputting(self): 
        if self.match('sulat'):
            if self.match('('):
                if self.first(printable):
                    self.printable()
                if self.match(')'):
                    return
                else:
                    self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "(", ")"')
            else:
                self.err('"("')
                
    def printable(self):
        if self.first(math):
            self.math()
            if self.first(printable_continue):
                self.printable_continue()

    def printable_continue(self):
        if self.match(','):
            if self.first(math):
                self.math()
                if self.first(printable_continue):
                    self.printable_continue()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')
        
    def value_id_expression(self):
        if self.match('('):
            if self.first(value_id_continue_plus):
                self.value_id_continue_plus()
                if self.match(')'):
                    if self.first(value_id_continue):
                        self.value_id_continue()
                else:
                    self.err('")"')
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "["')
        elif self.first(value_id_sub_expression):
            self.value_id_sub_expression()

    def value_id_sub_expression(self):
        if self.first(value_id):
            self.value_id()
            if self.first(value_id_continue):
                self.value_id_continue()

    def value_id(self):
        if self.match('Identifier'):
            if self.first(value_id_ext):
                self.value_id_ext()
        
    def value_id_ext(self):
        if self.match('['):
            if self.first(allowed_value):
                self.allowed_value()
                if self.match(']'):
                    if self.first(value_index_continue):
                        self.value_index_continue()
                else:
                    self.err('"Yunit Literal", "Identifier", "]"')
            else:
                self.err('"Yunit Literal", "Identifier"')
        elif self.match('('):
            if self.first(arg):
                self.arg()
                if self.match(')'):
                    return
                else:
                    self.err('",", ")"')      
                
    def allowed_value(self):
        if self.match('Yunit Literal'):
            return
        elif self.match('Identifier'):
            return
        
    def value_index_continue(self):
        if self.match('['):
            if self.first(allowed_value):
                self.allowed_value()
                if self.match(']'):
                    if self.first(value_index_continue):
                        self.value_index_continue()
                else:
                    self.err('"Yunit Literal", "Identifier", "]"')
            else:
                self.err('"Yunit Literal", "Identifier"')

    def arg(self):
        if self.first(math):
            self.math()
            if self.first(arg_continue):
                self.arg_continue()
    
    def arg_continue(self):
        if self.match(','):
            if self.first(math):
                self.math()
                if self.first(arg_continue):
                    self.arg_continue()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("')

    def value_id_continue(self):
        if self.match('+'):
            if self.first(value_id_continue_plus):
                self.value_id_continue_plus()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "["')
        elif self.first(sub_mop):
            self.sub_mop()
            if self.first(num_dec_expression):
                self.num_dec_expression()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')

    def sub_mop(self):
        if self.match('-'):
            return
        elif self.match('*'):
            return
        elif self.match('/'):
            return
        elif self.match('%'):
            return
        elif self.match('**'):
            return

    def value_id_continue_plus(self):
        if self.first(value_id_expression):
            self.value_id_expression()
        elif self.first(num_sub_expression):
            self.num_sub_expression()
        elif self.first(baybay_sub_expression):
            self.baybay_sub_expression()
        elif self.first(math_tala_expression):
            self.math_tala_expression()

    def num_typecast(self):
        if self.match('saYunit'):
            if self.match('('):
                if self.first(typecast_value):
                    self.typecast_value()
                    if self.match(')'):
                        return
                    else:
                        self.err('")"')
                else:
                    self.err('"Punto Literal", "Titik Literal", "Baybay Literal", "Yunit Literal", "Identifier"')
            else:
                self.err('"("')
        elif self.match('saPunto'):
            if self.match('('):
                if self.first(typecast_value):
                    self.typecast_value()
                    if self.match(')'):
                        return
                    else:
                        self.err('")"')
                else:
                    self.err('"Punto Literal", "Titik Literal", "Baybay Literal", "Yunit Literal", "Identifier"')
            else:
                self.err('"("')
                    
    def baybay_typecast(self):
        if self.match('saBaybay'):
            if self.match('('):
                if self.first(typecast_value):
                    self.typecast_value()
                    if self.match(')'):
                        return
                    else:
                        self.err('")"')
                else:
                    self.err('"Punto Literal", "Titik Literal", "Baybay Literal", "Yunit Literal", "Identifier"')
            else:
                self.err('"("')

    def titik_typecast(self):
        if self.match('saTitik'):
            if self.match('('):
                if self.first(titik_typecast_value):
                    self.titik_typecast_value()
                    if self.match(')'):
                        return
                    else:
                        self.err('")"')
                else:
                    self.err('"Titik Literal", "Baybay Literal", "Yunit Literal", "Identifier"')
            else:
                self.err('"("')
    
    def typecast_value(self):
        if self.match('Punto Literal'):
            return
        elif self.first(titik_typecast_value):
            self.titik_typecast_value()

    def titik_typecast_value(self):
        if self.match('Titik Literal'):
            return
        elif self.match('Baybay Literal'):
            return
        elif self.match('Yunit Literal'):
            return
        elif self.first(value_id):
            self.value_id()

    def func_dec(self):
        if self.match('takda'):
            if self.match('Identifier'):
                if self.match('('):
                    self.param()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(global_call):
                                    self.global_call()
                                if self.first(func_content):
                                    self.func_content()
                                    if self.first(func_content_continue):
                                        self.func_content_continue()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"global", "yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('",", ")"')
                else:
                    self.err("(")
            else:
                self.err('"Identifier"')
                                
    def param(self):
        if self.first(param_var_dec):
            self.param_var_dec()
        if self.current != ')':
            self.err('")", "yunit", "punto", "baybay", "titik", "bool"')

    def param_var_dec(self):
        if self.match('yunit'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.first(param_num_next):
                        self.param_num_next()
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('punto'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.first(param_num_next):
                        self.param_num_next()
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('baybay'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.first(param_baybay_next):
                        self.param_baybay_next()
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('titik'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.first(param_titik_next):
                        self.param_titik_next()
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('bool'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.first(param_bool_next):
                        self.param_bool_next()
                else:
                    self.err('Identifier')
            else:
                self.err('":"')

    def param_num_next(self):
        if self.match(','):
            if self.first(param_var_dec):
                self.param_var_dec()
            else:
                self.err('yunit, punto, baybay, titik, bool')
        elif self.match('='):
            if self.first(num_dec_expression):
                self.num_dec_expression()
                if self.first(param_default_continue):
                    self.param_default_continue()
            else:
                self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
    
    def param_baybay_next(self):
        if self.match(','):
            if self.first(param_var_dec):
                self.param_var_dec()
            else:
                self.err('"yunit", "punto", "baybay", "titik", "bool", ')
        elif self.match('='):
            if self.first(baybay_dec_expression):
                self.baybay_dec_expression()
                if self.first(param_default_continue):
                    self.param_default_continue()
            else:
                self.err('"Identifier", "Baybay Literal", "saBaybay", "("')
  
    def param_titik_next(self):
        if self.match(','):
            if self.first(param_var_dec):
                self.param_var_dec()
            else:
                self.err("yunit", "punto", "baybay", "titik", "bool", '')
        elif self.match('='):
            if self.first(titik_expression):
                self.titik_expression()
                if self.first(param_default_continue):
                    self.param_default_continue()
            else:
                self.err('"Identifier", "Titik Literal", "saTitik"')
    
    def param_bool_next(self):
        if self.match(','):
            if self.first(param_var_dec):
                self.param_var_dec()
            else:
                self.err('"yunit", "punto", "baybay", "titik", "bool", ')
        elif self.match('='):
            if self.first(condition):
                self.condition()
                if self.first(param_default_continue):
                    self.param_default_continue()
            else:
                self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')

    def param_default_continue(self):
        if self.match(','):
            if self.first(param_var_dec_default):
                self.param_var_dec_default()
                if self.first(param_default_continue):
                    self.param_default_continue()
            else:
                self.err('"yunit", "punto", "baybay", "titik", "bool", ')

    def param_var_dec_default(self):
        if self.match('yunit'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.match('='):
                        if self.first(num_dec_expression):
                            self.num_dec_expression()
                        else:
                            self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
                    else:
                        self.err('"="')
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('punto'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.match('='):
                        if self.first(num_dec_expression):
                            self.num_dec_expression()
                        else:
                            self.err('"Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("')
                    else:
                        self.err('"="')
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('baybay'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.match('='):
                        if self.first(baybay_dec_expression):
                            self.baybay_dec_expression()
                        else:
                            self.err('"Identifier", "Baybay Literal", "saBaybay", "("')
                    else:
                        self.err('"="')
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('titik'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.match('='):
                        if self.first(titik_expression):
                            self.titik_expression()
                        else:
                            self.err('"Identifier", "Titik Literal", "saTitik"')
                    else:
                        self.err('"="')
                else:
                    self.err('Identifier')
            else:
                self.err('":"')
        elif self.match('bool'):
            if self.match(':'):
                if self.match('Identifier'):
                    if self.match('='):
                        if self.first(condition):
                            self.condition()
                        else:
                            self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
                    else:
                        self.err('"="')
                else:
                    self.err('Identifier')
            else:
                self.err('":"')

    def global_call(self):
        if self.match('global'):
            if self.match('Identifier'):
                if self.first(nickname):
                    self.nickname()
            else:
                self.err('"Identifier"')
        if self.match('newline'):
            self.newline()
            if self.first(global_call):
                self.global_call()
        else:
            self.err('"newline", "bilang"')

    def nickname(self):
        if self.match('bilang'):
            if self.match('Identifier'): 
                return  
            else:
                self.err('"Identifier"')

    def func_content(self):
        if self.first(statement_for_func_dec):
                self.statement_for_func_dec()
        elif self.first(return1): 
            self.return1()
            if self.match('newline'):
                self.newline()
            else:
                self.err('newline')
        elif self.first(func_loop):
            self.func_loop()
            if self.match('newline'):
                self.newline()
            else:
                self.err('newline')
        elif self.first(func_conditional):
            self.func_conditional()

    def func_content_continue(self):
        if self.first(func_content):
            self.func_content()
            if self.first(func_content_continue):
                self.func_content_continue()
        
    def return1(self):
        if self.match('balik'):
            if self.first(return_val):
                self.return_val()
                if self.current == 'newline':
                    return
                else:
                    self.err('"[", "(", "|", "+", "-", "*", "/", "%", "**", "at", "o", ",", ">", "<", ">=", "<=", "==", "!=", ")", "]", "}", "newline"')

    def return_val(self):
        if self.first(math):
            self.math()

    def func_loop(self):
        if self.match('para'):
            if self.match('Identifier'):
                if self.match('sa'):
                    if self.first(iterable):
                        self.iterable()
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_body):
                                    self.func_loop_body()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('"[", "{", "lawak", "Identifier"')
                else:
                    self.err('sa')
            else:
                self.err('Identifier')
        elif self.match('habang'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_body):
                                    self.func_loop_body()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_body):
                                    self.func_loop_body()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')
        elif self.match('gawin'):
            self.newline()
            if self.match('{'):
                if self.match('newline'):
                    self.newline()
                    if self.first(func_loop_body):
                        self.func_loop_body()
                    if self.match('}'):
                        if self.match('tuwing'):
                            if self.match('('):
                                if self.first(condition):
                                    self.condition()
                                    if self.match(')'):
                                        return
                                    else:
                                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                                elif self.first(cond):
                                    self.cond()
                                    if self.match(')'):
                                        return
                                    else:
                                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                                else:
                                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
                            else:
                                self.err('"("')
                        else:
                            self.err('tuwing')
                    else:
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "balik", "labas", "tuloy", "kung", "pili", "}"')
                else:
                    self.err('newline')
            else:
                self.err('{')

    def iterable(self):
        if self.match('Baybay Literal'):
            return 
        elif self.first(value_id):
            self.value_id()
        elif self.match('lawak'):
            if self.match('('):
                if self.first(lawak_value):
                    self.lawak_value()
                    if self.match(','):
                        if self.first(lawak_value):
                            self.lawak_value()
                            if self.match(','):
                                if self.first(lawak_value):
                                    self.lawak_value()
                                    if self.match(')'):
                                        return
                                    else:
                                        self.err('")"')
                                else:
                                    self.err('"Yunit Literal", "Identifier"')
                            else:
                                self.err('","')
                        else:
                            self.err('"Yunit Literal", "Identifier"')
                    else:
                        self.err('","')
                else:
                    self.err('"Yunit Literal", "Identifier"')
            else:
                self.err('"("')
                                                  
    def lawak_value(self):
        if self.match('Yunit Literal'):
            return 
        elif self.first(value_id):
            self.value_id()
        
    def func_loop_body(self):
        if self.first(func_loop_content):
            self.func_loop_content()
            if self.first(func_loop_content_continue):
                self.func_loop_content_continue()
    
    def func_loop_content(self):
        if self.first(statement_for_func_dec):
            self.statement_for_func_dec()
        elif self.first(loop_jumps):
            self.loop_jumps()   
            if self.match('newline'):
                self.newline()
            else:
                self.err('newline')
        elif self.first(return1):
            self.return1()
            if self.match('newline'):
                self.newline()
            else:
                self.err('newline')
        elif self.first(func_loop):
            self.func_loop()
            if self.match('newline'):
                self.newline()
            else:
                self.err('newline')
        elif self.first(func_loop_conditional):
            self.func_loop_conditional()
            
    def loop_jumps(self):
        if self.match('labas'):
            return
        if self.match('tuloy'):
            return

    def func_loop_content_continue(self):
        if self.first(func_loop_content):
            self.func_loop_content()
            if self.first(func_loop_content_continue):
                self.func_loop_content_continue()     
    
    def func_loop_conditional(self):
        if self.match('kung'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_content):
                                    self.func_loop_content()
                                    if self.first(func_loop_content_continue):
                                        self.func_loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(func_loop_conditional_continue):
                                                self.func_loop_conditional_continue()
                                            if self.first(func_loop_conditional_end):
                                                self.func_loop_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik"')
                            else:
                                self.err('newline')
                        else:   
                            self.err('{')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_content):
                                    self.func_loop_content()
                                    if self.first(func_loop_content_continue):
                                        self.func_loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(func_loop_conditional_continue):
                                                self.func_loop_conditional_continue()
                                            if self.first(func_loop_conditional_end):
                                                self.func_loop_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik"')
                            else:
                                self.err('newline')
                        else:   
                            self.err('{')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')
        elif self.match('pili'):
            if self.match('('):
                if self.first(pili_val):
                    self.pili_val()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_pag_block):
                                    self.func_loop_pag_block() 
                                    if self.match('kusa'):
                                        if self.match('{'):
                                            if self.match('newline'):
                                                self.newline()
                                                if self.first(func_loop_body):
                                                    self.func_loop_body()   
                                                    if self.match('}'):
                                                        if self.match('newline'):
                                                            if self.match('}'):
                                                                if self.match('newline'):
                                                                    self.newline()
                                                                else:
                                                                    self.err('newline')
                                                            else:
                                                                self.err('"}"')
                                                        else:
                                                            self.err('newline')
                                                    else:
                                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik", "}"')
                                                else:
                                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik"')
                                            else:
                                                self.err('newline')
                                        else:
                                            self.err('"{"')
                                    else:
                                        self.err('kusa')
                                else:
                                    self.err('"pag"')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('")"')
                else:
                    self.err('"Yunit Literal", "Baybay Literal", "Identifier"')
            else:
                self.err('"("')
                            
    def func_loop_conditional_continue(self):
        if self.match('kundi'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_content):
                                    self.func_loop_content()
                                    if self.first(func_loop_content_continue):
                                        self.func_loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(func_loop_conditional_continue):
                                                self.func_loop_conditional_continue()
                                            if self.first(func_loop_conditional_end):
                                                self.func_loop_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "para", "habang", "gawin", "kung", "pili", "balik"')
                            else:
                                self.err('newline')
                        else:   
                            self.err('{')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_loop_content):
                                    self.func_loop_content()
                                    if self.first(func_loop_content_continue):
                                        self.func_loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(func_loop_conditional_continue):
                                                self.func_loop_conditional_continue()
                                            elif self.first(func_loop_conditional_end):
                                                self.func_loop_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "balik", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "balik"')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')

    def func_loop_conditional_end(self):
        if self.match('edi'):
            self.newline()
            if self.match('{'):
                if self.match('newline'):
                    self.newline()
                    if self.first(func_loop_content):
                        self.func_loop_content()
                        if self.first(func_loop_content_continue):
                            self.func_loop_content_continue()
                        if self.match('}'):
                            if self.match('newline'):
                                self.newline()
                            else:
                                self.err('newline')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "balik", "}"')
                    else:
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "balik"')
                else:
                    self.err('newline')
            else:
                self.err('{')
                        
    def func_loop_pag_block(self):
        if self.match('pag'):
            if self.first(pag_val):
                self.pag_val()
                self.newline()
                if self.match('{'):
                    if self.match('newline'):
                        self.newline()
                        if self.first(func_loop_body):
                            self.func_loop_body()
                            if self.match('}'):
                                if self.match('newline'):
                                    self.newline()
                                    if self.first(func_loop_pag_continue):
                                        self.func_loop_pag_continue()
                                else:
                                    self.err('newline')
                            else:
                                self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "}"')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", ')
                    else:
                        self.err('newline')
                else:
                    self.err('{')
            else:
                self.err('"Yunit Literal", "Baybay Literal"')

    def func_loop_pag_continue(self):
        if self.first(func_loop_pag_block):
            self.func_loop_pag_block()

    def func_conditional(self):
        if self.match('kung'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_content):
                                    self.func_content()
                                    if self.first(func_content_continue):
                                        self.func_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(func_conditional_continue):
                                                self.func_conditional_continue()
                                            if self.first(func_conditional_end):
                                                self.func_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_content):
                                    self.func_content()
                                    if self.first(func_content_continue):
                                        self.func_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(func_conditional_continue):
                                                self.func_conditional_continue()
                                            if self.first(func_conditional_end):
                                                self.func_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('{')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("') 
        elif self.match('pili'):
            if self.match('('):
                if self.first(pili_val):
                    self.pili_val()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_pag_block):
                                    self.func_pag_block()
                                    if self.match('kusa'):
                                        self.newline()
                                        if self.match('{'):
                                            if self.match('newline'):
                                                self.newline()
                                                if self.first(func_pili_body):
                                                    self.func_pili_body()   
                                                    if self.match('}'):
                                                        if self.match('newline'):
                                                            self.newline()
                                                            if self.match('}'):
                                                                if self.match('newline'):
                                                                    self.newline()
                                                            else:
                                                                self.err('"}"')
                                                        else:
                                                            self.err('"newline"')
                                                    else:
                                                        self.err('"}"')
                                                else:
                                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"')
                                            else:
                                                self.err('"newline"')
                                        else:
                                            self.err('"{"')
                                    else:
                                        self.err('"kusa"')
                                else:
                                    self.err('"pag"')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('")"')
                else:
                    self.err('"Yunit Literal", "Baybay Literal"')
            else:
                self.err('"("')    

    def func_conditional_continue(self):
        if self.match('kundi'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_content):
                                    self.func_content()
                                    if self.first(func_loop_content_continue):
                                        self.func_loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):   
                                            self.newline()
                                            if self.first(func_conditional_continue):
                                                self.func_conditional_continue()
                                            elif self.first(func_conditional_end):
                                                self.func_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(func_content):
                                    self.func_content()
                                    if self.first(func_loop_content_continue):
                                        self.func_loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):   
                                            self.newline()
                                            if self.first(func_conditional_continue):
                                                self.func_conditional_continue()
                                            elif self.first(func_conditional_end):
                                                self.func_conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')
    
    def func_conditional_end(self):
        if self.match('edi'):
            self.newline()
            if self.match('{'):
                if self.match('newline'):
                    self.newline()
                    if self.first(func_content):
                        self.func_content()
                        if self.first(func_content_continue):
                            self.func_content_continue()
                        if self.match('}'):
                            if self.match('newline'):
                                self.newline()  
                            else:
                                self.err('newline')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "}"')
                    else:
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", ')
                else:
                    self.err('newline')
            else:
                self.err('{')
                    
    def pili_val(self):
        if self.first(value_id):
            self.value_id()
        elif self.match('Yunit Literal'):
            return
        elif self.match('Titik Literal'):
            return
        
    def func_pag_block(self):
        if self.match('pag'):
            if self.first(pag_val):
                self.pag_val()
                self.newline()
                if self.match('{'):
                    if self.match('newline'):
                        self.newline()
                        if self.first(func_pili_body):
                            self.func_pili_body()
                            if self.match('}'):
                                if self.match('newline'):
                                    self.newline()
                                    if self.first(func_pag_continue):
                                        self.func_pag_continue()
                                else:
                                    self.err('newline')
                            else:
                                self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "}"')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili"')
                    else:
                        self.err('newline')
                else:
                    self.err('{')
            else:
                self.err('"Yunit Literal", "Titik Literal"')  
    
    def pag_val(self):
        if self.match('Yunit Literal'):
            return
        elif self.match('Titik Literal'):
            return

    def func_pili_body(self):
        if self.first(func_pili_content):
            self.func_pili_content()
            if self.first(func_pili_content_continue):
                self.func_pili_content_continue()
    
    def func_pili_content(self):
        if self.first(func_content):
            self.func_content()
    
    def func_pili_content_continue(self):
        if self.first(func_pili_content):
            self.func_pili_content()
            if self.first(func_pili_content_continue):
                self.func_pili_content_continue()
    
    def func_pag_continue(self):
        if self.first(func_pag_block):
            self.func_pag_block()
                                  
    def conditional(self):
        if self.match('kung'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(conditional_content):
                                    self.conditional_content() 
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(conditional_continue):
                                                self.conditional_continue()
                                            if self.first(conditional_end):
                                                self.conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(conditional_content):
                                    self.conditional_content() 
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(conditional_continue):
                                                self.conditional_continue()
                                            if self.first(conditional_end):
                                                self.conditional_end()
                                        else:
                                            self.err('"newline"')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')
        elif self.match('pili'):
            if self.match('('):
                if self.first(pili_val):
                    self.pili_val()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(pag_block):
                                    self.pag_block()
                                    if self.match('kusa'):
                                        self.newline()
                                        if self.match('{'):
                                            if self.match('newline'):
                                                self.newline()
                                            if self.first(pili_body):
                                                self.pili_body()   
                                                if self.match('}'):
                                                    if self.match('newline'):
                                                        self.newline()
                                                        if self.match('}'):
                                                            if self.match('newline'):
                                                                self.newline()
                                                            else:
                                                                self.err('"newline"')
                                                        else:
                                                            self.err('"}"')
                                                    else:
                                                        self.err('newline')
                                                else:
                                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                                            else:
                                                self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili"')
                                        else:
                                            self.err('"{"')
                                    else:
                                        self.err('"pag", "kusa"')
                                else:
                                    self.err('"pag"')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('")"')
                else:
                    self.err('"Yunit Literal", "Titik Literal"')
            else:
                self.err('"("')

    def conditional_content(self):
        if self.first(statement_for_conditional):
            self.statement_for_conditional()
            if self.first(conditional_content_continue):
                self.conditional_content_continue()

    def conditional_content_continue(self):
        if self.first(conditional_content):
            self.conditional_content()
            if self.first(conditional_content_continue):
                self.conditional_content_continue()

    def conditional_continue(self):
        if self.match('kundi'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                if self.first(conditional_content):
                                    self.conditional_content() 
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(conditional_continue):
                                                self.conditional_continue()
                                            elif self.first(conditional_end):
                                                self.conditional_end()
                                        else:
                                            self.err('"newline"')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                if self.first(conditional_content):
                                    self.conditional_content() 
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(conditional_continue):
                                                self.conditional_continue()
                                            elif self.first(conditional_end):
                                                self.conditional_end()
                                        else:
                                            self.err('newline')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')

    def conditional_end(self):
        if self.match('edi'):
            self.newline()
            if self.match('{'):
                if self.match('newline'):
                    self.newline()
                    if self.first(conditional_content):
                        self.conditional_content()
                        if self.match('}'):
                            if self.match('newline'):
                                self.newline()
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                    else:
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", ')
                else:
                    self.err('"newline"')
            else:
                self.err('"{"')
                     
    def pag_block(self):
        if self.match('pag'):
            if self.first(pag_val):
                self.pag_val()
                self.newline()
                if self.match('{'):
                    if self.match('newline'):
                        self.newline()
                        if self.first(pili_body):
                            self.pili_body()
                            if self.match('}'):
                                if self.match('newline'):
                                    self.newline()
                                    if self.first(pag_continue):
                                        self.pag_continue()
                                else:
                                    self.err('"newline"')
                            else:
                                self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "}"')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili"')
                    else:
                        self.err('"newline"')
                else:
                    self.err('"{"')
            else:
                self.err('"Yunit Literal", "Titik Literal"')

    def pili_body(self):
        if self.first(pili_content):
            self.pili_content()
            if self.first(pili_content_continue):
                self.pili_content_continue()
        
    def pili_content(self):
        if self.first(statement_for_conditional):
            self.statement_for_conditional()
            
    def pili_content_continue(self):
        if self.first(pili_content):
            self.pili_content()
            if self.first(pili_content_continue):
                self.pili_content_continue()
            
    def pag_continue(self):
        if self.first(pag_block):
            self.pag_block()

    def loop(self):
        if self.match('para'):
            if self.match('Identifier'):
                if self.match('sa'):
                    if self.first(iterable):
                        self.iterable()
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"Identifier", "Baybay Literal", "lawak"')
                else:
                    self.err('"sa"')
            else:   
                self.err('Identifier')
        elif self.match('habang'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.match('}'):
                                        return
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('newline')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')
        elif self.match('gawin'):
            self.newline()
            if self.match('{'):
                if self.match('newline'):
                    self.newline()
                    if self.first(loop_body):
                        self.loop_body()
                        if self.match('}'):
                            if self.match('tuwing'):
                                if self.match('('):
                                    if self.first(condition):
                                        self.condition()
                                        if self.match(')'):
                                            return
                                        else:
                                            self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                                    elif self.first(cond):
                                        self.cond()
                                        if self.match(')'):
                                            return
                                        else:
                                            self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                                    else:
                                        self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
                                else:
                                    self.err('"("')
                            else:
                                self.err('tuwing')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                    else:
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                else:
                    self.err('"newline"')
            else:
                self.err('"{"')
    
    def loop_body(self):
        if self.first(loop_content):
            self.loop_content()
            if self.first(loop_content_continue):
                self.loop_content_continue()

    def loop_content(self):
        if self.first(statement_for_looping):
            self.statement_for_looping()
        elif self.first(loop_jumps):
            self.loop_jumps()
            if self.match('newline'):
                self.newline()
            else:
                self.err('newline')
        elif self.first(loop_conditional):
            self.loop_conditional()

    def loop_content_continue(self):
        if self.first(loop_content):
            self.loop_content()
            if self.first(loop_content_continue):
                self.loop_content_continue()

    def loop_conditional(self):
        if self.match('kung'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.first(loop_content_continue):
                                        self.loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(loop_conditional_continue):
                                                self.loop_conditional_continue()
                                            if self.first(loop_conditional_end):
                                                self.loop_conditional_end()
                                        else:
                                            self.err('"newline"')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.first(loop_content_continue):
                                        self.loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(loop_conditional_continue):
                                                self.loop_conditional_continue()
                                            if self.first(loop_conditional_end):
                                                self.loop_conditional_end()
                                        else:
                                            self.err('"newline"')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')
        elif self.match('pili'):
            if self.match('('):
                if self.first(pili_val):
                    self.pili_val()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_pag_block):
                                    self.loop_pag_block()
                                    if self.match('kusa'):
                                        self.newline()
                                        if self.match('{'):
                                            if self.match('newline'):
                                                self.newline()
                                                if self.first(loop_body):
                                                    self.loop_body()  
                                                    self.newline() 
                                                    if self.match('}'):
                                                        if self.match('newline'):
                                                            self.newline()
                                                            if self.match('}'):
                                                                if self.match('newline'):
                                                                    self.newline()
                                                                else:
                                                                    self.err('"newline"')
                                                            else:
                                                                self.err('"}"')
                                                        else:
                                                            self.err('"newline"')
                                                    else:
                                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                                else:
                                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                                            else:
                                                self.err('newline')
                                        else:
                                            self.err('"}"')
                                    else:
                                        self.err('"pag", "kusa"')
                                else:
                                    self.err('"pag"')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('")"')
                else:
                    self.err('"Yunit Literal", "Titik Literal"')
            else:
                self.err('"("') 

    def loop_conditional_continue(self):
        if self.match('kundi'):
            if self.match('('):
                if self.first(condition):
                    self.condition()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.first(loop_content_continue):
                                        self.loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(loop_conditional_continue):
                                                self.loop_conditional_continue()
                                        else:
                                            self.err('"newline"')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"{"')
                    else:
                        self.err('")"')
                elif self.first(cond):
                    self.cond()
                    if self.match(')'):
                        self.newline()
                        if self.match('{'):
                            if self.match('newline'):
                                self.newline()
                                if self.first(loop_body):
                                    self.loop_body()
                                    if self.first(loop_content_continue):
                                        self.loop_content_continue()   
                                    if self.match('}'):
                                        if self.match('newline'):
                                            self.newline()
                                            if self.first(loop_conditional_continue):
                                                self.loop_conditional_continue()
                                        else:
                                            self.err('"newline"')
                                    else:
                                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                                else:
                                    self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                            else:
                                self.err('"newline"') 
                        else:
                            self.err('"{"')
                    else:
                        self.err('"[", "(", "+", "-", "", "/", "%", "*", ">", "<", ">=", "<=", "==", "!=", ")", "at", "o", ")"')
                else:
                    self.err('"di","Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "(", "Totoo", "Peke"')
            else:
                self.err('"("')

    def loop_conditional_end(self):
        if self.match('edi'):
            self.newline()
            if self.match('{'):
                if self.match('newline'):
                    self.newline()
                    if self.first(loop_body):
                        self.loop_body()
                        if self.first(loop_content_continue):
                            self.loop_content_continue()
                        if self.match('}'):
                            if self.match('newline'):
                                self.newline()
                            else:
                                self.err('"newline"')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                    else:
                        self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                else:
                    self.err('"newline"')
            else:
                self.err('"{"')

    def loop_pag_block(self):
        if self.match('pag'):
            if self.first(pag_val):
                self.pag_val()
                self.newline()
                if self.match('{'):
                    if self.match('newline'):
                        self.newline()
                        if self.first(loop_body):
                            self.loop_body()
                            if self.match('}'):
                                if self.match('newline'):
                                    self.newline()
                                    if self.first(loop_pag_continue):
                                        self.loop_pag_continue()
                                else:
                                    self.err('"newline"')
                            else:
                                self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "}"')
                        else:
                            self.err('"yunit", "punto", "baybay", "titik", "bool", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", ')
                    else:
                        self.err('"newline"')
                else:
                    self.err('"{"')
            else:
                self.err('"Yunit Literal", "Titik Literal"')
        
    def loop_pag_continue(self):
        if self.first(loop_pag_block):
            self.loop_pag_block()
        
#------------------------ OTHER FUNCTIONS -------------------------------------
    def next(self):
        self.num += 1
        if self.num < self.max:
            self.current = self.tokens[self.num]['for_syntax']
            self.line = self.tokens[self.num]['rows']
        else:
            self.current = None
        if self.current in ['space', 'Line Comment', 'tab']:
            self.next()

    def newline(self):
        while self.current == 'newline':
            self.next()

    def end(self):
        while self.current != None and self.current != 'newline':
            self.next()
        
    def match(self, token):
        if self.current == token:
            self.next()
            return True
        return False
        
    def first(self, list):
        if self.current in list:
            return True
        return False
    
    def err(self, error_list):
        if self.current == None:
            self.errors.append(f"Syntax Error: on Line {self.line} expecting : {error_list}")
        else:
            self.errors.append(f"Syntax Error on Line {self.line}: Unexpected {self.current}, expecting : {error_list}")
        self.end()
        return
    
