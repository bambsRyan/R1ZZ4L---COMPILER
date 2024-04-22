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
        value[name] = None
        self.variables[d_type].update(value)
        variable[name] = d_type
        self.all_variables.update(variable)

    def newline(self):
        while self.current == 'newline':
            self.semantic()

    def match(self):
        self.newline()
        if self.current == 'g.ssSawa':
            self.semantic()
            self.newline()
        elif self.current == 'yunit':
            self.yunit()
            self.newline()
            self.match()
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
        elif self.current == 'Identifier':
            self.expression()
        elif self.current == 'diks':
            self.diks()
            self.newline()
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
                        y += str(int(eval(self.val)))
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
                        y += str(int(eval(self.val)))
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

    def saYunit(self):
        y = ''
        x = 0
        self.semantic()
        self.semantic()
        if self.current == 'Baybay Literal':
            y  = f' int({self.val[1,-1].replace('~', '-')})'
        elif self.current == 'Titik Literal':
            y = f' int({self.val.replace[1,-1].replace('~', '-')})'
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
                        y += str(float(eval(self.val)))
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
                        y += str(self.saYunit())
                        continue
                    elif self.current == 'Yunit Literal':
                        y += str(float(eval(self.val)))
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
                
    def saPunto(self):
        y = ''
        x = 0
        self.semantic()
        self.semantic()
        if self.current == 'Baybay Literal':
            y  = f' float({self.val[1,-1].replace('~', '-')})'
        elif self.current == 'Titik Literal':
            y = f' float({self.val[1,-1].replace('~', '-')})'
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
            self.declare('baybay', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'Identifier':
                    print(self.current)
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
                        self.titk_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
            
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
                    print(self.current)
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
                print(y)
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
        x = ''
        y = ''
        comparator = False
        if self.val in self.var:
            x = self.all_variables[self.val]
            if x in ['yunit', 'punto', 'baybay', 'titik']:
                self.semantic()
                self.semantic()
                while self.current != 'newline':
                    if self.current == 'Identifier':
                        y = self.Identifier()
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
                    elif self.current in ['<', '>', '==', '!=', '<=', '>=']:
                        comparator = True
                    y += self.val
                    self.semantic()
                if x == 'yunit': 
                    if comparator:
                        self.semantic_error.append(f"TypeError on line {self.line}: unsupported data for {y} : Boolean Value")
                        self.cont = False
                        return
                try:
                    if x == 'yunit':
                        self.variables[x][name] = int((eval(y)))
                    elif x == 'punto':
                        self.variables[x][name] = float(eval(y))    
                    elif x == 'baybay':
                        self.variables[x][name]  = str(eval(y))
                    elif x == 'titik':
                        self.variables[x][name] = str(eval(y))
                except (NameError, SyntaxError, TypeError) as e:
                    self.semantic_error.append(f"NameError on line {self.line}: {e}")
                    self.cont = False
                    return
        else:
            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
            self.cont = False
            return
        self.newline()