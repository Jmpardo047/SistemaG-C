from csv import reader
data = []
with open('data\libro.csv','r') as file:
    lector = reader(file)
    for item in lector:
        data.append(item)
        dicbase = {
            'codtransaccion' : item[0]
        }
print (data)