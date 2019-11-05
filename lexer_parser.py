import ply.lex as lex
import ply.yacc as yacc
import dirFunciones as directorio, cuadruplos as cuad
import cuboSemantico as cubo
import sys, json, os

aprobado = True


varNombreTemp = []

global varTipoActual, tipoTemp

global NombreFuncActual, scopeActual, tipoActual, tempNombreFunc

nombreFunc = ''
tempCTE = 'TEMPCTEAAAAAAAAA'
tempSigno = ''

arrayNombreFunc = []

temTipoCTE = ''



#contadores
contadorScope = 0
contadorINT = 0
contadorFLOAT = 0
contadorCHAR = 0
contadorDATASET = 0
contadorBOOL = 0
contadorVARID = 0

interruptorVARID = False


tempTipoVarFuncEntrada = ''
tempIdVarFuncEntrada = ''

tempTipo_modulos = ''
idTemp_modulos = ''
#variables que determinan el manejo de las funciones y scope actual

NombreFuncActual = ''
scopeActual = ''
tipoActual = ''
tempNombreVar = ''

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
#t_CTE_I = r'[0-9]+'
#t_CTE_F = r'[0-9]+\.[0-9]+'
#t_CTE_CHAR = r'(\'[^\']*\')'


tokens = tokens + list(reserved.values())

def t_CTE_B(t):
    r'TRUE|FALSE'
    global temTipoCTE
    temTipoCTE = 'BOOL'
    return t

def t_CTE_CHAR(t):
    r'(\'[^\']*\')'
    global temTipoCTE
    temTipoCTE = 'CHAR'
    return t


