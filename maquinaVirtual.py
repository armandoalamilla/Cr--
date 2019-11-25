import cuadruplos as cuad
import memoria as mem
import average as avg
import median as median
import plot as plot
import dirFunciones as directorio
import mode as mode
from ast import literal_eval
import sys

cuadActual = 0
contadorFuncEspeciales = 1
pilaFuncionesEspeciales = []
global direccionRead , valorRead, valorTipo, inputVal
pilaContexto=['GLOBAL']
pilaCuadActual = []
pilaReturn = []
mem.tablaMemoriaEjecución = {'GLOBAL' : {}}
#print(mem.tablaMemoriaEjecución)
contadorParam=1
def maquinaVirtual():
    global cuadActual, pilaContexto,contadorParam, pilaCuadActual, pilaReturn, contadorFuncEspeciales, pilaFuncionesEspeciales

    while cuadActual < cuad.contQuadAux:
        #print(cuadActual)
        #print(pilaContexto)
        #print(mem.tablaMemoriaEjecución)
        if cuad.PQuad[cuadActual]['operator'] == 'GOTO':
            cuadActual = cuad.PQuad[cuadActual]['result']
        elif cuad.PQuad[cuadActual]['operator'] == 'PRINT':
            print("IMPRIME CONSOLA:",mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result'],pilaContexto[len(pilaContexto)-1]))
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'READ':
            direccionRead = cuad.PQuad[cuadActual]['result']
            print(direccionRead)
            valorRead = input("INGRESA EL VALOR DE LA VAR: ")

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

            mem.almacenaMemoriaEjecucion(direccionRead ,inputVal,pilaContexto[len(pilaContexto)-1])
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == '=':
            direccionVar = cuad.PQuad[cuadActual]['result']
            valor = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1])
            mem.almacenaMemoriaEjecucion(direccionVar,valor,pilaContexto[len(pilaContexto)-1])
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == '+':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) + mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '-':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) - mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '*':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) * mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '/':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) / mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '>':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) > mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '<':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) < mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '==':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) == mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '!=':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) != mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '>=':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) >= mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == '<=':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) <= mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == 'AND':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) and mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == 'OR':
            resultado = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1]) or mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['right_operand'],pilaContexto[len(pilaContexto)-1])
            #print('suma es igual', resultado)
            mem.almacenaMemoriaEjecucion(cuad.PQuad[cuadActual]['result'],resultado,pilaContexto[len(pilaContexto)-1])
            cuadActual+=1        
        elif cuad.PQuad[cuadActual]['operator'] == 'GOTOF':
            evalua = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-1])
            if not evalua:
                cuadActual = cuad.PQuad[cuadActual]['result']
            else:
                cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'ERA':
            #solicitar crear espeacio en memoria para la func
            if cuad.PQuad[cuadActual]['left_operand'] != pilaContexto[len(pilaContexto)-1]:
                pilaContexto.append(cuad.PQuad[cuadActual]['left_operand'])
                mem.generaMemoriaEjecucion(pilaContexto[len(pilaContexto)-1])
            else:            
                pilaContexto.append(cuad.PQuad[cuadActual]['left_operand'])
            #print(mem.tablaMemoriaEjecución)
            cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == 'PARAM':
            #obtener dir de memoria de param
            tempVarParam = directorio.funcionLista[pilaContexto[len(pilaContexto)-1]]['paramDefinidos'][contadorParam]['name']
            direccion = directorio.funcionLista[pilaContexto[len(pilaContexto)-1]]['variables'][tempVarParam]['dirMemoria']
            #obtener los valores del contexto anterior en base a los cuads
            valor = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['left_operand'],pilaContexto[len(pilaContexto)-2])
            mem.almacenaMemoriaEjecucion(direccion,valor,pilaContexto[len(pilaContexto)-1])
            contadorParam +=1
            if cuad.PQuad[cuadActual+1]['operator'] == 'GOSUB':
                contadorParam = 1
                pilaCuadActual.append(cuadActual+1)
                cuadActual = directorio.funcionLista[pilaContexto[len(pilaContexto)-1]]['cuadInicial']
            else:
                cuadActual+=1
        elif cuad.PQuad[cuadActual]['operator'] == 'GOSUB':
            if cuad.PQuad[cuadActual]['left_operand'] != pilaContexto[len(pilaContexto)-2]:
                mem.tablaMemoriaEjecución[pilaContexto[len(pilaContexto)-1]].clear()
            
            pilaContexto.pop()
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'ENDPROC':
            cuadActual = pilaCuadActual.pop()
        elif cuad.PQuad[cuadActual]['operator'] == 'RETURN':
            result = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result'],pilaContexto[len(pilaContexto)-1])
            direccion = directorio.funcionLista['MAIN']['variables'][pilaContexto[len(pilaContexto)-1]]['dirMemoria']
            mem.almacenaMemoriaEjecucion(direccion,result,pilaContexto[len(pilaContexto)-2])
            cuadActual +=1
        elif cuad.PQuad[cuadActual]['operator'] == 'AVERAGE':
            result = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result'],pilaContexto[len(pilaContexto)-1])
            pilaFuncionesEspeciales.append(result)
            if len(pilaFuncionesEspeciales) == 4:
                print('PROCESANDO DATOS.....')
                avg.average(pilaFuncionesEspeciales[0],pilaFuncionesEspeciales[1],pilaFuncionesEspeciales[2],pilaFuncionesEspeciales[3])
                pilaFuncionesEspeciales.clear()
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'MEDIAN':
            result = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result'],pilaContexto[len(pilaContexto)-1])
            pilaFuncionesEspeciales.append(result)
            if len(pilaFuncionesEspeciales) == 4:
                print('PROCESANDO DATOS.....')
                median.median(pilaFuncionesEspeciales[0],pilaFuncionesEspeciales[1],pilaFuncionesEspeciales[2],pilaFuncionesEspeciales[3])
                pilaFuncionesEspeciales.clear()
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'MODE':
            result = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result'],pilaContexto[len(pilaContexto)-1])
            pilaFuncionesEspeciales.append(result)
            if len(pilaFuncionesEspeciales) == 2:
                print('PROCESANDO DATOS.....')
                mode.mode(pilaFuncionesEspeciales[0],pilaFuncionesEspeciales[1])
                pilaFuncionesEspeciales.clear()
            cuadActual += 1
        elif cuad.PQuad[cuadActual]['operator'] == 'PLOT':

            result = mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result'],pilaContexto[len(pilaContexto)-1])
            pilaFuncionesEspeciales.append(result)
            if len(pilaFuncionesEspeciales) == 4:
                print('PROCESANDO DATOS.....')
                plot.plot(pilaFuncionesEspeciales[0],pilaFuncionesEspeciales[1],pilaFuncionesEspeciales[2],pilaFuncionesEspeciales[3])
                pilaFuncionesEspeciales.clear()
            cuadActual += 1        

            
        else:
            cuadActual+=1
