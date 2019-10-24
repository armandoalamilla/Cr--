funcionLista = {}
lista_vars = {}
variables = 'variables'
name= 'name'
scope = 'scope'
tipo = 'tipo'
from ast import literal_eval


def almacenaFuncion(nombreFunc2, scope2, tipo2):
    global variables, name, scope, tipo
 
    #print(checaFuncionDeclararada(nombreFunc))
    funcionLista[nombreFunc2] = {
        name : nombreFunc2,
        scope2 : scope2,
        tipo : tipo2,
        variables : {}
    }


def almacenaVarsEnFunc(nombreFunc, nombreVar, tipoVar):

    lista_vars[nombreVar] =  {
            'name' : nombreVar,
            'tipo' : tipoVar,
        }

    funcionLista[nombreFunc][variables].update(lista_vars)
    lista_vars.clear()

def checaFuncionDeclararada(nombreFunc):
   
   if funcionLista[nombreFunc].get(name):
       return True
   else:
       return False
        
    
    


        
       


        


    








    

