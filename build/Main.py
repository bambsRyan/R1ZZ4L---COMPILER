from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, PanedWindow, Frame
import tkinter as tk
import tkinter.ttk as ttk
import Lexer as lx
import Syntax as syn
import os 
import sys
import Semantic as sem
from time import perf_counter

OUTPUT_PATH = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "frame0")
button = False
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1870x990")
window.title("R1ZZ4L")
window.configure(bg="#FFFFFF")

canvas = Canvas(window,bg="#FFFFFF", height=990, width=1870, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)


class Compilation:
    def __init__(self, x):
        self.token = x
        self.val = ''
        self.num = -1
        self.max = len(x)
        self.line = 1
        self.variables= {'yunit':{}, 'punto':{}, 'baybay':{}, 'titik':{}, 'bool':{}, 'yunit_list':{}, 'punto_list':{}, 'baybay_list':{}, 'titik_list':{}, 'bool_list':{}}
        self.functions = {}
        self.all_variables = {}
        self.variables_for_function = {'yunit':{}, 'punto':{}, 'baybay':{}, 'titik':{}, 'bool':{}, 'yunit_list':{}, 'punto_list':{}, 'baybay_list':{}, 'titik_list':{}, 'bool_list':{}}
        self.func_variables = {}
        self.func_var = []
        self.var = []
        self.semantic_error = []
        self.cont = True
        self.nested_for = {}
        self.isFunc = False
        self.index = 0
        self.isReturn = False
        self.return_value = None
        self.isContinue = False
        self.isBreak = False

    def sem(self):
        self.semantic()
        self.check_takda()  # function = ["function_name": "function_index number"]
        self.num = -1
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
        value = {}
        if d_type == 'yunit':
            value[name] = 0
        elif d_type == 'punto':
            value[name] = 0.0
        elif d_type == 'baybay' or d_type == 'titik':
            value[name] = ''
        elif d_type == 'yunit_list':
            value[name] = []
        elif d_type == 'punto_list':
            value[name] = []
        elif d_type == 'baybay_list':
            value[name] = []
        elif d_type == 'titik_list':
            value[name] = []
        elif d_type == 'bool_list':
            value[name] = []
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
            elif self.current == 'bool':
                self.boolean()
                self.newline()
            elif self.current == 'Identifier':
                self.expression()
                self.newline()
            elif self.current == 'sulat':
                self.sulat()
                self.newline()
            elif self.current == 'kung':
                self.kung()
                self.newline()
            elif self.current == 'pili':
                self.pili()
                self.newline()
            elif self.current == 'habang':
                self.index += 1
                self.habang()
                self.index -= 1
                self.newline()
            elif self.current == 'gawin':
                self.index += 1
                self.gawin()
                self.index -= 1
                self.newline()
            elif self.current == 'para':
                self.index += 1
                self.para()
                self.index -= 1
                self.newline()
            elif self.current == 'laktaw':
                self.semantic()
                self.newline()
            elif self.current == 'takda':
                self.takda()
                self.newline()
            elif self.current == 'tapos':
                self.cont = False
            elif self.current == 'gg.ssSawa':
                self.semantic()
                self.newline()

#=================FUNCTION=========================
    def check_takda(self):
        while self.current != None:
            if self.current == 'takda':
                self.semantic()
                self.functions[self.val] = [self.num, self.line]
                self.all_variables[self.val] = 'function'
            self.semantic()

    def func_Identifier(self):
        name = self.val
        z = ''
        x = ''
        try:
            x = self.func_variables[self.val]
            if not self.isFunc:
                z = 'self.variables[x][name]'
            else:
                z = 'self.variables_for_function[x][name]'
        except (KeyError, NameError, SyntaxError, TypeError) as e :
            self.semantic_error.append(f"NameError on line {self.line}: Variable '{self.val}' is not defined")
            self.y = None
            self.cont = False
            return
        if x not in ['yunit_list', 'punto_list', 'baybay_list', 'titik_list', 'bool_list','function']:
            self.semantic()
            if self.current =='[':
                self.semantic_error.append(f"TypeError on line {self.line}: {name} is not subscriptable")
                self.cont = False
                return
            return self.variables_for_function[x][name]
        else:
            self.semantic()
            if x == 'function':
                parameters = []
                self.semantic()
                ctr = 1
                cop = 0
                specific = ''
                z = ''
                while ctr != 0:
                    while self.current != ',' and ctr != 0:
                        if self.current == 'Identifier':
                            try: 
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} is not defined")
                                self.cont = False
                                return
                            if z == 'yunit_list' and z == 'punto_list' and z == 'baybay_list' and z == 'titik_list':
                                self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid parameter")
                                self.cont = False
                                return
                            parameters.append(z)
                            specific += str(z)
                            continue
                        elif self.current == '(':
                            ctr += 1
                        elif self.current == ')':
                            ctr -= 1
                        elif self.current in ['>', '<', '==', '>=', '<=', '!=', '==']:
                            cop += 1
                            if cop > 1:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: multiple comparison operators")
                                self.cont = False
                                return
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            z += self.val.replace('~', '-')
                            self.semantic()
                            continue
                        elif self.current == 'at':
                            z += 'and'
                            self.semantic()
                            continue
                        elif self.current == 'o':
                            z += 'or'
                            self.semantic()
                            continue
                        elif self.current == 'Totoo':
                            z += 'True'
                            self.semantic()
                            continue
                        elif self.current == 'Peke':
                            z += 'False'
                            self.semantic()
                            continue
                        if ctr != 0:
                            z += self.val
                            specific += self.val
                            self.semantic()
                    if self.current == ',':
                        self.semantic()
                    if z != '':
                        try:
                            parameters.append(eval(z))
                            z = ''
                        except:
                            self.semantic_error.append(f"TypeError on line {self.line}: {specific} is not a valid parameter")
                            self.cont = False
                            return
                line = self.line
                num = self.num
                answer = self.run(self.functions[name][0], self.functions[name][1], parameters)
                self.line = line
                self.num = num
                self.semantic()
                return answer
            while self.current not in ['+', '-', '*', '/', '%', '**','newline',',', ')','{']:
                if self.current == 'Identifier':
                    x = self.Identifier()
                    z += str(x)
                    continue
                z += self.val.replace('~', '-')
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
    
    def func_dec(self, d_type, name):
        variable = {}
        value = {}
        if d_type == 'yunit':
            value[name] = 0
        elif d_type == 'punto':
            value[name] = 0.0
        elif d_type == 'baybay' or d_type == 'titik':
            value[name] = ''
        elif d_type == 'yunit_list':
            value[name] = []
        elif d_type == 'punto_list':
            value[name] = []
        elif d_type == 'baybay_list':
            value[name] = []
        elif d_type == 'titik_list':
            value[name] = []
        elif d_type == 'bool_list':
            value[name] = []
        elif d_type == 'bool':
            value[name] = True
        self.variables_for_function[d_type].update(value)
        variable[name] = d_type
        self.func_variables.update(variable)

    def yunit_param(self, name, param_name):
        y = ''
        if self.current == "=":
            self.semantic()
            self.func_var.append(param_name)
            self.func_dec('yunit', param_name)
            ctr = 0
            while self.current != ',' and self.current != ')':
                if self.current == 'Identifier':
                    z = self.val
                    x = self.all_variables[self.val]
                    if x == 'function':
                        holder = self.Identifier()
                    else:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} is not a valid parameter for {param_name}")
                    if type(holder) != int and type(holder) != float:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Yunit Literal")
                        self.cont = False
                        return
                    if type(holder) == float:
                        holder = int(holder)
                    y += str(holder)
                    continue
                elif self.current == 'saYunit':
                    y += str(self.saYunit())
                    self.semantic()
                    continue
                elif self.current == 'saPunto':
                    y += str(int(self.saPunto()))
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(int(eval(self.val.replace('~', '-'))))
                elif self.current == 'Yunit Literal':
                    y += str(eval(self.val.replace('~', '-')))
                elif self.current in ['+', '-', '*', '/', '**']:
                    y += self.val
                elif self.current == '(':
                    y += '('
                    ctr += 1
                elif self.current == ')':
                    y += ')'
                    ctr -= 1
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Yunit')
                    self.cont = False
                    return
                self.semantic()
                if ctr == 0 and self.current in [',',')']:
                    break
            if self.cont == False:
                return
            try:
                self.variables_for_function['yunit'][param_name] = eval(y)
            except SyntaxError as e:
                self.cont = False
                return
        else:
            self.semantic_error.append(f"Semantic Error on line: Too few argument for {name}")
            self.cont = False
            return

    def punto_param(self, name, param_name):
        y = ''
        if self.current == "=":
            self.semantic()
            self.func_var.append(param_name)
            self.func_dec('baybay', param_name)
            ctr = 0
            while self.current != ',' and self.current != ')':
                if self.current == 'Identifier':
                    z = self.val
                    x = self.all_variables[self.val]
                    if x == 'function':
                        holder = self.Identifier()
                    else:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} is not a valid parameter for {param_name}")
                    if type(holder) != int and type(holder) != float:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Punto Literal")
                        self.cont = False
                        return
                    if type(holder) == int:
                        holder = float(holder)
                    y += str(holder)
                    continue
                elif self.current == 'saYunit':
                    y += str(float(self.saYunit()))
                    self.semantic()
                    continue
                elif self.current == 'saPunto':
                    y += str(self.saPunto())
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(eval(self.val.replace('~', '-')))
                elif self.current == 'Yunit Literal':
                    y += str(float(eval(self.val.replace('~', '-'))))
                elif self.current in ['+', '-', '*', '/', '**']:
                    y += self.val
                elif self.current == '(':
                    y += '('
                    ctr += 1
                elif self.current == ')':
                    y += ')'
                    ctr -= 1
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Punto')
                    self.cont = False
                    return
                self.semantic()
                if ctr == 0 and self.current in [',',')']:
                    break
            if self.cont == False:
                return
            try:
                self.variables_for_function['punto'][param_name] = eval(y)
            except SyntaxError as e:
                self.cont = False
                return
        else:
            self.semantic_error.append(f"Semantic Error on line: Too few argument for {name}")
            self.cont = False
            return

    def baybay_param(self, name, param_name):
        y = ''
        if self.current == "=":
            self.semantic()
            self.func_var.append(param_name)
            self.func_dec('baybay', param_name)
            ctr = 0
            while self.current != ',' and self.current != ')':
                if self.current == 'Identifier':
                    z = self.val
                    x = self.all_variables[self.val]
                    if x == 'function':
                        holder = self.Identifier()
                    else:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} is not a valid parameter for {param_name}")
                    if type(holder) != str:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Baybay Literal")
                        self.cont = False
                        return
                    y += "\"" + str(holder) + "\""
                    continue
                elif self.current == 'saBaybay':
                    y += str(self.saBaybay())
                    continue
                elif self.current == 'Baybay Literal':
                    y += str(self.val)
                elif self.current == '+':
                    y += self.val
                else:   
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Baybay')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                self.variables_for_function['baybay'][param_name] = eval(y)
                if self.current == ',':
                    self.semantic()
                    self.baybay_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            self.semantic_error.append(f"Semantic Error on line: Too few argument for {name}")
            self.cont = False
            return

    def titik_param(self, name, param_name):
        y = ''
        if self.current == "=":
            self.semantic()
            self.func_var.append(param_name)
            self.func_dec('titik', param_name)
            ctr = 0
            while self.current != ',' and self.current != ')':
                if self.current == 'Identifier':
                    z = self.val
                    x = self.all_variables[self.val]
                    if x == 'function':
                        holder = self.Identifier()
                    else:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} is not a valid parameter for {param_name}")
                    if type(holder) != str:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Literal")
                        self.cont = False
                        return
                    y += "\"" + str(holder) + "\""
                    continue
                elif self.current == 'saTitik':
                    y += str(self.saTitik())
                    continue

                elif self.current == 'Titik Literal':
                    y += str(self.val)
                elif self.current == '+':
                    y += self.val
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Titik')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                self.variables['baybay'][param_name] = eval(y)
                if self.current == ',':
                    self.semantic()
                    self.baybay_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            self.semantic_error.append(f"Semantic Error on line: Too few argument for {name}")
            self.cont = False
            return

    def bool_param(self, name, param_name):
        y = ''
        isBool = False
        if self.current == "=":
            self.semantic()
            self.func_var.append(param_name)
            self.func_dec('bool', param_name)
            ctr = 0
            while self.current != ',' and self.current != ')':
                if self.current == 'Identifier':
                    z = self.val
                    x = self.all_variables[self.val]
                    if x == 'function':
                        holder = self.Identifier()
                    else:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} is not a valid parameter for {param_name}")
                    if type(holder) != str:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Literal")
                        self.cont = False
                        return
                    y += "\"" + str(holder) + "\""
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
                elif self.current == '[':
                    self.semantic()
                    if self.current == 'Yunit Literal' or self.current == 'saYunit':
                        y += str(self.yunit_list()) + ' '   
                        isBool = False
                    elif self.current == 'Punto Literal' or self.current == 'saPunto':
                        y += str(self.punto_list()) + ' '
                        isBool = False
                    elif self.current == 'Baybay Literal' or self.current == 'saBaybay':
                        y += str(self.baybay_list()) + ' '
                        isBool = False
                    elif self.current == 'Titik' or self.current == 'saTitik':
                        y += str(self.titik_list()) + ' '
                        isBool = False
                    continue
                elif self.current in ['>', '<', '>=', '<=', '+', '-', '*', '/', '%', '**']:
                    y += self.current + ' '
                    if isBool == True:
                        self.semantic_error.append(f"TypeError on line {self.line}: Invalid operator for Boolean")
                        self.cont = False
                        return 
                else:
                    y += self.val + ' '
                    isBool = False
                self.semantic()
                if self.cont == False:
                    return
            if self.cont == False:
                return
            try:
                self.variables['bool'][param_name] = eval(y)
                if self.current == ',':
                    self.semantic()
                    self.baybay_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            self.semantic_error.append(f"Semantic Error on line: Too few argument for {name}")
            self.cont = False
            return

    def return_val(self):
        isBool = False
        isCond = False
        y = ''
        z = ''
        while self.current != 'newline':
            if self.current == 'Identifier':
                try:
                    if not self.isFunc:
                        x = self.all_variables[self.val]
                    else:
                        x = self.func_variables[self.val]
                except:
                    self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                    self.cont = False
                    return
                if not self.isFunc:
                    z = self.Identifier()
                else:
                    z = self.func_Identifier()
                if self.cont == False:
                    return  
                if type(z) == bool:
                    y += str(z)+ ' '
                    isBool = True
                elif type(z) == str:
                    y +='\''+ z+ '\' '
                    isBool = False
                else:
                    y += str(z)+ ' '
                    isBool = False
                continue
            elif self.current == 'di':
                y+= 'not'
                isBool = False
            elif self.current == 'Totoo':
                y += 'True'+ ' '
                isBool = True
            elif self.current == 'Peke':
                y += 'False'+ ' '
                isBool = True
            elif self.current == 'saBaybay':
                y +='\''+ str(self.saBaybay())+ '\' '
                isBool = False
                continue
            elif self.current == 'saPunto':
                y += str(self.saPunto())+ ' '
                isBool = False
                continue
            elif self.current == 'saTitik':
                y +='\'' +str(self.saTitik()) + '\' '
                isBool = False
                continue
            elif self.current == 'saYunit':
                y += str(self.saYunit()) + ' '
                isBool = False
                continue
            elif self.current == 'Baybay Literal' or self.current == 'Titik Literal':
                y += str(self.val) + ' '
                isBool = False
            elif self.current == 'at':
                y += 'and' + ' '
                isBool = False
            elif self.current == 'o':
                y += 'or' + ' '
                isBool = False
            elif self.current == '[':
                self.semantic()
                if self.current == 'Yunit Literal' or self.current == 'saYunit':
                    y += str(self.yunit_list()) + ' '
                    isBool = False
                elif self.current == 'Punto Literal' or self.current == 'saPunto':
                    y += str(self.punto_list()) + ' '
                    isBool = False
                elif self.current == 'Baybay Literal' or self.current == 'saBaybay':
                    y += str(self.baybay_list()) + ' '
                    isBool = False
                elif self.current == 'Titik Literal' or self.current == 'saTitik':
                    y += str(self.titik_list()) + ' '
                    isBool = False
                continue
            elif self.current in ['>', '<', '>=', '<=', '+', '-', '*', '/', '%', '**']:
                if self.current in ['>', '<', '>=', '<=']:
                    isCond = True
                y += self.current + ' '
                if isBool == True:
                    self.semantic_error.append(f"TypeError on line {self.line}: Invalid operator for Boolean")
                    self.cont = False
                    return
            elif self.current in ['==', '!=']:
                y += self.current + ' '
                isBool = True
            else:
                y += self.val + ' '
                isBool = False
            self.semantic()
        return eval(y)
            
    def run(self, num, line, parameters,var_name):
        self.num = num -1 
        self.line = line
        self.semantic()
        self.jump(2)
        while self.current != ')':
            if self.current == 'yunit':
                self.jump(2)
                name = self.val
                self.semantic()
                if len(parameters) != 0:
                    try:
                        if type(parameters[0]) != int and type(parameters[0]) != float:
                            self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                            self.cont = False
                            return
                        self.func_var.append(name)
                        self.variables_for_function['yunit'][name] = parameters[0]
                        parameters = parameters[1:]
                        if self.current == '=':
                            self.semantic()
                            ctr = 1
                            while self.current != ',' and self.current != ')':
                                self.semantic()
                                if self.current == '(':
                                    ctr += 1
                                elif self.current == ')':
                                    ctr -= 1
                                if ctr == 0:
                                    break
                    except:
                        self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                        self.cont = False
                        return
                else:
                    self.yunit_param(var_name,name)
                    parameters = parameters[1:]
                    if self.cont == False:
                        return
            elif self.current == 'punto':
                self.jump(2)
                name = self.val
                self.semantic()
                if len(parameters) != 0:
                    try:
                        if type(parameters[0]) != int and type(parameters[0]) != float:
                            self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                            self.cont = False
                            return
                        self.func_var.append(name)
                        self.variables_for_function['punto'][name] = parameters[0]
                        parameters = parameters[1:]
                        if self.current == '=':
                            self.semantic()
                            ctr = 1
                            while self.current != ',' and self.current != ')':
                                self.semantic()
                                if self.current == '(':
                                    ctr += 1
                                elif self.current == ')':
                                    ctr -= 1
                                if ctr == 0:
                                    break
                    except:
                        self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                        self.cont = False
                        return
                else:
                    self.punto_param(var_name,name)
                    parameters = parameters[1:]
                    if self.cont == False:
                        return
            elif self.current == 'baybay':
                self.jump(2)
                name = self.val
                self.semantic()
                if len(parameters) != 0:
                    try:
                        if type(parameters[0]) != str:
                            self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                            self.cont = False
                            return
                        self.func_var.append(name)
                        self.variables_for_function['baybay'][name] = parameters[0]
                        parameters = parameters[1:]
                        if self.current == '=':
                            self.semantic()
                            ctr = 1
                            while self.current != ',' and self.current != ')':
                                self.semantic()
                                if self.current == '(':
                                    ctr += 1
                                elif self.current == ')':
                                    ctr -= 1
                                if ctr == 0:
                                    break
                    except:
                        self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                        self.cont = False
                        return
                else:
                    self.baybay_param(var_name,name)
                    parameters = parameters[1:]
                    if self.cont == False:
                        return
            elif self.current == 'titik':
                self.jump(2)
                name = self.val
                self.semantic()
                if len(parameters) != 0:
                    try:
                        if type(parameters[0]) != str:
                            self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                            self.cont = False
                            return
                        self.func_var.append(name)
                        self.variables_for_function['titik'][name] = parameters[0]
                        parameters = parameters[1:]
                        if self.current == '=':
                            self.semantic()
                            ctr = 1
                            while self.current != ',' and self.current != ')':
                                self.semantic()
                                if self.current == '(':
                                    ctr += 1
                                elif self.current == ')':
                                    ctr -= 1
                                if ctr == 0:
                                    break
                    except:
                        self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                        self.cont = False
                        return
                else:
                    self.titik_param(var_name,name)
                    parameters = parameters[1:]
                    if self.cont == False:
                        return
            elif self.current == 'bool':
                self.jump(2)
                name = self.val
                self.semantic()
                if len(parameters) != 0:
                    try:
                        if type(parameters[0]) != bool:
                            self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                            self.cont = False
                            return
                        self.func_var.append(name)
                        self.variables_for_function['bool'][name] = parameters[0]
                        parameters = parameters[1:]
                        if self.current == '=':
                            self.semantic()
                            ctr = 1
                            while self.current != ',' and self.current != ')':
                                self.semantic()
                                if self.current == '(':
                                    ctr += 1
                                elif self.current == ')':
                                    ctr -= 1
                                if ctr == 0:
                                    break
                    except:
                        self.semantic_error.append(f"TypeError on line {self.line}: invalid parameter for {name}")
                        self.cont = False
                        return
                else:
                    self.bool_param(var_name,name)
                    parameters = parameters[1:]
                    if self.cont == False:
                        return
            if self.current == ',':
                self.semantic()
        if parameters != []:
            self.semantic_error.append(f"TypeError on line {self.line}: too many parameters for {var_name}")
            self.cont = False
            return
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        while self.current != '}' and self.cont and self.isReturn == False:
            if self.current == 'sulat':
                self.sulat()
                self.newline()
            elif self.current == 'yunit':
                self.yunit()
                self.newline()
            elif self.current == 'baybay':
                self.baybay()
            elif self.current == 'Identifier':
                self.expression()
                self.newline()   
            elif self.current == 'kung':
                self.kung()
                self.newline()
            elif self.current == 'balik':
                self.isReturn = True
                self.semantic()
                self.return_value = self.return_val()
                self.newline()
                break   
        self.semantic()
        return self.return_value

    def takda(self):
        self.find('{')
        self.semantic()
        open_ctr = 1
        close_ctr = 0
        while open_ctr != close_ctr:
            if self.current == '{':
                open_ctr += 1
            elif self.current == '}':
                close_ctr += 1
            self.semantic()

