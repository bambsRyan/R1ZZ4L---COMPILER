program = ["g.ssSawa"]
packages = ["hakot"]
nickname = ["bilang"]
body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda", "subok"]
statement = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "takda", "subok"]
statement_for_conditional = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili"]
statement_for_looping = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin"]
statement_for_func_dec = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura"]
var_dec = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks"]
num_Identifier = ["Identifier"]
num_Identifier_continue = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("]
num_ext = [","]
num_dec_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "("]
num_dec_expression_continue = ["|", "+", "-", "*", "/", "%", "**"]
num_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~"]
num_sub_expression = ["Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~"]
num_value = ["Punto Literal", "Yunit Literal", "saYunit, saPunto"]
mop = ["|", "+", "-", "*", "/", "%", "**"]
baybay_Identifier = ["Identifier"]
baybay_Identifier_continue = ["="]
baybay_ext = [","]
baybay_dec_expression = ["Identifier", "Baybay Literal", "saBaybay", "("]
baybay_dec_expression_continue = ["+"]
baybay_expression = ["Identifier", "Baybay Literal", "saBaybay"]
baybay_sub_expression = ["Baybay Literal", "saBaybay"]
baybay_value = ["Baybay Literal", "saBaybay"]
titik_Identifier = ["Identifier"]
titik_Identifier_continue = ["="]
titik_expression = ["Identifier", "Titik Literal", "saTitik"]
titik_sub_expression = ["Titik Literal", "saTitik"]
titik_ext = [","]
bool_Identifier = ["Identifier"]
bool_identifier_continue  = ["="]
bool_ext = [","]
condition = ["di"]
cond = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "Totoo", "Peke", "("]
negate = ["di"]
condition_statement = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "Totoo", "Peke"]
condition_id_continue = [">", "<", ">=", "<=", "==", "!="]
condition_sub_expression = ["(", "Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "Totoo", "Peke"]
condition_continue = ["at", "o"]
cop = [">", "<", ">=", "<=", "==", "!="]
eop = ["==", "!="]
lop = ["at", "o"]
tala_Identifier = ["Identifier"]
tala_ext = [","]
tala_dec_expression = ["Identifier", "[", "("]
tala_dec_expression_continue = ["+"]
tala_expression = ["Identifier", "["]
tala_sub_expression = ["["]
tala_content = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("]
tala_content_continue = [","]
diks_Identifier = ["Identifier"]
diks_ext = [","]
diks_dec_expression = ["Identifier", "{", "("]
diks_dec_expression_continue = ["|"]
diks_expression = ["Identifier", "{"]
diks_sub_expression = ["{"]
diks_content = ["Yunit Literal", "Baybay Literal", "Identifier"]
diks_content_continue = [","]
jumps = ["laktaw", "tapos", "bura"]
del_val = ["["]
id = ["Identifier"]
id_continue = ["(", ".""["]
aop = ["=", "+=", "-=", "*=", "/="]
allowed_aop = ["di", "kuha"]
math = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("]
math_continue = ["-", "*", "/", "%", "**", ">", "<", ">=", "<=", "==", "!=", "at", "o", "|"]
math_expression = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{"]
math_value_id_expression_continue = [">", "<", ">=", "<=", "==", "!="]
math_num_expression_continue = [">", "<", ">=", "<=", "==", "!="]
math_baybay_expression_continue = ["==", "!="]
math_titik_expression_continue = ["==", "!="]
math_tala_expression_continue = ["==", "!="]
math_diks_expression_continue = ["==", "!="]
inputting = ["kuha"]
data_type = ["yunit", "punto", "baybay", "titik", "bool"]
prompt = [","]
outputting = ["sulat"]
printable = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("]
printable_continue = [","]
value_id_expression = ["(", "Identifier"]
value_id_sub_expression = ["Identifier"]
value_id = ["Identifier"]
value_id_ext = [".", "[", "("]
value_id_sub_ext = ["[", "("]
allowed_value = ["Yunit Literal", "Baybay Literal", "Identifier"]
value_index_continue = ["["]
arg = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("]
arg_continue = [","]
value_id_continue = ["|", "+", "-", "*", "/", "%", "**"]
sub_mop = ["-", "*", "/", "%", "**"]
value_id_continue_plus = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "["]
num_typecast = ["saYunit", "saPunto"]
baybay_typecast = ["saBaybay"]
titik_typecast = ["saTitik"]
typecast_value = ["Punto Literal", "Titik Literal", "Baybay Literal", "Yunit Literal", "Identifier"]
titik_typecast_value = ["Titik Literal", "Baybay Literal", "Yunit Literal", "Identifier"]
func_dec = ["takda"]
param = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks"]
param_var_dec = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks"]
param_num_next = [",", "=", "△"]
param_baybay_next = [",", "=", "△"]
param_titik_next = [",", "=", "△"]
param_bool_next = [",", "=", "△"]
param_tala_next = [",", "=", "△"]
param_diks_next = [",", "=", "△"]
param_default_continue = [","]
param_var_dec_default = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks"]
global_call = ["global"]
func_content = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "subok"]
func_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "subok"]
return1 = ["balik"]
return_val = ["Identifier", "Punto Literal", "Yunit Literal", "saYunit", "saPunto", "~", "Baybay Literal", "saBaybay", "Titik Literal", "saTitik", "[", "{", "("]
func_loop = ["para", "habang", "gawin"]
iterable = ["[", "{"]
lawak_value = ["Yunit Literal", "Identifier"]
func_loop_body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "subok"]
func_loop_content = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "subok"]
loop_jumps = ["labas", "tuloy"]
func_loop_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "subok"]
func_loop_conditional = ["kung", "pili"]
func_loop_conditional_continue = ["kundi"]
func_loop_conditional_end = ["edi"]
func_loop_pag_block = ["pag"]
func_loop_pili_body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "labas", "tuloy", "kung", "pili", "subok"]
func_loop_pag_continue = ["pag"]
func_loop_exception_handling = ["subok"]
func_conditional = ["kung", "pili"]
func_conditional_continue = ["kundi"]
func_conditional_end = ["edi"]
pili_val = ["Identifier", "Yunit Literal", "Titik Literal"]
func_pag_block = ["pag"]
pag_val = ["Yunit Literal", "Titik Literal"]
func_pili_body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "subok", "labas"]
func_pili_content = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "subok", "labas"]
func_pili_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "balik", "para", "habang", "gawin", "kung", "pili", "subok", "labas"]
func_pag_continue = ["pag"]
func_exception_handling = ["subok"]
exception = ["AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "Value Error", "ZeroDivError"]
error = ["AttribError", "ExcessError", "ImportError", "IndexError", "KeyError", "MemoryError", "NameError", "TypeError", "Value Error", "ZeroDivError"]
error_continue = [","]
exception_handling = ["subok"]
conditional = ["kung", "pili"]
conditional_content = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "subok"]
conditional_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "subok"]
conditional_continue = ["kundi"]
conditional_end = ["edi"]
pag_block = ["pag"]
pili_body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "labas"]
pili_content = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "labas"]
pili_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "kung", "pili", "labas"]
pag_continue = ["pag"]
conditional_exception_handling = ["subok"]
loop = ["para", "habang", "gawin"]
loop_body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "subok"]
loop_content = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "subok"]
loop_content_continue = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "subok"]
loop_conditional = ["kung", "pili"]
loop_conditional_continue = ["kundi"]
loop_conditional_end = ["edi"]
loop_pag_block = ["pag"]
loop_pili_body = ["yunit", "punto", "baybay", "titik", "bool", "tala", "diks", "Identifier", "sulat", "laktaw", "tapos", "bura", "para", "habang", "gawin", "labas", "tuloy", "kung", "pili", "subok"]
loop_pag_continue = ["pag"]
loop_exception_handling = ["subok"]