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
    '''programa : REGLA_PROGRAMA ID DOSPUNTOS vars bloque
                | REGLA_PROGRAMA ID DOSPUNTOS bloque    
    '''

def p_vars(p):
    '''vars : REGLA_VAR declaracionVar'''

def p_declaracionVar(p):
    '''declaracionVar : var_id DOSPUNTOS tipo PUNTOYCOMA'''

def p_var_id(p):    
    '''var_id : ID 
                | ID COMA var_id'''

def p_tipo(p):
    '''tipo : REGLA_INT 
            | REGLA_FLOAT'''

def p_bloque(p):
    '''bloque : ABRECOR CIERRACOR 
                | ABRECOR varios_estatutos CIERRACOR'''

def p_varios_estatutos(p):
    '''varios_estatutos : estatuto 
                            | estatuto varios_estatutos'''

def p_estatuto(p):
    '''estatuto : asignacion 
                | condicion 
                | escritura'''

def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNTOYCOMA'''

def p_condicion(p):
    '''condicion : REGLA_IF ABREPAR expresion CIERRAPAR bloque PUNTOYCOMA
                    | REGLA_IF ABREPAR expresion CIERRAPAR bloque REGLA_ELSE bloque PUNTOYCOMA'''

def p_escritura(p):
    '''escritura : REGLA_PRINT ABREPAR imprime CIERRAPAR PUNTOYCOMA'''

def p_imprime(p):
    '''imprime : expresion 
                | CTE_S
                | expresion COMA imprime
                | CTE_S COMA imprime'''

def p_expresion(p):
    '''expresion : exp
                | exp MAYORQUE exp
                | exp MENORQUE exp
                | exp DIFDE exp'''

def p_exp(p):
    '''exp : termino
            | termino SUMA exp
            | termino RESTA exp'''


def p_termino(p):
    '''termino : factor
                | factor MULTIPLICACION termino
                | factor DIVISION termino'''

def p_factor(p):
    '''factor : ABREPAR expresion CIERRAPAR
                | SUMA var_cte
                | RESTA var_cte
                | var_cte'''

def p_var_cte(p):
    '''var_cte : ID
                | CTE_I
                | CTE_F'''

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




