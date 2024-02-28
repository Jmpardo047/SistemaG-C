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
            'Marca' : item [4],
            'Categoria' : item [5],
            'Tipo' : item [6],
            'Valor' : item [7],
            'Proovdeor' : item [8],
            'Nroserial' : item [9],
            'Empresa' : item[10],
            'Estado' : item[11]
        }
        database.update({item[2]:dicbase})
campus = core.VerifyEx() # el diccionario que devuelve la verificacion de existencia del json se almacena en la variable campus
campus["activos"].update(database) #se accede al diccionario, en este caso el json en la llave activos, y se le actualiza la informacion de data base
core.UpdateData('campus.json',campus) 
# la linea 26 de codigo actualiza toda la informacion guardada en dicbase y actualizada en data base para que sobreescriba los archivos en el json