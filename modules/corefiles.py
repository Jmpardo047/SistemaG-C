import os
import json
import sys
import modules.dicbase as db
BASE_DIRECTORY = 'data/'
dictStruct = {
    'activos':{},
    'personas':{
        'personasn': {},
        'personasj': {}
    },
    'personas':{
         'personasn':{},
         'personasj':{}
    },
    'zonas': {},
    'asignaciones':{}
}
def validInt()->int:
    try:
        num = int(input((')..')))
    except ValueError:
        DelLine()
        return validInt()
    else:
        return num

def validFloat()->float:
    try:
        num = float(input(')..'))
    except ValueError:
        DelLine()
        return validFloat()
    else:
        return num

def ValidStr():
        txt = (input(')..'))
        if (bool(txt) == True):
            return txt
        else:
            DelLine()
            return ValidStr()

def DelLine():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
def VerifyEx():
    if (CheckFile('campus.json') == False):
        CreateFile('campus.json',dictStruct)
        db.AddInit()
        return ReadFile('campus.json')
    else:
        return ReadFile('campus.json')

def CheckFile(file):
    if (os.path.isfile(BASE_DIRECTORY+file)):
        return True
    else:
        return False
    
def CreateFile(*param):
    with open (BASE_DIRECTORY+param[0],'w') as wf:
        json.dump(param[1],wf,indent=4)

def ReadFile(file):
    with open(BASE_DIRECTORY+file,'r') as rf:
        return json.load(rf)

def UpdateFile(archivo,data):
    with open(BASE_DIRECTORY+ archivo,'w') as fw:
        json.dump(data,fw,indent=4)

def ValidataCode(activos:dict):
    cod = input(')..')
    if (cod not in activos.keys()):
        print('Código ingresado no coincide con ningún activo')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(ValidataCode(activos))
        else:
            pass
    else:
        return cod

def ValidZone(zonas:dict):
    cod = input(')..')
    if (cod not in zonas.keys()):
        print('Nùmero ingresado no coincide con ninguna zona')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(ValidZone(zonas))
        else:
            pass
    else:
        return cod

def ValidPpl(personas : dict):
    os.system('cls')
    print('Ingrese el tipo de persona donde desea buscar su codigo')
    lstTipo = list(personas.keys())
    print(lstTipo)
    tipoPerso = ValidStr().lower()
    if (tipoPerso in lstTipo):
        print('Ingrese el codigo de la persona')
        code = input(':)_')
        if (code not in personas[tipoPerso]):
            print('Código ingresado no coincide con ninguna persona')
            rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
            if (rp == True):
                return(ValidPpl(personas))
            else:
                pass
        else:
            return [code,tipoPerso]
    else:
        print('Tipo de persona seleccionada no encontrada')
        rp = bool(input('Desea volver a intentar? --- S(Si) o Enter(No)'))
        if (rp == True):
            return(ValidPpl(personas))
        else:
                pass