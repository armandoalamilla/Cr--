funcionLista = {}
lista_vars = {}
from ast import literal_eval

def cambiaScope(scopeTemp):    
    actual_scope = scopeTemp

def almacenaFuncion(nombreFunc, scope, tipo):
    funcionLista[nombreFunc] = {
        'name' : nombreFunc,
        'scope' : scope,
        'type' : tipo,
    }


def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar):
    lista_vars[nombreVar] =  {
            'name' : nombreVar,
            'tipo' : tipoVar,
            'func' : nombreFunc         

        }
        
       


        


    








    

