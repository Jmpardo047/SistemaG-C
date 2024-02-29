from csv import reader
import modules.corefiles as core
def AddInit():
    data = []
    database = {}
    with open('data\libro.csv','r') as file:
        lector = reader(file)
        for item in lector:
            data.append(item)
            dicbase = {
                'codtransaccion' : item[0],
                'nroformulario' : item[1],
                'codecampus' : item[2],
                'nombre' : item [3],
                'marca' : item [4],
                'categoria' : item [5],
                'tipo' : item [6],
                'valor' : item [7],
                'proveedor' : item [8],
                'nroserial' : item [9],
                'empresa' : item[10],
                'estado' : item[11],
                'historial' : {}
            }
            database.update({item[2]:dicbase})
    campus = core.VerifyEx() 
    campus["activos"].update(database) 
    core.UpdateFile('campus.json',campus) 
