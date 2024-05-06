class Semantic:
    def __init__(self, tokens):
        self.token = tokens
        self.val = ''
        self.num = -1
        self.max = len(tokens)
        self.line = 1
        self.all_variables = {}
        self.semantic_error = []
        self.nested_for = {}

    def semantics(self):
        self.semantic()
        self.match()

    def semantic(self):
        self.num += 1
        if self.num < self.max:
            self.current = self.token[self.num]['for_syntax']
            self.val = self.token[self.num]['value']
            self.line = self.token[self.num]['rows']
        else:
            self.current = None
        if self.current in ['space', 'Line Comment', 'tab']:
            self.semantic()
        if self.current == 'newline':
            self.line += 1
        # print(self.current)

    def newline(self):
        while self.current == 'newline':
            self.semantic()

    def match(self):
        while self.current != None and len(self.semantic_error) == 0:
            if self.current == 'yunit':
                self.yunit()
                self.newline()
            elif self.current == 'punto':
                self.punto()
                self.newline()
            elif self.current == 'baybay':
                self.baybay()
                self.newline()
            elif self.current == 'titik':
                self.titik()
                self.newline()
            elif self.current == 'bool':
                self.boolean()
                self.newline()
            elif self.current == 'Identifier':
                self.expression()
                self.newline()
            elif self.current == 'kung':
                self.if_statement()
                self.newline()
            elif self.current == 'kundi':
                self.elif_statement()
                self.newline()
            else:
                self.semantic()
        print(self.all_variables)

    def find(self, token):
        while self.current != token and self.num < self.max:
            self.semantic()

    def jump(self, num):
        ctr = 0
        while ctr != num and self.num < self.max:
            self.semantic()
            ctr += 1

    def declare(self, d_type, name):
        variable = {}
        try:
            x = self.all_variables[name]
            self.semantic_error.append(f'Semantic Error in line {self.line} : {name} is already defined')
        except:
            variable[name] = d_type
            self.all_variables.update(variable)

    def yunit_list(self):
        x = 0
        while self.current != ']':
            if self.current == 'Identifier':
                try: 
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Error: {self.val} is not defined')
                    return
                if x == 'yunit_list' or x == 'yunit' or  x == 'punto_list' or x == 'punto':
                    self.semantic()
                else:
                    self.semantic_error.append(f'Error: {self.val} is not a valid value for Yunit Array')
                    return
            elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                self.semantic()
            elif self.current == 'saPunto' or self.current == 'saYunit':
                self.jump(4)
            elif self.current in ['(', ')', '+', '-', '*','**', '/']:
                self.semantic()
            elif self.current == ',':
                self.semantic()
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Yunit Array')
                return
        self.semantic()

    def yunit(self):
        val = ''
        self.find('Identifier')
        while self.current != 'newline':
            val = self.val
            self.semantic()
            if self.current == '[':
                self.declare('yunit_list', val)
                self.jump(2)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current =='[':
                            self.semantic()
                            self.yunit_list()
                        elif self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'yunit_list':   
                                self.semantic()
                        elif self.current == '+':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for yunit list')
                            return
            else:
                self.declare('yunit', val)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x != 'yunit' and x != 'punto':
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for yunit')
                                return
                            else:
                                self.semantic()
                        elif self.current in ['+', '-', '*', '**', '/','(', ')']:
                            self.semantic()
                        elif self.current == 'saPunto' or self.current == 'saYunit':
                            self.jump(4)
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for yunit')
                            return
            if self.current == ',':
                self.semantic()
        
    def punto_list(self):
        x = 0
        while self.current != ']':
            if self.current == 'Identifier':
                try: 
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Error: {self.val} is not defined')
                    return
                if x == 'yunit_list' or x == 'yunit' or  x == 'punto_list' or x == 'punto':
                    self.semantic()
                else:
                    self.semantic_error.append(f'Error: {self.val} is not a valid value for Punto Array')
                    return
            elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                self.semantic()
            elif self.current == 'saPunto' or self.current == 'saYunit':
                self.jump(4)
            elif self.current in ['(', ')', '+', '-', '*','**', '/']:
                self.semantic()
            elif self.current == ',':
                self.semantic()
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Punto Array')
                return
        self.semantic()

    def punto(self):
        val = ''
        self.find('Identifier')
        while self.current != 'newline':
            val = self.val
            self.semantic()
            if self.current == '[':
                self.declare('punto_list', val)
                self.jump(2)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current =='[':
                            self.semantic()
                            self.punto_list()
                        elif self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'yunit_list':   
                                self.semantic()
                        elif self.current == '+':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Punto Array')
                            return
            else:
                self.declare('punto', val)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x != 'yunit' and x != 'punto':
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Punto')
                                return
                            else:
                                self.semantic()
                        elif self.current in ['+', '-', '*', '**', '/','(', ')']:
                            self.semantic()
                        elif self.current == 'saPunto' or self.current == 'saYunit':
                            self.jump(4)
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Punto')
                            return
            if self.current == ',':
                self.semantic()
    
    def baybay_list(self):
        x = 0
        while self.current != ']':
            if self.current == 'Identifier':
                try: 
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Error: {self.val} is not defined')
                    return
                if x == 'baybay_list' or x == 'baybay':
                    self.semantic()
                else:
                    self.semantic_error.append(f'Error: {self.val} is not a valid value for Baybay Array')
                    return
            elif self.current == 'Baybay Literal':
                self.semantic()
            elif self.current == 'saBaybay':
                self.jump(4)
            elif self.current in ['(', ')', '+']:
                self.semantic()
            elif self.current == ',':
                self.semantic()
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Baybay Array')
                return
        self.semantic()

    def baybay(self):
        val = ''
        self.find('Identifier')
        while self.current != 'newline':
            val = self.val
            self.semantic()
            if self.current == '[':
                self.declare('baybay_list', val)
                self.jump(2)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current =='[':
                            self.semantic()
                            self.baybay_list()
                        elif self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'baybay_list':   
                                self.semantic()
                        elif self.current == '+':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Baybay Array')
                            return
            else:
                self.declare('baybay', val)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x != 'baybay':
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Baybay')
                                return
                            else:
                                self.semantic()
                        elif self.current in ['+', '(', ')']:
                            self.semantic()
                        elif self.current == 'saBaybay':
                            self.jump(4)
                        elif self.current == 'Baybay Literal':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Baybay')
                            return
            if self.current == ',':
                self.semantic()

    def titik_list(self):
        x = 0
        while self.current != ']':
            if self.current == 'Identifier':
                try: 
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Error: {self.val} is not defined')
                    return
                if x == 'titik_list' or x == 'titik':
                    self.semantic()
                else:
                    self.semantic_error.append(f'Error: {self.val} is not a valid value for Titik Array')
                    return
            elif self.current == 'Titik Literal':
                self.semantic()
            elif self.current == 'saTitik':
                self.jump(4)
            elif self.current in ['(', ')', '+']:
                self.semantic()
            elif self.current == ',':
                self.semantic()
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Titik Array')
                return
        self.semantic()

    def titik(self):
        val = ''
        self.find('Identifier')
        while self.current != 'newline':
            val = self.val
            self.semantic()
            if self.current == '[':
                self.declare('titik_list', val)
                self.jump(2)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current =='[':
                            self.semantic()
                            self.titik_list()
                        elif self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'baybay_list':   
                                self.semantic()
                        elif self.current == '+':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Titik Array')
                            return
            else:
                self.declare('titik', val)
                if self.current == '=':
                    self.semantic()
                    while self.current != 'newline' and self.current != ',':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x != 'titik':
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Titik')
                                return
                            else:
                                self.semantic()
                        elif self.current in ['+', '(', ')']:
                            self.semantic()
                        elif self.current == 'saTitik':
                            self.jump(4)
                        elif self.current == 'Titik Literal':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for Titik')
                            return
            if self.current == ',':
                self.semantic()

    def boolean(self):
        val = ''
        x = ''
        self.find('Identifier')
        while self.current != 'newline':
            val = self.val
            self.semantic()
            try :
                x = self.all_variables[val]
                self.semantic_error.append(f'Semantic Error in line {self.line} : {val} is already defined')
            except:
                pass
            self.declare('bool', val)
            if self.current == '=':
                self.semantic()
                self.truth(['newline', ','])

    def truth(self):
        x = ''
        iscop = 0
        while self.current != 'newline':
            if self.current == 'Identifier':
                try:
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                    return
                if x == 'bool':
                    self.semantic()
                    if self.current in ['<', '>', '>=', '<=', '+', '-', '*', '%', '**', '/']:
                        self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid comparison to a boolean value')
                        return
                    else:
                        self.semantic()
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'bool':
                                self.semantic()
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for boolean')
                                return
                        elif self.current in ['Totoo', 'Peke']:
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for boolean')
                            return
                else:
                    if x == 'yunit' or x == 'punto':
                        iscop = 0
                        while self.current not in lst and self.current not in ['o', 'at']:
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'yunit' or x == 'punto':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for boolean')
                                    return
                            elif self.current in [ '>', '<', '!=' ,'==', '>=', '<=']:
                                self.semantic()
                                iscop += 1
                            elif self.current in ['+', '-', '*', '%', '**', '/',]:
                                self.semantic()
                            elif self.current == '(':
                                paren += 1
                                self.semantic()
                            elif self.current == ')':
                                paren -= 1
                                self.semantic()
                            elif self.current == 'saPunto' or self.current == 'saYunit':
                                self.jump(4)
                            elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                                self.semantic()
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for boolean')
                                return
                        if iscop != 1:  
                            self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                            return
                    elif x == 'baybay':
                        iscop = 0
                        while self.current not in lst and self.current not in ['o', 'at']:
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'baybay':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                                    return
                            elif self.current in [ '!=', '==']:
                                self.semantic()
                                iscop += 1
                            elif self.current in ['(', ')']:
                                self.semantic()
                            elif self.current == 'saBaybay':
                                self.jump(4)
                            elif self.current == 'Baybay Literal':
                                self.semantic()
                            else:
                                if self.current in [ '<', '>', '>=', '<=', '-', '*','%' ,'**', '/']:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operator for baybay')
                                    return
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                                return
                        if iscop != 1:  
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid expression for boolean')
                            return
                    elif x == 'titik':
                        iscop = False
                        while self.current not in lst and self.current not in ['o', 'at']:
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'titik':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                                    return
                            elif self.current in [ '!=', '==']:
                                self.semantic()
                                iscop = True
                            elif self.current in ['(', ')']:
                                self.semantic()
                            elif self.current == 'saTitik':
                                self.jump(4)
                            elif self.current == 'Titik Literal':
                                self.semantic()
                            else:
                                if self.current in [ '<', '>', '>=', '<=', '-', '*', '%' ,'**', '/']:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operator for titik')
                                    return
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                                return
                        if iscop == False:  
                            self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                            return
                    elif x == 'yunit_list':
                        iscop = False
                        while self.current != 'newline':
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'yunit_list':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a yunit list')
                                    return
                            elif self.current == '+':
                                self.semantic()
                            elif self.current == '[':
                                self.semantic()
                                self.yunit_list()
                            elif self.current in ['==', '!=']:
                                self.semantic()
                                iscop = True
                            elif self.current == 'newline':
                                break
                            elif self.current == ')':
                                self.semantic() 
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for yunit list')
                                return
                        if iscop == False:
                            self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                            return
                    elif x == 'punto_list':
                        iscop = False
                        while self.current != 'newline':
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'punto_list':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a punto list')
                                    return
                            elif self.current == '+':
                                self.semantic()
                            elif self.current == '[':
                                self.semantic()
                                self.punto_list()
                            elif self.current in ['==', '!=']:
                                self.semantic()
                                iscop = True
                            elif self.current == 'newline':
                                break
                            elif self.current == ')':
                                self.semantic() 
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for punto list')
                                return
                        if iscop == False:
                            self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                            return
                    elif x == 'baybay_list':
                        iscop = False
                        while self.current != 'newline':
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'baybay_list':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a baybay list')
                                    return
                            elif self.current == '+':
                                self.semantic()
                            elif self.current == '[':
                                self.semantic()
                                self.baybay_list()
                            elif self.current in ['==', '!=']:
                                self.semantic()
                                iscop = True
                            elif self.current == 'newline':
                                break
                            elif self.current == ')':
                                self.semantic() 
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for baybay list')
                                return
                        if iscop == False:
                            self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                            return
                    elif x == 'titik_list':
                        iscop = False
                        while self.current != 'newline':
                            if self.current == 'Identifier':
                                try:
                                    x = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                    return
                                if x == 'titik_list':
                                    self.semantic()
                                else:
                                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a titik list')
                                    return
                            elif self.current == '+':
                                self.semantic()
                            elif self.current == '[':
                                self.semantic()
                                self.titik_list()
                            elif self.current in ['==', '!=']:
                                self.semantic()
                                iscop = True
                            elif self.current == 'newline':
                                break
                            elif self.current == ')':
                                self.semantic() 
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for titik list')
                                return
                        if iscop == False:
                            self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                            return   
            elif self.current == 'Baybay Literal' or self.current == 'saBaybay':
                iscop = 0
                while self.current not in lst and self.current not in ['o', 'at']:
                    if self.current == 'Identifier':
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f'Semantic Error: {self.val} is not defined1')
                            return
                        if x == 'baybay':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                            return
                    elif self.current in ['+', '(', ')']:
                        self.semantic()
                    elif self.current in ['!=', '==']:
                        self.semantic()
                        iscop += 1
                    elif self.current == 'saBaybay':
                        self.jump(4)
                    elif self.current == 'Baybay Literal':
                        self.semantic()
                    else:
                        if self.current in [ '<', '>', '>=', '<=', '-', '*','%' ,'**', '/']:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operator for baybay')
                            return
                        self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                        return 
                if iscop != 1:  
                    self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                    return
            elif self.current == 'Titik Literal' or self.current == 'saTitik':  
                iscop = 0
                while self.current not in lst and self.current not in ['o', 'at']:
                    if self.current == 'Identifier':
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                            return
                        if x == 'titik':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                            return
                    elif self.current in ['(', ')']:
                        self.semantic()
                    elif self.current in ['!=', '==',]:
                        self.semantic()
                        iscop += 1
                    elif self.current == 'saTitik':
                        self.jump(4)
                    elif self.current == 'Titik Literal':
                        self.semantic()
                    else:
                        if self.current in [ '<', '>', '>=', '<=', '+', '-', '*', '%', '**', '/']:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operator for titik')
                            return
                        self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operand')
                        return
                if iscop != 0:
                    self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                    return
            elif self.current == 'Yunit Literal' or self.current == 'saYunit' or self.current == 'Punto Literal' or self.current == 'saPunto':
                iscop = 0
                while self.current not in lst and self.current not in ['o', 'at']:
                    if self.current == 'Identifier':
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                            return
                        if x == 'yunit' or x == 'punto':
                            self.semantic()
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for boolean')
                            return
                    elif self.current in [ '>', '<', '!=' ,'==', '>=', '<=']:
                        self.semantic()
                        iscop += 1
                    elif self.current in ['+', '-', '*', '**', '/', '(', ')']:
                        y+= self.current
                        self.semantic()
                    elif self.current == 'saPunto' or self.current == 'saYunit':
                        self.jump(4)
                    elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                        self.semantic()
                    else:
                        self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for titik')
                        return
                if iscop != 1:  
                    self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                    return
            elif self.current == '(':
                self.semantic()
            elif self.current in ['at', 'o']:
                self.semantic()
            elif self.current in ['Totoo', 'Peke']:
                self.semantic()
            elif self.current == ')':   
                self.semantic()
            elif self.current == '[':
                self.semantic()
                if self.current == ']':
                    self.semantic()
                elif self.current == 'Yunit Literal':
                    iscop = False
                    self.yunit_list()
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'yunit_list':
                                self.semantic()
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a yunit list')
                                return
                        elif self.current == '+':
                            self.semantic()
                        elif self.current == '[':
                            self.semantic()
                            self.yunit_list()
                        elif self.current in ['==', '!=']:
                            self.semantic()
                            iscop = True
                        elif self.current == 'newline':
                            break
                        elif self.current == ')':
                            self.semantic() 
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for yunit list')
                            return
                    if iscop == False:
                        self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                        return
                elif self.current == 'Punto Literal':
                    iscop = False
                    self.punto_list()
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'punto_list':
                                self.semantic()
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a punto list')
                                return
                        elif self.current == '+':
                            self.semantic()
                        elif self.current == '[':
                            self.semantic()
                            self.punto_list()
                        elif self.current in ['==', '!=']:
                            self.semantic()
                            iscop = True
                        elif self.current == 'newline':
                            break
                        elif self.current == ')':
                            self.semantic() 
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for punto list')
                            return
                    if iscop == False:
                        self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                        return
                elif self.current == 'Baybay Literal':
                    iscop = False
                    self.baybay_list()
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'baybay_list':
                                self.semantic()
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a baybay list')
                                return
                        elif self.current == '+':
                            self.semantic()
                        elif self.current == '[':
                            self.semantic()
                            self.baybay_list()
                        elif self.current in ['==', '!=']:
                            self.semantic()
                            iscop = True
                        elif self.current == 'newline':
                            break
                        elif self.current == ')':
                            self.semantic() 
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for baybay list')
                            return
                    if iscop == False:
                        self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                        return
                elif self.current == 'Titik Literal':
                    iscop = False
                    self.titik_list()
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            try:
                                x = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                                return
                            if x == 'titik_list':
                                self.semantic()
                            else:
                                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a titik list')
                                return
                        elif self.current == '+':
                            self.semantic()
                        elif self.current == '[':
                            self.semantic()
                            self.titik_list()
                        elif self.current in ['==', '!=']:
                            self.semantic()
                            iscop = True
                        elif self.current == 'newline':
                            break
                        elif self.current == ')':
                            self.semantic() 
                        else:
                            self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid conditional operator for titik list')
                            return
                    if iscop == False:
                        self.semantic_error.append(f'Semantic Error in line {self.line-1} :  Not a valid expression for boolean')
                        return   
            else: 
                self.semantic_error.append(f'Semantic Error in line {self.line}: {self.val} is not a valid value for boolean')
                return

    def yunit_lit(self):
        while self.current != ')' and self.current != 'newline':
            if self.current == 'Identifier':
                try:
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                    return
                if x != 'yunit' and x != 'punto':
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for yunit')
                    return
                else:
                    self.semantic()
            elif self.current in ['+', '-', '*', '**', '/']:
                self.semantic()
            elif self.current == '(':
                self.semantic()
                self.yunit_lit()
            elif self.current == 'saPunto' or self.current == 'saYunit':
                self.jump(4)
            elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                self.semantic()
            else:
                if self.current in ['o', 'at', '<', '>', '==', '>=', '<=']:
                    self.semantic_error.append(f'Semantic Error in line {self.line}: {self.val} is not a valid operator for yunit')
                    return 
                else:
                    self.semantic_error.append(f'Semantic Error in line {self.line}: {self.val} is not a valid value for yunit')
                    return
        if self.current == ')':
            self.semantic()

    def punto_lit(self):
        while self.current != ')' and self.current != 'newline':
            if self.current == 'Identifier':
                try:
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                    return
                if x != 'yunit' and x != 'punto':
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for punto')
                    return
                else:
                    self.semantic()
            elif self.current in ['+', '-', '*', '**', '/']:
                self.semantic()
            elif self.current == '(':
                self.semantic()
                self.punto_lit()
            elif self.current == 'saPunto' or self.current == 'saYunit':
                self.jump(4)
            elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                self.semantic()
            else:
                if self.current in ['o', 'at', '<', '>', '==', '>=', '<=']:
                    self.semantic_error.append(f'Semantic Error in line {self.line}: {self.val} is not a valid operator for punto')
                    return 
                else:
                    self.semantic_error.append(f'Semantic Error in line {self.line}: {self.val} is not a valid value for punto')
                    return
        if self.current == ')':
            self.semantic()

    def baybay_lit(self):
        while self.current != 'newline':
            if self.current == 'Identifier':
                try:
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                    return
                if x != 'baybay':
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for baybay')
                    return
                else:
                    self.semantic()
            elif self.current in ['+']:
                self.semantic()
            elif self.current == 'saBaybay':
                self.jump(4)
            elif self.current == 'Baybay Literal':
                self.semantic()
            elif self.current == '(':
                self.semantic()
                self.baybay_lit()
            else:
                if self.current in ['o', 'at', '<', '>', '==', '>=', '<=']:
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operator for baybay')
                    return 
                else:
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for baybay')
                    return

    def titik_lit(self):
        while self.current != 'newline':
            if self.current == 'Identifier':
                try:
                    x = self.all_variables[self.val]
                except:
                    self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                    return
                if x != 'titik':
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for titik')
                    return
                else:
                    self.semantic()
            elif self.current in ['+']:
                self.semantic()
            elif self.current == 'saTitik':
                self.jump(4)
            elif self.current == 'Titik Literal':
                self.semantic()
            else:
                if self.current in ['o', 'at', '<', '>', '==', '>=', '<=']:
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid operator for titik')
                    return 
                else:
                    self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for titik') 
                    return

    def expression(self):
        x = self.val
        paren = 0
        y =''
        try:
            y = self.all_variables[self.val]
        except:
            self.semantic_error.append(f'Error: {self.val} is not defined')
            return
        if y == 'yunit':
            self.jump(2) 
            self.yunit_lit()
            print(self.current)
        elif y == 'punto':
            self.jump(2)
            self.punto_lit()
        elif y == 'baybay':
            self.semantic()
            if self.current in ['=', '+=']:
                self.semantic()
                self.baybay_lit()
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid assignment operator for baybay')
        elif y == 'titik':
            self.semantic()
            if self.current == '=':
                self.semantic()
                self.titik_lit()
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid assignment operator for titik')
        elif y == 'bool':
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current == '(':
                    self.semantic()
                self.truth(['newline', ','])
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid assignment operator for boolean')
        elif y == 'yunit_list':
            self.semantic()
            if self.current == '=' or self.current == '+=':
                self.semantic()
                while self.current == '(':
                    self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current =='[':
                        self.semantic()
                        self.yunit_list()
                    elif self.current == 'Identifier':
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                            return
                        if x == 'yunit_list':
                            self.semantic()
                    elif self.current == '+':
                        self.semantic()
                    elif self.current in ['(', ')']:
                        self.semantic()
                    else:
                        self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid value for yunit list')
                        return
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line} : {self.val} is not a valid assignment operator for yunit list')
        elif y == 'punto_list':
            self.semantic()
            if self.current == '=' or self.current == '+=':
                self.semantic()
                while self.current == '(':
                    self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current =='[':
                        self.semantic()
                        self.punto_list()
                    elif self.current == 'Identifier':
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                            return
                        if x == 'punto_list':
                            self.semantic()
                    elif self.current == '+':
                        self.semantic()
                    elif self.current in ['(', ')']:
                        self.semantic()
                    else:
                        self.semantic_error.append(f'Semantic Error in line {self.line}:{self.val} is not a valid value for punto list')
                        return
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line}:{self.val} is not a valid assignment operator for punto list')
        elif y == 'baybay_list':
            self.semantic()
            while self.current == '(':
                    self.semantic()
            if self.current == '=' or self.current == '+=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current =='[':
                        self.semantic()
                        self.baybay_list()
                    elif self.current == 'Identifier':
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f'Semantic Error: {self.val} is not defined')
                            return
                        if x == 'baybay_list':
                            self.semantic()
                    elif self.current == '+':
                        self.semantic()
                    elif self.current in ['(', ')']:
                        self.semantic()
                    else:
                        self.semantic_error.append(f'Semantic Error in line {self.line}:{self.val} is not a valid value for baybay list')
                        return
            else:
                self.semantic_error.append(f'Semantic Error in line {self.line}:{self.val} is not a valid assignment operator for baybay list')
    
    def if_statement(self):
        self.jump(2)
        self.truth(['newline', ')'])
        print(self.current, self.val)

