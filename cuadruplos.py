#Declaracion de las pilas

#pila para "pending operators"
POper = []

#pila para "pending operands"
PilaO = []

#pila para los tipos
PTypes = []

#pila para los quadruplos
PQuad = []

#Pila de saltos
PJumps = []

#contador cuadruplos
contCuad = 0
contQuadAux = 0

right_operand = ''
right_type = ''
left_operand = ''
left_type = ''

#esta funcion se encarga de generar los cuadruplos
#se recibe el operador, left_operand, right_operand, result
#se añade el cuad a la pila y se actualiza el contador de cuads.
def agregarCuad(operator, left_operand, right_operand, result):
    PQuad.append({'operator':operator, 'left_operand':left_operand,'right_operand':right_operand, 'result':result})
    global contCuad, contQuadAux    
    contQuadAux = contQuadAux + 1
    


