import os
import json
import sys
BASE_DIRECTORY = 'data/'
dictStruct = {
    'activos':{},
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
        validInt()
    else:
        return num

def validFloat()->float:
    try:
        num = float(input(')..'))
    except ValueError:
        DelLine()
        validFloat()
    else:
        return num

def ValidStr():
        txt = (input(')..'))
        if (bool(txt) == True):
            return txt
        else:
            DelLine()
            ValidStr()

def DelLine():
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")
def VerifyEx():
    if (CheckFile('campus.json') == False):
        CreateFile('campus.json',dictStruct)
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

def UpdateData(archivo,data):
    with open(BASE_DIRECTORY+ archivo,'w') as fw:
        json.dump(data,fw,indent=4)