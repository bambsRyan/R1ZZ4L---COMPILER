class Compilation:
    def __init__(self, x):
        self.token = x
        self.val = ''
        self.num = -1
        self.max = len(x)
        self.line = 1
        self.variables= {'yunit':{}, 'punto':{}, 'baybay':{}, 'titik':{}, 'bool':{}, 'tala':{}, 'diks':{}} 
        self.all_variables = {}
        self.var = []
        self.semantic_error = []
        self.cont = True

    def sem(self):
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
        if self.current in ['space', 'Line Comment']:
            self.semantic()

    def declare(self, d_type, name):
        variable = {}
        value = {}
        if d_type == 'yunit':
            value[name] = 0
        elif d_type == 'punto':
            value[name] = 0.0
        elif d_type == 'baybay' or d_type == 'titik':
            value[name] = ''
        elif d_type == 'tala':
            value[name] = []
        elif d_type == 'diks':
            value[name] = {}
        elif d_type == 'bool':
            value[name] = True
        self.variables[d_type].update(value)
        variable[name] = d_type
        self.all_variables.update(variable)

    def newline(self):
        while self.current == 'newline':
            self.semantic()

    def match(self):
        while self.cont and self.current != None:
            self.newline()
            if self.current == 'g.ssSawa':
                self.semantic()
                self.newline()
            elif self.current == 'yunit':
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
            elif self.current == 'tala':
                self.tala()
                self.newline()
            elif self.current == 'bool':
                self.boolean()
                self.newline()
            elif self.current == 'Identifier':
                self.expression()
                self.newline()
            elif self.current == 'sulat':
                self.sulat()
                self.newline()
            elif self.current == 'diks':
                self.diks()
                self.newline()
            elif self.current == 'kung':
                self.kung()
            elif self.current == 'gg.ssSawa':
                self.semantic()
                self.newline()

    def Identifier(self):
        name = self.val
        z = ''
        x = ''
        try:
            x = self.all_variables[self.val]
            z = 'self.variables[x][name]'
        except (KeyError, NameError, SyntaxError, TypeError) as e :
            self.semantic_error.append(f"NameError on line {self.line}: Variable '{self.val}' is not defined")
            self.y = None
            self.cont = False 
            return
        if x not in  ['tala', 'diks']:
            self.semantic()
            if self.current =='[':
                self.semantic_error(f"TypeError on line {self.line}: {name} is not subscriptable")
                self.cont = False
                return
            return self.variables[x][name]
        else: 
            self.semantic()
            while self.current not in ['+', '-', '*', '/', '%', '**','newline',',', ')']:
                if self.current == 'Identifier':
                    x = self.Identifier()
                    z += str(x)
                    continue
                z += self.val
                self.semantic()
        try:
            return eval(z)
        except (IndexError) as e:
            self.semantic_error.append(f"IndexError on ine {self.line}: {e}")
            self.cont = False
        except (TypeError) as e:
            self.semantic_error.append(f"TypeError on line {self.line}: {str(e).replace('int', 'yunit').replace('float', 'punto')}")
            self.cont = False
            return

    def yunit(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('yunit', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.val
                        holder = self.Identifier()
                        if self.cont == False:
                            return
                        if type(holder) != int and type(holder) != float:
                            self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Yunit Litaral")
                            self.cont = False
                            return
                        if type(holder) == float:
                            holder = int(holder)
                        else:
                            holder = holder
                        y += str(holder)
                        continue
                    elif self.current == 'saYunit':
                        y += str(self.saYunit())
                        continue
                    elif self.current == 'Punto Literal':
                        y += str(int(eval(self.val.replace('~', '-'))))
                    elif self.current == 'Yunit Literal':
                        y += str(eval(self.val.replace('~', '-')))
                    else:
                        y += self.val
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['yunit'][s_name] = eval(y)
                    if self.current == ',':
                        self.yunit_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.yunit_continue()
        
    def yunit_continue(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('yunit', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.val
                        holder = self.Identifier()
                        if self.cont == False:
                            return
                        if type(holder) != int and type(holder) != float:
                            self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Yunit Litaral")
                            self.cont = False
                            return
                        if type(holder) == float:
                            holder = int(holder)
                        else:
                            holder = holder
                        y += str(holder)
                        continue
                    elif self.current == 'saYunit':
                        y += str(self.saYunit())
                        continue
                    elif self.current == 'Punto Literal':
                        y += str(int(eval(self.val.replace('~', '-'))))
                    elif self.current == 'Yunit Literal':
                        y += str(eval(self.val.replace('~', '-')))
                    else:
                        y += self.val
                    self.semantic()
                if self.cont == False:
                    return

                try:
                    self.variables['yunit'][s_name] = eval(y)
                    if self.current == ',':
                        self.yunit_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.yunit_continue()

    def saYunit(self):
        y = ''
        x = 0
        self.semantic()
        self.semantic()
        if self.current == 'Baybay Literal':
            y  = f' int({self.val[1:-1].replace('~', '-')})'
        elif self.current == 'Titik Literal':
            y = f' int({self.val.replace[1:-1].replace('~', '-')})'
        elif self.current == 'Identifier':
            y = f' int({self.Identifier()})'
        else:
            y = f' int({self.val.replace('~', '-')})'
        try:
            self.semantic()
            return eval(y)
        except:
            self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Yunit() with base 10: \"{self.current}\"")
            self.cont = False
            x = 0

    def punto(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('punto', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.val
                        holder = self.Identifier()
                        if self.cont == False:
                            return
                        if type(holder) != float and type(holder) != int:
                            self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Punto Litaral")
                            self.cont = False
                            return
                        if type(holder) == int:
                            holder = float(holder)
                        else:
                            holder = holder
                        y += str(holder)
                        continue
                    elif self.current == 'saPunto':
                        y += str(self.saPunto())
                        continue
                    elif self.current == 'Yunit Literal':
                        y += str(float(eval(self.val.replace('~','-'))))
                    elif self.current == 'Punto Literal':
                        y += str(eval(self.val.replace('~','-')))
                    else:   
                        y += self.val
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['punto'][s_name] = eval(y)
                    if self.current == ',':
                        self.punto_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.punto_continue()

    def punto_continue(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('punto', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.val
                        holder = self.Identifier()
                        if self.cont == False:
                            return
                        if type(holder) != float and type(holder) != int:
                            self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Punto Litaral")
                            self.cont = False
                            return
                        if type(holder) == int:
                            holder = float(holder)
                        else:
                            holder = holder
                        y += str(holder)
                        continue
                    elif self.current == 'saPunto':
                        y += str(self.saPunto())
                        continue
                    elif self.current == 'Yunit Literal':
                        y += str(float(eval(self.val.replace('~','-'))))
                    elif self.current == 'Punto Literal':
                        y += str(eval(self.val.replace('~','-')))
                    else:   
                        y += self.val
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['punto'][s_name] = eval(y)
                    if self.current == ',':
                        self.punto_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.punto_continue()
                
    def saPunto(self):
        y = ''
        x = 0
        self.semantic()
        self.semantic()
        if self.current == 'Baybay Literal':
            y  = f' float({self.val[1:-1].replace('~', '-')})'
        elif self.current == 'Titik Literal':
            y = f' float({self.val[1:-1].replace('~', '-')})'
        elif self.current == 'Identifier':
            y = f' float({self.Identifier()})'
        else:
            y = f' float({self.val.replace('~', '-')})'
        try:
            self.semantic()
            return eval(y)
        except:
            self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Punto() with base 10: \"{self.current}\"")
            self.cont = False
            x = 0

    def baybay(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('baybay', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.val
                        holder = self.Identifier()
                        if self.cont == False:
                            return
                        if type(holder) != str:
                            self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Baybay Litaral")
                            self.cont = False
                            return
                        y += f'\'{str(holder)}\''
                        continue
                    elif self.current == 'saBaybay':
                        y += str(self.saBaybay())
                        continue
                    else:   
                        y += self.val
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['baybay'][s_name] = eval(y)
                    if self.current == ',':
                        self.baybay_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.baybay_continue()
    
    def baybay_continue(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('baybay', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.val
                        holder = self.Identifier()
                        if self.cont == False:
                            return
                        if type(holder) != str:
                            self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Baybay Litaral")
                            self.cont = False
                            return
                        y += f'\'{str(holder)}\''
                        continue
                    elif self.current == 'saBaybay':
                        y += str(self.saBaybay())
                        continue
                    else:   
                        y += self.val
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['baybay'][s_name] = eval(y)
                    if self.current == ',':
                        self.baybay_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.baybay_continue()
        
    def saBaybay(self):
        y = ''
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            y = f' str({self.Identifier()})'
        else:
            y  = f'str({self.val})'
        try:
            self.semantic()
            return f'\"{eval(y)}\"'
        except:
            self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
            self.cont = False

    def titik(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('titik', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'Identifier':
                    z = self.val
                    holder = self.Identifier()
                    if self.cont == False:
                        return
                    if type(holder) != str and len(holder) != 1:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Litaral")
                        self.cont = False
                        return
                    y += f'\'{str(holder)}\''
                elif self.current == 'saTitik':
                    y += str(self.saTitik())
                    if len(y) != 1:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Litaral")
                        self.cont = False
                else:   
                    y += self.val
                self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['titik'][s_name] = eval(y)
                    if self.current == ',':
                        self.titik_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.titik_continue()
            
    def titik_continue(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('baybay', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'Identifier':
                    z = self.val
                    holder = self.Identifier()
                    if self.cont == False:
                        return
                    if type(holder) != str and len(holder) != 1:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Litaral")
                        self.cont = False
                        return
                    y += f'\'{str(holder)}\''
                elif self.current == 'saTitik':
                    y += str(self.saTitik())
                    if len(y) != 1:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Litaral")
                        self.cont = False
                else:   
                    y += self.val
                self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['titik'][s_name] = eval(y)
                    if self.current == ',':
                        self.titik_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return

    def saTitik(self):
        y = ''
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            y = f' str({self.Identifier()})'
        else:
            y  = f'str({self.val})'
        try:
            self.semantic()
            return f'\"{eval(y)}\"'
        except:
            self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Titik() : \"{self.current}\"")
            self.cont = False
        
    def tala(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('tala', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                y += '['
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    while self.current != ']':
                        if self.current == 'Identifier':
                            holder = self.Identifier()
                            if self.cont == False:
                                return
                            if type(holder) == str:
                                holder = f'\'{holder}\''
                            else:
                                holder = holder
                            y += str(holder)
                            continue
                        elif self.current == 'saBaybay':
                            y += str(self.saBaybay())
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                        elif self.current == 'saTitik':
                            y += str(self.saTitik())
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == '[':
                            y += str(self.tala_sub())
                            continue
                        else:
                            y += self.val
                        self.semantic()
                    y += ']'
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['tala'][s_name] = eval(y)
                    if self.current == ',':
                        self.tala_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.tala_continue()
                
    def tala_continue(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('tala', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                y += '['
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    while self.current != ']':
                        if self.current == 'Identifier':
                            holder = self.Identifier()
                            if self.cont == False:
                                return
                            if type(holder) == str:
                                holder = f'\'{holder}\''
                            else:
                                holder = holder
                            y += str(holder)
                            continue
                        elif self.current == 'saBaybay':
                            y += str(self.saBaybay())
                            continue
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                            continue
                        elif self.current == 'saTitik':
                            y += str(self.saTitik())
                            continue
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                            continue
                        elif self.current == 'Titik Literal' or self.current == 'Baybay Literal':
                            y += f'\'{self.val}\''
                        else:
                            y += self.val
                        self.semantic()
                    y += ']'
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['tala'][s_name] = eval(y)
                    if self.current == ',':
                        self.tala_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.tala_continue()

    def tala_sub(self):
        y = '['
        self.semantic()
        while self.current != ']':
            if self.current == '[':
                y += self.tala_sub()
                continue
            y += self.val
            self.semantic()
        y += ']'
        self.semantic()
        return y
    
    def expression(self):
        name = self.val
        x = self.all_variables[name]
        y = ''
        z = ''
        baybay_val= ''
        num_val = 0
        if x == 'baybay': 
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    baybay_val = input(x[1:-1])
                    self.variables['baybay'][name] = baybay_val 
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'baybay':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'saBaybay':
                            y += str(self.saBaybay())
                        elif self.current == 'Baybay Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current in ['+', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            if self.current in ['-', '*', '**','/', '%' ]:
                                self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                            else:
                                self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Baybay variable')
                            self.cont = False
                            return
                    self.variables['baybay'][name] = eval(y)
                    return
            elif self.current == '+=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    baybay_val = input(x[1:-1])
                    self.variables['baybay'][name] = baybay_val 
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'baybay':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'saBaybay':
                            y += str(self.saBaybay())
                        elif self.current == 'Baybay Literal':
                            y += str(self.val)
                        elif self.current in ['+', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            if self.current in ['-', '*', '**','/', '%' ]:
                                self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                            else:
                                self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Baybay variable')
                            self.cont = False
                            return
                    self.variables['baybay'][name] += eval(y)
                    return
            else:
                self.semantic_error.append(f'TypeError on line {self.line}: Invalid Assignment operator on baybay variable')
        elif x == 'yunit':
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = input(x[1:-1])
                        if num_val.find('.') == -1:
                            num_val = int(num_val)
                        else:
                            num_val = float(num_val)
                            num_val = int(num_val)
                    except TypeError:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Yunit variable')
                    self.variables['yunit'][name] = num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Yunit Variable variable1')
                            self.cont = False
                            return
                    self.variables['yunit'][name] = int(eval(y))
                    self.newline()
                    return
            elif self.current == '+=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = input(x[1:-1])
                        if num_val.find('.') == -1:
                            num_val = int(num_val)
                        else:
                            num_val = float(num_val)
                            num_val = int(num_val)
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Yunit variable')
                    self.variables['yunit'][name] += num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Yunit Variable variable')
                            self.cont = False
                            return
                    self.variables['yunit'][name] += int(eval(y))
                    self.newline()
                    return
            elif self.current == '-=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = input(x[1:-1])
                        if num_val.find('.') == -1:
                            num_val = int(num_val)
                        else:
                            num_val = float(num_val)
                            num_val = int(num_val)
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Yunit variable')
                    self.variables['yunit'][name] -= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                while self.current != 'newline':
                    if self.current == 'Identifier':
                        z = self.all_variables[self.val]
                        if z == 'yunit' or self.current == 'punto':
                            y += str(self.Identifier())
                        else:
                            self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                        continue
                    elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                        y += str(self.val)
                    elif self.current == 'saYunit':
                        y += str(self.saYunit())
                    elif self.current == 'saPunto':
                        y += str(self.punto())
                    elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                        y += self.current
                        self.semantic()
                    else:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Yunit Variable variable')
                        self.cont = False
                        return
                self.variables['yunit'][name] -= int(eval(y))
                self.newline()
                return
            elif self.current == '*=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = input(x[1:-1])
                        if num_val.find('.') == -1:
                            num_val = int(num_val)
                        else:
                            num_val = float(num_val)
                            num_val = int(num_val)
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Yunit variable')
                    self.variables['yunit'][name] = num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Yunit Variable variable')
                            self.cont = False
                            return
                    self.variables['yunit'][name] *= int(eval(y))
                    self.newline()
                    return
            elif self.current == '/=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = int(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Yunit variable')
                    self.variables['yunit'][name] /= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Yunit Variable variable')
                            self.cont = False
                            return
                    self.variables['yunit'][name] *= int(eval(y))
                    self.newline()
                    return   
        elif x == 'punto':
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = float(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Punto variable')
                    self.variables['punto'][name] = num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto Variable variable')
                            self.cont = False
                            return
                    self.variables['punto'][name] = float(eval(y))
                    self.newline()
                    return
            elif self.current == '+=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = float(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Punto variable')
                    self.variables['punto'][name] += num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto Variable variable')
                            self.cont = False
                            return
                    self.variables['punto'][name] += float(eval(y))
                    self.newline()
                    return
            elif self.current == '-=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = float(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Punto variable')
                    self.variables['punto'][name] -= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto Variable variable')
                            self.cont = False
                            return
                    self.variables['punto'][name] -= float(eval(y))
                    self.newline()
                    return
            elif self.current == '*=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = float(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Punto variable')
                    self.variables['punto'][name] *= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto Variable variable')
                            self.cont = False
                            return
                    self.variables['punto'][name] *= float(eval(y))
                    self.newline()
                    return
            elif self.current == '/=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = float(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append('TypeError on Line {self.line}: Invalid input for Punto variable')
                    self.variables['punto'][name] /= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            z = self.all_variables[self.val]
                            if z == 'yunit' or self.current == 'punto':
                                y += str(self.Identifier())
                            else:
                                self.semantic_error(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.punto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto Variable variable')
                            self.cont = False
                            return
                    self.variables['punto'][name] *= float(eval(y))
                    self.newline()
                    return   
        else:
            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
            self.cont = False
            return
        self.newline()

    def sulat(self):
        x = ''
        y = ''
        z = ''
        a = ''
        titik_ctr = False
        self.semantic()
        self.semantic()
        while self.current != ')':  # sulat('a',x , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            while self.current != ',' and self.current != ')':
                if self.current == 'Identifier':
                    x = ''
                    a = self.all_variables[self.val]
                    if a == 'Titik Literal':
                        titik_ctr = True
                    elif a == 'Baybay Literal':
                        a = self.val[1:-1]
                    x += str(self.Identifier())
                    if not self.cont:
                        return
                    if x == '':
                        y += f'\'\''
                    y += x
                    continue
                elif self.current == 'saBaybay':
                    y += str(self.saBaybay())
                    continue
                elif self.current == 'saPunto':
                    y += str(self.saPunto())
                    continue
                elif self.current == 'saTitik':
                    y += str(self.saTitik())
                    titik_ctr = True
                    continue
                elif self.current == 'saYunit':
                    y += str(self.saYunit())
                    continue
                elif self.current == ';':
                    y += ':'
                elif self.current == 'Titik Literal':
                    titik_ctr = True
                elif self.current == 'Yunit Literal':
                    y += str(self.val.replace('~', '-'))
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(self.val.replace('~', '-'))
                    self.semantic()
                    continue
                elif self.current in ['+','-','*','**', '/','%']:
                    if titik_ctr == True: 
                        self.semantic_error.append(f"TypeError on Line {self.line}: Invalid operators for Titik Literal")
                        self.cont = False
                        return
                    else:
                        y += str(self.current)
                        self.semantic()
                        continue
                y += str(self.val)
                self.semantic()
            titik_ctr = False
            if self.current == ',':
                self.semantic() 
            z += str(eval(y))
            y = ''
        print(z)
        self.semantic()
        self.newline()

    def boolean(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        isBool = False
        self.semantic()
        self.semantic()
        s_name = self.val
        if s_name in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
            self.cont = False
            return
        else:
            self.var.append(s_name)
            self.declare('bool', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    if self.current == 'Identifier':
                        z = self.Identifier()
                        if self.cont == False:
                            return  
                        if type(z) == bool:
                            y += str(z)+ ' '
                            isBool = True
                        elif type(z) == str:
                            y += z[1:-1]+ ' '
                            isBool = False
                        else:
                            y += str(z)+ ' '
                            isBool = False
                        continue
                    elif self.current == 'Totoo':
                        y += 'True'+ ' '
                        isBool = True
                    elif self.current == 'Peke':
                        y += 'False'+ ' '
                        isBool = True
                    elif self.current == 'saBaybay':
                        y += str(self.saBaybay())+ ' '
                        isBool = False
                        continue
                    elif self.current == 'saPunto':
                        y += str(self.saPunto())+ ' '
                        isBool = False
                        continue
                    elif self.current == 'saTitik':
                        y += str(self.saTitik()) + ' '
                        isBool = False
                        continue
                    elif self.current == 'saYunit':
                        y += str(self.saYunit()) + ' '
                        isBool = False
                        continue
                    elif self.current == 'Baybay Literal' or self.current == 'Titik Literal':
                        y += str(self.val[1:-1]) + ' '
                        isBool = False
                    elif self.current == 'at':
                        y += 'and' + ' '
                        isBool = False
                    elif self.current == 'o':
                        y += 'and' + ' '
                        isBool = False
                    else:
                        y += self.val + ' '
                        isBool = False
                    self.semantic()
                if self.cont == False:
                    return
                try:
                    self.variables['bool'][s_name] = eval(y)
                    if self.current == ',':
                        self.bool_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            elif self.current == ',':
                self.bool_continue()    