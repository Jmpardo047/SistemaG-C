from csv import reader
import corefiles as core
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
campus = core.VerifyEx() # el diccionario que devuelve la verificacion de existencia del json se almacena en la variable campus
campus["activos"].update(database) #se accede al diccionario, en este caso el json en la llave activos, y se le actualiza la informacion de data base
core.UpdateData('campus.json',campus) 
# la linea 26 de codigo actualiza toda la informacion guardada en dicbase y actualizada en data base para que sobreescriba los archivos en el json