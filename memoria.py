#iniciar memoria

#variables globales
Vgi = 1000
Vgf = 3000
Vgb = 5000
Vgc = 7000
Vgd = 9000

#variables locales
Vli = 11000
Vlf = 13000
Vlb = 15000
Vlc = 17000
Vld = 19000

#constantes
Cteint = 21000
Ctefloat = 23000
Ctebool = 25000
Ctechar = 27000
Ctedataset = 29000

#temporales
Tgi = 43000
Tgf = 45000
Tgb = 47000
Tgc = 49000
Tgd = 51000

contadorTemporalINT = Tgi
contadorTemporalFLOAT = Tgf
contadorTemporalCHAR = Tgc
contadorTemporalBOOL = Tgb
contadorTemporalDATASET = Tgd

tablaConstantes= {'INT': {}, 'FLOAT' : {}, 'CHAR': {}, 'BOOL': {}, 'DATASET': {}}
tablaMemoriaEjecución = {}
def almacenaConstantes(tipo,direccion,nombre):
    tablaConstantes[tipo][nombre] = {
        'direccion' : direccion,
        'valor' : nombre
    }

def obtenerMemoria(tipo,nombre):
    return tablaConstantes[tipo][nombre]['direccion']

def generaDirTemporal(tipo):
    global contadorTemporalINT, contadorTemporalFLOAT, contadorTemmporalCHAR
    global contadorTemporalDATASET, contadorTemporalBOOL
    if tipo == 'INT':
        contadorTemporalINT += 1
        return contadorTemporalINT - 1
    elif tipo == 'FLOAT':
        contadorTemporalFLOAT += 1
        return contadorTemporalFLOAT - 1
    elif tipo == 'CHAR':
        contadorTemporalCHAR += 1
        return contadorTemporalCHAR - 1
    elif tipo == 'BOOL':
        contadorTemporalBOOL += 1
        return contadorTemporalBOOL - 1
    else:
        contadorTemporalDATASET += 1
        return contadorTemporalDATASET - 1

def almacenaMemoriaEjecucion(direccion,valor):
    tablaMemoriaEjecución[direccion]= {'valor' : valor}

def obtenerValordeMemoria(direccion):
    #checar constantes enteras
    if direccion >= 21000 and direccion < 23000:
        for a in tablaConstantes['INT']:
            if tablaConstantes['INT'][a]['direccion'] == direccion:
                return tablaConstantes['INT'][a]['valor']
    #checar constantes float
    elif direccion >= 23000 and direccion < 25000:
        for a in tablaConstantes['FLOAT']:
            if tablaConstantes['FLOAT'][a]['direccion'] == direccion:
                return tablaConstantes['FLOAT'][a]['valor']
    #checa las temporales int
    elif direccion >= 43000 and direccion < 45000:
        return tablaMemoriaEjecución[direccion]['valor']
    #checa las temporales float
    elif direccion >= 45000 and direccion < 47000:
        return tablaMemoriaEjecución[direccion]['valor']
    #checar variables globales enteras
    elif direccion >= 1000 and direccion < 3000:
        return tablaMemoriaEjecución[direccion]['valor']
    #checar variables globales float
    elif direccion > 3000 and direccion < 5000:
        return tablaMemoriaEjecución[direccion]['valor']


        
            
        









#almacenaConstantes('INT',43000,5)

#print(tablaConstantes['INT'])