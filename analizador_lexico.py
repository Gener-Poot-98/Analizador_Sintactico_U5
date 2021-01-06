import sys
import ply.lex as lex

tokens = (

    # RESERVERD WORDS LIST

    'AND','ARRAY','AS','BREAK','CASE','CATCH','CLASS','CONST','CONTINUE','DEBUGGER','DECLARE','DEFAULT',
    'DELETE','DO','ECHO','ELSE','ELSEIF','EMPTY','EXPORT','EXTENDS','FINALLY','FOR','FOREACH','FUNCTION',
    'GLOBAL','IF','IMPLEMENTS','IMPORT','IN','INCLUDE','INSTANCEOF','LET','NEW','OR','PRINT','PRIVATE',
    'PROTECTED','PUBLIC','REQUIRE','RETURN','STATIC','SUPER','SWITCH','THIS','THROW','TRY','TYPEOF','VAR',
    'WHILE','WITH','XOR','YIELD',

    #boolean
    'TRUE','FALSE',

    # SYMBOLS
    'SUMA','INCREMENTO','PLUSEQUAL','RESTA','DECREMENTO','MINUSEQUAL','MULTIPLICACION',
    'TIMESTIMES','DIVISION','MENOR','MENOR_IGUAL','MAYOR','MAYOR_IGUAL','IGUAL',
    'DESIGUAL','DISTINTO','ES_IGUAL','PUNTOYCOMA','COMA','PARENT_IZQ','PARENT_DER','CORCHETE_IZQ',
    'CORCHETE_DER','LLAVE_IZQ','LLAVE_DER','DOS_PUNTOS','AMPERSANT','HASHTAG','PUNTO','COMILLAS',
    'APOSTROFE','DOT_DOT',

    # OTHERS
    'COMMENTS','COMMENTS_C99','VARIABLE','IDVAR','NUMERO','STRING','VOID', 'ALERT',
)


# RE Tokens

# Ignored characters
t_ignore = " \t"

def t_VOID(t):
    r'VOID|void'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print (chr(27)+"[1;31m"+"\t ERROR: Illegal character"+chr(27)+"[0m")
    print ("\t\tLine: "+str(t.lexer.lineno)+"\t=> " + t.value[0])
    t.lexer.skip(1)

# RE RESERVERD WORDS LIST
def t_DEBUGGER(t):
    r'debugger'
    return t

def t_DELETE(t):
    r'delete'
    return t

def t_EXPORT(t):
    r'export'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_IN(t):
    r'in'
    return t

def t_LET(t):
    r'let'
    return t

def t_SUPER(t):
    r'super'
    return t

def t_THIS(t):
    r'this'
    return t

def t_TYPEOF(t):
    r'typeof'
    return t

def t_WITH(t):
    r'with'
    return t

def t_YIELD(t):
    r'yield'
    return t

def t_ALERT(t):
    r'alert'
    return t

def t_AND(t):
    r'and|AND|\&\&'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_AS(t):
    r'as'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_CONST(t):
    r'const'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_DECLARE(t):
    r'declare'
    return t

def t_DEFAULT(t):
    r'default'
    return t

def t_DO(t):
    r'do'
    return t

def t_ECHO(t):
    r'echo'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ELSEIF(t):
    r'elseif'
    return t

def t_EMPTY(t):
    r'empty'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FOREACH(t):
    r'foreach'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GLOBAL(t):
    r'global'
    return t

def t_IF(t):
    r'if'
    return t

def t_IMPLEMENTS(t):
    r'implements'
    return t

def t_INCLUDE(t):
    r'include'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_NEW(t):
    r'new'
    return t

def t_OR(t):
    r'or|\|\||OR'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_REQUIRE(t):
    r'require'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_STATIC(t):
    r'static'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_TRY(t):
    r'try'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_XOR(t):
    r'xor'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

# RE SYMBOLS
t_SUMA      = r'\+'
t_RESTA     = r'-'
t_MULTIPLICACION     = r'\*'
t_DIVISION    = r'/'
t_IGUAL     = r'='
t_DISTINTO   = r'!'
t_MENOR      = r'<'
t_MAYOR   = r'>'
t_PUNTOYCOMA      = r';'
t_COMA     = r','
t_PARENT_IZQ    = r'\('
t_PARENT_DER    = r'\)'
t_CORCHETE_IZQ  = r'\['
t_CORCHETE_DER  = r'\]'
t_LLAVE_IZQ    = r'{'
t_LLAVE_DER    = r'}'
t_DOS_PUNTOS     = r':'
t_AMPERSANT = r'\&'
t_HASHTAG   = r'\#'
t_PUNTO       = r'\.'
t_COMILLAS    = r'\"'
t_APOSTROFE = r'\''

def t_MENOR_IGUAL(t):
    r'<='
    return t

def t_MAYOR_IGUAL(t):
    r'>='
    return t

def t_DESIGUAL(t):
    r'!='
    return t

def t_ES_IGUAL(t):
    r'=='
    return t

def t_DECREMENTO(t):
    r'--'
    return t

def t_INCREMENTO(t):
    r'\+\+'
    return t

def t_TIMESTIMES(t):
    r'\*\*'
    return t

def t_DOT_DOT(t):
    r'::'
    return t


# RE OTHERS


def t_COMMENTS(t):
    r'\/\*([^*]|\*[^\/])*(\*)+\/'
    t.lexer.lineno += t.value.count('\n')

def t_COMMENTS_C99(t):
    r'(\/\/|\#)(.)*?\n'
    t.lexer.lineno += 1

def t_IDVAR(t):
    r'\$\w+(\d\w)*'
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_VARIABLE(t):
    r'\w+(\w\d)*'
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t


lexer = lex.lex()
script = 'prueba.js'
scriptfile = open(script, 'r')
scriptdata = scriptfile.read()
#print (scriptdata)
lexer.input(scriptdata)

print (chr(27)+"[0;36m"+"INICIO DEL ANÁLISIS LÉXICO"+chr(27)+"[0m")
i = 1
while True:
    tok = lexer.token()
    if not tok:
        break
    print ("\t"+str(i)+" - "+"Linea: "+str(tok.lineno)+"\t"+str(tok.type)+"  -->  "+str(tok.value))
    i += 1

print (chr(27)+"[0;36m"+"FIN DEL ANÁLISIS LÉXICO"+chr(27)+"[0m")