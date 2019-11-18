import cuadruplos as cuad
import memoria as mem
import dirFunciones as directorio
cuadActual = 0

def maquinaVirtual():
    global cuadActual
    while cuadActual < cuad.contQuadAux:
        if cuad.PQuad[cuadActual]['operator'] == 'GOTO':
            cuadActual = cuad.PQuad[cuadActual]['result']
        elif cuad.PQuad[cuadActual]['operator'] == '=':
            if mem.checarRangoMemoriaScope(cuad.PQuad[cuadActual]['result']) == 'MAIN':
                print("lalalala")
            cuadActual += 1
        else:
            cuadActual+=1
        
        


            