def t_CTE_F(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    global temTipoCTE
    temTipoCTE = 'FLOAT'
    return t

def t_CTE_I(t):
    r'[0-9]+'
    t.value = int(t.value)
    global temTipoCTE
    temTipoCTE = 'INT'
    return t


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
    '''programa : REGLA_PROGRAMA ID DOSPUNTOS pN1 REGLA_MAIN pN11 bloque REGLA_END
                | REGLA_PROGRAMA ID DOSPUNTOS pN1 vars REGLA_MAIN pN11 bloque REGLA_END
                | REGLA_PROGRAMA ID DOSPUNTOS pN1 pN24 programa_modulos_aux pN25 REGLA_MAIN pN11 bloque REGLA_END
                | REGLA_PROGRAMA ID DOSPUNTOS pN1 vars pN24 programa_modulos_aux pN25 REGLA_MAIN pN11 bloque REGLA_END
    '''

# pN1: almacena el main en el dir de funciones
def p_pN1(p):
    ''' pN1 : '''
    global contadorScope, arrayNombreFunc, nombreFunc
    nombreFunc = "MAIN"
    directorio.almacenaFuncion('MAIN','GLOBAL','VOID')

# pN11: cambia la func actual a main -- punto neuralgico 11
def p_pN11(p):
    ''' pN11 : '''
    global nombreFunc
    nombreFunc = 'MAIN'

#agregar cuad de goto a main antes de las func -- pn 24
def p_pN24(p):
    ''' pN24 : '''
    cuad.agregarCuad('GOTO','','','t'+str(cuad.contCuad))


def p_pN25(p):
    ''' pN25 : '''
    cuad.PQuad[0]['left_operand'] = cuad.contQuadAux




def p_programa_modulos_aux(p):
    ''' programa_modulos_aux : modulos
                            | modulos programa_modulos_aux'''


def p_modulos(p):
    ''' modulos : REGLA_FUNCION pN8 tipo_func DOSPUNTOS pN4 pN3 ABREPAR modulos_aux CIERRAPAR pN7 pN8 pN9 vars pN10 bloque pN21'''
    global idTemp_modulos, tempTipo_modulos, arrayNombreFunc


def p_modulos_aux(p):
    ''' modulos_aux : pN6 tipo pN5
                    | pN6 tipo COMA pN5 modulos_aux '''

    #print(p[1],tempTipoVarFuncEntrada)

#agrega el modulo -- punto neuralgico 3
def p_pN3(p):
    '''pN3 : '''
    global contadorScope, idTemp_modulos, tempTipo_modulos, arrayNombreFunc, nombreFunc
    #print(contadorScope, p[4])
    #arrayNombreFunc.append(idTemp_modulos)
    scopeActual = 'LOCAL'
    #print(nombreFunc, tempTipo_modulos)
    directorio.almacenaFuncion(nombreFunc,scopeActual,tempTipo_modulos)


#almacenar ID de modulo -- punto neuralgico 4
def p_pN4(p):
    ''' pN4 : ID '''
    global nombreFunc
    nombreFunc = p[1]


#almacenar variables de entrada de funciones -- punto neuralgico 5
#NOTA IMPORTANTE, AGREGAR EN EL DIR FUNC LOS PARAMETROS COMO NUEVO ATRIBUTO <-- OJO
def p_pN5(p):
    ''' pN5 : '''
    global tempIdVarFuncEntrada, tempIdVarFuncEntrada
    #print(tempIdVarFuncEntrada,tempTipoVarFuncEntrada)
    directorio.almacenaVarsEnFunc(nombreFunc,tempIdVarFuncEntrada,tempTipoVarFuncEntrada)
    directorio.almacenaParmsEnFunc(nombreFunc,tempIdVarFuncEntrada,tempTipoVarFuncEntrada)


#almacenar id de la var de entrada de la func -- punto neuralgico 6
def p_pN6(p):
    ''' pN6 : ID '''
    global tempIdVarFuncEntrada
    tempIdVarFuncEntrada = p[1]

#almacenar num de parametros de entrada, -- punto neuralgico 7
def p_pN7(p):
    ''' pN7 : '''
    global nombreFunc, contadorINT, contadorFLOAT, contadorBOOL, contadorDATASET, contadorCHAR

    directorio.almacenaNumParametros(nombreFunc,contadorINT,contadorFLOAT,contadorBOOL,contadorDATASET,contadorCHAR)
    #print(nombreFunc)
    #print("INT:",contadorINT,'FLOAT:',contadorFLOAT,'BOOL:',contadorBOOL,'DATASET:',contadorDATASET,'CHAR:',contadorCHAR)


#iniciar los contadores en 0 cada que inicia una nueva funcion y/o se declaran variables -- punto neuralgico 8
def p_pN8(p):
    ''' pN8 : '''
    global contadorINT, contadorFLOAT, contadorBOOL, contadorDATASET, contadorCHAR
    contadorINT = 0
    contadorFLOAT = 0
    contadorBOOL = 0
    contadorDATASET = 0
    contadorCHAR = 0

#inicializar el contador de var id en 0 -- punto neuralgico 9
def p_pN9(p):
    ''' pN9 : '''
    global contadorVARID
    contadorVARID = 0

#guardar num de vars locales de la funcion en el dir de funciones -- punto neuralgico 10
def p_pN10(p):
    ''' pN10 : '''
    global contadorINT, contadorFLOAT, contadorBOOL, contadorDATASET, contadorCHAR, nombreFunc
    directorio.almacenaNumVarLocales(nombreFunc,contadorINT,contadorFLOAT,contadorBOOL,contadorDATASET,contadorCHAR)
    #print(nombreFunc)
    #print('INT:',contadorINT,'FLOAT:',contadorFLOAT,'BOOL:',contadorBOOL,'DATASET',contadorDATASET,'CHAR',contadorCHAR)

#reiniciar contadores de cuads a 0 al terminar una funcion y genera el cuad ENDPROC -- pn 20
def p_pN21(p):
    ''' pN21 : '''
    cuad.agregarCuad('ENDPROC','','','t'+str(cuad.contCuad))
    cuad.contCuad = 0





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
    global contadorINT, contadorFLOAT, contadorCHAR, contadorDATASET, contadorBOOL, interruptorVARID, contadorVARID

    tempTipoVarFuncEntrada = p[1]

    #print(contadorScope, arrayNombreFunc)
    #print(arrayNombreFunc,contadorScope)
    for x in varNombreTemp:
        #print(x)
        directorio.almacenaVarsEnFunc(nombreFunc,x,p[1])
    varNombreTemp.clear()

    #contar el numero de tipos para paremetros - func
    if directorio.funcionLista[nombreFunc]['scope'] == 'LOCAL' and interruptorVARID == False:
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
    elif interruptorVARID == True: #verifica si viene de varid
        if p[1] == 'INT':
            contadorINT = contadorVARID
        elif p[1] == 'FLOAT':
            contadorFLOAT = contadorVARID
        elif p[1] == 'CHAR':
            contadorCHAR = contadorVARID
        elif p[1] == 'BOOL':
            contadorBOOL = contadorVARID
        elif p[1] == 'DATASET':
            contadorDATASET = contadorVARID
        interruptorVARID = False
        contadorVARID = 0

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
    '''expresion : exp pN22_LUCIA exp pN23_LUCIA
                 | exp  '''

#almacenar el simbolo de mayorque y menorque en la pila POper -- punto neuralgico 21
def p_pN22_LUCIA(p):
    ''' pN22_LUCIA : MAYORQUE
             | MENORQUE
             | MAYORQUEIGUAL
             | MENORQUEIGUAL
             | IGUALIGUAL
             | DIFDE '''
    cuad.POper.append(p[1])

#checa la semantica cuando es > o < -- pN
def p_pN23_LUCIA(p):
    ''' pN23_LUCIA : '''
    try:
        cuad.POper[len(cuad.POper)-1]
    except IndexError:
        print("pila vacia")
    else:
        if cuad.POper[len(cuad.POper)-1] == '>' or cuad.POper[len(cuad.POper)-1] == '<' or cuad.POper[len(cuad.POper)-1] == '>=' or cuad.POper[len(cuad.POper)-1] == '<='or cuad.POper[len(cuad.POper)-1] == '==' or cuad.POper[len(cuad.POper)-1] == '!=':
            cuad.right_operand = cuad.PilaO.pop()
            cuad.right_type = cuad.PTypes.pop()
            cuad.left_operand = cuad.PilaO.pop()
            cuad.left_type = cuad.PTypes.pop()
            operator = cuad.POper.pop()
            result_type = cubo.sem_cubo[cuad.left_type][cuad.right_type][operator]
            if result_type != 'error':
                result = 't'+str(cuad.contCuad)
                cuad.agregarCuad(operator,cuad.left_operand,cuad.right_operand,result)
                cuad.PilaO.append(result)
                cuad.PTypes.append(result_type)
            else:
                print("HORROR DE TIPOS")
                sys.exit()



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
    ''' llamada_funcion : pN13 ABREPAR llamada_funcion_aux CIERRAPAR PUNTOYCOMA'''

def p_llamada_funcion_aux(p):
    ''' llamada_funcion_aux : exp
                            | exp COMA llamada_funcion_aux'''

def p_escritura(p):
    ''' escritura : REGLA_PRINT ABREPAR escritura_aux CIERRAPAR PUNTOYCOMA '''


def p_escritura_aux(p):
    ''' escritura_aux : expresion pN19
                        | expresion COMA pN19 escritura_aux '''

#genera cuad de escritura -- pN19
def p_pN19(p):
    ''' pN19 : '''
    cuad.PTypes.pop()
    cuad.agregarCuad('PRINT','',cuad.PilaO.pop(),'t'+str(cuad.contCuad))


def p_condicion(p):
    '''condicion : REGLA_IF ABREPAR logical_expresion CIERRAPAR bloque PUNTOYCOMA
        |  REGLA_IF ABREPAR logical_expresion CIERRAPAR bloque REGLA_ELSE bloque PUNTOYCOMA
        '''

def p_asignacion(p):
    '''asignacion : pN12 pN16 logical_expresion PUNTOYCOMA
        | pN12 array pN16 logical_expresion PUNTOYCOMA '''
    global nombreFunc


    if cuad.POper[len(cuad.POper)-1] == '=':
        cuad.right_operand = cuad.PilaO.pop()
        cuad.right_type = cuad.PTypes.pop()
        cuad.left_operand = cuad.PilaO.pop()
        cuad.left_type = cuad.PTypes.pop()
        operator = cuad.POper.pop()
        result_type = cubo.sem_cubo[cuad.left_type][cuad.right_type][operator]
        if result_type != 'error':
            result = 't'+str(cuad.contCuad)
            cuad.agregarCuad(operator,cuad.right_operand,'',cuad.left_operand)
            cuad.PilaO.append(cuad.left_operand)
            cuad.PTypes.append(result_type)
            #print('asignacion',cuad.PTypes)
            #print('asignacion',cuad.PilaO)
            #print('asignacion',cuad.POper)
            #cuad.PilaO.clear()
            #cuad.PTypes.clear()
        else:
            print("HORROR DE TIPOS")
            sys.exit()


#almacenar igual en POPer -- punto neuralgico 16
def p_pN16(p):
    ''' pN16 : IGUAL '''
    cuad.POper.append(p[1])



#verifica que la variable exista en el dir de funciones y almacenar en la pila de operandos -- punto neuralgico 12
def p_pN12(p):
    ''' pN12 : ID '''
    global nombreFunc, tempCTE, tempNombreVar

    try:
        directorio.funcionLista[nombreFunc]['variables'][p[1]]
    except KeyError:
        print('variable',p[1],'en',nombreFunc,'no esta declarada')
        sys.exit()
    else:
        cuad.PilaO.append(p[1])
        tempNombreVar = p[1]
        cuad.PTypes.append(directorio.funcionLista[nombreFunc]['variables'][p[1]]['tipo'])




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
    cuad.agregarCuad('READ','',p[3],'t'+str(cuad.contCuad))
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
    global nombreFunc, contadorINT, contadorFLOAT, contadorBOOL, contadorCHAR, contadorDATASET


    if p[1] != None :
        if p[5] == '[' : #verifica si es matrix
            directorio.almacenaVarsEnFunc(nombreFunc,p[1],p[9])
            if p[9] == 'INT':
                contadorINT = contadorINT + 1
            elif p[9] == 'FLOAT':
                contadorFLOAT = contadorFLOAT + 1
            elif p[9] == 'CHAR':
                contadorCHAR = contadorCHAR + 1
        else:   #verifica si es array
            directorio.almacenaVarsEnFunc(nombreFunc,p[1],p[6])
            if p[6] == 'INT':
                contadorINT = contadorINT + 1
            elif p[6] == 'FLOAT':
                contadorFLOAT = contadorFLOAT + 1
            elif p[6] == 'CHAR':
                contadorCHAR = contadorCHAR + 1





def p_var_id(p):
    ''' var_id : ID
                | ID COMA var_id
                '''
    global varNombreTemp, interruptorVARID, contadorVARID
    contadorVARID = contadorVARID + 1
    interruptorVARID = True
    varNombreTemp.append(p[1])


def p_var_cte(p):
    ''' var_cte : pN20
                | pN20 array
                | pN13 ABREPAR var_cte_aux CIERRAPAR
                | CTE_I
                | CTE_F
                | CTE_CHAR
                | CTE_BOOL
                | CTE_D
                '''
    global tempCTE, tempType

    if p[1] != None:
        cuad.PilaO.append(p[1])
        #tempType = p[1]

def p_pN20(p):
    ''' pN20 : ID '''
    global nombreFunc, tempCTE, tempNombreVar, temTipoCTE

    try:
        directorio.funcionLista[nombreFunc]['variables'][p[1]]
    except KeyError:
        print('variable',p[1],'en',nombreFunc,'no esta declarada')
        sys.exit()
    else:
        cuad.PilaO.append(p[1])
        tempNombreVar = p[1]
        temTipoCTE = directorio.funcionLista[nombreFunc]['variables'][p[1]]['tipo']





#checa que la funcion este declarada en el dir de funciones -- punto neuralgico 13
def p_pN13(p):
    ''' pN13 : ID '''
    global nombreFunc
    try:
        directorio.funcionLista[p[1]]
    except KeyError:
        print('La funcion',p[1],'en',nombreFunc,'no esta declarada')
        sys.exit()





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
    ''' exp : termino pN17
            | termino pN17 pN14 exp '''

#almacenar el simbolo de suma y resta en la pila POper -- punto neuralgico 14
def p_pN14(p):
    ''' pN14 : SUMA
             | RESTA '''
    cuad.POper.append(p[1])

#checa la semantica cuando es + o - -- pN 17
def p_pN17(p):
    ''' pN17 : '''
    try:
        cuad.POper[len(cuad.POper)-1]
    except IndexError:
        print("pila vacia")
    else:
        if cuad.POper[len(cuad.POper)-1] == '+' or cuad.POper[len(cuad.POper)-1] == '-':
            cuad.right_operand = cuad.PilaO.pop()
            cuad.right_type = cuad.PTypes.pop()
            cuad.left_operand = cuad.PilaO.pop()
            cuad.left_type = cuad.PTypes.pop()
            operator = cuad.POper.pop()
            result_type = cubo.sem_cubo[cuad.left_type][cuad.right_type][operator]
            if result_type != 'error':
                result = 't'+str(cuad.contCuad)
                cuad.agregarCuad(operator,cuad.left_operand,cuad.right_operand,result)
                cuad.PilaO.append(result)
                cuad.PTypes.append(result_type)
            else:
                print("HORROR DE TIPOS")
                sys.exit()







def p_termino(p):
    ''' termino : factor pN18
                | factor pN18 pN15 termino '''

#almacenar * o / en POper -- punto neuralgico 15
def p_pN15(p):
    ''' pN15 : MULTIPLICACION
            | DIVISION '''

    cuad.POper.append(p[1])

#checa la semantica cuando es + o - -- pN 18
def p_pN18(p):
    ''' pN18 : '''
    try:
        cuad.POper[len(cuad.POper)-1]
    except IndexError:
        print("pila vacia")
    else:
        if cuad.POper[len(cuad.POper)-1] == '*' or cuad.POper[len(cuad.POper)-1] == '/':
            cuad.right_operand = cuad.PilaO.pop()
            cuad.right_type = cuad.PTypes.pop()
            cuad.left_operand = cuad.PilaO.pop()
            cuad.left_type = cuad.PTypes.pop()
            operator = cuad.POper.pop()
            result_type = cubo.sem_cubo[cuad.left_type][cuad.right_type][operator]
            if result_type != 'error':
                result = 't'+str(cuad.contCuad)
                cuad.agregarCuad(operator,cuad.left_operand,cuad.right_operand,result)
                cuad.PilaO.append(result)
                cuad.PTypes.append(result_type)
            else:
                print("HORROR DE TIPOS")
                sys.exit()



def p_factor(p):
    ''' factor : pN24_LUCIA logical_expresion CIERRAPAR pN25_LUCIA
                | var_cte pN2 '''


#meter el tipo en la pila de operandos -- punto neuralgico 2
def p_pN2(p):
    ''' pN2 : '''
    global tempCTE, temTipoCTE
    cuad.PTypes.append(temTipoCTE)

#meter el signo de parentesis en la pila de operadores -- punto neuralgico 24
def p_pN24_LUCIA(p):
    ''' pN24_LUCIA : ABREPAR '''
    #print("ENTRA A PN24")
    cuad.POper.append(p[1])
    #print(cuad.POper)

#sacar el signo de parentesis en la pila de operadores -- punto neuralgico 25
def p_pN25_LUCIA(p):
    ''' pN25_LUCIA : '''
    #print("ENTRA A PN25")
    cuad.POper.pop()
    #print(cuad.POper)



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


print(cuad.POper)
print(cuad.PTypes)
print(cuad.PilaO)
contador = 0
for x in cuad.PQuad:
    print(contador,x)
    contador += 1



if aprobado == True:
    print("Archivo APROBADO")
    sys.exit()
else:
    print("Archivo :(")
    sys.exit()
