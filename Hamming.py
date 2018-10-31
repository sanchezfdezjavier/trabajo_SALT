import random
import copy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple



def generar_mensaje(k):
    # Dev. un mensaje de datos (0s y 1s) de la longitud máxima que se puede
    # autocorregir con k bits de paridad:
    # Ejemplo: si k = 3, long = 4 (7, incluyendo los bits de paridad, 8
    # incluyendo la situación de no error)

    longitud_mensaje = 2**k - 1 - k
    mensaje = []
    for _ in range(longitud_mensaje):
        bit_aleatorio = random.choice([0, 1])
        mensaje.append(bit_aleatorio)
    return mensaje

def cifra_binaria(n, k):
    # Dev. la cifra k-ésima de un número n considerando su expresión binaria
    # Considerando n como un número binario, la cifra 0 es la de las unidades,
    # la 1, las decenas, etc. Por ejemplo, si n = 23 = "10111" (en binario):
    # cifra_binaria(23,0) -> 1
    # cifra_binaria(23,1) -> 1
    # cifra_binaria(23,2) -> 1
    # cifra_binaria(23,3) -> 0
    # cifra_binaria(23,4) -> 1

    for _ in range(k):
        n = n // 2
    return n % 2

def insertar_bits_de_paridad(mensaje, k):
    # Insertamos 0s en las posiciones (2**0, 2**1, ...) de los bits de paridad:
    for i in range(k):
        mensaje.insert(2**i - 1, 0)

    # Calculamos el valor real de los k bits de paridad:
    for i in range(k):
        # Calculamos el bit de paridad i-ésimo:
        suma_de_bits = 0
        for j in range(len(mensaje)):
            suma_de_bits += cifra_binaria(j+1, i) * mensaje[j]
        mensaje[2**i-1] = suma_de_bits % 2

def alterar_lista_de_bits(lista, p):
    for i in range(len(lista)):
        alterar = random.random() < p
        if alterar:
            lista[i] = 1 - lista[i]

def bits_de_paridad_alterados(mensaje, k):
    bits_de_paridad = [0] * k
    for i in range(k):
        for j in range(len(mensaje)):
            bits_de_paridad[i] = (cifra_binaria(j+1, i) * mensaje[j] + bits_de_paridad[i]) % 2
    return bits_de_paridad

def posicion_del_error(bits_alterados):
    posicion = 0
    long = len(bits_alterados)
    for i in range(long):
        posicion += bits_alterados[long-i-1]*(2**(i))
    return posicion

def corregir_bit_erroneo(mensaje, posicion_error):
    if posicion_error != 0:
        mensaje[posicion_error - 1] = 1 - mensaje[posicion_error - 1]

def son_listas_iguales(lista_a, lista_b):
    if len(lista_a) != len(lista_b):
        return False
    for i in range(len(lista_a)):
        if lista_a[i] != lista_b[i]:
            return False
    return True

def Hamming(k, p, iter):

    contador_mensajes_alterados = 0
    contador_mensajes_alterados_y_corregidos_bien = 0

    for i in range(iter):
        # Generar el mensaje que se emite:
        mensaje_original = generar_mensaje(k)
        insertar_bits_de_paridad(mensaje_original, k)

        mensaje_emitido = copy.deepcopy(mensaje_original)
        alterar_lista_de_bits(mensaje_emitido, p)

        bits_alterados = bits_de_paridad_alterados(mensaje_emitido, k)
        posicion_error = posicion_del_error(bits_alterados)

        if mensaje_emitido != mensaje_original:
            contador_mensajes_alterados += 1
            # Corregir el mensaje:
            corregir_bit_erroneo(mensaje_emitido, posicion_error)
            if mensaje_emitido == mensaje_original:
                contador_mensajes_alterados_y_corregidos_bien += 1
    contador_mensajes_alterados_y_corregidos_mal = contador_mensajes_alterados - contador_mensajes_alterados_y_corregidos_bien
    return contador_mensajes_alterados/iter, contador_mensajes_alterados_y_corregidos_bien/iter, contador_mensajes_alterados_y_corregidos_mal/iter

def simulacion(iter):
    print('                                       %               %               %')
    print('                                mensajes        mensajes        mensajes')
    print('                                alterado        alterado        alterado')
    print('   n + k               p                     y corregido  y no corregido')
    print(' --------         ------       ---------    ------------  --------------')
    for k in [3, 4, 5, 6, 7, 8, 9]:
        n = 2**k - 1 - k
        for p in [0.1, 0.01, 0.001]:
            (p_alterado, p_alterado_y_corregido, p_alterado_y_no_corregido) = Hamming(k, p, iter)
            print (repr(n).rjust(4) + " + " + repr(k), "{:15.4f}".format(float(p)),  "{:15.4f}".format(float(p_alterado)),  "{:15.4f}".format(float(p_alterado_y_corregido)),  "{:15.4f}".format(float(p_alterado_y_no_corregido)))


def get_parameters_plot():
    list_p_alterado  = []
    list_p_alteado_y_corregido = []
    list_p_alterado_y_no_corregido = []
    indices = []

    for k in [3, 4, 5, 6, 7, 8, 9]:
        n = 2**k - 1 - k
        for p in [0.1, 0.01, 0.001]:
            p_alterado, p_alterado_y_corregido, p_alterado_y_no_corregido = Hamming(k, p, 100)

            list_p_alterado.append(p_alterado)
            list_p_alteado_y_corregido.append(p_alterado_y_corregido)
            list_p_alterado_y_no_corregido.append(p_alterado_y_corregido)
            indices.append(repr(n).rjust(4) + " + " + repr(k))


    return indices, list_p_alterado, list_p_alteado_y_corregido, list_p_alterado_y_no_corregido

def test_barchart():

    n_groups = len(get_parameters_plot()[1])

    means_men = get_parameters_plot()[1]


    means_women = get_parameters_plot()[2]


    other_values = get_parameters_plot()[3]


    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.25

    opacity = 0.8
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, means_men, bar_width,
                    alpha=opacity, color='b',
                    error_kw=error_config,
                    label='alterado')

    rects2 = ax.bar(index + bar_width, means_women, bar_width,
                    alpha=opacity, color='r',
                    error_kw=error_config,
                    label='alterado y corregido')
    rects3 = ax.bar(index + bar_width + bar_width, other_values, bar_width,
                    alpha=opacity, color = 'g',
                    error_kw=error_config,
                    label= 'alterado y no corregido')

    ax.set_xlabel('messages length')
    ax.set_ylabel('messages number')
    ax.set_title('Hamming results')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(get_parameters_plot()[0], fontsize = 3.5)
    ax.legend()

    fig.tight_layout()
    plt.show()


simulacion(1)
test_barchart()
print(get_parameters_plot())