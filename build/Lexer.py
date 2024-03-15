arop = '+-*/%'
alphanum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
digits = "123456789"
delim1 = [' ', '']
delim2 = [' ', '\n', '$', '']
delim3 = [' ', '(','']
delim4 = [' ',',',')', '']
delim5 = [' ', '{', '', '$', '\n']
delim6 = [' ', ')', ']', '}', ',', '\n', '$', '']
delim7 = [' ', '\n', '$', '']
delim8 = [' ', '(', '[', '{', '~', '\n', '$', '']
delim9 = [' ', '(', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
          'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
          '4', '5', '6', '7', '8', '9', '']
delim10 = ['+', '-', '*', '/', '%', '<', '>', '=', '!', ')', ']', '{', '}', ',', ';', ' ', '\n', '$', '']
delim11 = ['+', '-', '*', '/', '%', '(', ')', '<', '>', '=', '!', '[', ']', '{','}', ',', '.', ';', ' ', '\n', '$', '']
delim12 = [' ', ')', ']','{', '}', ',', ';' ,'+', '=', '\n', '!', '$','']
delim13 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '']
delim14 = [' ', '(', '[', '"', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
           '9', '']
delim15 = [' ', '(', '[', '{', '"', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q',
           'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
           '9','\'' ,'']
delim16 = [' ', ')', ']', '{' ,'}', ',', '=', '\n', '!', '$', '']
delim17 = [' ', '"', '(', '[', ']', '{', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9','\'', '']
delim18 = [' ','$', ',', '+', ')', '[', ']', '{' , '}', '!', '=', '\n','']
delim19 = [' ', '~', '"', '}', '\n', '$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9', '']
delim20 = [' ', ']', ')' ,'{ ', '}', '!', '=', 't' ,'\n', '$', ',' ,'']
delim21 = ['"' ,' ', '~', '(', ')', '[', '{', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 
           'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', 
           '7', '8','9','\'', '']
delim22 = [' ', '+', '-', '*', '/', '%', '!', '=', '>', '<', '{', ')', ']', '}', ',', '\n', '$', '']
delim23 = [' ', '"', '(', '[', '{', '~', '\n', '$', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9','\'', '']
delim24 = [' ', '"', '(', '[', '{', '~', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
           '4', '5', '6', '7', '8', '9','\'', '']
