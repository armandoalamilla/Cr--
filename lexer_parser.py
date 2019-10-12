import ply.lex as lex
import ply.yacc as yacc
import sys

aprobado = True


reserved = {
    'PROGRAM' : 'REGLA_PROGRAMA',
    'FUNC' : 'REGLA_FUNCION',
    'MAIN' : 'REGLA_MAIN',
    'IF' : 'REGLA_IF',
    'ELSE' : 'REGLA_ELSE',
    'PRINT' : 'REGLA_PRINT',
    'READ' : 'REGLA_READ',
    'VAR' : 'REGLA_VAR',
    'WHILE' : 'REGLA_WHILE',
    'INT' : 'REGLA_INT',
    'FLOAT' : 'REGLA_FLOAT',
    'CHAR' : 'REGLA_CHAR',
    'BOOL' : 'REGLA_BOOL',
    'AND' : 'REGLA_AND',
    'OR' : 'REGLA_OR',
    'NOT' : 'REGLA_NOT',
    'END' : 'REGLA_END',
    'AVERAGE' : 'REGLA_AVERAGE',
    'MEDIAN' : 'REGLA_MEDIAN',
    'MODE' : 'REGLA_MODE',
    'DATASET' : 'REGLA_DATASET',
    'PLOT' : 'REGLA_PLOT',
    'PIECHART' : 'REGLA_PIECHART',
    'VARIANZA' : 'REGLA_VARIANZA',
    'DESV_T' : 'REGLA_DESV_T',
    'DIST_T' : 'REGLA_DIST_T',
    'BASIC_V_P' : 'REGLA_BASIC_V_P'
}


tokens = [
    'SUMA','RESTA','MULTIPLICACION','DIVISION','RESIDUO'
          'MENORQUE', 'MENORQUEIGUAL'
          'MAYORQUE', 'MAYORQUEIGUAL',
          'IGUALIGUAL','DIFDE',
          'AND','OR','NOT'
          'ABREPAR','CIERRAPAR',
          'ABRECOR','CIERRACOR',
          'ABREBRACK','CIERRABRACK',
          'COMA','PUNTOYCOMA','DOSPUNTOS','IGUAL',
          'CTE_I','CTE_F','CTE_CHAR','CTE_BOOL','CTE_D',
          'ID',
          'IF',
          'ELSE',
          'FUNC',
          'MAIN
]

#tokens

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_RESIDUO = r'\%'
t_MAYORQUE = r'\>'
t_MAYORQUEIGUAL = r'\>='
t_MENORQUE = r'\<'
t_MENORQUE = r'\<='
t_IGUALIGUAL = r'\=='
t_DIFDE = r'\!='
t_AND = r'\AND'
t_OR = r'\OR'
t_NOT = r'\NOT'
t_ABREPAR = r'\('
t_CIERRAPAR = r'\)'
t_ABRECOR = r'\{'
t_CIERRACOR = r'\}'
t_ABREBRACK = r'\['
t_CIERRABRACK = r'\]'
t_COMA = r'\,'
t_PUNTOYCOMA = r'\;'
t_DOSPUNTOS = r'\:'
t_IGUAL = r'\='
t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'

t_CTE_CHAR = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_BOOL = r'\TRUE|FALSE'
t_CTE_D = r'\"([^\\\n]|(\\.))*?\"'


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
    '''programa : REGLA_PROGRAMA ID PUNTOYCOMA REGLA_MAIN bloque REGLA_END 
                | REGLA_PROGRAMA ID PUNTOYCOMA vars REGLA_MAIN bloque REGLA_END
                | REGLA_PROGRAMA ID PUNTOYCOMA modulos REGLA_MAIN bloque REGLA_END
                | REGLA_PROGRAMA ID PUNTOYCOMA vars modulos REGLA_MAIN bloque REGLA_END  
    '''

def p_vars(p):
    ''' vars : VAR declaracionVar'''

def p_tipo(p):
    '''tipo : REGLA_INT
        | REGLA_FLOAT
        | REGLA_CHAR
        | REGLA_DATASET
        | REGLA_BOOL '''

def p_tipo_func(p):
    '''tipo_func : REGLA_INT
        | REGLA_FLOAT
        | REGLA_CHAR
        | REGLA_BOOL '''

def p_declaracionVar(p):
    ''' declaracionVar : var_id DOSPUNTOS tipo PUNTOYCOMA
                        | var ID ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_INT PUNTOYCOMA
                        | var ID ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_FLOAT PUNTOYCOMA
                        | var ID ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_CHAR PUNTOYCOMA
                        | var ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK REGLA_INT PUNTOYCOMA
                        | var ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK REGLA_FLOAT PUNTOYCOMA
                        | | var ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK REGLA_CHAR PUNTOYCOMA
                        '''

def p_var_id(p):
    ''' var_id : ID
                | ID COMA var_id  '''



def p_error(p):
    global aprobado
    aprobado = False
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()

parser = yacc.yacc()

"""archivo = "prueba.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

if aprobado == True:
    print("Archivo :)")
    sys.exit()
else:
    print("Archivo :(")
    sys.exit()"""




