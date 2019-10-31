#Declaracion de las pilas

#pila para "pending operators"
POper = []

#pila para "pending operands"
PilaO = []

#pila para los tipos
PTypes = []

#pila para los quadruplos
PQuad = []

#contador cuadruplos
contCuad = 0

right_operand = ''
right_type = ''
left_operand = ''
left_type = ''

def agregarCuad(operator, left_operand, right_operand, result):
    PQuad.append({'operator':operator, 'left_operand':left_operand,'right_operand':right_operand, 'result':result})
    global contCuad
    contCuad = contCuad + 1


