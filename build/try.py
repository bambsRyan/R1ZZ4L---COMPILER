

print([1,2,3]< [1,1,2])
# class GaleShapley:
#     def __init__(self, men_preferences:dict, women_preferences:dict) -> None:
#         self.men_preferences = men_preferences
#         self.women_preferences = women_preferences
#         self.matches = {}
#         print("men: ",men_preferences)
#         print("women: ",women_preferences)

#     # def stable_matching(self):
#     #     try:
#     #         unengaged_men = list(self.men_preferences.keys())
#     #         while unengaged_men:
#     #             for man in unengaged_men:
#     #                 women_list = list(self.men_preferences[man].preferences.keys())
#     #                 best_choice = women_list.pop(0)
#     #                 fiance = self.matches.get(best_choice)
#     #                 if not fiance:
#     #                     # She's free
#     #                     print(f"{best_choice} is engaged to {man}")
#     #                     self.matches[best_choice] = man
#     #                     unengaged_men.remove(man)
#     #                 else:
#     #                     # She's engaged
#     #                     if list(self.women_preferences[best_choice].preferences.keys()).index(man) > list(self.women_preferences[best_choice].preferences.keys()).index(fiance):
#     #                         # She prefers new guy
#     #                         print(f"{best_choice} dumps {fiance} for {man}")
#     #                         self.matches[best_choice] = man
#     #                         unengaged_men.remove(man)
#     #                         unengaged_men.append(fiance)
#     #                     else:
#     #                         print(f"{best_choice} rejects {man}")
#     #         return self.matches
#     #     except Exception as e:
#     #         print("Error: ",e)
#     #         return None
        
#     def stable_matching(self):
#         unengaged_men = list(self.men_preferences.keys())
#         while unengaged_men:
#             for man in unengaged_men:
#                 women_list = list(self.men_preferences[man].preferences.keys())
#                 while women_list:
#                     best_choice = women_list.pop(0)
#                     fiance = self.matches.get(best_choice)
#                     if not fiance:
#                         # She's free
#                         print(f"{best_choice} is engaged to {man}")
#                         self.matches[best_choice] = man
#                         unengaged_men.remove(man)
#                         break
#                     else:
#                         # She's engaged
#                         if list(self.women_preferences[best_choice].preferences.keys()).index(man) > list(self.women_preferences[best_choice].preferences.keys()).index(fiance):
#                             # She prefers new guy
#                             print(f"{best_choice} dumps {fiance} for {man}")
#                             self.matches[best_choice] = man
#                             unengaged_men.remove(man)
#                             unengaged_men.append(fiance)
#                             break
#                         else:
#                             # She rejects him, he will propose to the next woman in his list
#                             print(f"{best_choice} rejects {man}")
#                             continue
#         return self.matches

#     def score(self):
#         total_score = 0
#         men_score = 0
#         women_score=0
#         for woman, man in self.matches.items():
#             woman_score = self.women_preferences[woman].preferences[man]
#             man_score = self.men_preferences[man].preferences[woman]

#             men_score+=man_score
#             women_score+=woman_score

#             match_score = woman_score + man_score
#             total_score += match_score
            
#             print(f"{woman}(ranked: {self.men_preferences[man][woman]}) is engaged to {man}(ranked: {self.women_preferences[woman][man]}): {match_score}")
#         print(f"Men score: {men_score}")
#         print(f"Women score: {women_score}")
#         print(f"Total score: {total_score}")
#         return total_score
    
# class Preferences:
#     def __init__(self, preferences) -> None:
#         self.preferences={}
#         total=len(preferences)
#         for rank,preference in enumerate(preferences):
#             self.preferences[preference] = total-rank
#         self.list=self.preferences.keys()

#     def __getitem__(self, key):
#         return self.preferences.get(key)

#     def __str__(self) -> str:
#         return str(self.preferences)
    

#     def __repr__(self) -> str:
#         return str(self.preferences)
    

    

# men={
#     "a":Preferences(["z","y","x"]),
#     "b":Preferences(["y","x","z"]), 
#     "c":Preferences(["z","y","x"]),
#     "d":Preferences(["z","y","x",]),
#     "e":Preferences(["z","y","x"])
# }

# women={
#     "x":Preferences(["b","a","c"]),
#     "y":Preferences(["c","b","a"]),
#     "z":Preferences(["a","c","b"])
# }

