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


#esta funcion se encarga de almacenar la funcion en el directorio de funciones
#se recibe el nombre de la funcion, scope y su tipo
#se genera la estancia de la funcion junto con los demas atributos.
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

#esta funcion se encarga de almacenar las variables en la tabla de variables
#se recibe el nombre de la función, nombre de var, su tipo y dimension para los arrays.
#se genera uel directorio de la tabla de variables y se une a su respectiva instancia en el
#directorio de funciones.
def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar, dimension):

    lista_vars[nombreVar] =  {
            'name' : nombreVar,
            'tipo' : tipoVar,
            'dirMemoria' : '',
            'valor' : '',
            'dimension' : dimension,
            'varsDim' : {
            'Li': 0,
            'Ls': 0,
            '-k': 0,
            'AUX' : 0,
            }
        }

    funcionLista[nombreFunc][variables].update(lista_vars)
    lista_vars.clear()

#en esta funcion se almacenan las direcciones de variables declaradas.
#se recibe el nombre de la funcion, nombre de la variable y la direccion.
#se asigna la direccion a la variable.
def almacenaDirMemoria(nombreFunc, nombreVar,direccion):
    funcionLista[nombreFunc]['variables'][nombreVar]['dirMemoria'] = direccion

#en esta funcion se almacenan los parametros de entrada de las funciones en el dir de funciones.
#se recibe el nombre de la funcion y variable ademas del tipo de variable.
#se crea la instancia de los paramDefinidos en el dir de funciones.
def almacenaParmsEnFunc(nombreFunc, nommbreVar, tipoVar):
    global contParams
    funcionLista[nombreFunc]['paramDefinidos'][contParams] = {
        'name' : nommbreVar,
        'tipo' : tipoVar,
    }
    contParams += 1

#esta funcion se encarga de checar si la función esta declarada.
#recibe el nombre de la función.
#retorna un booleano
def checaFuncionDeclararada(nombreFunc):

   if funcionLista[nombreFunc].get(name):
       return True
   else:
       return False

#esta funcion se encarga de almacenar el numero de parametros en el dir de funciones.
#los parametros que se reciben son el nombre de la funcion y los contadores de int, float, bool, dataset y char
#se genera la instancia dentro del directorio de funciones con el num. de parametros.
def almacenaNumParametros(nombreFunc,contadorINT,contadorFLOAT,contadorBOOL,contadorD,contadorCHAR):

    funcionLista[nombreFunc][numParametrosDef] = {'INT' : contadorINT, 'FLOAT' : contadorFLOAT,
    'CHAR' : contadorCHAR, 'BOOL' : contadorBOOL , 'DATASET' : contadorD}

#esta funcion se encarga de almacenar el num local de variables locales.
#los parametros que se reciben nombre del funcion y los contadores de los diferentes tipos.
#se genera la instancia dentro del directorio de funciones con el num. de variables locales.
def almacenaNumVarLocales(nombreFunc,contadorINT,contadorFLOAT,contadorBOOL,contadorD,contadorCHAR):

    funcionLista[nombreFunc][numLocalVariables] = {'INT' : contadorINT, 'FLOAT' : contadorFLOAT,
    'CHAR' : contadorCHAR, 'BOOL' : contadorBOOL ,'DATASET' : contadorD}


def almacenaValorEnVar(nombreFunc,direcciom, valor):
    for x in funcionLista[nombreFunc]['variables']:
        if funcionLista[nombreFunc]['variables'][x]['dirMemoria'] == direcciom:
            funcionLista[nombreFunc]['variables'][x]['valor'] = valor
