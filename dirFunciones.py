funcionLista = {}


def cambiaScope(scopeTemp):    
    actual_scope = scopeTemp


def almacenaFuncion(nombreFunc, scope, tipo):
    funcionLista[nombreFunc] = {
        'name' : nombreFunc,
        'scope' : scope,
        'type' : tipo,
        'variables' : ''
    }

def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar):
    import varTable as tablaVars
    funcionLista[nombreFunc]['variables'] = tablaVars.addVariable(nombreVar,tipoVar)
    








    

