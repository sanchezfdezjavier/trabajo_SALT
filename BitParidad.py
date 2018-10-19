# -*- coding: utf-8 -*-
"""
Segundo programa de la simulación en SALT, teoría de la información
@author Fernando 


"""
import random
import copy
import matplotlib.pyplot as plt

#Fer
def generar_lista_de_bits(n): 
    lista = []
    for i in range(n):
        bit_aleatorio = random.choice([0, 1])
        lista.append(bit_aleatorio)
    return lista

#Fer
def alterar_lista_de_bits(lista, p):
    for i in range(len(lista)):
        alterar = random.random() < p # Bernouilli(p)
        if alterar:
            lista[i] = 1 - lista[i]
#Fer
def annadir_bit_paridad(lista_a):
    bit_paridad = sum(lista_a)%2
    lista_a.append(bit_paridad)

#Fer
def probabilidad_empirica_error_detectado(n, p):
    N = 10**3
    contador_mensajes_alterados = 0
    cont_mensajes_alterados_y_detectados = 0
    for i in range(N):  
        # Generar el mensaje que se emite:
        mensaje_emitido = generar_lista_de_bits(n)
        
        # Generar el mensaje que se recibe:
        annadir_bit_paridad(mensaje_emitido)
        mensaje_recibido = copy.deepcopy(mensaje_emitido)
        alterar_lista_de_bits(mensaje_recibido, p)
        
        # Calculamos el bit de paridad del mensaje recibido:    
        mensaje_recibido_cumple_paridad = sum(mensaje_recibido) % 2 == 0
        
        if mensaje_emitido != mensaje_recibido:
            contador_mensajes_alterados += 1
            if not mensaje_recibido_cumple_paridad:
                cont_mensajes_alterados_y_detectados += 1
        contador_mensajes_alterados_y_no_detectados = contador_mensajes_alterados-cont_mensajes_alterados_y_detectados     
    return contador_mensajes_alterados/N, cont_mensajes_alterados_y_detectados/N, contador_mensajes_alterados_y_no_detectados/N

#Fer
def simulacion_original():

    print('                                       %               %               %')
    print('                                mensajes        mensajes        mensajes')
    print('                                alterado        alterado        alterado')
    print('   n + 1               p                     y detectado  y no detectado')
    print('   -----          ------        ---------    ------------ --------------')
    for n in [7, 15, 31, 63]:
        for p in [0.1, 0.01, 0.001]:
            (p_alterado, p_alterado_y_detectado, p_alterado_y_no_detectado) = probabilidad_empirica_error_detectado(n, p)
            print (repr(n).rjust(4) + " + 1" , "{:15.4f}".format(float(p)),  "{:15.4f}".format(float(p_alterado)),  "{:15.4f}".format(float(p_alterado_y_detectado)),  "{:15.4f}".format(float(p_alterado_y_no_detectado)))
#Javi
def simulacion():
   pass

#Javi
#Genera tantas listas como distacia entre los parametros
#La longitud de cada lista se correspondera con el valor del intervalo en el que se encuentre
#El parametro n es el numero de listas de una misma longituda que se quieren hacer
def generate_random_lists(begin, finish, n):
    bit_lists = []
    for i in range(begin, finish +1):
        for j in range(0,n+1):
            bit_lists.append(generar_lista_de_bits(i))
    return bit_lists, n

#Javi
#Añade el bit de paridad a todas las listas de la lista
def add_parity_bit_to_lists(lists):
    for list in lists:
        annadir_bit_paridad(list)


