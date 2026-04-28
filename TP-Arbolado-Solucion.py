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
    for arbol in lista_arboles:
        especies_en_lista.append(arbol["nombre_com"])
    return set(especies_en_lista)

print(especies(leer_parque(archivo_arbolado,"GENERAL PAZ")))

#Ejercicio 3

def contar_ejemplares(lista_arboles):
    cantidad_ejemplares:dict = {}
    for arbol in lista_arboles:
        if arbol["nombre_com"] in cantidad_ejemplares:
            cantidad_ejemplares[arbol["nombre_com"]] += 1
        else:
            cantidad_ejemplares[arbol["nombre_com"]] = 1
    return cantidad_ejemplares

general_paz = leer_parque(archivo_arbolado,"GENERAL PAZ")
ejemplares_general = contar_ejemplares(general_paz)

print(ejemplares_general["Jacarandá"])

#Ejercicio 4

def obtener_alturas(lista_arboles,especie):
    lista_alturas:list = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            lista_alturas.append((float(arbol["altura_tot"])))
    return lista_alturas

def prom(lista):
    prom:int = 0
    for i in lista:
        prom += i
    prom = prom/len(lista)
    return prom
print(max(obtener_alturas(general_paz,"Jacarandá")),prom(obtener_alturas(general_paz,"Jacarandá")))

#Ejercicio 5

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones:list = []
    for arbol in lista_arboles:
        if arbol["nombre_com"] == especie:
            inclinaciones.append(float(arbol["inclinacio"]))
    return inclinaciones

#Ejercicio 6

def especimen_mas_incliado(lista_arboles):
    mas_inclinado_esp:str
    mas_inclinado_inc:int = 0
    for especie in especies(lista_arboles):
        if max(obtener_inclinaciones(lista_arboles,especie))>= mas_inclinado_inc:
            mas_inclinado_esp = especie
            mas_inclinado_inc = max(obtener_inclinaciones(lista_arboles,especie))
    return mas_inclinado_esp, mas_inclinado_inc

parque_centenario = leer_parque(archivo_arbolado,"CENTENARIO")
print(especimen_mas_incliado(parque_centenario))

#Ejercicio 7

def especie_promedio_mas_inclinada(lista_arboles):
    mayor_inclinacion_esp:str
    mayor_inclinacion_prom:int = 0
    for especie in especies(lista_arboles):
        if prom(obtener_inclinaciones(lista_arboles,especie))>=mayor_inclinacion_prom:
            mayor_inclinacion_prom = prom(obtener_inclinaciones(lista_arboles,especie))
            mayor_inclinacion_esp = especie
    return mayor_inclinacion_esp, mayor_inclinacion_prom

parq_los_andes = leer_parque(archivo_arbolado,"ANDES, LOS")
print(especie_promedio_mas_inclinada(parq_los_andes))
