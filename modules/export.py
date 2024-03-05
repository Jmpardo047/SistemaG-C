import pandas as pd
from barcode import Code128
from barcode.writer import ImageWriter
import json
import os
def ExportFile():
    with open ('data/campus.json', 'r') as file:
        data = json.load(file)
        activos,personas,zonas,asignaciones = data.values()
        dicbase = {
                'codtransaccion' : [],
                'nroformulario' :[],
                'codecampus' :[],
                'nombre' : [],
                'marca' : [],
                'categoria' : [],
                'tipo' : [],
                'valor' : [],
                'proveedor' : [],
                'nroserial' : [],
                'empresa' : [],
                'estado' : [],
                'codigo': []
            }
        for keys,values in activos.items():
            dicbase['codtransaccion'].append(values['codtransaccion'])
            dicbase['nroformulario'].append(values['nroformulario'])
            dicbase['codecampus'].append(values['codecampus'])
            dicbase['nombre'].append(values['nombre'])
            dicbase['marca'].append(values['marca'])
            dicbase['categoria'].append(values['categoria'])
            dicbase['tipo'].append(values['tipo'])
            dicbase['valor'].append(values['valor'])
            dicbase['proveedor'].append(values['proveedor'])
            dicbase['nroserial'].append(values['nroserial'])
            dicbase['empresa'].append(values['empresa'])
            dicbase['estado'].append(values['estado'])
            dicbase['codigo'].append(Barcodes(values['codecampus']))
    
    df = pd.DataFrame(dicbase)
    if (os.path.isfile('campus.xlsx')):
        df.to_excel('campus.xlsx', index=False)
    else:
        df.to_excel('campus.xlsx', index=False, sheet_name='Campus')

def Barcodes(data):
    code = Code128(data,writer=ImageWriter())
    return code