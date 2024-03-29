from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, PanedWindow, Frame
import tkinter as tk
import tkinter.ttk as ttk
import Lexer as lx
import Syntax as syn
import os 
import sys

OUTPUT_PATH = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
ASSETS_PATH = os.path.join(OUTPUT_PATH, "assets", "frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()   

window.geometry("1870x990")
window.title("R1ZZ4L")
window.configure(bg="#FFFFFF")

canvas = Canvas(window,bg="#FFFFFF", height=990, width=1870, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)


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
    
def update_lexeme_tokens_table():
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

def syntax_analyzer():
    read = lx.Lexer('')
    read.tokens.clear()
    read.error.clear()
    lexeme_tokens_area.delete(*lexeme_tokens_area.get_children())
    line = coding_area.get("1.0", "end-1c")
    read = lx.Lexer(line)
    read.Tokenize()

    for token in read.tokens:
        lexeme_tokens_area.insert("", "end", values=(token[0], token[1]), tags=('custom_font'))

    lexeme_tokens_area.heading("#1", text="Lexeme", anchor="center",)
    lexeme_tokens_area.heading("#2", text="Token Type", anchor="center")

    lexeme_tokens_area.column("#1", width=250, anchor="center")
    lexeme_tokens_area.column("#2", width=250, anchor="center")

    lexeme_tokens_area.column("#1", stretch=tk.YES)
    lexeme_tokens_area.column("#2", stretch=tk.YES)

    if len(read.error) > 0: 
        update_lexical_errors_text("Can't compile in Syntax.. Lexical errors occur")
        return
    parser = syn.Parser(read.tokens)    
    parser.parse()
    update_lexical_errors_text(parser.errors[0])



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

def update_line_numbers(event=None):
    line_numbers.delete("1.0", "end")
    first_visible_line = int(coding_area.index("@0,0").split('.')[0])
    last_visible_line = int(coding_area.index("@0,{}".format(coding_area.winfo_height())).split('.')[0])
    for i in range(first_visible_line, last_visible_line + 1):
        line_numbers.insert("end", str(i).rjust(4) + '\n')

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