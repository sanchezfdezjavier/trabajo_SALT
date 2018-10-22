import BitParidad as bp
import Alteracion as alt
import matplotlib.pyplot as plt
import random as rnd

class Bit_Paridad():

    def __init__(self, start, finish, n, p):
        self.start = start
        self.finish = finish
        self.n = n
        self.p = p
        self.messages_prob = self.__generate_random_lists(start, finish, n)
        self.messages_raw = self.messages_prob[0]
        self.messages = self.messages_prob[0]
        self.messages_parity = self.messages
        self.__add_parity_bit_to_lists()
        #cambio
        self.__alter_messages(p)
        self.altered_messages = self.messages
        self.counter_alter_messages = 0
        self.counter_alter_messages_and_detected = 0
        self.counter_alter_messages_and_ndetected = 0

    #Genera tantas listas como distacia entre los parametros
    #La longitud de cada lista se correspondera con el valor del intervalo en el que se encuentre
    #El parametro n es el numero de listas de una misma longituda que se quieren hacer
    def __generate_random_lists(self,begin, finish, n):
        bit_lists = []
        for i in range(begin, finish +1):
            for j in range(0,n+1):
                bit_lists.append(bp.generar_lista_de_bits(i))
        return bit_lists, n

    #Añade el bit de paridad a todas las listas de la lista
    def __add_parity_bit_to_lists(self):
        for i in range(len(self.messages)):
            parity_bit = sum(self.messages[i])%2
            self.messages_parity[i].append(parity_bit)

    #Altera todos los mensajes
    def __alter_messages(self, p):
        try:
            for message in self.messages_parity:
                for i in range(len(message)):
                    alter = rnd.random() < p
                    if alter:
                        self.messages[message] = 1 - message[i]
        except:
            print("__alter_messages no funciona")

    #Comprueba la paridad de todos los mensajes
    def __paritty_check(self):
        pass

    def get_messages_prob(self):
        return self.messages_prob

    def get_messages_raw(self):
        return self.messages_raw

    def get_messages_parity(self):
        return self.messages_parity

    def get_altered_messages(self):
        return self.altered_messages


    #Vamos a testear lo que tengo hecho.

bit_paridad1 = Bit_Paridad(2,4,2,1)
print(bit_paridad1.get_messages_prob())
print("\n\n\n")
print(bit_paridad1.get_messages_raw())
print("\n\n\n")
print(bit_paridad1.get_messages_parity())
print("\n\n\n")
print(bit_paridad1.get_altered_messages())


