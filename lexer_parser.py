import ply.lex as lex
import ply.yacc as yacc
import sys

aprobado = True


reserved = {
    'PROGRAM' : 'REGLA_PROGRAMA',
    'VAR' : 'REGLA_VAR',
    'IF' : 'REGLA_IF',
    'ELSE' : 'REGLA_ELSE',
    'INT' : 'REGLA_INT',
    'FLOAT' : 'REGLA_FLOAT',
    'PRINT' : 'REGLA_PRINT'
}


tokens = [
    'SUMA','RESTA','DIVISION','MULTIPLICACION','MAYORQUE','MENORQUE','DIFDE',
    'ABREPAR','CIERRAPAR','ABRECOR','CIERRACOR','COMA','PUNTOYCOMA','ID','CTE_I',
    'CTE_F','CTE_S','DOSPUNTOS','IGUAL'
]

#tokens

t_SUMA = r'\+'
t_RESTA = r'\-'
t_DIVISION = r'\/'
t_MULTIPLICACION = r'\*'
t_IGUAL = r'\='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_DIFDE = r'\<>'
t_ABREPAR = r'\('
t_CIERRAPAR = r'\)'
t_ABRECOR = r'\{'
t_CIERRACOR = r'\}'
t_COMA = r'\,'
t_PUNTOYCOMA = r'\;'
t_DOSPUNTOS = r'\:'
t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_S = r'\"([^\\\n]|(\\.))*?\"'

tokens = tokens + list(reserved.values())

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

#caracteres que se ignoran

t_ignore = ' \t\n'

def t_error(t):   
    global aprobado 
    aprobado = False
    print("Caracter malo '%s'" % t.value[0])
    t.lexer.skip(1)
    print("debug: elton john")

#haz lexer
lex.lex()

def p_programa(p):
    '''programa : PROGRAMA ID PUNTOYCOMA MAIN bloque END 
                | PROGRAMA ID PUNTOYCOMA vars MAIN bloque END
                | PROGRAMA ID PUNTOYCOMA modulos MAIN bloque END
                | PROGRAMA ID PUNTOYCOMA vars modulos MAIN bloque END  
    '''

def p_vars(p):
    ''' vars : VAR declaracionVar'''

def p_declaracionVar(p):
    ''' declaracionVar : var_id DOSPUNTOS tipo PUNTOYCOMA'''

def p_var_id(p):
    ''' var_id : ID
                | ID COMA var_id  '''



def p_error(p):
    global aprobado
    aprobado = False
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()

parser = yacc.yacc()

archivo = "prueba.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

if aprobado == True:
    print("Archivo :)")
    sys.exit()
else:
    print("Archivo :(")
    sys.exit()




