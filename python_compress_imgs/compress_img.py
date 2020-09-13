from skimage import io
import cv2
import pandas as pd
import numpy as np
import os
from os import system

'''
f1 = [1,2,5,7,9,11,11]
f2 = [2,3,4,5,7,10,13]
f3 = [14,15,1,2,3,4,5]

matriz = [
          [1,2,5,7,9,11,11],
          [2,3,4,5,7,10,13],
          [14,15,1,2,3,4,5]
         ]
'''

img_path = 'delta_NDVI.png'
img = cv2.imread(img_path, 0)
img_reverted = cv2.bitwise_not(img)
matriz_delta = cv2.resize(img_reverted, dsize=(200,200), interpolation=cv2.INTER_CUBIC) # print(matriz_delta)

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
cv2.imshow('dst_rt', matriz_delta)
cv2.waitKey(0)

Datos = pd.DataFrame(matriz_delta)                                                 
Tabla = pd.ExcelWriter('C:/Users/Usuario/Desktop/dataFuel.xlsx', engine='xlsxwriter')    # Engine indica que modulo usar para crear la tabla Excel.
Datos.to_excel(Tabla, sheet_name='Valores', index = False, header= False)                # index y header sacan los nombres de las columnas y filas.

'''
Datos = pd.DataFrame.from_dict({"Fila 1":f1, "Fila 2":f2, "Fila 3":f3}, orient="index")  
Tabla = pd.ExcelWriter('C:/Users/Usuario/Desktop/tabla.xlsx', engine='xlsxwriter')  
Datos.to_excel(Tabla, sheet_name='Valores', header= False) 
'''

# ----- Formateo -----
workbook = Tabla.book                                                        
worksheet = Tabla.sheets["Valores"]
formato = workbook.add_format({"align": "center"})     # Creo un formato con texto alineado al centro para luego aplicarselo a las columnas.
worksheet.set_column("A:GR", 15, formato)              # Selecciono de la columna A a la H y le digo que su anchura debe ser 15 y le aplico el formato definido arriba.
workbook.close()

# ----- GUARDAR Y ELIMINAR -----
# Tabla.save()
# input()
# os.remove('C:/Users/Usuario/Desktop/tabla.xlsx')
# print("Tabla borrada. Fin de programa")