# gs=GaleShapley(men, women)
# gs.stable_matching()
# gs.score()


# x = 
# try:
#     print(eval(x))
# except SyntaxError as e:
#     print(e)
# except NameError as e:
#     print(e)
# except TypeError as e:
#     print(e)


# # Define temperature input (crisp value)
# temperature = 22  # Can be replaced with sensor reading

# # Define membership functions (triangular in this case)
# def cold(temp):
#   return max(0, min((20 - temp) / 5, 1))  

# def warm(temp):
#   return max(0, min((temp - 20) / 5, (temp - 25) / 5))

# def hot(temp):  # Overlapping membership function 
#   return max(0, 1 - (temp - 25) / 5)

# # Define fuzzy rules
# def ac_power(temp_cold, temp_warm, temp_hot):
#   # Sample rules with varying weight based on membership degree
#   return 0.8 * temp_cold + 0.5 * temp_warm - 0.2 * temp_hot

# # Fuzzify inputs
# cold_degree = cold(temperature)
# warm_degree = warm(temperature)
# hot_degree = hot(temperature)

# # Apply fuzzy rules
# ac_power_level = ac_power(cold_degree, warm_degree, hot_degree)

# # Defuzzification (simple center of gravity method here)
# # Can be replaced with other methods
# crisp_ac_level = (cold_degree * 0 + warm_degree * 25 + hot_degree * 50) / (cold_degree + warm_degree + hot_degree)

# print("Temperature:", temperature)
# print("Cold degree:", cold_degree)
# print("Warm degree:", warm_degree)
# print("Hot degree:", hot_degree)
# print("Air conditioner power level:", crisp_ac_level)

# class Compilation:
#     def __init__(self, x):
#         self.token =  x
#         self.val = ''
#         self.num = -1
#         self.max = len(x)
#         self.line = 1
#         self.variables= {'yunit':{}, 'punto':{}, 'baybay':{}, 'titik':{}, 'bool':{}, 'tala':{}, 'diks':{}} 
#         self.all_variables = {}
#         self.var = []
#         self.semantic_error = []
#         self.cont = True

#     def sem(self):
#         self.semantic()
#         self.match()

#     def semantic(self):
#         self.num += 1
#         if self.num < self.max:
#             self.current = self.token[self.num]['for_syntax']
#             self.val = self.token[self.num]['value']
#             self.line = self.token[self.num]['rows']
#         else:
#             self.current = None
#         if self.current in ['space', 'Line Comment']:
#             self.semantic()

#     def declare(self, d_type, name):
#         variable = {}
#         value = {}
#         value[name] = None
#         self.variables[d_type].update(value)
#         variable[name] = d_type
#         self.all_variables.update(variable)

#     def newline(self):
#         while self.current == 'newline':
#             self.semantic()

#     def match(self):
#         self.newline()
#         while self.cont == True and self.current != None:
#             if self.current == 'g.ssSawa':
#                 self.semantic()
#                 self.newline()
#             elif self.current == 'yunit':
#                 self.yunit()
#                 self.newline()
#             elif self.current == 'punto':
#                 self.punto()
#                 self.newline()
#             elif self.current == 'baybay':
#                 self.baybay()
#                 self.newline()
#             elif self.current == 'titik':
#                 self.titik()
#                 self.newline()
#             elif self.current == 'tala':
#                 self.tala()
#                 self.newline()

#     def yunit(self):
#         x = ''
#         y = ''
#         self.semantic()
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"NameError on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else:
#             self.var.append(s_name)
#             self.declare('yunit', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 while self.current != 'newline' and self.current != ',':
#                     if self.current == 'Identifier':
#                         self.Identifier()
#                     elif self.current == 'saYunit':
#                         y += 'int'
#                     else:
#                         y += self.val
#                     self.semantic()
#                 try:
#                     self.variables['yunit'][s_name] = eval(y)
#                 except SyntaxError as e:
#                     self.semantic_error.append(f"Type Error on line {self.line}: {e}")
#             self.newline()






