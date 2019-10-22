#declaracion de la estructura de datos.
lista_variables = {} 


def addVariable(variable_name, variable_type):
      
    lista_variables[variable_name] = {
        'name' : variable_name,
        'tipo' : variable_type
    }

    return lista_variables


    




#addVariable("var1", "")
#addVariable("var1", "FLOAT")

#print(lista_variables["var1"].get('tipo'))    
#print(lista_variables)