import string

LET = 0
DIG = 1
UNKNOWN = 2
EOF = -1

INT_LIT = 10
IDENT = 12
ASSIGN_OP = 31
ADD_OP = 33
SUB_OP = 35
MULT_OP = 37
DIV_OP = 39
LEFT_PAREN = 50
RIGHT_PAREN = 55

char_class = None
lexeme = []
nxt_ch = ''
nxt_tok = None
file = None


def ADD_Char():
    global lexeme
    lexeme.append(nxt_ch)


def GET_Char():
    global nxt_ch, char_class  
    nxt_ch = file.read(1)
    
    if nxt_ch:
        if nxt_ch.isalpha():
            char_class = LET
        elif nxt_ch.isdigit():
            char_class = DIG
        else:
            char_class = UNKNOWN
    else:
        char_class = EOF


def get_non_blank():
    
    global nxt_ch 
    while nxt_ch.isspace():
        GET_Char()


def lookup(char):
    """التعرف على العمليات والعلامات الخاصة"""
    global nxt_tok

    token_map = {
        '(': LEFT_PAREN,
        ')': RIGHT_PAREN,
        '+': ADD_OP,
        '-': SUB_OP,
        '*': MULT_OP,
        '/': DIV_OP
    }

    ADD_Char()
    nxt_tok = token_map.get(char, EOF)
    return nxt_tok


def LEx():
    global nxt_tok, lexeme

    lexeme = []
    get_non_blank()

    if char_class == LET:
        ADD_Char()
        GET_Char()
        while char_class in {LET, DIG}:
            ADD_Char()
            GET_Char()
        nxt_tok = IDENT

    elif char_class == DIG:
        ADD_Char()
        GET_Char()
        while char_class == DIG:
            ADD_Char()
            GET_Char()
        nxt_tok = INT_LIT

    elif char_class == UNKNOWN:
        lookup(nxt_ch)
        GET_Char()

    elif char_class == EOF:
        nxt_tok = EOF
        lexeme = ['E', 'O', 'F']

    print(f"Next token is: {nxt_tok}, Next lexeme is {''.join(lexeme)}")
    return nxt_tok


def main():
    global file

    try:
        file = open("/Users/ahmedsherif/Desktop/LX.txt", "r")
    except FileNotFoundError:
        print("ERROR - cannot open LX.txt")
        return

    GET_Char()
    while LEx() != EOF:
        pass

    file.close()


if __name__ == "__main__":
    main()
