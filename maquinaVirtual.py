import cuadruplos as cuad
import memoria as mem
import dirFunciones as directorio
from ast import literal_eval
import sys

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
            print(direccionRead)
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

            #En esta parte se comprueba que el tipo del valor ingresado concuerde
            #con el tipo de la variable ya antes declarada, si es asi, el valor
            #es convertido a el tipo correspondiente y lo almacena en memoria
            if (valorTipo[8] == 'i'):
                print('Lo que se ingresó es tipo int')
                if (direccionRead >= 1000 and direccionRead < 3000) | (direccionRead >= 11000 and direccionRead < 13000):
                    print("Si concuerda con el tipo de la variable")
                    inputVal = int(valorRead)
                else:
                    print("HORROR DE TIPOS")
                    sys.exit()
            elif (valorTipo[8] == 'f'):
                print('Lo que se ingresó es tipo float')
                if (direccionRead >= 3000 and direccionRead < 5000) | (direccionRead >= 13000 and direccionRead < 15000):
                    print("Si concuerda con el tipo de la variable")
                    inputVal = float(valorRead)
                else:
                    print("HORROR DE TIPOS")
                    sys.exit()
            elif (valorTipo[8] == 'b'):
                print('Lo que se ingresó es tipo bool')
                if (direccionRead >= 5000 and direccionRead < 7000) | (direccionRead >= 15000 and direccionRead < 17000):
                    print("Si concuerda con el tipo de la variable")
                    inputVal = bool(valorRead)
                else:
                    print("HORROR DE TIPOS")
                    sys.exit()
            else:
                print('Lo que se ingresó es tipo string')
                if (direccionRead >= 7000 and direccionRead < 9000) | (direccionRead >= 17000 and direccionRead < 19000):
                    print("Si concuerda con el tipo de la variable")
                    inputVal = valorRead
                else:
                    print("HORROR DE TIPOS")
                    sys.exit()

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
