import cuadruplos as cuad
import memoria as mem
import dirFunciones as directorio
from ast import literal_eval
cuadActual = 0

global direccionRead , valorRead, valorTipo, inputVal



def maquinaVirtual():
    global cuadActual

    while cuadActual < cuad.contQuadAux:
        if cuad.PQuad[cuadActual]['operator'] == 'GOTO':
            cuadActual = cuad.PQuad[cuadActual]['result']
        elif cuad.PQuad[cuadActual]['operator'] == 'PRINT':
            print("IMPRIME CONSOLA:",mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result']))
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'READ':
            direccionRead = cuad.PQuad[cuadActual]['result'];
            valorRead = input("INGRESA EL VALOR DE LA VAR: ");

            def get_type(input_data): #Identifica que tipo es lo que se ingreso'
                try:
                    return type(literal_eval(input_data))
                except (ValueError, SyntaxError):
                    # A string, so return str
                    return str

            valorTipo = str(get_type(valorRead)) #Aqui guarda string
                                                 #<class 'int'>
                                                 #<class 'float'>
                                                 #<class 'bool'>
                                                 #<class 'string'>
                                                 #dependiendo lo ingresado
            if (valorTipo[8] == 'i'):
                print('es int')
                inputVal = int(valorRead)
            elif (valorTipo[8] == 'f'):
                print('es float')
                inputVal = float(valorRead)
            elif (valorTipo[8] == 'b'):
                print('es bool')
                inputVal = bool(valorRead)
            else:
                print('es string')
                inputVal = valorRead

            mem.almacenaMemoriaEjecucion(direccionRead ,inputVal)
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == '=':
            direccionVar = cuad.PQuad[cuadActual]['result']
            valor = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'])
            mem.almacenaMemoriaEjecucion(direccionVar,valor)
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == '+':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) + mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '-':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) - mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '*':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) * mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '/':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) / mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '>':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) > mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '<':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) < mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '==':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) == mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '!=':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) != mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '>=':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) >= mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '<=':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand']) <= mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == 'GOTOF':
            evalua = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'])
            if not evalua:
                cuadActual = cuad.PQuad[cuadActual]['result']
            else:
                cuadActual += 1
        else:
            cuadActual+=1