#                 #     y = 0
#                 #     if self.current in ['+', '-', '*', '**', '/', '%', '(', ')', 'Yunit Literal','Punto Literal','Identifier', 'saYunit']:
#                 #         if self.current == 'Identifier':
#                 #             y = self.identifier()
#                 #         elif self.current == 'saYunit':
#                 #             y = self.saYunit()
#                 #         elif self.current in ['+', '-', '*', '**', '/', '%']:
#                 #             y = self.val
#                 #         elif self.current == 'Yunit Literal':
#                 #             y = self.val.replace('~', '-')
#                 #         elif self.current == 'Punto Literal':
#                 #             y = self.val.split('.')
#                 #             y = int(y[0].replace('~', '-'))
#                 #         x += str(y)
#                 #     self.semantic()
#                 # try:     
#                 #     self.variables['yunit'][s_name] = eval(x)
#                 # except:
#                 #     pass
#                 # if self.current == ',':
#                 #     self.yunit_continue()
#                 # else:
#                 #     self.newline()

#     def yunit_continue(self):
#         x = ''
#         y = ''
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else:
#             self.var.append(s_name)
#             self.declare('yunit', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 while self.current != 'newline' and self.current != ',':
#                     y = 0
#                     if self.current in ['+', '-', '*', '**', '/', '%', '(', ')', 'Yunit Literal','Punto Literal','Identifier', 'saYunit']:
#                         if self.current == 'Identifier':
#                             y = self.identifier()
#                         elif self.current == 'saYunit':
#                             y = self.saYunit()
#                         elif self.current in ['+', '-', '*', '**', '/', '%']:
#                             y = self.val
#                         elif self.current == 'Yunit Literal':
#                             y = self.val.replace('~', '-')
#                         elif self.current == 'Punto Literal':
#                             y = self.val.split('.')
#                             y = int(y[0].replace('~', '-'))
#                         x += str(y)
#                     self.semantic()
#                 try:     
#                     self.variables['yunit'][s_name] = eval(x)
#                 except:
#                     pass
#                 if self.current == ',':
#                     self.yunit_continue()
#                 else:
#                     self.newline()

#     def punto(self):
#         x = ''
#         y = ''
#         self.semantic()
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else:
#             self.var.append(s_name)
#             self.declare('punto', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 while self.current != 'newline' and self.current != ',':
#                     y = 0
#                     if self.current in ['+', '-', '*', '**', '/', '%', '(', ')', 'Yunit Literal','Punto Literal','Identifier', 'saPunto']:
#                         if self.current == 'Identifier':
#                             y = self.identifier()
#                         elif self.current == 'saPunto':
#                             y = self.saPunto()
#                         elif self.current in ['+', '-', '*', '**', '/', '%']:
#                             y = self.val
#                         elif self.current == 'Yunit Literal':
#                             y = float(self.val.replace('~', '-'))        
#                         elif self.current == 'Punto Literal':
#                             y = self.val.replace('~', '-')
#                         x += str(y)
#                         print(x)
#                     self.semantic()
#                 try:
#                     self.variables['punto'][s_name] = eval(x)
#                 except:
#                     pass
#                 if self.current == ',':
#                     self.punto_continue()
#                 else:
#                     self.newline()

#     def punto_continue(self):
#         x = ''
#         y = ''
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else:
#             self.var.append(s_name)
#             self.declare('punto', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 while self.current != 'newline' and self.current != ',':
#                     y = 0
#                     if self.current in ['+', '-', '*', '**', '/', '%', '(', ')', 'Yunit Literal','Punto Literal','Identifier', 'saPunto']:
#                         if self.current == 'Identifier':
#                             y = self.identifier()
#                         elif self.current == 'saPunto':
#                             y = self.saPunto()
#                         elif self.current in ['+', '-', '*', '**', '/', '%']:
#                             y = self.val
#                         elif self.current == 'Yunit Literal':
#                             y = float(self.val.replace('~', '-'))        
#                         elif self.current == 'Punto Literal':
#                             y = self.val.replace('~', '-')
#                         x += str(y)
#                     self.semantic()
#                 try:
#                     self.variables['punto'][s_name] = eval(x)
#                 except:
#                     pass
#                 if self.current == ',':
#                     self.punto_continue()
#                 else:
#                     self.newline()

#     def identifier(self):
#         name = self.val
#         d_type = ''
#         val = ''
#         for key, value in self.all_variables.items():
#             val = key
#             d_type = value 
#             if key == name:
#                 break
#         if val == '':
#             return eval("self.variables[d_type][self.val]")
#         else:
#             self.semantic_error.append(f"NameError: name '{self.val}' is not defined")
#             self.cont = False

