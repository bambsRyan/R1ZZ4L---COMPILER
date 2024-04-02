arop = '+-*/%'
alphanum = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0',
            '1','2','3','4','5','6','7','8','9'] #alphabet + num
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
digits = ['1','2','3','4','5','6','7','8','9']
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
delim11 = ['+', '-', '*', '/', '%', '(', ')', '<', '>', '=', '!', '[', ']', '{','}', ',', '.', ';', ' ', '\n', '$']
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
        self.current = ''
        self.next = ''
        self.index = -1
        self.frfr = False
        self.string = ''
        self.line_number = 0
        self.line = 1
        self.values = {}
        self.identifier_num = 0
        self.punto_index = 0
        self.yunit_index = 0
        self.titik_index = 0

    def traverse(self):
        self.index += 1
        self.line_number += 1
        if self.index < len(self.code) and self.index + 1 < len(self.code):
            self.current = self.code[self.index]
            self.next = self.code[self.index + 1]
        elif self.index < len(self.code) and self.index + 1 == len(self.code):
            self.current = self.code[self.index]
            self.next = ''
        else:
            self.current = ''
            self.next = ''
            self.frfr = True

    def Tokenize(self):
        self.traverse()
        while (self.frfr != True): 
            self.Lexical()
            self.traverse()

    def addTokens(self, token, string = None):
        self.values['token'] = token
        self.values['rows'] = self.line
        self.values['columns'] = self.line_number 
        self.values['value'] = string
        self.tokens.append(self.values)
        self.values = {}
        self.string = ''
    
    def invalid_delim(self):
        self.error.append(['Error: Invalid delimeter ' + self.string + ' at line number ' + str(self.line)])
        self.string = ''
        return
    
    def single_line(self):
        while self.current != '\n':
            self.string += self.current
            self.traverse()
        self.addTokens('single_line', self.string)
        self.string = ''
        return

    def lexical_again(self):
        if self.current != '':
            self.Lexical()
        return

    def state(self, character):
        if self.current == character:
            self.string += self.current
            self.traverse()
            return True
        return False
    
    def final_state(self, character):
        if self.current == character:
            self.string += self.current
            return True
        return False

    def delim_next_check(self, delim, token):
        if self.next in delim:
            self.addTokens(self.string, token)
        else: 
            self.invalid_delim()
        return 

    def delim_current_check(self, delim, token):
        if self.current in delim:
            self.addTokens(self.string, token)
        else:
            self.invalid_delim()
        self.lexical_again()
        return

    def check_identifier(self):
        if len(self.string) != 0:
            if self.current in alphanum or self.current == '_':
                self.Identifier()
            else:
                if self.current not in delim11:
                    self.invalid_delim()
                    self.lexical_again()
                else:
                    self.identifier_num += 1
                    self.addTokens(f'identifier{self.identifier_num}', self.string)
                    self.string = ''
                    self.lexical_again()
        else:
            if self.current in alphabet:
                self.Identifier()
            else:
                self.error.append(['Error: Invalid character ' + self.current + ' at line number ' + str(self.line)])
        return

    def Identifier(self):
        while self.current in alphanum or self.current == '_':
            self.string += self.current
            self.traverse()
        if self.current in delim11:
            self.identifier_num += 1
            self.addTokens( f'identifier{self.identifier_num}', self.string)
            self.lexical_again()
        else:
            self.invalid_delim()
            self.lexical_again()
        return

    def Lexical(self):
        if self.current == '\n':
            self.addTokens('newline','\\n')
            self.line_number = -1
            self.line += 1
            return
        elif self.current == ' ':
            self.addTokens('space','\' \'')
            return
        elif self.current == '\t':
            self.addTokens('tab','\\t')
            return  
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
                                                    self.delim_next_check(delim4, 'AttribError')
                                                    return
        elif self.state('a'):
            if self.final_state('t'):
                self.delim_next_check(delim1, 'at')
                return
            elif self.final_state('y'):
                self.delim_next_check(delim1, 'ay')
                return
        elif self.state('b'):
            if self.state('a'):
                if self.state('l'):
                    if self.state('i'):
                        if self.final_state('k'):
                            self.delim_next_check(delim8, 'balik')
                            return
                elif self.state('y'):
                    if self.state('b'):
                        if self.state('a'):
                            if self.final_state('y'):
                                self.delim_next_check(delim3, 'baybay')
                                return
            elif self.state('i'):
                if self.state('l'):
                    if self.state('a'):
                        if self.state('n'):
                            if self.final_state('g'):
                                self.delim_next_check(delim1, 'bilang')
                                return
            elif self.state('o'):
                if self.state('o'):
                    if self.final_state('l'):
                        self.delim_next_check(delim3, 'bool')
                        return
            elif self.state('u'):
                if self.state('k'):
                    if self.state('o'):
                        if self.final_state('d'):
                            self.delim_next_check(delim3, 'bukod')
                            return
                elif self.state('r'):
                    if self.final_state('a'):  
                        self.delim_next_check(delim1, 'bura')
                        return
        elif self.state('d'):
            if self.state('i'):
                if self.current in delim3:
                    self.delim_current_check(delim3, 'di')
                    return
                elif self.state('k'):
                    if self.final_state('s'):
                        self.delim_next_check(delim3, 'diks')
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
                                                    self.delim_next_check(delim4, 'ExcessError')
                                                    return
        elif self.state('e'):
            if self.state('d'):
                if self.final_state('i'):
                    self.delim_next_check(delim5, 'edi')
                    return
        elif self.state('g'):
            if self.state('a'):
                if self.state('w'):
                    if self.state('i'):
                        if self.final_state('n'):
                            self.delim_next_check(delim5, 'gawin')
                            return
            elif self.state('g'):
                if self.state('.'):
                    self.start()
                    return
            elif self.state('.'):
                self.start()
                return
        elif self.state('h'):
            if self.state('a'):
                if self.state('b'):
                    if self.state('a'):
                        if self.state('n'):
                            if self.final_state('g'):
                                self.delim_next_check(delim3, 'habang')
                                return
                elif self.state('k'):
                    if self.state('o'):
                        if self.final_state('t'):
                            self.delim_next_check(delim1, 'hakot')
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
                                                    self.delim_next_check(delim4, 'ImportError')
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
                                                self.delim_next_check(delim4, 'IndexError')
                                                return
        elif self.state('i'):
            if self.state('b'):
                if self.state('a'):
                    if self.state('n'):
                        if self.final_state('g'):    
                            self.delim_next_check(delim1, 'ibang')
                            return
        
        elif self.state('K'):
            if self.state('e'):
                if self.state('y'):
                    if self.state('E'):
                        if self.state('r'):
                            if self.state('r'):
                                if self.state('o'):
                                    if self.final_state('r'):
                                        self.delim_next_check(delim4, 'KeyError')
                                        return
        elif self.state('k'):
            if self.state('u'):
                if self.state('h'):
                    if self.final_state('a'):
                        self.delim_next_check(delim3, 'kuha')
                        return
                elif self.state('s'):
                    if self.final_state('a'):
                        self.delim_next_check(delim5, 'kusa')
                        return
                elif self.state('n'):
                    if self.state('d'):
                        if self.final_state('i'):
                            self.delim_next_check(delim3, 'kundi')
                            return
                    elif self.final_state('g'):
                        self.delim_next_check(delim3, 'kung')
                        return
        elif self.state('l'):
            if self.state('a'):
                if self.state('b'):
                    if self.state('a'):
                        if self.final_state('s'):
                            self.delim_next_check(delim7, 'labas')
                            return
                elif self.state('k'):
                    if self.state('t'):
                        if self.state('a'):
                            if self.final_state('w'):
                                self.delim_next_check(delim7, 'laktaw')
                                return
                elif self.state('w'):
                    if self.state('a'):
                        if self.final_state('k'):
                            self.delim_next_check(delim3, 'lawak')
                            return
        elif self.final_state('o'):
            self.delim_next_check(delim1, 'o')
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
                                                    self.delim_next_check(delim4, 'MemoryError')
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
                                            self.delim_next_check(delim4, 'NameError')
                                            return
        elif self.state('p'):
            if self.state('a'):
                if self.state('r'):
                    if self.final_state('a'):
                        self.delim_next_check(delim3, 'para')
                        return
                elif self.final_state('g'):
                    self.delim_next_check(delim1, 'pag')
                    return
            elif self.state('i'):
                if self.state('l'):
                    if self.final_state('i'):
                        self.delim_next_check(delim3, 'pili')
                        return
            elif self.state('u'):
                if self.state('n'):
                    if self.state('t'): 
                        if self.final_state('o'):
                            self.delim_next_check(delim3, 'punto')
                            return
        elif self.state('P'):
            if self.state('e'):
                if self.state('k'):
                    if self.final_state('e'):
                        self.delim_next_check(delim6, 'Peke')
                        return
        elif self.state('s'):
            if self.final_state('a'):
                self.delim_next_check(delim1, 'sa')
                return
            elif self.state('u'):
                if self.state('l'):
                    if self.state('a'):
                        if self.final_state('t'):
                            self.delim_next_check(delim3, 'sulat')
                            return
                elif self.state('b'):
                    if self.state('o'):
                        if self.final_state('k'):
                            self.delim_next_check(delim5, 'subok')
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
                                            self.delim_next_check(delim4, 'TypeError')
                                            return
            elif self.state('o'):
                if self.state('t'):
                    if self.state('o'):
                        if self.final_state('o'):
                            self.delim_next_check(delim6, 'Totoo')
                            return
        elif self.state('t'):
            if self.state('a'):
                if self.state('k'):
                    if self.state('d'):
                        if self.final_state('a'):
                            self.delim_next_check(delim1, 'takda')
                            return
                elif self.state('l'):
                    if self.final_state('a'):
                        self.delim_next_check(delim3, 'tala')
                        return
                elif self.state('p'):
                    if self.state('o'):
                        if self.final_state('s'):
                            self.delim_next_check(delim7, 'tapos')
                            return
            elif self.state('i'):
                if self.state('t'):
                    if self.state('i'):
                        if self.final_state('k'):
                            self.delim_next_check(delim3, 'titik')
                            return
            elif self.state('u'):
                if self.state('l'):
                    if self.state('o'):
                        if self.final_state('y'):
                            self.delim_next_check(delim7, 'tuloy')
                            return
                elif self.state('w'):
                    if self.state('i'):
                        if self.state('n'):
                            if self.final_state('g'):
                                self.delim_next_check(delim3, 'tuwing')
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
                                                    self.delim_next_check(delim4, 'ValueError')
                                                    return
        elif self.state('W'):
                if self.state('a'):
                    if self.state('l'):
                        if self.final_state('a'):
                            self.delim_next_check(delim6, 'wala')
                            return
        elif self.state('y'):
                if self.state('u'):
                    if self.state('n'):
                        if self.state('i'):
                            if self.final_state('t'):
                                self.delim_next_check(delim3, 'yunit')
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
                                                            self.delim_next_check(delim4, 'ZeroDivError')
                                                            return
        elif self.state('='):
            if self.current in delim15:
                self.delim_current_check(delim15, '=')
            elif self.final_state('='):
                self.delim_next_check(delim15, '==')
            return
        elif self.state('+'):
            if self.current in delim14:
                self.delim_current_check(delim14, '+')
            elif self.final_state('='):
                self.delim_next_check(delim14, '+=')
            return  
        elif self.state('-'):
            if self.current in delim9:
                self.delim_current_check(delim9, '-')
            elif self.final_state('='):
                self.delim_next_check(delim9, '-=')
            return  
        elif self.state('*'):
            if self.current in delim9:
                self.delim_current_check(delim9, '*')
            elif self.final_state('='):
                self.delim_next_check(delim9, '*=')
            elif self.final_state('*'):
                self.delim_next_check(delim9, '**')
            return
        elif self.state('/'):
            if self.current in delim9:
                self.delim_current_check(delim9, '/')
            elif self.final_state('='):
                self.delim_next_check(delim9, '/=')
            return
        elif self.final_state('%'):
            self.delim_next_check(delim9, '%')
            return
        elif self.state('!'):
            if self.final_state('='):
                self.delim_next_check(delim15, '!=')
                return
        elif self.state('<'):
            if self.current in delim9:
                self.delim_current_check(delim9, '<')
            elif self.final_state('='):
                self.delim_next_check(delim9, '<=')
            return
        elif self.state('>'):
            if self.current in delim9:
                self.delim_current_check(delim9, '>')
            elif self.final_state('='):
                self.delim_next_check(delim9, '>=')
            return
        elif self.final_state('('):
            self.delim_next_check(delim21, '(')
            return
        elif self.final_state(')'):
            self.delim_next_check(delim22, ')')
            return
        elif self.final_state('['):
            self.delim_next_check(delim17, '[')
            return
        elif self.final_state(']'):
            self.delim_next_check(delim18, ']')
            return
        elif self.final_state('{'):
            self.delim_next_check(delim19, '{')
            return
        elif self.final_state('}'):
            self.delim_next_check(delim20, '}')
            return
        elif self.final_state(','):
            self.delim_next_check(delim23, ',')
            return
        elif self.final_state('.'):
            self.delim_next_check(delim13, '.')
            return
        elif self.final_state(';'):
            self.delim_next_check(delim24, ';')
            return
        elif self.final_state('$'):
            self.single_line()
            return
        elif self.state('0'):
            self.zero()
            return
        elif self.state('\"'):
            self.baybaylit()     
            return
        elif self.state('\''):
            self.titiklit()
            return
        elif self.current in digits:
            self.numlit()
            return
        self.check_identifier()
        return
    
    def zero(self):
        if self.current in delim10:
            self.addTokens('Yunit Literal', '0')
        elif self.state('.'):
            self.punto()
        else:
            self.invalid_delim()
            self.lexical_again()
        return
    def numlit(self):
        self.yunit_inde = 0
        self.string += self.current
        self.traverse()
        while self.current in num and self.current != '.' and self.yunit_index != 10:    
            self.string += self.current
            self.yunit_index += 1 
            self.traverse()
        if self.current in delim10:
            self.addTokens('Yunit Literal', self.string)
        elif self.current == '.' and self.next in num:
            self.string += self.current
            self.traverse()
            self.punto()
        else: 
            self.invalid_delim()
            self.lexical_again()
        return

    def punto(self):
        self.punto_index = 0
        while self.punto_index !=7 and self.current in num:
            self.string += self.current
            self.punto_index += 1
            self.traverse()
        if self.current in delim27:
            self.addTokens('Punto Literal', self.string)
        else:
            self.invalid_delim()
            self.lexical_again()
        return
    def baybaylit(self):
        while self.current != '\"' and self.current != 'newline':
            if self.current == '\\' and self.next == 'n':
                self.string += '\n'
                self.traverse()
                self.traverse()
                continue
            elif self.current == '\\' and self.next == 't':
                self.string += '\t'
                self.traverse()
                self.traverse()
                continue
            self.string += self.current
            self.traverse()
        if self.state('\"'):
            self.addTokens('Baybay Literal', self.string)
        else:
            self.error.append(['Error: Invalid array of strings \'' + self.current + '\' at line number ' + str(self.line)])
            self.string = ''   
            self.lexical_again()
        return
    def titiklit(self):
        self.titik_index = 0
        while self.titik_index != 1 and self.current != '\'':
            self.string += self.current
            self.titik_index += 1
            self.traverse()
        if self.state('\''):
            self.addTokens('Titik Literal', self.string)
        else:
            self.error.append(['Error: Invalid array of characters \'' + self.string + '\' at line number ' + str(self.line)])
            self.string = ''
            self.lexical_again()
    def start(self):
        if self.state('s'):
            if self.state('s'):
                if self.state('S'):
                    if self.state('a'):
                        if self.state('w'):
                            if self.final_state('a'):
                                self.delim_next_check(delim5, self.string)
                                return
        components = self.string.split('.')
        self.identifier_num += 1
        self.addTokens(f'Identifier{self.identifier_num}', components[0])
        self.addTokens('.', '.')
        self.string = components[1]
        if self.current != '':
            self.check_identifier() 
        return





            

        