#================STATEMENTS=========================

    def Identifier(self):
        name = self.val
        z = ''
        x = ''
        try:
            x = self.all_variables[self.val]
            if not self.isFunc:
                z = 'self.variables[x][name]'
            else:
                z = 'self.variables_for_function[x][name]'
        except (KeyError, NameError, SyntaxError, TypeError) as e :
            self.semantic_error.append(f"NameError on line {self.line}: Variable '{self.val}' is not defined")
            self.y = None
            self.cont = False
            return
        if x not in ['yunit_list', 'punto_list', 'baybay_list', 'titik_list', 'bool_list','function']:
            self.semantic()
            if self.current =='[':
                self.semantic_error.append(f"TypeError on line {self.line}: {name} is not subscriptable")
                self.cont = False
                return 
            return self.variables[x][name]
        else:
            self.semantic()
            if x == 'function':
                parameters = []
                self.semantic()
                ctr = 1
                cop = 0
                specific = ''
                z = ''
                while ctr != 0:
                    while self.current != ',' and ctr != 0:
                        if self.current == 'Identifier':
                            try: 
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} is not defined")
                                self.cont = False
                                return
                            if z == 'yunit_list' and z == 'punto_list' and z == 'baybay_list' and z == 'titik_list':
                                self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid parameter")
                                self.cont = False
                                return
                            parameters.append(z)
                            specific += str(z)
                            continue
                        elif self.current == '(':
                            ctr += 1
                        elif self.current == ')':
                            ctr -= 1
                        elif self.current in ['>', '<', '==', '>=', '<=', '!=', '==']:
                            cop += 1
                            if cop > 1:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: multiple comparison operators")
                                self.cont = False
                                return
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            z += self.val.replace('~', '-')
                            self.semantic()
                            continue
                        elif self.current == 'at':
                            z += 'and'
                            self.semantic()
                            continue
                        elif self.current == 'o':
                            z += 'or'
                            self.semantic()
                            continue
                        elif self.current == 'Totoo':
                            z += 'True'
                            self.semantic()
                            continue
                        elif self.current == 'Peke':
                            z += 'False'
                            self.semantic()
                            continue
                        if ctr != 0:
                            z += self.val
                            specific += self.val
                            self.semantic()
                    if self.current == ',':
                        self.semantic()
                    if z != '':
                        try:
                            parameters.append(eval(z))
                            z = ''
                        except:
                            self.semantic_error.append(f"TypeError on line {self.line}: {specific} is not a valid parameter")
                            self.cont = False
                            return
                line = self.line
                num = self.num
                self.isFunc = True
                answer = self.run(self.functions[name][0], self.functions[name][1], parameters,name)
                self.isFunc = False
                self.line = line
                self.num = num
                self.semantic()
                return answer
            while self.current not in ['+', '-', '*', '/', '%', '**','newline',',', ')','{']:
                if self.current == 'Identifier':
                    x = self.Identifier()
                    z += str(x)
                    continue
                z += self.val.replace('~', '-')
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
        
    def yunit_list(self, ctr = 0):
        x = []
        y = ''
        while self.current != ']':
            while self.current != ',' and self.current != ']':
                if self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                    y += self.val.replace('~', '-')
                elif self.current == '[':
                    self.semantic()
                    x.append(self.yunit_list(ctr+1))
                    if ctr != 0:
                        self.semantic()
                        return x
                    continue
                elif self.current == 'Identifier':
                    try: 
                        if not self.isFunc:
                            z = self.all_variables[self.val]
                        else:
                            z = self.func_variables[self.val]
                    except:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} is not defined")
                        self.cont = False
                        return
                    if z != 'yunit_list' and z != 'yunit' and z != 'punto':
                        self.semantic_error.append(f'Semantic Error on line {self.line}: {self.val} is not a Yunit Literal or Yunit List')
                        self.cont = False
                        return
                    else:
                        if z == 'yunit_list':
                            if not self.isFunc:
                                x.append(self.variables[z][self.val])
                            else:
                                x.append(self.variables_for_function[z][self.val])
                        else:
                            if not self.isFunc:
                                y+=str(self.variables[z][self.val])
                            else:
                                y+=str(self.variables_for_function[z][self.val])
                elif self.current in ['+', '-', '*', '/', '**', '(', ')']:
                    y += self.val
                elif self.current == 'saYunit':
                    y += str(self.saYunit())
                elif self.current == 'saPunto':
                    y += str(self.saPunto())
                else:
                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a Yunit literal or Yunit list")
                    self.cont = False
                    return
                self.semantic()
            if self.current == ',':
                self.semantic()
            if y != '':
                x.append(int(eval(y)))
                y = ''
        self.semantic()
        return x

    def saYunit(self):
        y = ''
        x = 0
        self.semantic()
        self.semantic()
        if self.current == 'Baybay Literal' or self.current == 'Titik Literal':
            y = f"int({self.val[1:-1].replace('~', '-')})"
            try:
                self.semantic() 
                self.semantic()
                return eval(y)
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
                self.cont = False
                return
        elif self.current == 'Identifier':
            if not self.isFunc:
                y = f"int({self.Identifier()})"
            else:
                y = f"int({self.func_Identifier()})"
            try:
                self.semantic() 
                return eval(y)
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
                self.cont = False
                return
        else:
            y = f"int({self.val.replace('~', '-')})"
            try:
                self.semantic() 
                self.semantic()
                return eval(y)
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
                self.cont = False
                return

    def yunit(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        self.find('Identifier')
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('yunit_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('yunit_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current not in ['newline', ","]:
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.yunit_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['yunit_list'][val].append(i)
                                else:
                                    self.variables_for_function['yunit_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'yunit_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid parameter for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == int:
                                    if not self.isFunc:
                                        self.variables['yunit_list'][val].append(i)
                                    else:
                                        self.variables_for_function['yunit_list'][val].append(i)
                                    continue
                                elif type(i) == float:
                                    if not self.isFunc:
                                        self.variables['yunit_list'][val].append(int(i))
                                    else:
                                        self.variables_for_function['yunit_list'][val].append(int(i))
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['yunit_list'][val].append(i)
                                    else:
                                        self.variables_for_function['yunit_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Yunit Literal")
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Yunit List")
                        self.cont = False
                        return
        elif self.current == "=":
            self.semantic()
            if not self.isFunc:
                self.var.append(val)
                self.declare('yunit', val)
            else:
                self.func_var.append(val)
                self.func_dec('yunit', val)
            while self.current != ',' and self.current != 'newline':
                if self.current == 'Identifier':    
                    z = self.val
                    if not self.isFunc:
                        holder = self.Identifier()
                    else:
                        holder = self.func_Identifier()
                    if self.cont == False:
                        return
                    if type(holder) != int and type(holder) != float:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Yunit Literal")
                        self.cont = False
                        return
                    if type(holder) == float:
                        holder = int(holder)
                    y += str(holder)
                    continue
                elif self.current == 'saYunit':
                    y += str(self.saYunit())
                    self.semantic()
                    continue
                elif self.current == 'saPunto':
                    y += str(int(self.saPunto()))
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(int(eval(self.val.replace('~', '-'))))
                elif self.current == 'Yunit Literal':
                    y += str(eval(self.val.replace('~', '-')))
                elif self.current in ['+', '-', '*', '/', '**', '(', ')']:
                    y += self.val
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Yunit')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['yunit'][val] = eval(y)
                else:
                    self.variables_for_function['yunit'][val] = eval(y)
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('yunit', val)
            else:
                self.func_var.append(val)
                self.func_dec('yunit', val)
        if self.current == ',':
            self.semantic()
            self.yunit_continue()
        self.newline()
     
    def yunit_continue(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        val = self.val
        if val in self.var:
            self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
            self.cont = False
            return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('yunit_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('yunit_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.yunit_list()
                        for i in valuelist:
                            if not self.isFunc:
                                self.variables['yunit_list'][val].append(i)
                            else:
                                self.variables_for_function['yunit_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'yunit_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid value for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == int:
                                    if not self.isFunc:
                                        self.variables['yunit_list'][val].append(i)
                                    else:
                                        self.variables_for_function['yunit_list'][val].append(i)
                                    continue
                                elif type(i) == float:
                                    if not self.isFunc:
                                        self.variables['yunit_list'][val].append(int(i))
                                    else:
                                        self.variables_for_function['yunit_list'][val].append(int(i))
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Yunit Literal")
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Yunit List")
                        self.cont = False
                        return
        elif self.current == "=":
            self.semantic()
            if not self.isFunc:
                self.var.append(val)
                self.declare('yunit', val)
            else:
                self.func_var.append(val)
                self.func_dec('yunit', val)
            while self.current != ',' and self.current != 'newline':
                if self.current == 'Identifier':    
                    z = self.val
                    if not self.isFunc:
                        holder = self.Identifier()
                    else:
                        holder = self.func_Identifier()
                    if self.cont == False:
                        return
                    if type(holder) != int and type(holder) != float:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Yunit Literal")
                        self.cont = False
                        return
                    if type(holder) == float:
                        holder = int(holder)
                    y += str(holder)
                    continue
                elif self.current == 'saYunit':
                    y += str(self.saYunit())
                    self.semantic()
                    continue
                elif self.current == 'saPunto':
                    y += str(int(self.saPunto()))
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(int(eval(f'{self.val.replace("~", "-")}')))
                elif self.current == 'Yunit Literal':
                    y += str(eval(f'{self.val.replace("~", "-")}'))
                elif self.current in ['+', '-', '*', '/', '**', '(', ')']:
                    y += self.val
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Yunit')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['yunit'][val] = eval(y)
                else:
                    self.variables_for_function['yunit'][val] = eval(y)
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('yunit', val)
            else:
                self.func_var.append(val)
                self.func_dec('yunit', val)
        if self.current == ',':
            self.semantic()
            self.yunit_continue()
        self.newline()

    def punto_list(self, ctr = 0):
        x = []
        y = ''
        while self.current != ']':
            while self.current != ',' and self.current != ']':
                if self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                    y += self.val.replace('~', '-')
                elif self.current == '[':
                    self.semantic()
                    x.append(self.yunit_list(ctr + 1))
                    if ctr != 0:
                        self.semantic()
                        return x
                    continue
                elif self.current == 'Identifier':
                    try: 
                        if not self.isFunc:
                            z = self.all_variables[self.val]
                        else:
                            z = self.func_variables[self.val]
                    except:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} is not defined")
                        self.cont = False
                        return
                    if z != 'yunit_list' and z != 'yunit' and z != 'punto':
                        self.semantic_error.append(f'Semantic Error on line {self.line}: {self.val} is not a Punto Literal or Punto List')
                        self.cont = False
                        return
                    else:
                        if z == 'punto_list':
                            if not self.isFunc:
                                x.append(self.variables[z][self.val])
                            else:
                                x.append(self.variables_for_function[z][self.val])
                        else:
                            if not self.isFunc:
                                y+=str(self.variables[z][self.val])
                            else:
                                y+=str(self.variables_for_function[z][self.val])
                elif self.current in ['+', '-', '*', '/', '**', '(', ')']:
                    y += self.val
                elif self.current == 'saYunit':
                    y += str(self.saYunit())
                elif self.current == 'saPunto':
                    y += str(self.saPunto())
                else:
                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a Punto literal or Punto List")
                    self.cont = False
                    return
                self.semantic()
            if self.current == ',':
                self.semantic()
            if y != '':
                x.append(float(eval(y)))
                y = ''
        self.semantic()
        return x

    def saPunto(self):
        y = ''
        x = 0
        self.semantic()
        self.semantic()
        if self.current == 'Baybay Literal' or self.current == 'Titik Literal':
            y = f"float({self.val[1:-1].replace('~', '-')})"
            try:
                self.semantic() 
                self.semantic()
                return eval(y)
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for saPunto : \"{self.current}\"")
                self.cont = False
                return
        elif self.current == 'Identifier':
            if not self.isFunc:
                y = f"float({self.Identifier()})"
            else:
                y = f"float({self.func_Identifier()})"
            try:
                self.semantic() 
                return eval(y)
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for saPunto : \"{self.current}\"")
                self.cont = False
                return
        else:
            y = f"float({self.val.replace('~', '-')})"
            try:
                self.semantic() 
                self.semantic()
                return eval(y)
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for saPunto : \"{self.current}\"")
                self.cont = False
                return

    def punto(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        self.find('Identifier')
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('punto_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('punto_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current not in ['newline', ","]:
                    if self.current == '[':
                        self.semantic()
                        valuelist = self.punto_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['punto_list'][val].append(i)
                                else:
                                    self.variables_for_function['punto_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'punto_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid value for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == int:
                                    if not self.isFunc:
                                        self.variables['punto_list'][val].append(float(i))
                                    else:
                                        self.variables_for_function['punto_list'][val].append(float(i))
                                    continue
                                elif type(i) == float:
                                    if not self.isFunc:
                                        self.variables['punto_list'][val].append(i)
                                    else:
                                        self.variables_for_function['punto_list'][val].append(i)
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['punto_list'][val].append(i)
                                    else:
                                        self.variables_for_function['punto_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Punto Literal")
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Punto List")
                        self.cont = False
                        return
        elif self.current == "=":
            self.semantic()
            if not self.isFunc:
                self.var.append(val)
                self.declare('punto', val)
            else:
                self.func_var.append(val)
                self.func_dec('punto', val)
            while self.current != ',' and self.current != 'newline':
                if self.current == 'Identifier':    
                    z = self.val
                    if not self.isFunc:
                        holder = self.Identifier()
                    else:
                        holder = self.func_Identifier()
                    if self.cont == False:
                        return
                    if type(holder) != int and type(holder) != float:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Yunit Literal")
                        self.cont = False
                        return
                    if type(holder) == int:
                        holder = float(holder)
                    y += str(holder)
                    continue
                elif self.current == 'saYunit':
                    y += str(float(self.saYunit()))
                    self.semantic()
                    continue
                elif self.current == 'saPunto':
                    y += str(self.saPunto())
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(eval(f'{self.val.replace("~", "-")}'))
                elif self.current == 'Yunit Literal':
                    y += str(float(eval(f'{self.val.replace("~", "-")}')))
                elif self.current in ['+', '-', '*', '/', '**', '(', ')']:
                    y += self.val
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Punto')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['punto'][val] = eval(y)
                else:
                    self.variables_for_function['punto'][val] = eval(y)
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('punto', val)
            else:
                self.func_var.append(val)
                self.func_dec('punto', val)
        if self.current == ',':
            self.semantic()
            self.punto_continue()
        self.newline()

    def punto_continue(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('punto_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('punto_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.punto_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['punto_list'][val].append(i)
                                else:
                                    self.variables_for_function['punto_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'punto_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid value for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == int:
                                    if not self.isFunc:
                                        self.variables['punto_list'][val].append(float(i))
                                    else:
                                        self.variables_for_function['punto_list'][val].append(float(i))
                                    continue
                                elif type(i) == float:
                                    if not self.isFunc:
                                        self.variables['punto_list'][val].append(i)
                                    else:
                                        self.variables_for_function['punto_list'][val].append(i)
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['punto_list'][val].append(i)
                                    else:
                                        self.variables_for_function['punto_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Punto Literal")
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Punto List")
                        self.cont = False
                        return
        elif self.current == "=":
            self.semantic()
            if not self.isFunc:
                self.var.append(val)
                self.declare('punto', val)
            else:
                self.func_var.append(val)
                self.func_dec('punto', val)
            while self.current != ',' and self.current != 'newline':
                if self.current == 'Identifier':    
                    z = self.val
                    holder = self.Identifier()
                    if self.cont == False:
                        return
                    if type(holder) != int and type(holder) != float:
                        self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Punto Literal")
                        self.cont = False
                        return
                    if type(holder) == int:
                        holder = float(holder)
                    y += str(holder)
                    continue
                elif self.current == 'saYunit':
                    y += str(float(self.saYunit()))
                    self.semantic()
                    continue
                elif self.current == 'saPunto':
                    y += str(self.saPunto())
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(eval(f'{self.val.replace("~", "-")}'))
                elif self.current == 'Yunit Literal':
                    y += str(eval(f'float({self.val.replace("~", "-")})'))
                elif self.current in ['+', '-', '*', '/', '**', '(', ')']:
                    y += self.val
                else:
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Yunit')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['punto'][val] = eval(y)
                else:
                    self.variables_for_function['punto'][val] = eval(y)
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('punto', val)
            else:
                self.func_var.append(val)
                self.func_dec('punto', val)
        if self.current == ',':
            self.semantic()
            self.punto_continue()
        self.newline()

    def baybay_list(self, ctr = 0): 
        x = []
        y = ''
        while self.current != ']':
            while self.current != ',' and self.current != ']':
                if self.current == 'Baybay Literal':
                    y +=self.val
                elif self.current == '[':
                    self.semantic()
                    x.append(self.baybay_list(ctr + 1))
                    if ctr != 0:
                        self.semantic()
                        return x
                    continue
                elif self.current == 'Identifier':
                    try: 
                        if not self.isFunc:
                            z = self.all_variables[self.val]
                        else:
                            z = self.func_variables[self.val]
                    except:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} is not defined")
                        self.cont = False
                        return
                    if z != 'baybay_list':
                        self.semantic_error.append(f'Semantic Error on line {self.line}: {self.val} is not a Baybay Literal or Baybay List')
                        self.cont = False
                        return
                    else:
                        if z == 'baybay_list':
                            if not self.isFunc:
                                x.append(self.variables[z][self.val])
                            else:
                                x.append(self.variables_for_function[z][self.val])
                        else:
                            if not self.isFunc:
                                y+=str(self.variables[z][self.val])
                            else:
                                y += str(self.variables_for_function[z][self.val])
                elif self.current in ['+', '(', ')']:
                    y += self.val
                elif self.current in ['-', '*', '/', '**']:
                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Baybay List")
                    self.cont = False
                    return
                elif self.current == 'saBaybay':
                    y += str(self.saBaybay())
                else:
                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a Baybay literal or Baybay list")
                    self.cont = False
                    return
                self.semantic()
            if self.current == ',':
                self.semantic()
            if y != '':
                x.append(str(eval(y)))
                y = ''
        self.semantic()
        return x

    def saBaybay(self):
        y = ''
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            if not self.isFunc:
                y = f'str({self.Identifier()})'
            else: 
                y = f'str({self.func_Identifier()})'
            try:
                self.semantic() 
                return f'\"{eval(y)}\"'
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
                self.cont = False
                return
        else:
            y  = f'str({self.val})'
            try:
                self.semantic() 
                self.semantic()
                return f'\"{eval(y)}\"'
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
                self.cont = False
                return

    def baybay(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        self.find('Identifier')
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('baybay_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('baybay_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.baybay_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['baybay_list'][val].append(i)
                                else:
                                    self.variables_for_function['baybay_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'baybay_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid value for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == str:
                                    if not self.isFunc:
                                        self.variables['baybay_list'][val].append(i)
                                    else:
                                        self.variables_for_function['baybay_list'][val].append(i)
                                    continue
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['baybay_list'][val].append(i)
                                    else:
                                        self.variables_for_function['baybay_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Baybay Literal")
                                    self.cont = False
                                    return
                            self.semantic()
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Baybay List")
                        self.cont = False
                        return
        elif self.current == "=":
            self.semantic()
            if not self.isFunc:
                self.var.append(val)
                self.declare('baybay', val)
            else:
                self.func_var.append(val)
                self.func_dec('baybay', val)
            while self.current != 'newline' and self.current != ',':
                if self.current == 'Identifier':
                    z = self.val
                    if not self.isFunc:
                        holder = self.Identifier()
                    else:
                        holder = self.func_Identifier()
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
                elif self.current == 'Baybay Literal':
                    y += str(self.val)
                elif self.current == '+':
                    y += self.val
                else:   
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Baybay')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['baybay'][val] = eval(y)
                else:
                    self.variables_for_function['baybay'][val] = eval(y)
                if self.current == ',':
                    self.semantic()
                    self.baybay_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('baybay', val)
            else:
                self.func_var.append(val)
                self.func_dec('baybay', val)
        if self.current == ',':
            self.semantic()
            self.baybay_continue()  

    def baybay_continue(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('baybay_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('baybay_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.baybay_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['baybay_list'][val].append(i)
                                else:
                                    self.variables_for_function['baybay_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'baybay_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid value for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == str:
                                    if not self.isFunc:
                                        self.variables['baybay_list'][val].append(i)
                                    else:
                                        self.variables_for_function['baybay_list'][val].append(i)
                                    continue
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['baybay_list'][val].append(i)
                                    else:
                                        self.variables_for_function['baybay_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Baybay Literal")
                                    self.cont = False
                                    return
                            self.semantic()
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Baybay List")
                        self.cont = False
                        return
        elif self.current == "=":
            self.semantic()
            if not self.isFunc:
                self.var.append(val)
                self.declare('baybay', val)
            else:
                self.func_var.append(val)
                self.func_dec('baybay', val)
            while self.current != 'newline' and self.current != ',':
                if self.current == 'Identifier':
                    z = self.val
                    if not self.isFunc:
                        holder = self.Identifier()
                    else:
                        holder = self.func_Identifier()
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
                elif self.current == 'Baybay Literal':
                    y += str(self.val)
                elif self.current == '+':
                    y += self.val
                else:   
                    self.semantic_error.append(f'Semantic Error on Line {self.line}: {self.current} is not a valid value for Baybay')
                    self.cont = False
                    return
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['baybay'][val] = eval(y)
                else:
                    self.variables_for_function['baybay'][val] = eval(y)
                if self.current == ',': 
                    self.semantic()
                    self.baybay_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('baybay', val)
            else:
                self.func_var.append(val)
                self.func_dec('baybay', val)
        if self.current == ',':
            self.semantic()
            self.baybay_continue() 
    
    def saTitik(self):
        y = ''
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            if not self.isFunc:
                y = f'str(\'{self.Identifier()})\''
            else:
                y = f'str(\'{self.func_Identifier()})\''
            try:
                self.semantic() 
                return f'\"{eval(y)}\"'
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for saTitik : \"{self.current}\"")
                self.cont = False
                return
        else:
            y  = f'str({self.val})'
            try:
                self.semantic() 
                self.semantic()
                return f'\"{eval(y)}\"'
            except:
                self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for saTitik : \"{self.current}\"")
                self.cont = False
                return
            
    def titik_list(self, ctr =0):
        x = []
        y = ''
        while self.current != ']':
            while self.current != ',' and self.current != ']':
                if self.current == 'Titik Literal':
                    y +=self.val
                elif self.current == '[':
                    self.semantic()
                    x.append(self.titik_list(ctr + 1))
                    if ctr != 0:
                        self.semantic()
                        return x
                    continue
                elif self.current == 'Identifier':
                    try: 
                        if not self.isFunc:
                            z = self.all_variables[self.val]
                        else:
                            z = self.func_variables[self.val]
                    except:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} is not defined")
                        self.cont = False
                        return
                    if z != 'titik_list':
                        self.semantic_error.append(f'Semantic Error on line {self.line}: {self.val} is not a Titik Literal or Titik List')
                        self.cont = False
                        return
                    else:
                        if z == 'titik_list':
                            if not self.isFunc:
                                x.append(self.variables[z][self.val])
                            else:
                                x.append(self.variables_for_function[z][self.val])
                        else:
                            if not self.isFunc:
                                y+=str(self.variables[z][self.val])
                            else:
                                y+=str(self.variables_for_function[z][self.val])
                elif self.current in ['+', '(', ')']:
                    y += self.val
                elif self.current in ['-', '*', '/', '**']:
                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Titik List")
                    self.cont = False
                    return
                elif self.current == 'saTitik':
                    y += str(self.saTitik())
                else:
                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a Titik literal or Titik list")
                    self.cont = False
                    return
                self.semantic()
            if self.current == ',':
                self.semantic()
            if y != '':
                x.append(str(eval(y)))
                y = ''
        self.semantic()
        return x
    
    def titik(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        self.find('Identifier')
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('titik_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('titik_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.titik_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['titik_list'][val].append(i)
                                else:
                                    self.variables_for_function['titik_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'titik_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid parameter for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == str:
                                    if not self.isFunc:
                                        self.variables['titik_list'][val].append(i)
                                    else:
                                        self.variables_for_function['titik_list'][val].append(i)
                                    continue
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['titik_list'][val].append(i)
                                    else:
                                        self.variables_for_function['titik_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Titik Literal")
                                    self.cont = False
                                    return
                            self.semantic()
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Titik List")
                        self.cont = False
                        return
        elif self.current == '=':
            if not self.isFunc:
                self.var.append(val)
                self.declare('titik', val)
            else:
                self.func_var.append(val)
                self.func_dec('titik', val)
            self.semantic()
            if self.current == 'Identifier':
                z = self.val
                if not self.isFunc:
                    holder = self.Identifier()
                else:
                    holder = self.func_Identifier()
                if self.cont == False:
                    return
                if type(holder) != str and len(holder) != 1:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} does not contain Titik Literal")
                    self.cont = False
                    return
                y += f'\'{str(holder)}\''
            elif self.current == 'saTitik':
                y += str(self.saTitik())
                if len(y[1:-1]) < 1:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} does not contain Titik Literal")
                    self.cont = False
            elif self.current == 'Titik Literal':
                y += self.val
            elif self.current == '+':
                y += self.val
            else:
                self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Litaral")
                self.cont = False
            self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['titik'][val] = eval(y)
                else:
                    self.variables_for_function['titik'][val] = eval(y)
                if self.current == ',':
                    self.titik_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('titik', val)
            else:
                self.func_var.append(val)
                self.func_dec('titik', val)
        if self.current == ',':
            self.semantic()
            self.titik_continue()  
        
    def titik_continue(self):
        valuelist = []
        value = 0
        string = ''
        y = ''
        self.find('Identifier')
        val = self.val
        if not self.isFunc:
            if val in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        else:
            if val in self.func_var:
                self.semantic_error.append(f"NameError on line {self.line}: {val} is already defined")
                self.cont = False
                return
        self.semantic()
        if self.current == '[':
            if not self.isFunc:
                self.var.append(val)
                self.declare('titik_list', val)
            else:
                self.func_var.append(val)
                self.func_dec('titik_list', val)
            self.jump(2)
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic() 
                        valuelist = self.titik_list()
                        if self.cont:
                            for i in valuelist:
                                if not self.isFunc:
                                    self.variables['titik_list'][val].append(i)
                                else:
                                    self.variables_for_function['titik_list'][val].append(i)
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                        if x != 'titik_list':
                            self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid parameter for {val}")
                            self.cont = False
                            return
                        if not self.isFunc:
                            valuelist = self.Identifier()
                        else:
                            valuelist = self.func_Identifier()
                        if type(valuelist) == list:
                            for i in valuelist:
                                if type(i) == str:
                                    if not self.isFunc:
                                        self.variables['titik_list'][val].append(i)
                                    else:
                                        self.variables_for_function['titik_list'][val].append(i)
                                    continue
                                elif type(i) == list:
                                    if not self.isFunc:
                                        self.variables['titik_list'][val].append(i)
                                    else:
                                        self.variables_for_function['titik_list'][val].append(i)
                                else:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {val} have values that is not a Titik Literal")
                                    self.cont = False
                                    return
                            self.semantic()
                        else:
                            self.semantic_error.append(f"Semantic on line {self.line}: {val} is not a list")
                            self.cont = False
                            return
                    elif self.current == '+':
                        self.semantic()
                    else:
                        self.semantic_error.append(f"Semantic Error on line {self.line}: {self.current} is not a valid value for Titik List")
                        self.cont = False
                        return
        if self.current == '=':
            if not self.isFunc:
                self.var.append(val)
                self.declare('titik', val)
            else:
                self.func_var.append(val)
                self.func_dec('titik', val)
            self.semantic()
            if self.current == 'Identifier':
                z = self.val
                if not self.isFunc:
                    holder = self.Identifier()
                else:
                    holder = self.func_Identifier()
                if self.cont == False:
                    return
                if type(holder) != str and len(holder) != 1:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} does not contain Titik Literal")
                    self.cont = False
                    return
                y += f'\'{str(holder)}\''
            elif self.current == 'saTitik':
                y += str(self.saTitik())
                if len(y[1:-1]) < 1:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} does not contain Titik Literal")
                    self.cont = False
            elif self.current == 'Titik Literal':
                y += self.val
            elif self.current == '+':
                y += self.val
            else:
                self.semantic_error.append(f"TypeError on line {self.line}: {z} does not contain Titik Litaral")
                self.cont = False
            self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['titik'][val] = eval(y)
                else:
                    self.variables_for_function['titik'][val] = eval(y)
                if self.current == ',':
                    self.titik_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        else:
            if not self.isFunc:
                self.var.append(val)
                self.declare('titik', val)
            else:
                self.func_var.append(val)
                self.func_dec('titik', val)
        if self.current == ',':
            self.semantic()
            self.titik_continue()  

    def sulat(self):
        x = ''
        y = ''
        z = ''
        a = ''
        titik_ctr = False
        isBaybay = False
        isBool = False
        self.semantic()
        self.semantic()
        while self.current != ')': 
            ctr = 1
            while self.current != ',' and self.current != ')' and ctr != 0:
                if self.current == 'Identifier':
                    x = ''
                    try:
                        if not self.isFunc:
                            a = self.all_variables[self.val]
                        else:
                            a = self.func_variables[self.val]
                    except:
                        self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                        self.cont = False
                        return
                    if a == 'titik':
                        titik_ctr = True
                        if not self.isFunc:
                            x += str('\'' +self.Identifier() +'\'')
                        else:
                            x += str('\'' +self.func_Identifier() +'\'')
                    elif a == 'baybay':
                        isBaybay = True
                        if not self.isFunc:
                            x += str('\'' +self.Identifier() +'\'')
                        else:
                            x += str('\'' +self.func_Identifier() +'\'')
                    else:
                        if not self.isFunc:
                            x += str(self.Identifier())
                        else:
                            x += str(self.func_Identifier())
                        if a == 'bool':
                            self.isBool = True
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
                elif self.current == 'Totoo':
                    y += str(True)
                    self.semantic()
                    continue
                elif self.current == 'Peke':
                    y += str(False)
                    self.semantic()
                    continue
                elif self.current == 'Punto Literal':
                    y += str(self.val.replace('~', '-'))
                    self.semantic()
                    continue
                elif self.current == '[':
                    self.semantic()
                    if self.current == 'Yunit Literal' or self.current == 'saYunit':
                        y += str(self.yunit_list()) + ' '
                        isBool = False
                    elif self.current == 'Punto Literal' or self.current == 'saPunto':
                        y += str(self.punto_list()) + ' '
                        isBool = False
                    elif self.current == 'Baybay Literal' or self.current == 'saBaybay':
                        y += str(self.baybay_list()) + ' '
                        isBool = False
                    self.semantic()
                    continue
                elif self.current == '(':
                    y += str('(')
                    self.semantic()
                    ctr += 1
                    continue
                elif self.current in ['+','-','*','**', '/','%']:
                    if isBool == True:
                        self.semantic_error.append(f"Semantic Eror on line{self.line}: Invalid operators for boolean")
                        isBool = False
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
                if isBaybay == True and self.current in  ['+', '-', '*', '/', '**', '%']:
                    self.semantic_error.append(f"TypeError on Line {self.line}: Invalid operators for Baybay Literal")
                    self.cont = False
                    return
            titik_ctr = False
            if self.current == ',':
                self.semantic()
                self.isBool = False
            try:
                z += str(eval(y))
            except:
                pass
            y = ''
        add_lexical_errors(z.replace('-', '~').replace('True', 'Totoo').replace('False', 'Peke'))
        self.semantic()
        self.newline()

    def expression(self):
        holder = ''
        name = self.val
        if not self.isFunc:
            try:
                x = self.all_variables[name]
            except:
                self.semantic_error.append(f"Semantic Error on line {self.line}: {name} not defined")
                self.cont = False
                return
        else:
            try:
                x = self.func_variables[name]
            except:
                self.semantic_error.append(f"Semantic Error on line {self.line}: {name} not defined")
                self.cont = False
                return
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
                    if not self.isFunc:
                        self.variables['baybay'][name] = baybay_val
                    else:
                        self.variables_for_function['baybay'][name] = baybay_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'baybay' or z == 'baybay_list' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == str:
                                        y += str(holder)
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == str:
                                        y += str(holder)
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
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
                    if not self.isFunc:
                        self.variables['baybay'][name] = eval(y)
                    else:
                        self.variables_for_function['baybay'][name] = eval(y)
                    return
            elif self.current == '+=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    baybay_val = input(x[1:-1])
                    if not self.isFunc:
                        self.variables['baybay'][name] = baybay_val 
                    else:
                        self.variables_for_function['baybay'][name] += baybay_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'baybay'or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == str:
                                        y += str(holder)
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == str:
                                        y += str(holder)
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
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
                    if not self.isFunc:
                        self.variables['baybay'][name] += eval(y)
                    else:
                        self.variables_for_function['baybay'][name] += eval(y)
                    return
            else:
                self.semantic_error.append(f'TypeError on line {self.line}: Invalid Assignment operator on baybay variable')
                self.cont = False
                return
        elif x == 'yunit':
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = int(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Yunit variable')
                    if not self.isFunc:
                        self.variables['yunit'][name] = num_val
                    else:
                        self.variables_for_function['yunit'][name] = num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
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
                    if not self.isFunc:
                        self.variables['yunit'][name] = int(eval(y))
                    else:
                        self.variables_for_function['yunit'][name] = int(eval(y))
                    self.newline()
                    return
            elif self.current == '+=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = int(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Yunit variable')
                    if not self.isFunc:
                        self.variables['yunit'][name] += num_val
                    else:
                        self.variables_for_function['yunit'][name] += num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
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
                    if not self.isFunc:
                        self.variables['yunit'][name] += int(eval(y))
                    else:
                        self.variables_for_function['yunit'][name] += int(eval(y))
                    self.newline()
                    return
            elif self.current == '-=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = int(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Yunit variable')
                    if not self.isFunc:
                        self.variables['yunit'][name] = num_val
                    else:
                        self.variables_for_function['yunit'][name] = num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
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
                    if not self.isFunc:
                        self.variables['yunit'][name] = int(eval(y))
                    else:
                        self.variables_for_function['yunit'][name] -= int(eval(y))
                    self.newline()
                    return
            elif self.current == '*=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        num_val = int(input(x[1:-1]))
                    except TypeError:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Yunit variable')
                    if not self.isFunc:
                        self.variables['yunit'][name] = num_val
                    else:
                        self.variables_for_function['yunit'][name] /= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
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
                    if not self.isFunc:
                        self.variables['yunit'][name] *= int(eval(y))
                    else:
                        self.variables_for_function['yunit'][name] *= int(eval(y))
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
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Yunit variable')
                    if not self.isFunc:
                        self.variables['yunit'][name] = num_val
                    else:
                        self.variables_for_function['yunit'][name] /= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(int(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
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
                    if not self.isFunc:
                        self.variables['yunit'][name] /= int(eval(y))
                    else:
                        self.variables_for_function['yunit'][name] /= int(eval(y))
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
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Punto variable')
                    if not self.isFunc:
                        self.variables['punto'][name] = num_val
                    else:
                        self.variables_for_function['punto'][name] = num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto variable')
                            self.cont = False
                            return
                    if not self.isFunc:
                        self.variables['punto'][name] = float(eval(y))
                    else:
                        self.variables_for_function['punto'][name] = float(eval(y))
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
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Punto variable')
                    if not self.isFunc:
                        self.variables['punto'][name] += num_val
                    else:
                        self.variables_for_function['punto'][name] += num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto variable')
                            self.cont = False
                            return
                    if not self.isFunc:
                        self.variables['punto'][name] += float(eval(y))
                    else:
                        self.variables_for_function['punto'][name] += float(eval(y))
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
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Punto variable')
                    if not self.isFunc:
                        self.variables['punto'][name] -= num_val
                    else:
                        self.variables_for_function['punto'][name] -= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto variable')
                            self.cont = False
                            return
                    if not self.isFunc:
                        self.variables['punto'][name] -= float(eval(y))
                    else:
                        self.variables_for_function['punto'][name] -= float(eval(y))
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
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Punto variable')
                    if not self.isFunc:
                        self.variables['punto'][name] *= num_val
                    else:
                        self.variables_for_function['punto'][name] *= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto variable')
                            self.cont = False
                            return
                    if not self.isFunc:
                        self.variables['punto'][name] *= float(eval(y))
                    else:
                        self.variables_for_function['punto'][name] *= float(eval(y))
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
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Punto variable')
                    if not self.isFunc:
                        self.variables['punto'][name] /= num_val
                    else:
                        self.variables_for_function['punto'][name] /= num_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'yunit' or z == 'punto' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                                else:
                                    holder = self.func_Identifier()
                                    if type(holder) == int or type(holder) == float:
                                        y += str(float(holder))
                                    else:
                                        if z == 'function':
                                            self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                            self.cont = False
                                            return
                                        else:
                                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                            self.cont = False
                                            return
                            else:   
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'Yunit Literal' or self.current == 'Punto Literal':
                            y += str(self.val.replace('~','-'))
                            self.semantic()
                        elif self.current == 'saYunit':
                            y += str(self.saYunit())
                        elif self.current == 'saPunto':
                            y += str(self.saPunto())
                        elif self.current in ['+', '-', '*', '**', '/', '%', '(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Punto variable')
                            self.cont = False
                            return
                    if not self.isFunc:
                        self.variables['punto'][name] /= float(eval(y))
                    else:
                        self.variables_for_function['punto'][name] /= float(eval(y))
                    self.newline()
                    return
        elif x == 'titik':
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic()
                    self.semantic()
                    x = self.val
                    try:
                        titik_val = input(x[1:-1])
                    except:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Titik variable')
                        self.cont = False
                        return
                    if len(titik_val) != 0:
                        self.semantic_error.append(f'TypeError on Line {self.line}: Invalid input for Titik variable')
                        self.cont = False
                        return
                    if not self.isFunc:
                        self.variables['titik'][name] = titik_val
                    else:
                        self.variables_for_function['titik'][name] = titik_val
                    self.semantic()
                    self.semantic()
                    self.newline()
                    return
                else:
                    while self.current != 'newline':
                        if self.current == 'Identifier':
                            if not self.isFunc:
                                try:
                                    z = self.all_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            else:
                                try:
                                    z = self.func_variables[self.val]
                                except:
                                    self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                    self.cont = False
                                    return
                            if z == 'titik' or z == 'function':
                                if not self.isFunc:
                                    holder = self.Identifier()
                                else:
                                    holder = self.func_Identifier()
                                if type(holder) == str and len(holder) == 1:
                                    y += str(holder)
                                else:
                                    if z == 'function':
                                        self.semantic_error.append(f"TypeError on line {self.line}: Invalid value returned by function")
                                        self.cont = False
                                        return
                                    else:
                                        self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                        self.cont = False
                                        return
                            else:
                                self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                                self.cont = False
                                return
                            continue
                        elif self.current == 'saTitik':
                            y += str(self.saBaybay())
                        elif self.current == 'Titik Literal':
                            y += str(self.val)
                            self.semantic()
                        elif self.current in ['(', ')']:
                            y += self.current
                            self.semantic()
                        else:
                            if self.current in ['+', '-', '*', '**','/', '%' ]:
                                self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                            else:
                                self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik variable')
                            self.cont = False
                            return
                    if not self.isFunc:
                        self.variables['titik'][name] = eval(y)
                    else:
                        self.variables_for_function['titik'][name] = eval(y)
                    return
            else:
                self.semantic_error.append(f'TypeError on line {self.line}: Invalid Assignment operator on Titik variable')
        elif x == 'bool':
            self.semantic()
            if self.current == '=':
                self.semantic()
                if self.current == 'kuha':
                    self.semantic_error.append(f"TypeError on line {self.line}: Invalid input for Boolean variable")
                    self.cont = False
                    return
                else:
                    if not self.isFunc:
                        self.variables[x][name] = self.condition()
                    else:
                        self.variables_for_function[x][name] = self.condition()
        elif x == 'titik_list':
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.titik_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'titik_list' or z == 'function':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif holder[0] == str and len(holder[0]) == 1:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['titk_list'][name] = eval(y)
                else:
                    self.variables_for_function['titik_list'][name] = eval(y)
                    return
            elif self.current == '+=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.titik_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'titik_list' or z == list:
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif holder[0] == str and len(holder[0]) == 1:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['titk_list'][name] += eval(y)
                else:
                    self.variables_for_function['titik_list'][name] += eval(y)
                    return
            else:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not a valid Assignment operator")
                self.cont = False
                return
        elif x == 'baybay_list':
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.baybay_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'baybay_list':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif holder[0] == str:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['baybay_list'][name] = eval(y)
                else:
                    self.variables_for_function['baybay_list'][name] = eval(y)
                    return
            elif self.current == '+=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.baybay_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'baybay_list' or z == 'function':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif holder[0] == str :
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['baybay_list'][name] += eval(y)
                else:
                    self.variables_for_function['baybay_list'][name] += eval(y)
                    return
            else:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not a valid Assignment operator")
                self.cont = False
                return
        elif x == 'yunit_list':
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.yunit_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'yunit_list' or z == 'function':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif type(holder[0]) == int:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['yunit_list'][name] = eval(y)
                else:
                    self.variables_for_function['yunit_list'][name] = eval(y)
                    return
            elif self.current == '+=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.yunit_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'yunit_list' or z == 'function':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif type(holder[0]) == int:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['yunit_list'][name] += eval(y)
                else:
                    self.variables_for_function['yunit_list'][name] += eval(y)
                    return
            else:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not a valid Assignment operator")
                self.cont = False
                return
        elif x == 'punto_list':
            self.semantic()
            if self.current == '=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.punto_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'punto_list':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif type(holder[0]) == float:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['punto_list'][name] = eval(y)
                else:
                    self.variables_for_function['punto_list'][name] = eval(y)
                    return
            elif self.current == '+=':
                self.semantic()
                while self.current != 'newline':
                    if self.current == '[':
                        self.semantic()
                        y += str(self.punto_list())
                    elif self.current == 'Identifier':
                        if not self.isFunc:
                            try:
                                z = self.all_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        else:
                            try:
                                z = self.func_variables[self.val]
                            except:
                                self.semantic_error.append(f"Semantic Error on line {self.line}: {self.val} not defined")
                                self.cont = False
                                return
                        if z == 'punto_list'or z== 'function':
                            if not self.isFunc:
                                holder += str(self.Identifier())
                            else:
                                holder += str(self.func_Identifier())
                            if type(holder) == list:
                                if len(holder) == 0:
                                    y += str(holder)
                                elif type(holder[0]) == float:
                                    y += str(holder)
                                else:
                                    self.semantic_error.append(f'TypeError in Line {self.line}: Invalid return value for function')
                                    self.cont = False
                                    return
                        else:
                            self.semantic_error.append(f'TypeError in Line {self.line}: Invalid Identifier')
                            self.cont = False
                            return
                    elif self.current in ["(,", ")", "+"]:
                        y += self.current
                        self.semantic()
                    else:
                        if self.current in ['-', '*', '**','/', '%' ]:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid operator')
                        else:
                            self.semantic_error.append(f'TypeError on Line {self.line}: Invalid Assignment on Titik array variable')
                        self.cont = False
                        return
                if not self.isFunc:
                    self.variables['punto_list'][name] += eval(y)
                else:
                    self.variables_for_function['punto_list'][name] += eval(y)
                    return
            else:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not a valid Assignment operator")
                self.cont = False
                return
        elif x == 'function':
            self.Identifier()
            self.semantic()
        else:
            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
            self.cont = False
            return
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
        if not self.isFunc:
            if s_name in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
                self.cont = False
                return
        else:
            if s_name in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
                self.cont = False
                return
        if not self.isFunc:
            self.var.append(s_name)
            self.declare('bool', self.val)
        else:
            self.func_var.append(s_name)
            self.func_dec+('bool', self.val)
        self.semantic()
        if self.current == '=':
            self.semantic()
            while self.current != 'newline' and self.current != ',':
                if self.current == 'Identifier':
                    if not self.isFunc:
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                            self.cont = False
                            return
                    else:
                        try:
                            x = self.func_variables[self.val]
                        except:
                            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                            self.cont = False
                            return
                    if not self.isFunc:
                        z = self.Identifier()
                    else:
                        z = self.func_Identifier()
                    if self.cont == False:
                        return  
                    if type(z) == bool:
                        y += str(z)+ ' '
                        isBool = True
                    elif type(z) == str:
                        y += '\'' + z+ '\' '
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
                    y += '\'' + str(self.saBaybay())+ '\' '
                    isBool = False
                    continue
                elif self.current == 'saPunto':
                    y += str(self.saPunto())+ ' '
                    isBool = False
                    continue
                elif self.current == 'saTitik':
                    y += '\'' + str(self.saTitik()) + '\' '
                    isBool = False
                    continue
                elif self.current == 'saYunit':
                    y += str(self.saYunit()) + ' '
                    isBool = False
                    continue
                elif self.current == 'Baybay Literal' or self.current == 'Titik Literal':
                    y += str(self.val) + ' '
                    isBool = False
                elif self.current == 'at':
                    y += 'and' + ' '
                    isBool = False
                elif self.current == 'o':
                    y += 'and' + ' '
                    isBool = False
                elif self.current == '[':
                    self.semantic()
                    if self.current == 'Yunit Literal' or self.current == 'saYunit':
                        y += str(self.yunit_list()) + ' '   
                        isBool = False
                    elif self.current == 'Punto Literal' or self.current == 'saPunto':
                        y += str(self.punto_list()) + ' '
                        isBool = False
                    elif self.current == 'Baybay Literal' or self.current == 'saBaybay':
                        y += str(self.baybay_list()) + ' '
                        isBool = False
                    elif self.current == 'Titik' or self.current == 'saTitik':
                        y += str(self.titik_list()) + ' '
                        isBool = False
                    continue
                elif self.current in ['>', '<', '>=', '<=', '+', '-', '*', '/', '%', '**']:
                    y += self.current + ' '
                    if isBool == True:
                        self.semantic_error.append(f"TypeError on line {self.line}: Invalid operator for Boolean")
                        self.cont = False
                        return 
                else:
                    y += self.val + ' '
                    isBool = False
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['bool'][s_name] = eval(y)
                else:
                    self.variables_for_function['bool'][s_name] = eval(y)
                if self.current == ',':
                    self.bool_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        elif self.current == ',':
            self.bool_continue()    

    def bool_continue(self):
        x = ''
        y = ''
        z = ''
        holder = ''
        isBool = False
        self.semantic()
        s_name = self.val
        if not self.isFunc:
            if s_name in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
                self.cont = False
                return
        else:
            if s_name in self.var:
                self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
                self.cont = False
                return
        if not self.isFunc:
            self.var.append(s_name)
            self.declare('bool', self.val)
        else:
            self.func_var.append(s_name)
            self.func_dec+('bool', self.val)
        self.semantic()
        if self.current == '=':
            self.semantic()
            while self.current != 'newline' and self.current != ',':
                if self.current == 'Identifier':
                    if not self.isFunc:
                        try:
                            x = self.all_variables[self.val]
                        except:
                            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                            self.cont = False
                            return
                    else:
                        try:
                            x = self.func_variables[self.val]
                        except:
                            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                            self.cont = False
                            return
                    if not self.isFunc:
                        z = self.Identifier()
                    else:
                        z = self.func_Identifier()
                    if self.cont == False:
                        return
                    if type(z) == bool:
                        y += str(z)+ ' '
                        isBool = True
                    elif type(z) == str:
                        y += '\'' + z+ '\' '
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
                    y += str(self.val) + ' '
                    isBool = False
                elif self.current == 'at':
                    y += 'and' + ' '
                    isBool = False
                elif self.current == 'o':
                    y += 'and' + ' '
                    isBool = False
                elif self.current in ['>', '<', '>=', '<=', '+', '-', '*', '/', '%', '**']:
                    y += self.current + ' '
                    if isBool == True:
                        self.semantic_error.append(f"TypeError on line {self.line}: Invalid operator for Boolean")
                        self.cont = False
                        return 
                else:
                    y += self.val + ' '
                    isBool = False
                self.semantic()
            if self.cont == False:
                return
            try:
                if not self.isFunc:
                    self.variables['bool'][s_name] = eval(y)
                else:
                    self.variables_for_function['bool'][s_name] = eval(y)
                if self.current == ',':
                    self.bool_continue()
                    return
                self.newline()
            except SyntaxError as e:
                self.cont = False
                return
        elif self.current == ',':
            self.bool_continue()    

    def condition(self):
        isBool = False
        isCond = False
        ctr = False
        enter = 1
        y = ''
        z = ''
        if enter != 0:
            while self.current != 'newline' and self.current != ')':
                if self.current == 'Identifier':
                    try:
                        if not self.isFunc:
                            x = self.all_variables[self.val]
                        else:
                            x = self.func_variables[self.val]
                    except:
                        self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                        self.cont = False
                        return
                    if not self.isFunc:
                        z = self.Identifier()
                    else:
                        z = self.func_Identifier()
                    if self.cont == False:
                        return  
                    if type(z) == bool:
                        y += str(z)+ ' '
                        isBool = True
                    elif type(z) == str:
                        y +='\''+ z+ '\' '
                        isBool = False
                    else:
                        y += str(z)+ ' '
                        isBool = False
                    continue
                elif self.current == 'di':
                    y+= 'not'
                    isBool = False
                elif self.current == 'Totoo':
                    y += 'True'+ ' '
                    isBool = True
                elif self.current == 'Peke':
                    y += 'False'+ ' '
                    isBool = True
                elif self.current == 'saBaybay':
                    y +='\''+ str(self.saBaybay())+ '\' '
                    isBool = False
                    continue
                elif self.current == 'saPunto':
                    y += str(self.saPunto())+ ' '
                    isBool = False
                    continue
                elif self.current == 'saTitik':
                    y +='\'' +str(self.saTitik()) + '\' '
                    isBool = False
                    continue
                elif self.current == 'saYunit':
                    y += str(self.saYunit()) + ' '
                    isBool = False
                    continue
                elif self.current == 'Baybay Literal' or self.current == 'Titik Literal':
                    y += str(self.val) + ' '
                    isBool = False
                elif self.current == 'at':
                    y += 'and' + ' '
                    isBool = False
                elif self.current == 'o':
                    y += 'or' + ' '
                    isBool = False
                elif self.current == '(':
                    y += self.current + ' '
                    enter += 1
                elif self.current == ')':
                    enter -= 1  
                elif self.current == '[':
                    self.semantic()
                    if self.current == 'Yunit Literal' or self.current == 'saYunit':
                        y += str(self.yunit_list()) + ' '
                        isBool = False
                    elif self.current == 'Punto Literal' or self.current == 'saPunto':
                        y += str(self.punto_list()) + ' '
                        isBool = False
                    elif self.current == 'Baybay Literal' or self.current == 'saBaybay':
                        y += str(self.baybay_list()) + ' '
                        isBool = False
                    elif self.current == 'Titik Literal' or self.current == 'saTitik':
                        y += str(self.titik_list()) + ' '
                        isBool = False
                    continue
                elif self.current in ['>', '<', '>=', '<=', '+', '-', '*', '/', '%', '**']:
                    if self.current in ['>', '<', '>=', '<=']:
                        isCond = True
                        ctr = True
                    y += self.current + ' '
                    if isBool == True:
                        self.semantic_error.append(f"TypeError on line {self.line}: Invalid operator for Boolean")
                        self.cont = False
                        return
                elif self.current in ['==', '!=']:
                    y += self.current + ' '
                    isBool = True
                    ctr = True
                else:
                    y += self.val + ' '
                    isBool = False
                self.semantic()
            if not isCond and not ctr:
                self.semantic_error.append(f"TypeError on line {self.line}: Invalid condition")
                self.cont = False
                return
            if self.cont == False:
                return
            try:
                return eval(y)
            except SyntaxError as e:
                self.semantic_error.append(f"SyntaxError on line {self.line}: {e}")
                self.cont = False
                return

    def kung(self):
        openctr = 1
        closectr = 0
        self.semantic()
        self.semantic()
        x = ''
        x = self.condition()
        if not self.cont:
            return
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        if x == True:
            while self.current != '}' and self.cont != False and self.isReturn == False:
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
                elif self.current == 'sulat':
                    self.sulat()
                    self.newline()
                elif self.current == 'kung':
                    self.kung()
                    self.newline()
                elif self.current == 'pili':
                    self.pili()
                    self.newline()
                elif self.current == 'Identifier':
                    self.expression()
                    self.newline()
                elif self.current == 'habang':
                    self.index += 1
                    self.habang()
                    self.index -= 1
                    self.newline()
                elif self.current == 'para':
                    self.index += 1
                    self.para()
                    self.index -= 1
                    self.newline()
                elif self.current == 'gawin':
                    self.index += 1
                    self.gawin()
                    self.index -= 1
                    self.newline()
                elif self.current == 'laktaw':
                    self.semantic()
                    self.newline()
                elif self.current == 'tapos':
                    self.cont == False
                if self.index == 1:
                    if self.current == 'tuloy':
                        self.isContinue = True
                        return
                    elif self.current == 'labas':
                        self.isBreak = True
                        ctr = 1
                        while ctr != 0:
                            if self.current == '{':
                                ctr += 1
                            elif self.current == '}':
                                ctr -= 1
                            self.semantic()
                            self.newline()
                        return
                if self.isFunc:
                    if self.current == 'balik':
                        self.isReturn = True
                        self.semantic()
                        self.return_value = self.return_val()
                        self.newline()
                        break
            self.semantic()
            self.newline()
            while self.current == 'kundi':
                self.semantic()
                self.semantic()
                x = self.condition()
                self.semantic()
                self.newline()
                self.semantic()
                self.newline()
                k_open = 1
                k_close = 0
                while k_open != k_close:
                    if self.current == '{':
                        k_open += 1
                    elif self.current == '}':
                        k_close += 1
                    self.semantic()
                    self.newline()
            if self.current == 'edi':
                self.semantic()
                self.newline()
                self.semantic()
                self.newline()
                e_open = 1
                e_close = 0
                while e_open != e_close:
                    if self.current == '{':
                        e_open += 1
                    elif self.current == '}':
                        e_close += 1
                    self.semantic()
                    self.newline()
            return
        else:
            while openctr != closectr:
                if self.current == '{':
                    openctr += 1
                elif self.current == '}':
                    closectr += 1
                self.semantic()
                self.newline()
            if self.current == 'kundi':
                while self.current == 'kundi':
                    bool_val = self.kundi()
                    self.newline()
                    if bool_val:
                        while self.current == 'kundi':
                            self.semantic()
                            self.semantic()
                            x = self.condition()
                            if not self.cont:
                                return
                            self.semantic()
                            self.newline()
                            self.semantic()
                            self.newline()
                            k_open = 1
                            k_close = 0
                            while k_open != k_close:
                                if self.current == '{':
                                    k_open += 1
                                elif self.current == '}':
                                    k_close += 1
                                self.semantic()
                                self.newline()
                        if self.current == 'edi':
                            self.semantic()
                            self.semantic()
                            e_open = 1
                            e_close = 0
                            while e_open != e_close:
                                if self.current == '{':
                                    e_open += 1
                                elif self.current == '}':
                                    e_close += 1
                                self.semantic()
                                self.newline()
                        return
            if self.current == 'edi':
                self.edi()
                self.newline()

    def kundi(self):
        openctr = 1
        closectr = 0
        self.semantic()
        self.semantic()
        x = ''
        x = self.condition()
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        if x == True:
            while self.current != '}' and self.cont != False and self.isReturn == False:
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
                elif self.current == 'sulat':
                    self.sulat()
                    self.newline()
                elif self.current == 'kung':
                    self.kung()
                    self.newline()
                elif self.current == 'pili':
                    self.pili()
                    self.newline()
                elif self.current == 'Identifier':
                    self.expression()
                    self.newline()
                elif self.current == 'habang':
                    self.index += 1
                    self.habang()
                    self.index -= 1
                    self.newline()
                elif self.current == 'para':
                    self.index += 1
                    self.para()
                    self.index -= 1
                    self.newline()
                elif self.current == 'gawin':
                    self.index += 1
                    self.gawin()
                    self.index -= 1
                    self.newline()
                elif self.current == 'tapos':
                    self.cont == False
                elif self.current == 'laktaw':
                    self.semantic()
                    self.newline()
                if self.index == 1:
                    if self.current == 'tuloy':
                        self.isContinue = True
                        return
                    elif self.current == 'labas':
                        self.isBreak = True
                        ctr = 1
                        while ctr != 0:
                            if self.current == '{':
                                ctr += 1
                            elif self.current == '}':
                                ctr -= 1
                            self.semantic()
                            self.newline()
                        return
                if self.isFunc:
                    if self.current == 'balik':
                        self.isReturn = True
                        self.semantic()
                        self.return_value = self.return_val()
                        self.newline()
                        break
            self.semantic()
        else:
            while openctr != closectr:
                if self.current == '{':
                    openctr += 1
                elif self.current == '}':
                    closectr += 1
                self.semantic()
                self.newline()
        return x
    
    def edi(self):
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        while self.current != '}' and self.cont != False:
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
                elif self.current == 'sulat':
                    self.sulat()
                    self.newline()
                elif self.current == 'kung':
                    self.kung()
                    self.newline()
                elif self.current == 'pili':
                    self.pili()
                    self.newline()
                elif self.current == 'Identifier':
                    self.expression()
                    self.newline()
                elif self.current == 'habang':
                    self.index += 1
                    self.habang()
                    self.index -= 1
                    self.newline()
                elif self.current == 'para':
                    self.index += 1
                    self.para()
                    self.index -= 1
                    self.newline()
                elif self.current == 'gawin':
                    self.index += 1
                    self.gawin()
                    self.index -= 1
                    self.newline()
                elif self.current == 'laktaw':
                    self.semantic()
                    self.newline()
                if self.index == 1:
                    if self.current == 'tuloy':
                        break
                    elif self.current == 'labas':
                        self.isBreak = True
                        ctr = 1
                        while ctr != 0:
                            if self.current == '{':
                                ctr += 1
                            elif self.current == '}':
                                ctr -= 1
                            self.semantic()
                            self.newline()
                        return
                if self.isFunc:
                    if self.current == 'balik':
                        self.isReturn = True
                        self.semantic()
                        self.return_value = self.return_val()
                        self.newline()
                        break
        self.semantic()

    def pili(self):
        y = None
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            try:
                x = self.all_variables[self.val].replace('titik','Titik Literal').replace('yunit', 'Yunit Literal')
            except:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                self.cont = False
                return
            y = self.Identifier() 
        else:
            x = self.current
            y = self.val
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        self.pag(x, y)

    def pag(self,x,y):
        while self.current == 'pag' and self.cont != False and self.current != 'kusa':
            self.semantic()
            if x == 'Yunit Literal':
                z = y == int(self.val)
            else:
                z = y == self.val
            if z:
                self.semantic()
                self.newline()
                self.semantic()
                self.newline()
                while self.current != '}' and self.cont != False:
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
                    elif self.current == 'sulat':
                        self.sulat()
                        self.newline()
                    elif self.current == 'kung':
                        self.kung()
                        self.newline()
                    elif self.current == 'pili':
                        self.pili()
                        self.newline()
                    elif self.current == 'Identifier':
                        self.expression()
                        self.newline()
                    elif self.current == 'habang':
                        self.index += 1
                        self.habang()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'para':
                        self.index += 1
                        self.para()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'gawin':
                        self.index += 1
                        self.gawin()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'laktaw':
                        self.semantic()
                        self.newline()
                    elif self.current == 'tapos':
                        self.cont == False
                    if self.index == 1:
                        if self.current == 'tuloy':
                            self.isContinue = True
                            return
                        elif self.current == 'labas':
                            self.isBreak = True
                            ctr = 1
                            while ctr != 0:
                                if self.current == '{':
                                    ctr += 1
                                elif self.current == '}':
                                    ctr -= 1
                                self.semantic()
                                self.newline()
                            return
                    if self.isFunc:
                        if self.current == 'balik':
                            self.isReturn = True
                            self.semantic()
                            self.return_value = self.return_val()
                            self.newline()
                            break
                self.semantic()
                while self.current == 'pag':
                    self.semantic()
                    self.semantic()
                    self.newline()
                    self.semantic()
                    self.newline()
                self.semantic()
                self.newline()
                self.semantic()
                self.newline()
                k_open = 1
                k_close = 0
                while k_open != k_close:
                    if self.current == '{':
                        k_open += 1
                    elif self.current == '}':
                        k_close += 1
                    self.semantic()
                    self.newline()
            else:                       
                    self.semantic()
                    self.newline()
                    self.semantic()
                    self.newline()
                    k_open = 1
                    k_close = 0
                    while k_open != k_close:
                        if self.current == '{':
                            k_open += 1
                        elif self.current == '}':
                            k_close += 1
                        self.semantic()
                        self.newline()
        if self.current == 'kusa':
            self.semantic()
            self.newline()
            self.semantic()
            self.newline()
            while self.current != '}' and self.cont != False:
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
                elif self.current == 'sulat':
                    self.sulat()
                    self.newline()
                elif self.current == 'kung':
                    self.kung()
                    self.newline()
                elif self.current == 'pili':
                    self.pili()
                    self.newline()
                elif self.current == 'Identifier':
                    self.expression()
                    self.newline()
                elif self.current == 'habang':
                    self.index += 1
                    self.habang()
                    self.index -= 1
                    self.newline()
                elif self.current == 'para':
                    self.index += 1
                    self.para()
                    self.index -= 1
                    self.newline()
                elif self.current == 'gawin':
                    self.index += 1
                    self.gawin()
                    self.index -= 1
                    self.newline()
                elif self.current == 'laktaw':
                    self.semantic()
                    self.newline()
                elif self.current == 'tapos':
                    self.cont == False
                if self.index == 1:
                    if self.current == 'tuloy':
                        self.isContinue = True
                        return
                if self.isFunc:
                    if self.current == 'balik':
                        self.isReturn = True
                        self.semantic()
                        self.return_value = self.return_val()
                        self.newline()
                        break
            self.semantic()
            self.newline()
            self.semantic()

    def habang(self):
        z = 0
        self.semantic()
        self.semantic()
        y = self.num
        x = self.condition()
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        while x == True:
            while self.current != '}' and self.cont != False and self.isReturn == False and self.isContinue == False and self.isBreak == False:
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
                elif self.current == 'sulat':
                    self.sulat()
                    self.newline()
                elif self.current == 'kung':
                    self.kung()
                    self.newline()
                elif self.current == 'pili':
                    self.pili()
                    self.newline()
                elif self.current == 'Identifier':
                    self.expression()
                    self.newline()
                elif self.current == 'habang':
                    self.index += 1
                    self.habang()
                    self.index -= 1
                    self.newline()
                elif self.current == 'para':
                    self.index += 1
                    self.para()
                    self.index -= 1
                    self.newline()
                elif self.current == 'gawin':
                    self.index += 1
                    self.gawin()
                    self.index -= 1
                    self.newline()
                elif self.current == 'tapos':
                    self.cont == False
                elif self.current == 'laktaw':
                    self.semantic()
                    self.newline()
                if self.index == 1:
                    if self.current == 'tuloy':
                        self.isContinue = True
                        break
                    elif self.current == 'labas':
                        self.isBreak = True
                        return
                if self.isFunc:
                    if self.current == 'balik':
                        self.isReturn = True
                        self.semantic()
                        self.return_value = self.return_val()
                        self.newline()
                        break
            if self.isContinue or self.isBreak:
                ctr = 1
                while ctr != 0:
                    if self.current == '{':
                        ctr += 1
                    elif self.current == '}':
                        ctr -= 1
                    self.semantic()
                    self.newline()
            if self.isBreak:
                return
            z = self.num
            self.num = y-1
            self.semantic()
            x = self.condition()
            self.isContinue = False
            self.semantic()
            self.newline()
            self.semantic()
            self.newline()
        self.num = z
        self.semantic()
        self.newline()

    def gawin(self):
        x = True
        self.semantic()
        self.newline()
        self.semantic()
        self.newline()
        z = self.num
        self.num = z-1
        self.semantic()
        while x:
            while self.current != '}' and self.cont != False and self.isReturn == False and self.isContinue == False and self.isBreak == False:
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
                elif self.current == 'sulat':
                    self.sulat()
                    self.newline()
                elif self.current == 'kung':
                    self.kung()
                    self.newline()
                elif self.current == 'pili':
                    self.pili()
                    self.newline()
                elif self.current == 'Identifier':
                    self.expression()
                    self.newline()
                elif self.current == 'habang':
                    self.index += 1
                    self.habang()
                    self.index -= 1
                    self.newline()
                elif self.current == 'para':
                    self.index += 1
                    self.para()
                    self.index -= 1
                    self.newline()
                elif self.current == 'gawin':
                    self.index += 1
                    self.gawin()
                    self.index -= 1
                    self.newline()
                elif self.current == 'laktaw':
                    self.semantic()
                    self.newline()
                elif self.current == 'tapos':
                    self.cont == False
                if self.index == 1:
                    if self.current == 'tuloy':
                        self.isContinue = True
                        return
                    elif self.current == 'labas':
                        self.isBreak = True
                        return
                if self.isFunc:
                    if self.current == 'balik':
                        self.isReturn = True
                        self.semantic()
                        self.return_value = self.return_val()
                        self.newline()
                        break
            if self.isContinue or self.isBreak:
                ctr = 1
                while ctr != 0:
                    if self.current == '{':
                        ctr += 1
                    elif self.current == '}':
                        ctr -= 1
                    self.semantic()
                    self.newline()
            if self.isBreak:
                return
            self.semantic()
            self.semantic()
            self.semantic()
            x = self.condition()
            self.semantic()
            if x:
                self.num = z-1
                self.semantic()
        self.newline() 

    def para(self):
        x = ''
        y = ''
        self.semantic()
        try: 
            x = self.all_variables[self.val]
            name = self.val
        except:
            self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
            self.cont = False
            return
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            try:
                y = self.all_variables[self.val]
            except:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                self.cont = False
                return
            if y not in ['baybay', 'yunit_list', 'punto_list', 'titik_list', 'baybay_list']:
                self.semantic_error.append(f"TypeError on line {self.line}: {name} is not iterable")
                self.cont = False
                return
            z = self.Identifier()
            if y == 'baybay' or y == 'baybay_list':
                if x != 'baybay':
                    self.semantic_error.append(f"TypeError on line {self.line}: {name} is not a valid variable")
                    self.cont = False
                    return  
            elif y == 'yunit_list':
                if x != 'yunit':
                    self.semantic_error.append(f"TypeError on line {self.line}: {name} is not a valid variable")
                    self.cont = False
                    return
            elif y == 'punto_list':
                if x != 'punto':
                    self.semantic_error.append(f"TypeError on line {self.line}: {name} is not a valid variable")
                    self.cont = False
                    return
            elif y == 'titik_list':
                if x != 'titik':
                    self.semantic_error.append(f"TypeError on line {self.line}: {name} is not a valid variable")
                    self.cont = False
                    return
            self.semantic()
            self.newline()
            num = self.num
            for a in z:
                self.variables[x][name] = a
                self.num = num - 1
                self.semantic()
                while self.current != '}' and self.cont != False and self.isReturn == False and self.isContinue == False:
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
                    elif self.current == 'sulat':
                        self.sulat()
                        self.newline()
                    elif self.current == 'kung':
                        self.kung()
                        self.newline()
                    elif self.current == 'pili':
                        self.pili()
                        self.newline()
                    elif self.current == 'Identifier':
                        self.expression()
                        self.newline()
                    elif self.current == 'habang':
                        self.index += 1
                        self.habang()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'para':
                        self.index += 1
                        self.para()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'gawin':
                        self.index += 1
                        self.gawin()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'tapos':
                        self.cont == False
                    elif self.current == 'laktaw':  
                        self.semantic()
                        self.newline()
                    if self.index == 1:
                        if self.current == 'tuloy':
                            self.isContinue = True
                            break
                        elif self.current == 'labas':
                            self.isBreak = True
                            return
                    if self.isFunc:
                        if self.current == 'balik':
                            self.isReturn = True
                            self.semantic()
                            self.return_value = self.return_val()
                            self.newline()
                            break
                if self.isContinue or self.isBreak:
                    ctr = 1
                    while ctr != 0:
                        if self.current == '{':
                            ctr += 1
                        elif self.current == '}':
                            ctr -= 1
                        self.semantic()
                        self.newline()
                if self.isBreak:
                    return
        elif self.current == 'lawak':
            self.semantic()
            b,c,d = self.lawak()
            self.semantic()
            self.newline()
            self.semantic()
            self.newline()
            num = self.num
            if x != 'yunit':
                self.semantic_error.append(f"TypeError on line {self.line}: {name} is not a yunit")
                self.cont = False
                return
            for a in range(b,c,d):
                self.variables[x][name] = a
                self.num = num - 1
                self.semantic()
                while self.current != '}' and self.cont != False and self.isReturn == False and self.isContinue == False:
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
                    elif self.current == 'sulat':
                        self.sulat()
                        self.newline()
                    elif self.current == 'kung':
                        self.kung()
                        self.newline()
                    elif self.current == 'pili':
                        self.pili()
                        self.newline()
                    elif self.current == 'Identifier':
                        self.expression()
                        self.newline()
                    elif self.current == 'habang':
                        self.index += 1
                        self.habang()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'para':
                        self.index += 1
                        self.para()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'gawin':
                        self.index += 1
                        self.gawin()
                        self.index -= 1
                        self.newline()
                    elif self.current == 'tapos':
                        self.cont == False
                    if self.index == 1:
                        if self.current == 'tuloy':
                            self.isContinue = True
                            break
                    if self.isFunc:
                        if self.current == 'balik':
                            self.isReturn = True
                            self.semantic()
                            self.return_value = self.return_val()
                            self.newline()
                            break
                if self.isContinue or self.isBreak:
                    ctr = 1
                    while ctr != 0:
                        if self.current == '{':
                            ctr += 1
                        elif self.current == '}':
                            ctr -= 1
                        self.semantic()
                        self.newline()
                if self.isBreak:
                    return
        self.semantic()
        self.newline()

    def lawak(self):
        a = 0
        b = 0
        c = 0
        self.semantic()
        if self.current == 'Identifier':
            try:
                x = self.all_variables[self.val]
                if x == 'yunit':
                    a = int(self.Identifier())
                else:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid variable")
                    self.cont = False
                    return
            except:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                self.cont = False
                return
        else:
            a = int(self.val)
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            try:
                x = self.all_variables[self.val]
                if x == 'yunit':
                    b = int(self.Identifier())
                else:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid variable")
                    self.cont = False
                    return
            except:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                self.cont = False
                return
        else:
            b = int(self.val)
        self.semantic()
        self.semantic()
        if self.current == 'Identifier':
            try:
                x = self.all_variables[self.val]
                if x == 'yunit':
                    c = int(self.Identifier())
                else:
                    self.semantic_error.append(f"TypeError on line {self.line}: {self.val} is not a valid variable")
                    self.cont = False
                    return
            except:
                self.semantic_error.append(f"NameError on line {self.line}: {self.val} is not defined")
                self.cont = False
                return
        else:
            c = int(self.val)
        self.semantic()
        return a,b,c


# UI --------------------------------------------------------------------------------------------------------------------------------
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#373737", foreground="white", fieldbackground="#373737", rowheight=45, font=("JetBrains Mono", 18))
style.configure("Treeview.Heading", font=("JetBrains Mono", 18))
style.map('Treeview', background=[('selected', '#141414')])

lexeme_tokens_area = ttk.Treeview(window, columns=("#1", "#2"), show="headings", style="Treeview.Heading")

def update_lexical_errors_text(text):
    lexical_errors_area.config(state="normal")  # Enable editing temporarily
    lexical_errors_area.delete("1.0", "end")
    lexical_errors_area.insert("1.0", text)
    lexical_errors_area.config(state="disabled")  # Disable editing
    
def add_lexical_errors(text):
    lexical_errors_area.config(state="normal")  # Enable editing temporarily
    lexical_errors_area.insert("end", text)
    lexical_errors_area.config(state="disabled")  # Disable editing

def update_lexeme_tokens_table():
    start=perf_counter()
    read = lx.Lexer('')
    read.tokens.clear()
    read.error.clear()
    lexeme_tokens_area.delete(*lexeme_tokens_area.get_children())
    line = coding_area.get("1.0", "end-1c")
    read = lx.Lexer(line)
    read.Tokenize()
    lexical_errors_text = ""    
    for token in read.tokens:
        lexeme_tokens_area.insert("", "end", values=(token['value'], token['token']), tags=('custom_font'))

    lexeme_tokens_area.heading("#1", text="Lexeme", anchor="center",)
    lexeme_tokens_area.heading("#2", text="Token Type", anchor="center")

    lexeme_tokens_area.column("#1", width=250, anchor="center")
    lexeme_tokens_area.column("#2", width=250, anchor="center")

    lexeme_tokens_area.column("#1", stretch=tk.YES)
    lexeme_tokens_area.column("#2", stretch=tk.YES)

    for e in read.error:
        lexical_errors_text += f"{e[0]}\n"
    if len(lexical_errors_text) == 0:
        update_lexical_errors_text("Lexical Compile Successfully")
    else:
           update_lexical_errors_text(lexical_errors_text)

    end=perf_counter()
    # print(end - start)

def syntax_analyzer():
    button = True
    read = lx.Lexer('')
    read.tokens.clear()
    read.error.clear()
    lexeme_tokens_area.delete(*lexeme_tokens_area.get_children())
    line = coding_area.get("1.0", "end-1c")
    read = lx.Lexer(line)
    read.Tokenize()
                
    for token in read.tokens:
        lexeme_tokens_area.insert("", "end", values=(token['value'], token['token']), tags=('custom_font'))

    lexeme_tokens_area.heading("#1", text="Lexeme", anchor="center",)
    lexeme_tokens_area.heading("#2", text="Token Type", anchor="center")

    lexeme_tokens_area.column("#1", width=250, anchor="center")
    lexeme_tokens_area.column("#2", width=250, anchor="center")
    
    lexeme_tokens_area.column("#1",  stretch=tk.YES)
    lexeme_tokens_area.column("#2", stretch=tk.YES)


    if len(read.error) > 0: 
        update_lexical_errors_text("Can't compile in Syntax.. Lexical errors occur")
        return
    # start=perf_counter()
    parser = syn.Parser(read.tokens)    
    parser.parse()
    update_lexical_errors_text(parser.errors[0])    
    if parser.errors[0] == "Syntax Completed: No errors found":
        update_lexical_errors_text("Syntax Completed: No errors found")
        update_lexical_errors_text("")
        update_lexical_errors_text("========================================  RUNNING  =======================================\n")
        comp = Compilation(read.tokens)
        comp.sem()
        # print(comp.variables)
        # print(comp.all_variables)
        # if comp.cont == False:
        #     update_lexical_errors_text(comp.semantic_error[0])
        #     return
        try:
            update_lexical_errors_text(comp.semantic_error[0])
        except:
            add_lexical_errors("\n=========================================  DONE  =========================================\n")
        # end=perf_counter()
    # print(end - start)


#Rectangle Task Bar
canvas.create_rectangle(0.0, 0.0, 1870.0, 55.0, fill="#E1DBD0", outline="")

#R1zz4l Icon
image_Rizzal = PhotoImage(file=relative_to_assets("Rizzal.png"))
Rizzal = canvas.create_image(30, 30, image=image_Rizzal)

#Rectangle Bottom   Ba
canvas.create_rectangle(0.0, 953.0, 1870.0, 990.0, fill="#E1DBD0", outline="black", width=1)

#Rectangle Left Side
canvas.create_rectangle(0.0, 54.0, 60.0, 953.0, fill="#32393D", outline="black", width=1)

#Rectangle Right Side
canvas.create_rectangle(1810.0, 54.0, 1870.0, 953.0, fill="#32393D", outline="black", width=1)

#Coding Area  Text
canvas.create_rectangle(59.0, 54.0, 1811.0, 907.0, fill="#000000", outline="")


coding_area = Text(window, bg="#000000", fg="#FFFFFF", insertbackground="white", height=31, width=120, wrap="none", font=("JetBrains Mono", 18), relief="flat", borderwidth=1)
coding_area.place(x=150, y=65)
placeholder_text = "Start coding here"
coding_area.insert("1.0", placeholder_text)
coding_area.tag_add("placeholder", "1.0", "1.0 lineend")
coding_area.tag_config("placeholder", foreground="#888888")

def remove_placeholder(event):
    if coding_area.tag_ranges("placeholder"):
        coding_area.delete("1.0", "1.0 lineend")
        coding_area.tag_remove("placeholder", "1.0", "1.0 lineend")

coding_area.bind("<FocusIn>", remove_placeholder)
coding_area_height = int(coding_area.cget("height"))

#Coding Area Numbering
line_numbers = Text(window, bg="#141414", fg="#7d7878", width=5, height=coding_area_height, wrap="none", font=("JetBrains Mono", 18), relief="flat", borderwidth=1)
line_numbers.place(x=60, y=65)
line_numbers.config(state="disabled")  # Making the line numbers non-editable

def update_line_numbers(event=None):
    line_numbers.config(state="normal")
    line_numbers.delete("1.0", "end")
    first_visible_line = int(coding_area.index("@0,0").split('.')[0])
    last_visible_line = int(coding_area.index("@0,{}".format(coding_area.winfo_height())).split('.')[0])
    for i in range(first_visible_line, last_visible_line + 1):
        line_numbers.insert("end", str(i).rjust(4) + '\n')
    line_numbers.config(state="disabled")

coding_area.bind("<Key>", update_line_numbers)
coding_area.bind("<Return>", update_line_numbers)
coding_area.bind("<ButtonRelease-1>", update_line_numbers)
coding_area.bind("<MouseWheel>", update_line_numbers)
coding_area.bind("<Configure>", update_line_numbers)
update_line_numbers()

#Lexical Error Window
lexical_error_frame = Frame(window, bg="#BFBFBF", highlightthickness=1, highlightbackground="black")
lexical_error_frame.place(x=59, y=600, width=1752, height=354)

lexical_error_canvas = Canvas(lexical_error_frame, bg="#BFBFBF", bd=0, highlightthickness=0, relief="ridge")
lexical_error_canvas.grid(row=0, column=0, sticky="nsew")
lexical_error_canvas.config(width=55, height=55)

lexical_errors_area = Text(window, bg="#BFBFBF", fg="#880808", font=("JetBrains Mono", 16),state="disabled", wrap="word", relief="flat", borderwidth=0)
lexical_errors_area.place(x=100, y=645, width=1128, height=290)

errorexpanded_geometry = (59, 600, 1752, 354)
errorcollapsed_geometry = (59, 879, 1752, 75)
errorcurrent_geometry = errorexpanded_geometry

image_errorcollapse = PhotoImage(file=relative_to_assets("errorcollapse.png"))
image_errorexpand = PhotoImage(file=relative_to_assets("errorexpand.png"))

def toggle_lexical_error_content():
    global errorcurrent_geometry
    if errorcurrent_geometry == errorexpanded_geometry:
        errorcurrent_geometry = errorcollapsed_geometry
        lexical_errors_area.place_forget()
    else:
        errorcurrent_geometry = errorexpanded_geometry
        lexical_errors_area.place(x=78, y=655, width=1128, height=290)
    x, y, width, height = errorcurrent_geometry
    lexical_error_frame.place(x=x, y=y, width=width, height=height)
    update_error_image()

toggle_errorbutton = tk.Button(window, image=image_errorcollapse, command=toggle_lexical_error_content, bg="#BFBFBF", relief="flat", borderwidth=1)
toggle_errorbutton.place(x=64, y=605)

def update_error_image():
    if errorcurrent_geometry == errorexpanded_geometry:
        toggle_errorbutton.configure(image=image_errorcollapse)
        toggle_errorbutton.place(x=64, y=605)
    else:
        toggle_errorbutton.configure(image=image_errorexpand)
        toggle_errorbutton.place(x=64, y=895)

#Lexeme Token Window
lexeme_token_frame = Frame(window, bg="#373737", highlightthickness=1, highlightbackground="black")
lexeme_token_frame.place(x=1230, y=54, width=581, height=900)

lexeme_token_canvas = Canvas(lexeme_token_frame, bg="#373737", bd=0, highlightthickness=0, relief="ridge")
lexeme_token_canvas.grid(row=0, column=0, sticky="nsew")
lexeme_token_canvas.config(width=63, height=63)

lexeme_tokens_area = ttk.Treeview(window, columns=("#1", "#2"), show="headings")
lexeme_tokens_area.place(x=1250, y=68, width=540, height=871)

lexeme_tokens_area.tag_configure('custom_font', font=("JetBrains Mono", 16))
    
tokenexpanded_geometry = (1230, 54, 581, 900)
tokencollapsed_geometry = (1746, 54, 65, 900)
tokencurrent_geometry = tokenexpanded_geometry

image_tokencollapse = PhotoImage(file=relative_to_assets("tokencollapse.png"))
image_tokenexpand = PhotoImage(file=relative_to_assets("tokenexpand.png"))

def toggle_lexeme_token_content():
    global tokencurrent_geometry
    if tokencurrent_geometry == tokenexpanded_geometry:
        tokencurrent_geometry = tokencollapsed_geometry
        lexeme_tokens_area.place_forget()
    else:
        tokencurrent_geometry = tokenexpanded_geometry
        lexeme_tokens_area.place(x=1250, y=68, width=540, height=871)
    x, y, width, height = tokencurrent_geometry
    lexeme_token_frame.place(x=x, y=y, width=width, height=height)
    update_token_image()

toggle_tokenbutton = tk.Button(window, image=image_tokencollapse, command=toggle_lexeme_token_content, bg="#373737", relief="flat", borderwidth=1)
toggle_tokenbutton.place(x=1195, y=55)

def update_token_image():
    if tokencurrent_geometry == tokenexpanded_geometry:
        toggle_tokenbutton.configure(image=image_tokencollapse)
        toggle_tokenbutton.place(x=1195, y=55)
    else:
        toggle_tokenbutton.configure(image=image_tokenexpand)
        toggle_tokenbutton.place(x=1711, y=55)

#Lexical Run Button
image_lexicalbutton = PhotoImage(file=relative_to_assets("lexicalbutton.png"))
lexical_button = tk.Button(window, image=image_lexicalbutton, bg="#E1DBD0", relief="flat", borderwidth=1, command=update_lexeme_tokens_table)
lexical_button.place(x=123, y=4)
lexical_button.config(padx=42, pady=13)

#Syntax Run Button
image_syntaxbutton = PhotoImage(file=relative_to_assets("syntaxbutton.png"))
syntax_button = tk.Button(window, image=image_syntaxbutton, bg="#E1DBD0", relief="flat", borderwidth=1, command=syntax_analyzer)
syntax_button.place(x=233, y=4)
syntax_button.config(padx=42, pady=13)

#Semantic Run Button
image_semanticbutton = PhotoImage(file=relative_to_assets("semanticbutton.png"))
semantic_button = tk.Button(window, image=image_semanticbutton, bg="#E1DBD0", relief="flat", borderwidth=1)
semantic_button.place(x=335, y=4)
semantic_button.config(padx=42, pady=13)

#Settings Button
image_settings = PhotoImage(file=relative_to_assets("settings.png"))
settings_button = tk.Button(window, image=image_settings, bg="#E1DBD0", relief="flat", borderwidth=1)
settings_button.place(x=1818, y=4)
settings_button.config(padx=42, pady=13)

#Run Button
image_run = PhotoImage(file=relative_to_assets("run.png"))
run_button = tk.Button(window, image=image_run, bg="#32393D", relief="flat", borderwidth=1)
run_button.place(x=7, y=68)
run_button.config(padx=42, pady=13)

#Debug Button
image_debug= PhotoImage(file=relative_to_assets("debug.png"))
debug_button = tk.Button(window, image=image_debug, bg="#32393D", relief="flat", borderwidth=1)
debug_button.place(x=7, y=126)
debug_button.config(padx=42, pady=13)

#Zoom In Button
image_zoomin= PhotoImage(file=relative_to_assets("zoomin.png"))
zoomin_button = tk.Button(window, image=image_zoomin, bg="#32393D", relief="flat", borderwidth=1)
zoomin_button.place(x=7, y=184)
zoomin_button.config(padx=42, pady=13)

#Zoom Out Button
image_zoomout= PhotoImage(file=relative_to_assets("zoomout.png"))
zoomout_button = tk.Button(window, image=image_zoomout, bg="#32393D", relief="flat", borderwidth=1)
zoomout_button.place(x=7, y=242)
zoomout_button.config(padx=42, pady=13)

#Vertical Dots Button
image_verticalmore= PhotoImage(file=relative_to_assets("verticalmore.png"))
verticalmore_button = tk.Button(window, image=image_verticalmore, bg="#E1DBD0", relief="flat", borderwidth=1)
verticalmore_button.place(x=1699, y=4)
verticalmore_button.config(padx=42, pady=13)

#Main Menu Button
image_mainmenu= PhotoImage(file=relative_to_assets("mainmenu.png"))
mainmenu_button = tk.Button(window, image=image_mainmenu, bg="#E1DBD0", relief="flat", borderwidth=1)
mainmenu_button.place(x=61, y=4)
mainmenu_button.config(padx=42, pady=13)

#Search Button
image_search = PhotoImage(file=relative_to_assets("search.png"))
search_button = tk.Button(window, image=image_search, bg="#E1DBD0", relief="flat", borderwidth=1)
search_button.place(x=1759, y=4)
search_button.config(padx=42, pady=13)

#Unlock Button
image_unlock = PhotoImage(file=relative_to_assets("unlock.png"))
unlock_button = tk.Button(window, image=image_unlock, bg="#E1DBD0", relief="flat", borderwidth=1)
unlock_button.place(x=1825, y=957)
unlock_button.config(padx=42, pady=13)

#Horizontal Dots Button
image_horizontalmore= PhotoImage(file=relative_to_assets("horizontalmore.png"))
horizontalmore_button = tk.Button(window, image=image_horizontalmore, bg="#32393D", relief="flat", borderwidth=1)
horizontalmore_button.place(x=7, y=300)
horizontalmore_button.config(padx=42, pady=13)

window.resizable(False, False)
window.mainloop()
