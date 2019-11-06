funcionLista = {}
lista_vars = {}
variables = 'variables'
name= 'name'
scope = 'scope'
tipo = 'tipo'
numParametrosDef = 'numParametrosDefinidos'
numLocalVariables = 'numLocalVariables'
paramDefinidos = 'paramDefinidos'
cuadContador = 'cuadContador'

contParams = 1



def almacenaFuncion(nombreFunc2, scope2, tipo2):
    global variables, name, scope, tipo, numParametrosDef,cuadContador
 
    #print(checaFuncionDeclararada(nombreFunc))
    funcionLista[nombreFunc2] = {
        name : nombreFunc2,
        scope : scope2,
        tipo : tipo2,
        cuadContador : '',
        numParametrosDef : {},
        paramDefinidos : {},
        numLocalVariables : {},
        variables : {}
    }


def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar):

    lista_vars[nombreVar] =  {
            'name' : nombreVar,
            'tipo' : tipoVar,
        }

    funcionLista[nombreFunc][variables].update(lista_vars)
    lista_vars.clear()

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


        
    
    


        
       


        


    








    

