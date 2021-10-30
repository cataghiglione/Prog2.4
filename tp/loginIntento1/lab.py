numbre = "2267524623"
print(len(numbre))
cuil = "20446509103"
print(len(cuil))

import csv
def verificar(nombre, telefono, cuil):
    Anses = open("Anses.csv", "r")
    reader = csv.reader(Anses, delimiter="|")
    datos = [nombre, str(telefono), str(cuil)]
    for fila in reader:
        if fila[0] != datos[0] and fila[1] != datos[1] and fila[2] != datos[2]:
            return False
    Anses.close()
    return True
