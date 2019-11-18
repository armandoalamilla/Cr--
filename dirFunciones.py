funcionLista = {}
lista_vars = {}
variables = 'variables'
name= 'name'
scope = 'scope'
tipo = 'tipo'
numParametrosDef = 'numParametrosDefinidos'
numLocalVariables = 'numLocalVariables'
paramDefinidos = 'paramDefinidos'
cuadInicial = 'cuadInicial'

contParams = 1



def almacenaFuncion(nombreFunc2, scope2, tipo2):
    global variables, name, scope, tipo, numParametrosDef,cuadContador
 
    #print(checaFuncionDeclararada(nombreFunc))
    funcionLista[nombreFunc2] = {
        name : nombreFunc2,
        scope : scope2,
        tipo : tipo2,
        cuadInicial : '',
        numParametrosDef : {},
        paramDefinidos : {},
        numLocalVariables : {},
        variables : {}
    }


def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar):

    lista_vars[nombreVar] =  {
            'name' : nombreVar,
            'tipo' : tipoVar,
            'dirMemoria' : '',
            'valor' : ''
        }

    funcionLista[nombreFunc][variables].update(lista_vars)
    lista_vars.clear()


def almacenaDirMemoria(nombreFunc, nombreVar,direccion):
    funcionLista[nombreFunc]['variables'][nombreVar]['dirMemoria'] = direccion

def almacenaParmsEnFunc(nombreFunc, nommbreVar, tipoVar):
    global contParams
    funcionLista[nombreFunc]['paramDefinidos'][contParams] = {
        'name' : nommbreVar,
        'tipo' : tipoVar,
    }
    contParams += 1

def checaFuncionDeclararada(nombreFunc):
   
   if funcionLista[nombreFunc].get(name):
       return True
   else:
       return False

def almacenaNumParametros(nombreFunc,contadorINT,contadorFLOAT,contadorBOOL,contadorD,contadorCHAR):

    funcionLista[nombreFunc][numParametrosDef] = {'INT' : contadorINT, 'FLOAT' : contadorFLOAT, 
    'CHAR' : contadorCHAR, 'BOOL' : contadorBOOL , 'DATASET' : contadorD}

def almacenaNumVarLocales(nombreFunc,contadorINT,contadorFLOAT,contadorBOOL,contadorD,contadorCHAR):

    funcionLista[nombreFunc][numLocalVariables] = {'INT' : contadorINT, 'FLOAT' : contadorFLOAT, 
    'CHAR' : contadorCHAR, 'BOOL' : contadorBOOL ,'DATASET' : contadorD}

def almacenaValorEnVar(nombreFunc,direcciom, valor):
    for x in funcionLista[nombreFunc]['variables']:
        if funcionLista[nombreFunc]['variables'][x]['dirMemoria'] == direcciom:
            funcionLista[nombreFunc]['variables'][x]['valor'] = valor
            




        
    
    


        
       


        


    








    

