import re
import os
import pandas as pd

# Los arrays que contendrán otros arrays dentro, serán nuestras matrices. Un array de estos equivale a una hoja de Excel.
TOemisores, TPemisores, TCemisores, TStotales = [], [], [], []

# Nuestros valores de PG
valores = ["0", "01", "025","05", "075", "1", "125", "150", "175", "2", "25", "3", "35", "4", "45", "5", "6", "7", "8", "9", "95"]

# Iteramos los valores.
for valor in valores:
    archivo = "resultado_0_" + valor + ".txt"
    with open(archivo, 'r') as file:

        # Itera sobre cada línea del archivo
        lines = []
        for line in file:

            if "integer" in line:

                # Elimina el carácter de nueva línea al final de la línea
                line = line.rstrip()
                lines.append(line)

        # Aqui guardaremos los valores para un PG específico. Luego, TOemisor en PG=0.X lo meteremos en TOemisores, etc.
        TOemisor, TPemisor, TCemisor, TStotal = [], [], [], []
    
        # Lo primero será añadir el valor de PG
        TOemisor.append(float("0."+valor))
        TPemisor.append(float("0."+valor))
        TCemisor.append(float("0."+valor))
        TStotal.append(float("0."+valor))

        # Inicializamos los valores
        valoresTO, valoresTC, valoresTS, valoresTP = 0,0,0,0

        for i in range(len(lines)):
            string = lines[i]
            # Busca el número en el string usando una expresión regular
            match = re.search(r'\d+', string)
            # Si se encuentra un número en el string
            if match:
                # Extrae el número como una cadena
                numero_str = match.group()

                # Convierte la cadena a un entero
                numero_int = int(numero_str)

                # Dependiendo del número de línea, guardamos en TOemisor u otro array
                if i==0:
                    S = numero_int
                elif i==1:
                    G = numero_int
                elif i>1 and i<=8:
                    TOemisor.append(numero_int)
                    valoresTO += numero_int
                elif i>8 and i<=15:
                    TCemisor.append(numero_int)
                    valoresTC += numero_int
                elif i>15 and i<=22:
                    TPemisor.append(numero_int)
                    valoresTP += numero_int
                else:
                    TStotal.append(numero_int)
                    valoresTS += numero_int

        valoresTO = valoresTO/10000
        valoresTC = valoresTC/10000
        valoresTS = valoresTS/10000
        valoresTP = valoresTP/10000
        TOemisor.append(valoresTO)
        TCemisor.append(valoresTC)
        TStotal.append(valoresTS)
        TPemisor.append(valoresTP)

        TOemisores.append(TOemisor)
        TPemisores.append(TPemisor)        
        TCemisores.append(TCemisor)
        TStotales.append(TStotal)

#Pasamos nuestras matrices a DataFrame para poder exportarlas

df_TOemisores = pd.DataFrame(TOemisores, columns=["PG", "TOemisor1", "TOemisor2", "TOemisor3", "TOemisor4", "TOemisor5", "TOemisor6", "TOemisor7", "Media TO"])

df_TCemisores = pd.DataFrame(TCemisores, columns=["PG", "TCemisor1", "TCemisor2", "TCemisor3", "TCemisor4", "TCemisor5", "TCemisor6", "TCemisor7", "Media TC"])

df_TPemisores = pd.DataFrame(TPemisores, columns=["PG", "TPemisor1", "TPemisor2", "TPemisor3", "TPemisor4", "TPemisor5", "TPemisor6", "TPemisor7", "Media TP"])

df_TStotales = pd.DataFrame(TStotales, columns=["PG", "TStotal1", "TStotal2", "TStotal3", "TStotal4", "TStotal5", "TStotal6", "TStotal7", "Media TS"])

# Exportamos datos filtrados a Excel, IMPORTANTE tener como workspace la carpeta en la que estamos trabajando.

string = "datos_filtrados.xlsx"
if string not in os.listdir():
    # Crear un escritor de Excel
    with pd.ExcelWriter(string) as writer:
        # Escribir el DataFrame de TCemisores en la primera hoja
        df_TOemisores.to_excel(writer, sheet_name='TOemisores', index=False)
        # Escribir el DataFrame de TOemisores en la segunda hoja
        df_TCemisores.to_excel(writer, sheet_name='TCemisores', index=False)

        df_TPemisores.to_excel(writer, sheet_name='TPemisores', index=False)

        df_TStotales.to_excel(writer, sheet_name='TStotales', index=False)
else:
    print("No se ha generado un archivo excel porque ya existe uno con el mismo nombre")