delim25 = ['\n' ]
delim26 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','(','']
delim27 = ['+', '-', '*', '/', '%', '<', '>', '=', '!', ')', ']', '}', ',', ' ', '\n', '$', '']\

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.error = []
        self.index = -1
        self.line = 1
        self.next = ''
        self.current = ''
        self.string = ''
        self.identifiers_no = 0
        self.error_line = 1
        self.stringline = ''
        self.yunitLimit = 0
        self.puntoLimit = 0
        self.numToken = None

    def traverse(self):
        self.index += 1
        if self.index < len(self.code) and self.index + 1 < len(self.code):
            self.current = self.code[self.index]
            self.next = self.code[self.index + 1]
        elif self.index < len(self.code) and self.index == len(self.code) - 1:
            self.current = self.code[self.index]
            self.next = ''

    def Tokenize(self):
        while self.index < len(self.code) - 1:
            self.traverse()
            self.Lexical()

    def state(self, character):
        if self.current == character:
            self.string += self.current
            self.traverse()
            return True
        elif self.current in character:
            self.string += self.current
            self.traverse()
            return True
        return False

    def final_state(self, character):
        if self.current == character:
            self.string += self.current
            return True

    def delim_check_current(self, delim, token, Lexical=False):
        if self.current in delim or self.index == len(self.code):
            self.tokens.append([self.string, token, self.error_line])
            self.string = ''
            if Lexical is True:
                self.Lexical()
            return True
        return False

    def delim_check_current_arop(self, delim, token, Lexical=False):
        if self.next == '' and self.index == len(self.code):
            self.tokens.append([self.string, token, self.error_line])
            self.string = ''
            self.index += 1
            return True
        if self.current in delim or self.index == len(self.code):
            self.tokens.append([self.string, token, self.error_line])
            self.string = ''
            if Lexical is True:
                self.Lexical()
            return True
        return False

    def delim_check_next(self, delim, token):
        if self.next in delim:
            self.tokens.append([self.string, token, self.error_line])
            self.string = ''
            return True
        return False

    def delim(self):
        if (self.next in alphanum or self.next == '_') and self.string != '.':
            self.identifiers()
            return
        else:
            self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
            self.string = ''
            return
        
    def delim2(self):
        self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
        self.string = ''
        return
    
    def if_identifiers(self):
        if self.next == '' and self.index >= len(self.code):
            self.identifiers_no += 1
            self.tokens.append([self.string, f'Identifier{self.identifiers_no}',self.error_line])
            self.string = ''
            return
        elif self.current in delim11:
            self.identifiers_no += 1
            self.tokens.append([self.string, f'Identifier{self.identifiers_no}',self.error_line])
            self.string = ''
            self.Lexical()
            return
        elif self.current in alphanum or self.current == '_':
            self.string += self.current
            self.identifiers()
        else:
            self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
            self.string = ''
            self.Lexical()

    def identifiers(self):
        len_ident = len(self.string)
        while len_ident < 15 and self.index < len(self.code) - 1:
            self.traverse()
            if self.current in delim11:
                self.identifiers_no += 1
                self.tokens.append([self.string, f'Identifier{self.identifiers_no}',self.error_line])
                self.string = ''
                self.Lexical()
                return
            elif self.current in alphanum or self.current == '_':
                self.string += self.current
                len_ident += 1
                if self.next in delim11:
                    self.identifiers_no += 1
                    self.tokens.append([self.string, f'Identifier{self.identifiers_no}',self.error_line])
                    self.string = ''
                    return
            else:
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
        if self.next in delim11:
            self.identifiers_no += 1
            self.tokens.append([self.string, f'Identifier{self.identifiers_no}',self.error_line])
        else:
            self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
        self.string = ''
        return

    def limit_yunit_punto(self, yunitlimit, puntolimit):
        self.numToken = "Yunit Literal"
        while True:
            self.inc_numLimit()
            if (self.yunitLimit <= yunitlimit and self.puntoLimit <= puntolimit and self.current in num or self.current == '.') and self.index != len(self.code):
                if self.current == '.':
                    self.string += self.current
                    self.traverse()
                    self.numToken = "Punto Literal"
                elif self.current in num and self.next in num or self.next == '.':
                    self.string += self.current
                    self.traverse()
                elif self.current in num and self.next in delim27 and self.numToken == 'Punto Literal':
                    self.string += self.current
                    self.tokens.append([self.string, self.numToken, self.error_line])
                    self.string = ''
                    self.inc_numLimit(clear=True)
                    break
                elif self.current in num and self.next in delim10 and self.numToken == 'Yunit Literal':
                    self.string += self.current
                    self.tokens.append([self.string, self.numToken, self.error_line])
                    self.string = ''
                    self.inc_numLimit(clear=True)
                    break
                else:
                    self.string += self.current
                    self.traverse()
                    self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                    self.string = ''
                    self.inc_numLimit(clear=True)
                    self.index -= 1
                    break
            elif self.index == len(self.code):
                self.tokens.append([self.string, self.numToken, self.error_line])
                self.string = ''
                self.inc_numLimit(clear=True)
                break
            else:
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.inc_numLimit(clear=True)
                self.index -= 1
                break

    def inc_numLimit(self, clear=False):
        if clear is True:
            self.yunitLimit = 0
            self.puntoLimit = 0
        elif self.current in num:
            if self.numToken == "Yunit Literal":
                self.yunitLimit += 1
            elif self.numToken == "Punto Literal":
                self.puntoLimit += 1

    def single_line(self):
        self.string = ''
        while self.next != '\n' and self.index < len(self.code):
            self.string += self.current
            self.traverse()
        self.tokens.append([self.string, 'Line-comment', self.error_line])
        self.string = ''
        return

    def literals(self):
        while self.current != '\"' and self.current != '\n' and self.index < len(self.code):
            self.string += self.current
            self.traverse() 

        if self.index < len(self.code) and self.current == '\"':
            self.string += self.current
            if self.next in delim12:
                self.tokens.append([self.string, 'Baybay Literal', self.error_line])
            else:
                self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
        elif self.index < len(self.code) and self.current == '\n':
            self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
            self.Lexical()
        else:
            self.error.append([f'Line {self.error_line}: Lexical error: \'{self.string}\' invalid character'])
        self.string = ''
        return

    def string2(self):
        self.string = ''
        for i in self.stringline:
            if i == '\n':
                break
            if i in alphanum or i == '_':
                self.string += i
                continue
            else:
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.error.append([f'Line {self.error_line}: Lexical error:\'{i}\' invalid character'])
                self.string = ''
                continue
        if self.current in alphanum or self.next == '_':
            self.identifiers()
            return
        if self.string:
            if self.current in delim11:
                self.identifiers_no += 1
                self.tokens.append([self.string, f'Identifier{self.identifiers_no}',self.error_line])
        self.string = ''
        self.stringline = ''
        return
    
    def titik(self):
        if self.index == len(self.code):
                self.error.append([f'Line{self.error_line}: Lexical error:\'{self.current}\' invalid character'])
                self.string = ''
                return
        elif self.state('\''):
            if self.delim_check_current(delim16,'Titik Literal'):
                self.string = ''
            else:
                self.delim2()
            self.Lexical()
            return
        elif self.current != '' and self.next == '\'':
            if self.current == '\n':
                self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid character'])
                self.string = ''
            else:
                self.string += self.current
                self.traverse()
                if self.state('\''):
                    if self.delim_check_current(delim16,'Titik Literal'):
                        self.string = ''
                    else:
                        self.delim2()
            print(self.string)
            self.Lexical()
        else:
            if self.index != len(self.code):
                self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid character'])
                self.string = ''
                if self.current in alphabet:
                    self.if_identifiers()
                else:
                    self.Lexical()
                return

    def gssSawa(self):
        if self.index < len(self.code): 
            x = self.index  
            if self.code[x] == '.':
                if x < len(self.code)-1: x += 1
                if self.code[x] == 's':
                    if x < len(self.code)-1: x += 1
                    if self.code[x] == 's':
                        if x < len(self.code)-1: x += 1
                        if self.code[x] == 'S':
                            if x < len(self.code)-1: x += 1
                            if self.code[x] == 'a':
                                if x < len(self.code)-1: x += 1
                                if self.code[x] == 'w':
                                    if x < len(self.code)-1: x += 1
                                    if self.code[x] == 'a':
                                        x += 1
                                        if x > len(self.code) - 1:
                                            return True
                                        else:
                                            if self.code[x] in delim2:
                                                return True
        return False

    def ggssSawa(self):
        if self.index < len(self.code): 
            x = self.index 
            if self.code[x] == '.':
                if x < len(self.code)-1: x += 1
                if self.code[x] == 's':
                    if x < len(self.code)-1: x += 1
                    if self.code[x] == 's':
                        if x < len(self.code)-1: x += 1
                        if self.code[x] == 'S':
                            if x < len(self.code)-1: x += 1
                            if self.code[x] == 'a':
                                if x < len(self.code)-1: x += 1
                                if self.code[x] == 'w':
                                    if x < len(self.code)-1: x += 1
                                    if self.code[x] == 'a':
                                        x += 1
                                        if x > len(self.code) - 1:
                                            return True
                                        else:
                                            if self.code[x] in delim2:
                                                return True
        return False
    # THE GREAT SNAKES N LADDERS ===================

    def Lexical(self):
        if self.code:
            if self.current == '\n':
                self.error_line += 1
                self.tokens.append(['\\n', 'newline', self.error_line])
                self.string = ''
                return
            elif self.current == '\t':
                self.tokens.append(['\\t', 'tab', self.error_line])
                self.string = ''
                return
            elif self.current == ' ':
                self.tokens.append(['\' \'', 'space', self.error_line])
                self.string = ''
                return
            elif self.state('\''):
                self.titik()
            elif self.state('A'):
                if self.state('t'):
                    if self.state('t'):
                        if self.state('r'):
                            if self.state('i'):
                                if self.state('b'):
                                    if self.state('E'):
                                        if self.state('r'):
                                            if self.state('r'):
                                                if self.state('o'):
                                                    if self.final_state('r'):
                                                        if self.delim_check_next(delim4, 'AttribError'):
                                                            return
                                                        else:
                                                            self.delim()
                                                            return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('a'):
                if self.final_state('t'):
                    if self.delim_check_next(delim1, 'at'):
                        return
                    else:
                        self.delim()
                        return
                elif self.final_state('y'):
                    if self.delim_check_next(delim1, 'ay'):
                        return
                    else:
                        self.delim()
                        return
                self.if_identifiers()
                return
            elif self.state('b'):
                if self.state('a'):
                    if self.state('l'):
                        if self.state('i'):
                            if self.final_state('k'):
                                if self.delim_check_next(delim8, 'balik'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('y'):
                        if self.state('b'):
                            if self.state('a'):
                                if self.final_state('y'):
                                    if self.delim_check_next(delim3, 'baybay'):
                                        return
                                    else:
                                        self.delim()
                                        return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('i'):
                    if self.state('l'):
                        if self.state('a'):
                            if self.state('n'):
                                if self.final_state('g'):
                                    if self.delim_check_next(delim1, 'bilang'):
                                        return
                                    else:
                                        self.delim()
                                        return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('o'):
                    if self.state('o'):
                        if self.final_state('l'):
                            if self.delim_check_next(delim3, 'bool'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('u'):
                    if self.state('r'):
                        if self.final_state('a'):
                            if self.delim_check_next(delim1, 'bura'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    elif self.state('k'):
                        if self.state('o'):
                            if self.final_state('d'):
                                if self.delim_check_next(delim3, 'bukod'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('d'):
                if self.state('i'):
                    if self.delim_check_current(delim3, 'di'):
                        return
                    elif self.state('k'):
                        if self.final_state('s'):
                            if self.delim_check_next(delim3, 'diks'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    elif self.current not in alphanum:
                        self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                        self.string = ''
                        self.Lexical()
                        return
                self.if_identifiers()
                return
            elif self.state('E'):
                if self.state('x'):
                    if self.state('c'):
                        if self.state('e'):
                            if self.state('s'):
                                if self.state('s'):
                                    if self.state('E'):
                                        if self.state('r'):
                                            if self.state('r'):
                                                if self.state('o'):
                                                    if self.final_state('r'):
                                                        if self.delim_check_next(delim4, 'ExcessError'):
                                                            return
                                                        else:
                                                            self.delim()
                                                            return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('e'):
                if self.state('d'):
                    if self.final_state('i'):
                        if self.delim_check_next(delim5, 'edi'):
                            return
                        else:
                            self.delim()
                            return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('g'):
                if self.state('a'):
                    if self.state('w'):
                        if self.state('i'):
                            if self.final_state('n'):
                                if self.delim_check_next(delim5, 'gawin'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.current == '.':
                    if self.gssSawa():
                        if self.state('.'):
                            if self.state('s'):
                                if self.state('s'):
                                    if self.state('S'):
                                        if self.state('a'):
                                            if self.state('w'):
                                                if self.final_state('a'):
                                                    if self.delim_check_next(delim2, 'g.ssSawa'):
                                                        return
                                                    else:
                                                        self.delim()
                                                        return
                    else:
                        self.identifiers_no += 1
                        self.tokens.append([self.string, f'Identifier{self.identifiers_no}', self.error_line])
                        self.string = ''
                        self.Lexical()
                        return
                elif self.index <= len(self.code)-1:
                    if self.state('g'):
                        if self.current == '.':
                            if self.ggssSawa():
                                if self.state('.'):
                                    if self.state('s'):
                                        if self.state('s'):
                                            if self.state('S'):
                                                if self.state('a'):
                                                    if self.state('w'):
                                                        if self.final_state('a'):
                                                            if self.delim_check_next(delim2, 'gg.ssSawa'):
                                                                return
                                                            else:
                                                                self.delim()
                                                                return
                            else:
                                self.identifiers_no += 1
                                self.tokens.append([self.string, f'Identifier{self.identifiers_no}', self.error_line])
                                self.string = ''
                                self.Lexical()
                                return
                self.if_identifiers()
                return
            elif self.state('h'):
                if self.state('a'):
                    if self.state('b'):
                        if self.state('a'):
                            if self.state('n'):
                                if self.final_state('g'):
                                    if self.delim_check_next(delim3, 'habang'):
                                        return
                                    else:
                                        self.delim()
                                        return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('k'):
                        if self.state('o'):
                            if self.final_state('t'):
                                if self.delim_check_next(delim1, 'hakot'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('I'):
                if self.state('m'):
                    if self.state('p'):
                        if self.state('o'):
                            if self.state('r'):
                                if self.state('t'):
                                    if self.state('E'):
                                        if self.state('r'):
                                            if self.state('r'):
                                                if self.state('o'):
                                                    if self.final_state('r'):
                                                        if self.delim_check_next(delim4, 'ImportError'):
                                                            return
                                                        else:
                                                            self.delim()
                                                            return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('n'):
                    if self.state('d'):
                        if self.state('e'):
                            if self.state('x'):
                                if self.state('E'):
                                    if self.state('r'):
                                        if self.state('r'):
                                            if self.state('o'):
                                                if self.final_state('r'):
                                                    if self.delim_check_next(delim4, 'IndexError'):
                                                        return
                                                    else:
                                                        self.delim()
                                                        return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('i'):
                if self.state('b'):
                    if self.state('a'):
                        if self.state('n'):
                            if self.final_state('g'):
                                if self.delim_check_next(delim1, 'ibang'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('K'):
                if self.state('e'):
                    if self.state('y'):
                        if self.state('E'):
                            if self.state('r'):
                                if self.state('r'):
                                    if self.state('o'):
                                        if self.final_state('r'):
                                            if self.delim_check_next(delim4, 'KeyError'):
                                                return
                                            else:
                                                self.delim()
                                                return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('k'):
                if self.state('u'):
                    if self.state('h'):
                        if self.final_state('a'):
                            if self.delim_check_next(delim3, 'kuha'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    elif self.state('s'):
                        if self.final_state('a'):
                            if self.delim_check_next(delim5, 'kusa'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    elif self.state('n'):
                        if self.state('d'):
                            if self.final_state('i'):
                                if self.delim_check_next(delim3, 'kundi'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        elif self.final_state('g'):
                            if self.delim_check_next(delim3, 'kung'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('l'):
                if self.state('a'):
                    if self.state('b'):
                        if self.state('a'):
                            if self.final_state('s'):
                                if self.delim_check_next(delim7, 'labas'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('k'):
                        if self.state('t'):
                            if self.state('a'):
                                if self.final_state('w'):
                                    if self.delim_check_next(delim7, 'laktaw'):
                                        return
                                    else:
                                        self.delim()
                                        return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('w'):
                        if self.state('a'):
                            if self.final_state('k'):
                                if self.delim_check_next(delim3, 'lawak'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.final_state('o'):
                if self.delim_check_next(delim1, 'o'):
                    return
                else:
                    self.delim()
                    return
            elif self.state('M'):
                if self.state('e'):
                    if self.state('m'):
                        if self.state('o'):
                            if self.state('r'):
                                if self.state('y'):
                                    if self.state('E'):
                                        if self.state('r'):
                                            if self.state('r'):
                                                if self.state('o'):
                                                    if self.final_state('r'):
                                                        if self.delim_check_next(delim4, 'MemoryError'):
                                                            return
                                                        else:
                                                            self.delim()
                                                            return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('N'):
                if self.state('a'):
                    if self.state('m'):
                        if self.state('e'):
                            if self.state('E'):
                                if self.state('r'):
                                    if self.state('r'):
                                        if self.state('o'):
                                            if self.final_state('r'):
                                                if self.delim_check_next(delim4, 'NameError'):
                                                    return
                                                else:
                                                    self.delim()
                                                    return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('p'):
                if self.state('a'):
                    if self.state('r'):
                        if self.final_state('a'):
                            if self.delim_check_next(delim3, 'para'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    elif self.final_state('g'):
                        if self.delim_check_next(delim1, 'pag'):
                            return
                        else:
                            self.delim()
                            return
                    self.if_identifiers()
                    return
                elif self.state('i'):
                    if self.state('l'):
                        if self.final_state('i'):
                            if self.delim_check_next(delim3, 'pili'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('u'):
                    if self.state('n'):
                        if self.state('t'): 
                            if self.final_state('o'):
                                if self.delim_check_next(delim3, 'punto'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('P'):
                if self.state('e'):
                    if self.state('k'):
                        if self.final_state('e'):
                            if self.delim_check_next(delim6, 'Peke'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('s'):
                if self.final_state('a'):
                    if self.delim_check_next(delim1, 'sa'):
                        return
                    else:
                        self.delim()
                        return
                elif self.state('u'):
                    if self.state('l'):
                        if self.state('a'):
                            if self.final_state('t'):
                                if self.delim_check_next(delim3, 'sulat'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('b'):
                        if self.state('o'):
                            if self.final_state('k'):
                                if self.delim_check_next(delim5, 'subok'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('T'):
                if self.state('y'):
                    if self.state('p'):
                        if self.state('e'):
                            if self.state('E'):
                                if self.state('r'):
                                    if self.state('r'):
                                        if self.state('o'):
                                            if self.final_state('r'):
                                                if self.delim_check_next(delim4, 'TypeError'):
                                                    return
                                                else:
                                                    self.delim()
                                                    return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                if self.state('o'):
                    if self.state('t'):
                        if self.state('o'):
                            if self.final_state('o'):
                                if self.delim_check_next(delim6, 'Totoo'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('t'):
                if self.state('a'):
                    if self.state('k'):
                        if self.state('d'):
                            if self.final_state('a'):
                                if self.delim_check_next(delim1, 'takda'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('l'):
                        if self.final_state('a'):
                            if self.delim_check_next(delim3, 'tala'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    elif self.state('p'):
                        if self.state('o'):
                            if self.final_state('s'):
                                if self.delim_check_next(delim7, 'tapos'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('i'):
                    if self.state('t'):
                        if self.state('i'):
                            if self.final_state('k'):
                                if self.delim_check_next(delim3, 'titik'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                elif self.state('u'):
                    if self.state('l'):
                        if self.state('o'):
                            if self.final_state('y'):
                                if self.delim_check_next(delim7, 'tuloy'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    elif self.state('w'):
                        if self.state('i'):
                            if self.state('n'):
                                if self.final_state('g'):
                                    if self.delim_check_next(delim3, 'tuwing'):
                                        return
                                    else:
                                        self.delim()
                                        return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('V'):
                if self.state('a'):
                    if self.state('l'):
                        if self.state('u'):
                            if self.state('e'):
                                if self.state('E'):
                                    if self.state('r'):
                                        if self.state('r'):
                                            if self.state('o'):
                                                if self.final_state('r'):
                                                    if self.delim_check_next(delim4, 'ValueError'):
                                                        return
                                                    else:
                                                        self.delim()
                                                        return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('W'):
                if self.state('a'):
                    if self.state('l'):
                        if self.final_state('a'):
                            if self.delim_check_next(delim6, 'Wala'):
                                return
                            else:
                                self.delim()
                                return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('y'):
                if self.state('u'):
                    if self.state('n'):
                        if self.state('i'):
                            if self.final_state('t'):
                                if self.delim_check_next(delim3, 'yunit'):
                                    return
                                else:
                                    self.delim()
                                    return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('Z'):
                if self.state('e'):
                    if self.state('r'):
                        if self.state('o'):
                            if self.state('D'):
                                if self.state('i'):
                                    if self.state('v'):
                                        if self.state('E'):
                                            if self.state('r'):
                                                if self.state('r'):
                                                    if self.state('o'):
                                                        if self.final_state('r'):
                                                            if self.delim_check_next(delim4, 'ZeroDivError'):
                                                                return
                                                            else:
                                                                self.delim()
                                                                return
                                                        self.if_identifiers()
                                                        return
                                                    self.if_identifiers()
                                                    return
                                                self.if_identifiers()
                                                return
                                            self.if_identifiers()
                                            return
                                        self.if_identifiers()
                                        return
                                    self.if_identifiers()
                                    return
                                self.if_identifiers()
                                return
                            self.if_identifiers()
                            return
                        self.if_identifiers()
                        return
                    self.if_identifiers()
                    return
                self.if_identifiers()
                return
            elif self.state('='):
                if self.delim_check_current_arop(delim15, '=', Lexical=True):
                    return
                elif self.final_state('='):
                    if self.delim_check_next(delim15, '=='):
                        return
                    else:
                        self.delim2()
                        return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.state('+'):
                if self.delim_check_current_arop(delim14, '+', Lexical=True):
                    return
                elif self.final_state('='):
                    if self.delim_check_next(delim14, '+='):
                        return
                    else:
                        self.delim2()
                        return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.state('-'):
                if self.delim_check_current_arop(delim9, '-', Lexical=True):
                    return
                elif self.final_state('='):
                    if self.delim_check_next(delim9, '-='):
                        return
                    else:
                        self.delim2()
                        return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.state('*'):
                if self.delim_check_current_arop(delim9, '*', Lexical=True):
                    return
                elif self.final_state('='):
                    if self.delim_check_next(delim9, '*='):
                        return
                    else:
                        self.delim2()
                        return
                elif self.final_state('*'):
                    if self.delim_check_next(delim9, '**'):
                        return
                    else:
                        self.delim2()
                        return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.state('/'):
                if self.final_state('='):
                    if self.delim_check_next(delim9, '/='):
                        return
                    else:
                        self.delim2()
                        return
                elif self.delim_check_current_arop(delim9, '/', Lexical=True):
                    return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.final_state('%'):
                if self.delim_check_next(delim9, '%'):
                    return
                else:
                    self.delim2()
                    return
            elif self.state('!'):
                if self.final_state('='):
                    if self.delim_check_next(delim15, '!='):
                        return
                    else:
                        self.delim2()
                        return
                if self.next == '' and self.index == len(self.code):
                    self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid character'])
                    self.string = ''
                    return
                self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.state('<'):
                if self.delim_check_current_arop(delim9, '<', Lexical=True):
                    return
                elif self.final_state('='):
                    if self.delim_check_next(delim9, '<='):
                        return
                    else:
                        self.delim2()
                        return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.state('>'):
                if self.delim_check_current_arop(delim9, '>', Lexical=True):
                    return
                elif self.final_state('='):
                    if self.delim_check_next(delim9, '>='):
                        return
                    else:
                        self.delim2()
                        return
                self.error.append([f'Line {self.error_line}: Lexical error:\'{self.string}\' invalid delimiter'])
                self.string = ''
                self.Lexical()
                return
            elif self.final_state('['):
                if self.delim_check_next(delim17, '['):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state('.'):
                if self.delim_check_next(delim13, '.'):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state(']'):
                if self.delim_check_next(delim18, ']'):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state('{'):
                if self.delim_check_next(delim19, '{'):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state('}'):
                if self.delim_check_next(delim20, '}'):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state('('):
                if self.delim_check_next(delim21, '('):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state(')'):
                if self.delim_check_next(delim22, ')'):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state(','):
                if self.delim_check_next(delim23, ','):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state(';'):
                if self.delim_check_next(delim24, ';'):
                    return
                else:
                    self.delim2()
                    return
            elif self.final_state('$'):
                self.single_line()
            elif self.final_state('?'):
                if self.next != '':
                    self.traverse()
                    if self.final_state('?'):
                        if self.next != '':
                            self.traverse()
                            self.block_comment()
                            return
                        else:
                            self.error.append(
                                [f'Line {self.error_line}: Lexical error: \'{self.string}\' invalid character'])
                            return
                    else:
                        self.error.append(
                            [f'Line {self.error_line}: Lexical error: \'{self.string}\' invalid character'])
                        self.string = ''
                        self.Lexical()
                        self.string = ''
                        return
                else:
                    self.error.append([f'Line {self.error_line}: Lexical error: \'{self.string}\' invalid character'])
                    self.string = ''
                    return
            elif self.state('\"'):
                self.literals()
            elif self.state('~'):
                if self.current in digits:
                    self.limit_yunit_punto(10, 7)
                elif self.current == "0":
                    self.limit_yunit_punto(1, 7)
                elif self.next == '' and self.index == len(self.code):
                    self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid character'])
                    self.string = ''
                    return
                elif self.delim_check_current(delim26,'~'):
                    self.string =''
                    self.Lexical()
                    return
                else:
                    self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid delimeter'])
                    self.string = ''
                    self.Lexical()
                    return
                return
            elif self.current in num:
                if self.current in digits:
                    self.limit_yunit_punto(10, 7)
                elif self.current == "0":
                    self.limit_yunit_punto(1, 7)
                else:
                    self.error.append([f'Line{self.error_line}: Lexical error:\'{self.string}\' invalid character'])
                    self.string = ''
                    self.Lexical()
                    return
                return
            else:
                if self.current in alphanum:
                    self.string = self.current
                    self.identifiers()
                    return
                else:
                    self.error.append([f'Line{self.error_line}: Lexical error:\'{self.current}\' invalid character'])
                    self.string = ''
                    return