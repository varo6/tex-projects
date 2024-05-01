import re
import os
# Abre el archivo en modo lectura
with open('resultado.txt', 'r') as file:
    # Itera sobre cada línea del archivo
    lines = []
    for line in file:
        # Imprime la línea
        if "integer" in line:
            # Elimina el carácter de nueva línea al final de la línea
            line = line.rstrip()
            lines.append(line)
    #print(lines)

    TOemisor, TPemisor, TCemisor, TStotal = [], [], [], []

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
            if i==0:
                S = numero_int
            elif i==1:
                G = numero_int
            elif i>1 and i<=8:
                TOemisor.append(numero_int)
            elif i>8 and i<=15:
                TCemisor.append(numero_int)
            elif i>15 and i<=22:
                TPemisor.append(numero_int)
            else:
                TStotal.append(numero_int)
            
    #valores = [0, 01, 025, 05, 075, 1, 125, 150, 175, 2, 25, 3, 35, 4, 45, 5, 6, 7, 8, 9, 95]

    archivos = os.listdir()
    for archivo in archivos:
        if archivo.endswith('.txt'):
            # Hacer algo con los archivos que terminan en ".txt"
            print(archivo)


    print(TOemisor)
    print(TCemisor)
    print(TPemisor)
    print(TStotal)

    #en un array doble llamado resultadoSorteo de esta forma int[][] -> [[Numeros,Premios],[Numeros,Premios],[Numeros,Premios]]