#     def saYunit(self):
#         y = ''
#         x = 0
#         self.semantic()
#         self.semantic()
#         if self.current == 'Baybay Literal':
#             y  = f' int({self.val.replace('\"', '').replace('~', '-')})'
#         elif self.current == 'Titik Literal':
#             y = f' int({self.val.replace('\'', '').replace('~', '-')})'
#         else:
#             y = f' int({self.val.replace('~', '-')})'
#         try:
#             self.semantic()
#             return eval(y)
#         except:
#             self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Yunit() with base 10: \"{self.current}\"")
#             self.cont = False
#             x = 0

#     def saPunto(self):
#         y = ''
#         x = 0
#         self.semantic()
#         self.semantic()
#         if self.current == 'Baybay Literal':
#             y  = f' float({self.val.replace('\"', '').replace('~', '-')})'
#         elif self.current == 'Titik Literal':
#             y = f' float({self.val.replace('\'', '').replace('~', '-')})'
#         else:
#             y = f' float({self.val.replace('~', '-')})'
#         try:
#             self.semantic()
#             return eval(y)
#         except:
#             self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Yunit() with base 10: \"{self.current}\"")
#             self.cont = False
#             x = 0

#     def baybay(self):
#         x = ''
#         s_name = ''
#         self.semantic()
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else:
#             self.var.append(s_name)
#             self.declare('baybay', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 while self.current not in ['newline', ',']:
#                     y = 0
#                     if self.current in ['+','Baybay Literal', 'saBaybay']:
#                         if self.current == 'saBaybay':
#                             y = self.saBaybay()
#                         elif self.current == 'Baybay Literal':
#                             y = self.val
#                         elif self.current == '+':
#                             y = self.val
#                         x += str(y)
#                         print(x)
#                     self.semantic()
#                 try:
#                     self.variables['baybay'][s_name] = str(eval(x))
#                 except:
#                     pass
#                 if self.current == ',':
#                     self.punto_continue()
#                 else:
#                     self.newline()

#     def baybay_continue(self):
#         x = ''
#         s_name = ''
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else:
#             self.var.append(s_name)
#             self.declare('baybay', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 while self.current not in ['newline', ',']:
#                     y = 0
#                     if self.current in ['+','Baybay Literal', 'saBaybay']:
#                         if self.current == 'saBaybay':
#                             y = self.saBaybay()
#                         elif self.current == 'Baybay Literal':
#                             y = self.val
#                         elif self.current == '+':
#                             y = self.val
#                         x += str(y)
#                         print(x)
#                     self.semantic()
#                 try:
#                     self.variables['baybay'][s_name] = str(eval(x))
#                 except:
#                     pass
#                 if self.current == ',':
#                     self.punto_continue()
#                 else:
#                     self.newline()

#     def saBaybay(self):
#         y = ''
#         self.semantic()
#         self.semantic()
#         y  = f'str({self.val})'
#         try:
#             self.semantic()
#             return f'\"{eval(y)}\"'
#         except:
#             self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for Baybay() : \"{self.current}\"")
#             self.cont = False

#     def titik(self):
#         x = ''
#         s_name = ''
#         self.semantic()
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else: 
#             self.var.append(s_name)
#             self.declare('titik', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 print(self.current)
#                 if self.current == 'Titik Literal':
#                     x = self.val
#                 elif self.current == 'Identifier':
#                     x = self.identifier()
#                 elif self.current == 'saTitik':
#                     x = self.saTitik()
#             self.semantic()
#             if self.current == ',':
#                 self.titik_continue()
#             self.newline()
    
#     def titik_continue(self):
#         x = ''
#         s_name = ''
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else: 
#             self.var.append(s_name)
#             self.declare('titik', self.val)
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 print(self.current)
#                 if self.current == 'Titik Literal':
#                     x = self.val
#                 elif self.current == 'Identifier':
#                     x = self.identifier()
#                 elif self.current == 'saTitik':
#                     x = self.saTitik()
#             self.semantic()
#             if self.current == ',':
#                 self.titik_continue()
#             self.newline()

