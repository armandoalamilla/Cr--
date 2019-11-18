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

tablaConstantes= {'INT': {}, 'FLOAT' : {}, 'CHAR': {}, 'BOOL': {}, 'DATASET': {}}
tablaTemporales = {'INT': {}, 'FLOAT' : {}, 'CHAR': {}, 'BOOL': {}, 'DATASET': {}}

def almacenaConstantes(tipo,direccion,nombre):
    tablaConstantes[tipo][nombre] = {
        'direccion' : direccion,
        'valor' : nombre
    }

def obtenerMemoria(tipo,nombre):
    return tablaConstantes[tipo][nombre]['direccion']

def checarRangoMemoriaScope(direccion):
    #checa si es del main/global
    if (direccion >= 1000 and direccion < 3000) or (direccion >= 3000 and direccion < 5000) or (direccion >= 5000 and direccion < 7000) or (direccion >= 7000 and direccion <9000) or (direccion >= 9000 and direccion < 11000):
        return 'MAIN'




#almacenaConstantes('INT',43000,5)

#print(tablaConstantes['INT'])