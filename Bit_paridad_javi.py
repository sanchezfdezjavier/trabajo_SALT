import random as rnd
import copy
import matplotlib.pyplot as plt
import numpy as np


class Bit_paridad_javi():

    def __init__(self, start, finish, n, p):
        self.start = start
        self.finish = finish
        self.n = n
        self.p = p
        self.messages_raw = []
        self.messages_raw = self.generate_messages_from_to()
        self.messages_parity = []
        self.messages_parity = self.add_parity_bit_to_messages()
        self.messages_parity_alterated = []
        self.messages_parity_alterated = self.alterate_messages()
        self.probabilities = ()
        self.probabilities = self.calculate_statistics()

    #Getters
    def get_n(self):

        return self.n

    def get_start(self):

        return self.start

    def get_finish(self):

        return self.finish

    def get_total_messages(self):

        return len(self.messages_parity_alterated)

    def get_messages_raw(self):

        return self.messages_raw

    def get_messages_parity(self):

        return self.messages_parity

    def get_messages_parity_alterated(self):

        return self.messages_parity_alterated

    def get_probabilities(self):

        return self.probabilities

    def get_length_group_messages(self):
        aux_length = []

        for message in self.messages_parity_alterated:
            aux_length.append(len(message))

        return aux_length
    # To print the charts indexes.
    def get_length_group_messages_simplified(self):

        aux_length = []

        for message in self.messages_parity_alterated:
            aux_length.append(len(message))
        set_length = set(aux_length)

        return_list = []

        for long in set_length:
            return_list.append(long)

        return_list.sort()
        return return_list

    def toString(self):

        print("Generamos ", self.n, " mensajes de cada longitud.")
        print("Los cuales van de ", self.start, " hasta ", self.finish)


    #Generates random message with a specified length
    def generate_bit_message(self, l):

        list = []
        for i in range(l):
            random_bit = rnd.choice([0,1])
            list.append(random_bit)
        return list

    #Generates messages groups. Each group has 'n' messages with a linear spaced length based on start and finish
    def generate_messages_from_to(self):

        messages_rep = []
        #Cambiar variable de control
        step = (len(range(self.start, self.finish)) * self.n ) // 20
        for i in range(self.start, self.finish, step):
            for j in range(0, self.n):
                messages_rep.append(self.generate_bit_message(i))
        return messages_rep

    #Adds the parity biy at the end of the message
    def add_parity_bit_to_messages(self):

        aux_messages_parity = copy.deepcopy(self.messages_raw)
        for i in range(len(self.messages_raw)):
            parity_bit = sum(self.messages_raw[i])%2
            aux_messages_parity[i].append(parity_bit)
        return aux_messages_parity

    #Modifies messages bits using the p given by the user
    def alterate_messages(self):

        aux_messages_parity_alterated = copy.deepcopy(self.messages_parity)

        for i in range(len(self.get_messages_parity())):
            for j in range(len(self.get_messages_parity()[i])):
                alterate = rnd.random() < self.p
                if alterate:
                    aux_messages_parity_alterated[i][j] = 1 - aux_messages_parity_alterated[i][j]

        return aux_messages_parity_alterated

    #Calculate the statistics for the whole group of messages
    def calculate_statistics(self):

        altered_messages_counter = 0
        altered_and_detected_messages_counter = 0

        for i in range(len(self.messages_parity_alterated)):
            received_message_satisfies_parity =  sum(self.messages_parity_alterated[i]) % 2 == 0

            if self.messages_parity[i] != self.messages_parity_alterated[i]:
                altered_messages_counter += 1
                if not received_message_satisfies_parity:
                    altered_and_detected_messages_counter +=1
            altered_and_no_detected_messages_counter = altered_messages_counter - altered_and_detected_messages_counter

        return altered_messages_counter, altered_and_detected_messages_counter, altered_and_no_detected_messages_counter

    #Calculates the statistics for each group of messages
    def calculate_separate_statistics(self):

        altered_messages_counter = 0
        altered_and_detected_messages_counter = 0
        altered_and_no_detected_messages_counter = 0
        return_list = []

        counter = 0
        for i in range(len(self.messages_parity_alterated)):
            if counter > 1:
                return_list.append(aux_list)
                altered_messages_counter = 0
                altered_and_detected_messages_counter = 0
                altered_and_no_detected_messages_counter = 0
                aux_list = []
                counter = 0
            else:
                received_message_satisfies_parity = sum(self.messages_parity_alterated[i]) % 2 == 0

                if self.messages_parity[i] != self.messages_parity_alterated[i]:
                    altered_messages_counter += 1
                    if not received_message_satisfies_parity:
                        altered_and_detected_messages_counter += 1
                altered_and_no_detected_messages_counter = altered_messages_counter - altered_and_detected_messages_counter
                aux_list = [altered_messages_counter, altered_and_detected_messages_counter, altered_and_no_detected_messages_counter]
                counter += 1

        return return_list

    #Testing graphs
    def plot_conclusions(self):
        pass










































































































































































































































































































































































































































































































































































#Testing
bitp = Bit_paridad_javi(20, 40, 5, 1)
print("\n")
print("Mensajes generados: {}".format(len(bitp.get_messages_parity_alterated())))
print("1-> Las longitudes de los grupos de mensajes generados son:\n {}".format(bitp.get_length_group_messages()))
print("\n\n")
print("2-> Las longitudes(simplificadas) de los grupos de mensajes generados son:\n {}".format(bitp.get_length_group_messages_simplified()))
print("\n\n")
print("3--> Las probabilidades generales son: {}".format(bitp.get_probabilities()))
print("\n\n")
print("4--> Las probabilidades por cada grupo de longitud n son:\n {}".format(bitp.calculate_separate_statistics()))