#     def saTitik(self):
#         y = ''
#         self.semantic()
#         self.semantic()
#         print(self.val)
#         y  = f'str({self.val})'
#         try:
#             self.semantic()
#             return y 
#         except:
#             self.semantic_error.append(f"Type Error on line {self.line}: invalid literal for saTitik() : \"{self.current}\"")
#             self.cont = False

#     def tala(self):
#         x = 0
#         y = ''
#         s_name = ''
#         self.semantic()
#         self.semantic()
#         s_name = self.val
#         if s_name in self.var:
#             self.semantic_error.append(f"Syntax Error on line {self.line}: {s_name} is already defined")
#             self.cont = False
#         else: 
#             self.var.append(s_name)
#             self.declare('tala', self.val)
#             self.variables['tala'][s_name] = []
#             self.semantic()
#             if self.current == '=':
#                 self.semantic()
#                 self.semantic()
#                 while self.current != ']':
#                     while self.current not in [',', ']']:
#                         if self.current in ['Yunit Literal', 'Punto Literal']:
#                             y += self.val
#                         elif self.current in ['+', '-', '*', '**', '/', '%']:
#                             y  += self.val
#                         self.semantic()
#                     self.variables['tala'][s_name].append(eval(y))
#         self.semantic()
#         self.newline()
                    
def diks(self):
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
            self.declare('diks', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                self.semantic()
                if self.current == 'Identifier':
                    holder = self.Identifier()
                    if self.cont == False:
                        return
                    if type(holder) == str:
                        holder = f'\'{holder}\''
                    elif type(holder) == int:
                        holder = holder
                    else:
                        self.semantic_error.append(f"TypeError on line {self.line}: {holder} does not contain Diks Litarals")
                        self.cont = False
                    if self.cont == False:
                        return
                    self.semantic()
                elif self.current == 'Baybay Literal':
                    y += str(eval(self.val))
                elif self.current == 'Titik Literal':   
                    y += str(eval(self.val))
                elif self.current == 'Yunit Literal':
                    y += str(eval(self.val.replace('~', '-')))
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    while self.current != '}':
                        if self.current == 'Identifier':
                            holder = self.Identifier()
                            if self.cont == False:
                                return
                            if type(holder) == str:
                                holder = f'\'{holder}\''
                            elif type(holder) == int: 
                                holder = holder
                            else:
                                self.semantic_error.append(f"TypeError on line {self.line}: {holder} does not contain Key Litarals")
                                self.cont = False
                            z += str(holder)
                            continue
                        elif self.current == 'saBaybay':
                            z += str(self.saBaybay())
                        elif self.current == 'saPunto':
                            z += str(self.saPunto())
                        elif self.current == 'saTitik':
                            z += str(self.saTitik())
                        elif self.current == 'saYunit':
                            z += str(self.saYunit())
                        elif self.current == ';':
                            z += ':'
                        elif self.current == 'Yunit Literal':
                            z += str(eval(self.val.replace('~', '-')))
                        elif self.current == 'Titik Literal':
                            z += str(eval(self.val))
                        elif self.current == 'Baybay Literal':
                            z += str(eval(self.val))
                        elif self.current == 'Punto Literal':
                            z += str(eval(self.val))
                        self.semantic()
                    exec("self.variables['diks'][s_name] = {eval(z), y}")
                    self.semantic()
                if self.current == ',':
                    self.diks_continue()
                    return

def diks_continue(self):
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
            self.declare('diks', self.val)
            self.semantic()
            if self.current == '=':
                self.semantic()
                y += '{'
                self.semantic()
                while self.current != 'newline' and self.current != ',':
                    while self.current != '}':
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
                        elif self.current == '{':
                            y += str(self.diks_sub())
                            continue
                        else:
                            y += self.val
                        self.semantic()
                    y += '}'
                    self.semantic()
                print(y)
                if self.cont == False:
                    return
                try:
                    self.variables['diks'][s_name] = eval(y)
                    if self.current == ',':
                        self.diks_continue()
                        return
                    self.newline()
                except SyntaxError as e:
                    self.cont = False
                    return
def diks_sub(self):
        y = '['
        self.semantic()
        while self.current != '}':
            if self.current == '{':
                y += self.tala_sub()
                continue
            y += self.val
            self.semantic()
        y += '}'
        self.semantic()
        return y