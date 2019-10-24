funcionLista = {}
lista_vars = {}
variables = 'variables'
from ast import literal_eval

def cambiaScope(scopeTemp):    
    actual_scope = scopeTemp

def almacenaFuncion(nombreFunc, scope, tipo):
    global variables
    funcionLista[nombreFunc] = {
        'name' : nombreFunc,
        'scope' : scope,
        'type' : tipo,
        variables : {}
    }


def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar):
    lista_vars[nombreVar] =  {
            'name' : nombreVar,
            'tipo' : tipoVar,
        }

    funcionLista[nombreFunc][variables].update(lista_vars)
    lista_vars.clear()

    
    


        
       


        


    








    

