# Materia: Laboratorio de Datos
# Título del trabajo: TP Arbolado
# Autores: Richard Pavez
# Descripcion general del contenido:
# Fecha de creacion: 23/8/2023
# Fecha de ultima modificacion: 

import csv

archivo_arbolado = "arbolado-en-espacios-verdes.csv"

#Ejercicio 1

def leer_parque(nombre_archivo,parque:str):
    with open(nombre_archivo, "rt",encoding="utf8") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        arboles_parque:list = []
        for linea in filas:
            if linea[10] == parque:
                arboles_parque.append(dict(zip(encabezado,linea)))
        return arboles_parque
    
print(len(leer_parque(archivo_arbolado,"GENERAL PAZ")))

#Ejercicio 2

def especies(lista_arboles):
    especies_en_lista:list = []
    for dic in lista_arboles:
        especies_en_lista.append(dic["nombre_com"])
    return set(especies_en_lista)

print(especies(leer_parque(archivo_arbolado,"GENERAL PAZ")))

#Ejercicio 3