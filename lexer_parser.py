import ply.lex as lex
import ply.yacc as yacc
import dirFunciones as directorio
import sys, json

aprobado = True


varNombreTemp = []

global varTipoActual, tipoTemp

global NombreFuncActual, scopeActual, tipoActual, tempNombreFunc

nombreFunc = ''

arrayNombreFunc = []

#contadores
contadorScope = 0
contadorINT = 0
contadorFLOAT = 0
contadorCHAR = 0
contadorDATASET = 0
contadorBOOL = 0


tempTipoVarFuncEntrada = ''
tempIdVarFuncEntrada = ''

tempTipo_modulos = ''
idTemp_modulos = ''
#variables que determinan el manejo de las funciones

NombreFuncActual = 'MAIN'
scopeActual = 'global'
tipoActual = 'VOID'

#directorio.almacenaFuncion(NombreFuncActual,scopeActual,tipoActual)



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
    'BASIC_V_P' : 'REGLA_BASIC_V_P',
    'VOID' : 'REGLA_VOID'
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
#t_RESIDUO = r'\%'
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


t_CTE_CHAR = r'\'' + r'([a-zA-Z_][a-zA-Z0-9_]*|.*|/*)' + r'\''



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
    '''programa : REGLA_PROGRAMA ID DOSPUNTOS pN1 REGLA_MAIN bloque REGLA_END 
                | REGLA_PROGRAMA ID DOSPUNTOS pN1 vars REGLA_MAIN bloque REGLA_END
                | REGLA_PROGRAMA ID DOSPUNTOS pN1 programa_modulos_aux REGLA_MAIN bloque REGLA_END
                | REGLA_PROGRAMA ID DOSPUNTOS pN1 vars  programa_modulos_aux REGLA_MAIN bloque REGLA_END  
    '''

# pN1: almacena el main en el dir de funciones
def p_pN1(p):
    ''' pN1 :'''
    global contadorScope, arrayNombreFunc, nombreFunc
    nombreFunc = "MAIN"
    directorio.almacenaFuncion('MAIN','GLOBAL','VOID')


    
  
def p_programa_modulos_aux(p):
    ''' programa_modulos_aux : modulos
                            | modulos programa_modulos_aux'''


def p_modulos(p):
    ''' modulos : REGLA_FUNCION pN8 tipo_func DOSPUNTOS pN4 pN3 ABREPAR modulos_aux CIERRAPAR vars bloque '''
    global idTemp_modulos, tempTipo_modulos, arrayNombreFunc


def p_modulos_aux(p):
    ''' modulos_aux : pN6 tipo pN5
                    | pN6 tipo COMA pN5 modulos_aux '''
    
    #print(p[1],tempTipoVarFuncEntrada)            

   

#almacenar ID de modulo -- punto neuralgico 4
def p_pN4(p):
    ''' pN4 : ID '''
    global nombreFunc
    nombreFunc = p[1] 


#almacenar variables de entrada de funciones -- punto neuralgico 5
def p_pN5(p):
    ''' pN5 : '''
    global tempIdVarFuncEntrada, tempIdVarFuncEntrada
    #print(tempIdVarFuncEntrada,tempTipoVarFuncEntrada)
    directorio.almacenaVarsEnFunc(nombreFunc,tempIdVarFuncEntrada,tempTipoVarFuncEntrada)


#almacenar id de la var de entrada de la func -- punto neuralgico 6
def p_pN6(p):
    ''' pN6 : ID '''
    global tempIdVarFuncEntrada
    tempIdVarFuncEntrada = p[1]

#almacenar num de parametros de entrada, -- punto neuralgico 7
def p_pN7(p):
    ''' pN7 : '''

#iniciar los contadores en 0 cada que inicia una nueva funcion -- punto neuralgico 8
def p_pN8(p):
    ''' pN8 : '''
    global contadorINT, contadorFLOAT, contadorBOOL, contadorDATASET, contadorCHAR
    contadorINT = 0
    contadorFLOAT = 0
    contadorBOOL = 0
    contadorDATASET = 0
    contadorCHAR = 0


#agrega el modulo -- punto neuralgico 3
def p_pN3(p):
    '''pN3 : '''
    global contadorScope, idTemp_modulos, tempTipo_modulos, arrayNombreFunc, nombreFunc
    #print(contadorScope, p[4])
    #arrayNombreFunc.append(idTemp_modulos)       
    scopeActual = 'LOCAL'
    #print(nombreFunc, tempTipo_modulos)
    directorio.almacenaFuncion(nombreFunc,scopeActual,tempTipo_modulos)
        
    
    
   


    
    
    

def p_vars(p):
    ''' vars : REGLA_VAR declaracionVar
                | REGLA_VAR declaracionVar vars'''

        


