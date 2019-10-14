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
    'DIST_N' : 'REGLA_DIST_N',
    'BASIC_V_P' : 'REGLA_BASIC_V_P'
}


tokens = [
    'SUMA','RESTA','MULTIPLICACION','DIVISION','RESIDUO',
          'MENORQUE', 'MENORQUEIGUAL',
          'MAYORQUE', 'MAYORQUEIGUAL',
          'IGUALIGUAL','DIFDE',
          'ABREPAR','CIERRAPAR',
          'ABRECOR','CIERRACOR',
          'ABREBRACK','CIERRABRACK',
          'COMA','PUNTOYCOMA','DOSPUNTOS','IGUAL',
          'CTE_I','CTE_F','CTE_CHAR','CTE_BOOL','CTE_D',
          'ID'
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
t_MENORQUEIGUAL = r'\<\='
t_IGUALIGUAL = r'\=\='
t_DIFDE = r'\!\='
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
    ''' vars : REGLA_VAR declaracionVar'''

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

def p_expresion(p):
    '''expresion : exp MAYORQUE exp
                   | exp MENORQUE exp
                   | exp MAYORQUEIGUAL exp
                   | exp MENORQUEIGUAL exp
                   | exp IGUALIGUAL exp
                   | exp DIFDE exp '''

def p_logical_expresion(p):
    '''logical_expresion : REGLA_NOT expresion
        | expresion REGLA_AND expresion
        | expresion REGLA_OR expresion '''

def p_estatuto(p):
    '''estatuto : llamada_funcion
        | asignacion
        | condicion
        | escritura
        | ciclo
        | func_pred
        | lectura '''

def p_condicion(p):
    '''condicion : REGLA_IF ABREPAR logical_expresion CIERRAPAR bloque PUNTOYCOMA
        |  REGLA_IF ABREPAR logical_expresion CIERRAPAR bloque REGLA_ELSE bloque PUNTOYCOMA
        '''

def p_asignacion(p):
    '''asignacion : ID IGUAL logical_expresion PUNTOYCOMA
        | ID array IGUAL logical_expresion PUNTOYCOMA
        '''

def p_ciclo(p):
    '''ciclo : REGLA_WHILE ABREPAR logical_expresion CIERRAPAR bloque PUNTOYCOMA
        '''

def p_func_pred(p):
    ''' func_pred : REGLA_AVERAGE ABREPAR CTE_D COMA CTE_I CIERRAPAR
        | REGLA_MEDIAN ABREPAR CTE_D COMA CTE_I CIERRAPAR
        | REGLA_MODE ABREPAR CTE_D COMA CTE_I CIERRAPAR
        | REGLA_PLOT ABREPAR CTE_D COMA CTE_CHAR COMA CTE_CHAR CIERRAPAR
        | REGLA_PIECHART ABREPAR CTE_D CIERRAPAR
        | REGLA_VARIANZA ABREPAR CTE_D COMA CTE_I CIERRAPAR
        | REGLA_DESV_T ABREPAR CTE_D COMA CTE_I CIERRAPAR
        | REGLA_DIST_N ABREPAR CTE_D COMA CTE_I CIERRAPAR
        | REGLA_BASIC_V_P ABREPAR CTE_D COMA CTE_CHAR CIERRAPAR
        '''

def p_lectura(p):
    ''' lectura : read ABREPAR ID CIERRAPAR PUNTOYCOMA
        | read ABREPAR ID array CIERRAPAR PUNTOYCOMA
        '''
def p_array(p):
    ''' array : ABREBRACK exp CIERRABRACK
        | ABREBRACK exp CIERRABRACK ABREBRACK exp CIERRABRACK
        '''

def p_declaracionVar(p):
    ''' declaracionVar : var_id DOSPUNTOS tipo PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_INT PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_FLOAT PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_CHAR PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK REGLA_INT PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK REGLA_FLOAT PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK REGLA_CHAR PUNTOYCOMA
                        | declaracionVar
                        '''

def p_var_id(p):
    ''' var_id : ID
                | ID COMA var_id  '''

def p_var_cte(p):
    ''' var_cte : ID 
                | ID array
                | ID ABREPAR var_cte_aux CIERRAPAR 
                | CTE_I
                | CTE_F
                | CTE_CHAR
                | CTE_BOOL
                | CTE_D
                '''

def p_var_cte_aux(p):
    ''' var_cte_aux : exp
                    | exp COMA var_cte_aux '''

def p_bloque(p):
    ''' bloque : ABRECOR estauto_aux CIERRACOR
                | ABRECOR CIERRACOR
    '''

def p_estatuo_aux(p):
    ''' estatuto_aux : estatuto 
                    | estatuto_aux '''

def p_exp(p):
    ''' exp : termino 
            | termino SUMA exp 
            | termino resta exp '''

def p_termino(p):
    ''' termino : factor 
                | factor MULTIPLICACION termino
                | factor DIVISION termino '''





        



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




