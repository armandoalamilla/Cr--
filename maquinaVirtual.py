import cuadruplos as cuad
import memoria as mem
import dirFunciones as directorio
cuadActual = 0

def maquinaVirtual():
    global cuadActual
    while cuadActual < cuad.contQuadAux:
        if cuad.PQuad[cuadActual]['operator'] == 'GOTO':
            cuadActual = cuad.PQuad[cuadActual]['result']
        elif cuad.PQuad[cuadActual]['operator'] == 'PRINT':
            print("IMPRIME CONSOLA:",mem.obtenerValordeMemoria(cuad.PQuad[cuadActual]['result']))
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
        else:
            cuadActual+=1
        
        


            