def p_tipo(p):
    '''tipo : REGLA_INT
        | REGLA_FLOAT
        | REGLA_CHAR
        | REGLA_DATASET
        | REGLA_BOOL '''
    global varNombreTemp, contadorScope, arrayNombreFunc, contadorScope, nombreFunc, tempTipoVarFuncEntrada
    global contadorINT, contadorFLOAT, contadorCHAR, contadorDATASET, contadorBOOL

    tempTipoVarFuncEntrada = p[1]
    
    #print(contadorScope, arrayNombreFunc)
    #print(arrayNombreFunc,contadorScope)
    for x in varNombreTemp:
        #print(x)      
        directorio.almacenaVarsEnFunc(nombreFunc,x,p[1])        
    varNombreTemp.clear()

    #contar el numero de tipos
    if p[1] == 'INT':
        contadorINT = contadorINT + 1
    elif p[1] == 'FLOAT':
        contadorFLOAT = contadorFLOAT + 1
    elif p[1] == 'CHAR':
        contadorCHAR = contadorCHAR + 1
    elif p[1] == 'BOOL':
        contadorBOOL = contadorBOOL + 1
    elif p[1] == 'DATASET':
        contadorDATASET = contadorDATASET + 1

    
    





       
    
    
      
    
   

    

def p_tipo_func(p):
    '''tipo_func : REGLA_INT
        | REGLA_FLOAT
        | REGLA_CHAR
        | REGLA_BOOL
        | REGLA_VOID '''
    global tempTipo_modulos   
    tempTipo_modulos = p[1]
    #print("tipo modulo",p[1])
    #directorio.almacenaFuncion(NombreFuncActual,scopeActual,tipoActual)
    
    

def p_expresion(p):
    '''expresion : exp MAYORQUE exp
                   | exp MENORQUE exp
                   | exp MAYORQUEIGUAL exp
                   | exp MENORQUEIGUAL exp
                   | exp IGUALIGUAL exp
                   | exp DIFDE exp
                   | exp '''

def p_logical_expresion(p):
    '''logical_expresion : REGLA_NOT expresion
        | expresion REGLA_AND expresion
        | expresion REGLA_OR expresion 
        | expresion '''

def p_estatuto(p):
    '''estatuto : llamada_funcion
        | asignacion
        | condicion
        | escritura
        | ciclo
        | func_pred
        | lectura '''

def p_llamada_funcion(p):
    ''' llamada_funcion : ID ABREPAR llamada_funcion_aux CIERRAPAR PUNTOYCOMA'''

def p_llamada_funcion_aux(p):
    ''' llamada_funcion_aux : exp
                            | exp COMA llamada_funcion_aux'''

def p_escritura(p):
    ''' escritura : REGLA_PRINT ABREPAR escritura_aux CIERRAPAR PUNTOYCOMA '''

def p_escritura_aux(p):
    ''' escritura_aux : expresion 
                        | expresion COMA escritura_aux '''

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
    ''' func_pred : REGLA_AVERAGE ABREPAR ID COMA CTE_I CIERRAPAR
        | REGLA_MEDIAN ABREPAR ID COMA CTE_I CIERRAPAR
        | REGLA_MODE ABREPAR ID COMA CTE_I CIERRAPAR
        | REGLA_PLOT ABREPAR ID COMA CTE_CHAR COMA CTE_CHAR CIERRAPAR
        | REGLA_PIECHART ABREPAR ID CIERRAPAR
        | REGLA_VARIANZA ABREPAR ID COMA CTE_I CIERRAPAR
        | REGLA_DESV_T ABREPAR ID COMA CTE_I CIERRAPAR
        | REGLA_DIST_N ABREPAR ID COMA CTE_I CIERRAPAR
        | REGLA_BASIC_V_P ABREPAR ID COMA CTE_CHAR CIERRAPAR
        '''

def p_lectura(p):
    ''' lectura : REGLA_READ ABREPAR ID CIERRAPAR PUNTOYCOMA
        | REGLA_READ ABREPAR ID array CIERRAPAR PUNTOYCOMA
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
                        | ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_INT PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK DOSPUNTOS  REGLA_FLOAT PUNTOYCOMA
                        | ID ABREBRACK CTE_I CIERRABRACK ABREBRACK CTE_I CIERRABRACK DOSPUNTOS REGLA_CHAR PUNTOYCOMA
                        '''
    global contadorScope, nombreFunc
    
        

    if p[1] != None :
        if p[5] != ':' :
            directorio.almacenaVarsEnFunc(nombreFunc,p[1],p[9])
        else:
            directorio.almacenaVarsEnFunc(nombreFunc,p[1],p[6])

    

        
def p_var_id(p):    
    ''' var_id : ID
                | ID COMA var_id
                '''
    global varNombreTemp
    varNombreTemp.append(p[1]) 
    

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
    ''' bloque : ABRECOR estatuto_aux CIERRACOR
                
    '''

def p_estatuo_aux(p):
    ''' estatuto_aux : estatuto 
                    | estatuto estatuto_aux '''

def p_exp(p):
    ''' exp : termino 
            | termino SUMA exp 
            | termino RESTA exp '''
    

def p_termino(p):
    ''' termino : factor 
                | factor MULTIPLICACION termino
                | factor DIVISION termino '''

def p_factor(p):
    ''' factor : ABREPAR logical_expresion CIERRAPAR 
                | var_cte 
                | SUMA var_cte 
                | RESTA var_cte '''




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


#imprimir dir de funciones
app_json = json.dumps(directorio.funcionLista, indent=4)
#pp_json2 = json.dumps(directorio.lista_vars, indent=4)
f = open("dirFunc.json", "w")
#g = open("dirVariables.json","w")
f.write(app_json)
#g.write(app_json2)
f.close()
#g.close()
#print(arrayNombreFunc)



if aprobado == True:
    print("Archivo APROBADO")
    sys.exit()
else:
    print("Archivo :(")
    sys.exit()




