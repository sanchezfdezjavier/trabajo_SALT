# -*- coding: utf-8 -*-
"""
Primer programa de la simulación en SALT, teoría de la información
@author Fernando 

Se emite un mensaje de n bits. Se altera durante la emisión con una probabilidad p. Calcular, teórica
y empíricamente, la probabilidad de que el mensaje quede alterado.
"""
import random
import copy

def probabilidad_teorica_correcto(n, p):
    return (1-p)**n

def generar_lista_de_bits(n): 
    lista = []
    for i in range(n):
        bit_aleatorio = random.choice([0, 1])
        lista.append(bit_aleatorio)
    return lista

def alterar_lista_de_bits(lista, p):
    for i in range(len(lista)): 
        alterar = random.random() < p # Bernouilli(p)
        if alterar:
            lista[i] = 1 - lista[i]

def probabilidad_empirica_correcto(n, p, iter):
    iter = 10**3
    contador_mensajes_iguales = 0
    for i in range(iter):
        # Generar el mensaje que se emite:
        mensaje_emitido = generar_lista_de_bits(n)
        
        # Generar el mensaje que se recibe:
        mensaje_recibido = copy.deepcopy(mensaje_emitido)
        alterar_lista_de_bits(mensaje_recibido, p)
        
        # Ver si el mensaje ha sido alterado:
        iguales = mensaje_emitido == mensaje_recibido
        
        # Contabilizar la alteración, en su caso:
        if iguales:
            contador_mensajes_iguales += 1
            
    return contador_mensajes_iguales/iter

""" -----------------------------------------------------------------
> probabilidad_teorica_correcto(100, 0.01)

> probabilidad_empirica_correcto(100, 0.01)
> probabilidad_empirica_correcto(100, 0.01)
> probabilidad_empirica_correcto(100, 0.01)

----------------------------------------------------------------- """